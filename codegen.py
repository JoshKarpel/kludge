#!/usr/bin/env python
import re
import subprocess
from pathlib import Path
from tempfile import gettempdir
from textwrap import dedent
from typing import Iterable

from openapi_schema_pydantic import OpenAPI, PathItem, Reference, Schema
from rich.console import Console
from rich.style import Style
from rich.text import Text
from typer import Typer

KUBERNETES_REPO = "https://github.com/kubernetes/kubernetes"

BASE_WORKDIR = Path(gettempdir()) / "kludge-codegen"

console = Console()

cli = Typer()


@cli.command()
def generate(
    tag: str = "release-1.25",
    out: Path = Path(__file__).parent.resolve() / "kludge" / "kube.py",
):
    kubernetes_dir = BASE_WORKDIR / "k8s" / tag

    if not kubernetes_dir.exists():
        kubernetes_dir.parent.mkdir(parents=True, exist_ok=True)
        console.print(
            Text(
                f"Cloning {KUBERNETES_REPO}@{tag} into {kubernetes_dir} ...",
                style=Style(color="yellow"),
            )
        )
        subprocess.run(
            # clone --depth=1 --branch release-1.25 https://github.com/kubernetes/kubernetes "${dir}"
            ["git", "clone", "--depth", "1", "--branch", tag, KUBERNETES_REPO, str(kubernetes_dir)],
            check=True,
        )

    console.print(
        Text(f"{KUBERNETES_REPO}@{tag} has been cloned to {kubernetes_dir}", style="green")
    )

    chunks = []

    chunks.extend(
        [
            "from __future__ import annotations",
            "from aiohttp import ClientSession",
            "from pydantic import BaseModel, Field",
            "",
        ]
    )

    specs_dir = kubernetes_dir / "api" / "openapi-spec" / "v3"

    pod_file = specs_dir / "api__v1_openapi.json"

    api: OpenAPI = OpenAPI.parse_file(pod_file)

    for name, schema in api.components.schemas.items():
        # if name not in ["io.k8s.api.core.v1.Pod", "io.k8s.api.core.v1.PodSpec"]:
        #     continue
        chunks.append(generate_class(name, schema))

    for path, spec in api.paths.items():
        if "watch" in path:
            continue
        chunks.extend(generate_functions(path, spec))

    out.write_text("\n".join(c for c in chunks if c))
    console.print(Text(f"Wrote generated code to {out}", style=Style(color="green")))


RE_PARAMS = re.compile(r"\{(\w+)\}")


def params_from_path(path: str) -> list[str]:
    return RE_PARAMS.findall(path)


def object_ref_to_name(ref: str) -> str:
    return (
        ref.replace("#/components/schemas/", "")
        .replace("io.k8s.api.authentication.", "Authentication")
        .replace("io.k8s.api.core.", "Core")
        .replace("io.k8s.apimachinery.pkg.apis.meta.", "Meta")
        .replace("v1", "V1")
        .replace(".", "")
    )


def camel_to_snake(s: str) -> str:
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def generate_functions(path: str, spec: PathItem) -> Iterable[str]:
    params = params_from_path(path)
    args = ["session: ClientSession"] + [f"{p}: str" for p in params]
    fmt_args = ", ".join(args)
    if spec.get is not None:
        op_id = spec.get.operationId
        response_types = spec.get.responses["200"].content
        if "application/json" in response_types:
            return_type = response_types["application/json"]
            if isinstance(return_type.media_type_schema, Reference):
                print(return_type.media_type_schema.ref)
                rt = object_ref_to_name(return_type.media_type_schema.ref)
            else:
                rt = return_type.media_type_schema.type

            return_line = (
                f"return {rt}.parse_obj(await response.json())"
                if rt != "string"
                else "return await response.text()"
            )

            yield dedent(
                f"""\
                async def {camel_to_snake(op_id)}({fmt_args}) -> {rt}:
                    \"\"\"
                    Original path: {path}
                    Op ID: {op_id}
                    Derived params: {params}
                    \"\"\"
                    async with session.get(f"{path}") as response:
                        {return_line}
                """
            )


def generate_class(name: str, schema: Schema) -> str:
    fields = []

    if schema.properties is None:
        console.print(f"{name=}")
        console.print(f"{schema=}")
        return ""

    for prop_name, prop in schema.properties.items():
        if prop.type is None:
            try:
                t = object_ref_to_name(prop.allOf[0].ref)
            except:
                console.print(f"{name=}")
                console.print(f"{prop.type=} {prop=}")
                t = "panic"
        elif prop.type == "string":
            t = "str"
        elif prop.type == "integer":
            t = "int"
        elif prop.type == "boolean":
            t = "bool"
        elif prop.type == "array":
            if isinstance(prop.items, Reference):
                item_type = object_ref_to_name(prop.items.ref)
            else:
                try:
                    item_type = object_ref_to_name(prop.items.allOf[0].ref)
                except Exception:
                    console.print(name)
                    console.print(prop_name)
                    console.print(prop)
                    console.print(f"panic {prop.type=} {prop.items=}")
                    item_type = "panic"
            t = f"list[{item_type}]"
        else:
            console.print(name)
            console.print(prop_name)
            console.print(prop)
            console.print(f"panic {prop.type=}")
            t = "panic"

        if prop.default is not None:
            if isinstance(prop.default, dict) and prop.type is None:
                d = f"default_factory={t}"
            elif prop.type == "string":
                d = f'default="{prop.default}"'
            else:
                d = f"default={prop.default}"
        elif prop_name == "kind":
            d = f'"{name.split(".")[-1]}"'
        elif prop_name == "apiVersion":
            d = '"v1"' if "v1" in name else "..."
        else:
            d = "..."

        if prop_name == "continue":
            prop_name = "continue_"

        fields.append(f'{camel_to_snake(prop_name)}: {t} = Field({d}, alias="{prop_name}")')
        # fields.append(f"{camel_to_snake(prop_name)}: {t} = Field({d}, alias=\"{prop_name}\", description=\"{prop.description}\")")

    fmt_fields = f"\n{' ' * 12}".join(fields)

    return dedent(
        f"""\
        class {object_ref_to_name(name)}(BaseModel):
            {fmt_fields}
        """
    )


if __name__ == "__main__":
    cli()
