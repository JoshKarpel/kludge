#!/usr/bin/env python

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from tempfile import gettempdir
from textwrap import dedent
from typing import Iterator

from openapi_schema_pydantic import OpenAPI, PathItem, Reference, Schema
from rich.console import Console, Group, RenderableType
from rich.panel import Panel
from rich.pretty import Pretty
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

    renderers = []

    for name, schema in api.components.schemas.items():
        if name in [
            "io.k8s.apimachinery.pkg.apis.meta.v1.Patch",
        ]:
            continue
        renderers.append(Klass(name, schema))

    for path, spec in api.paths.items():
        if "watch" in path:
            continue
        renderers.append(Funcs(path, spec))

    for r in renderers:
        for z in r.render():
            if isinstance(z, str):
                chunks.append(z)
            else:
                console.print(z)

    out.write_text("\n".join(c for c in chunks if c))
    console.print(Text(f"Wrote generated code to {out}", style=Style(color="green")))


@dataclass
class Error:
    title: str
    parts: list[RenderableType]

    def __rich__(self) -> RenderableType:
        return Panel(
            Group(*self.parts),
            title=self.title,
            title_align="left",
            border_style=Style(color="red"),
        )


@dataclass
class Klass:
    name: str
    schema: Schema

    def render(self) -> Iterator[str | Error]:
        fields = []

        if self.schema.properties is None:
            yield Error(
                title=f"Empty schema.properties in {self.name}",
                parts=[
                    Pretty(self.schema),
                ],
            )
            return

        required = self.schema.required or []

        for prop_name, prop in self.schema.properties.items():
            if prop.type is None:
                try:
                    t = object_ref_to_name(prop.allOf[0].ref)
                except:
                    console.print(f"{self.name=}")
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
                        yield Error(
                            title=f"Unknown array item type in {self.name}",
                            parts=[
                                f"{prop_name=}",
                                Pretty(prop),
                            ],
                        )
                        return
                t = f"list[{item_type}]"
            else:
                yield Error(
                    title=f"Unknown prop type in {self.name}",
                    parts=[
                        f"{prop_name=}",
                        Pretty(prop),
                    ],
                )
                return

            if prop.default is not None:
                if prop.type == "string":
                    d = f'default="{prop.default}"'
                else:
                    d = f"default={prop.default}"
            elif prop_name == "kind":
                d = f'"{self.name.split(".")[-1]}"'
            elif prop_name == "apiVersion":
                d = '"v1"' if "v1" in self.name else "..."
            else:
                d = "..."

            if prop_name not in required and prop.default is None:
                t = f"{t} | None"

            if prop_name == "continue":
                prop_name = "continue_"

            fields.append(f'{camel_to_snake(prop_name)}: {t} = Field({d}, alias="{prop_name}")')
            # fields.append(f"{camel_to_snake(prop_name)}: {t} = Field({d}, alias=\"{prop_name}\", description=\"{prop.description}\")")

        c = dedent(
            f"""\
            class {object_ref_to_name(self.name)}(BaseModel):
                \"\"\"
                Original name: {self.name}
                \"\"\"
            """
        )
        for f in fields:
            c += f"    {f}\n"

        yield c


@dataclass
class Funcs:
    path: str
    spec: PathItem

    def render(self) -> Iterator[str | Error]:
        params = params_from_path(self.path)
        args = ["session: ClientSession"] + [f"{p}: str" for p in params]
        fmt_args = ", ".join(args)
        if self.spec.get is not None:
            op_id = self.spec.get.operationId
            response_types = self.spec.get.responses["200"].content
            if "application/json" in response_types:
                return_type = response_types["application/json"]
                if isinstance(return_type.media_type_schema, Reference):
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
                            Original path: {self.path}
                            Op ID: {op_id}
                            Derived params: {params}
                            \"\"\"
                            async with session.get(f"{self.path}") as response:
                                {return_line}
                        """
                )


RE_PARAMS = re.compile(r"\{(\w+)\}")


def params_from_path(path: str) -> list[str]:
    return RE_PARAMS.findall(path)


def object_ref_to_name(ref: str) -> str:
    return (
        ref.replace("#/components/schemas/", "")
        .replace("io.k8s.api.authentication.", "Authentication")
        .replace("io.k8s.api.core.", "Core")
        .replace("io.k8s.apimachinery.pkg.apis.meta.", "Meta")
        .replace("io.k8s.api.autoscaling.", "Autoscaling")
        .replace("v1", "V1")
        .replace(".", "")
    )


def camel_to_snake(s: str) -> str:
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


if __name__ == "__main__":
    cli()
