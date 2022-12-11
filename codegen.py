#!/usr/bin/env python

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from tempfile import gettempdir
from textwrap import dedent
from typing import Iterable

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
            "from pydantic import BaseModel, Field",
            "from kludge.klient import Klient",
            "from textual import log",
            "from datetime import datetime",
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
        try:
            chunks.extend(r.render())
        except Error as e:
            console.print(e)

    for r in renderers:
        if isinstance(r, Klass):
            chunks.append(r.render_update_forward_refs_call())

    out.write_text("\n".join(c for c in chunks if c))
    console.print(Text(f"Wrote generated code to {out}", style=Style(color="green")))


@dataclass
class Error(Exception):
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

    def render(self) -> Iterable[str]:
        fields = []

        if self.schema.properties is None:  # root prop
            t = schema_to_type(self.schema)
            fields.append(f"__root__: {t} | None = Field(default=None)")

        else:  # object with sub-properties
            required = self.schema.required or []

            for prop_name, prop in self.schema.properties.items():
                t = schema_to_type(prop)

                if prop.default is not None:
                    if prop.type == "string":
                        d = f'default="{prop.default}"'
                    else:
                        d = f"default={prop.default}"
                elif prop_name == "kind":
                    d = f'default="{self.name.split(".")[-1]}"'
                elif prop_name == "apiVersion":
                    d = 'default="v1"' if "v1" in self.name else "..."
                else:
                    d = "..."

                # TODO: hack!
                # is there actually something different in e.g. how
                # CoreV1PodCondition.last_probe_time and CoreV1PodCondition.last_transition_time
                # are defined?
                if t == "MetaV1Time":
                    t = "datetime | None"
                    d = "default=None"
                elif (
                    prop_name not in required
                    and prop.default is None
                    and prop_name not in ("kind", "apiVersion")
                ):
                    t = f"{t} | None"
                    d = "default=None"

                if prop_name == "continue":
                    prop_name = "continue_"

                field_args = [d]
                attr_name = camel_to_snake(prop_name)
                if prop_name != attr_name:
                    field_args.append(f'alias="{prop_name}"')

                fa = ", ".join(field_args)

                fields.append(f"{attr_name}: {t} = Field({fa})")
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

    def render_update_forward_refs_call(self) -> str:
        return f"{object_ref_to_name(self.name)}.update_forward_refs()"


def schema_to_type(schema: Schema | Reference) -> str:
    if isinstance(schema, Reference):
        return object_ref_to_name(schema.ref)

    if schema.properties is not None:
        raise Error(
            title="schema_to_type doesn't support schema.properties", parts=[Pretty(schema)]
        )
    elif schema.type is not None:
        if schema.type == "string":
            return "str"
        elif schema.type == "integer":
            return "int"
        elif schema.type == "number":
            return "float"
        elif schema.type == "boolean":
            return "bool"
        elif schema.type == "array":
            item_type = schema_to_type(schema.items)
            return f"list[{item_type}]"
        elif schema.type == "object":
            if isinstance(schema.additionalProperties, Schema):
                vt = schema_to_type(schema.additionalProperties)
                return f"dict[str, {vt}]"
            elif isinstance(schema.additionalProperties, Reference):
                vt = object_ref_to_name(schema.additionalProperties.ref)
                return f"dict[str, {vt}]"
            else:
                return f"dict[str, object]"

    elif schema.oneOf is not None:
        return " | ".join(schema_to_type(s) for s in schema.oneOf)
    elif schema.allOf is not None:
        if len(schema.allOf) != 1:
            raise Error(title="Schema has more than one allOf entry", parts=[Pretty(schema)])

        entry = schema.allOf[0]

        if isinstance(entry, Reference):
            return object_ref_to_name(entry.ref)
        else:
            raise Error(
                title="Schema had an allOf that wasn't a single Ref", parts=[Pretty(schema)]
            )

    else:
        raise Error(
            title="Could not parse schema into a type",
            parts=[Pretty(schema)],
        )


@dataclass
class Funcs:
    path: str
    spec: PathItem

    def render(self) -> Iterable[str]:
        params = params_from_path(self.path)
        args = ["klient: Klient"] + [f"{p}: str" for p in params]
        fmt_args = ", ".join(args)
        if self.spec.get is not None:
            op_id = self.spec.get.operationId
            response_types = self.spec.get.responses["200"].content
            if "application/json" in response_types:
                return_type = response_types["application/json"]
                if isinstance(return_type.media_type_schema, Reference):
                    rt = object_ref_to_name(return_type.media_type_schema.ref)
                else:
                    rt = schema_to_type(return_type.media_type_schema)

                return_line = (
                    f"return {rt}.parse_obj(await response.json())"
                    if rt != "str"
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
                        async with await klient.get(f"{self.path}") as response:
                            {return_line}
                    """
                )

        if self.spec.delete is not None:
            op_id = self.spec.delete.operationId
            response_types = self.spec.delete.responses["200"].content
            if "application/json" in response_types:
                return_type = response_types["application/json"]
                if isinstance(return_type.media_type_schema, Reference):
                    rt = object_ref_to_name(return_type.media_type_schema.ref)
                else:
                    rt = schema_to_type(return_type.media_type_schema)

                return_line = f"return {rt}.parse_obj(await response.json())"

                yield dedent(
                    f"""\
                    async def {camel_to_snake(op_id)}({fmt_args}) -> {rt}:
                        \"\"\"
                        Original path: {self.path}
                        Op ID: {op_id}
                        Derived params: {params}
                        \"\"\"
                        async with await klient.get(f"{self.path}") as response:
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
        .replace("io.k8s.apimachinery.pkg.runtime", "Runtime")
        .replace("io.k8s.apimachinery.pkg.util.intstr", "Util")
        .replace("io.k8s.api.autoscaling.", "Autoscaling")
        .replace("io.k8s.apimachinery.pkg.api.resource.", "Resource")
        .replace("io.k8s.api.policy.", "Policy")
        .replace("v1", "V1")
        .replace(".", "")
    )


def camel_to_snake(s: str) -> str:
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s = s.replace("IP", "Ip")
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


if __name__ == "__main__":
    cli()
