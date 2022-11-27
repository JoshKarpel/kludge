#!/usr/bin/env python
import re
import subprocess
from pathlib import Path
from tempfile import gettempdir
from textwrap import dedent
from typing import Iterable

from openapi_schema_pydantic import OpenAPI, PathItem, Reference
from rich.console import Console
from rich.style import Style
from rich.syntax import Syntax
from rich.text import Text
from typer import Typer

KUBERNETES_REPO = "https://github.com/kubernetes/kubernetes"

BASE_WORKDIR = Path(gettempdir()) / "kludge-codegen"

console = Console()

cli = Typer()


@cli.command()
def generate(
    tag: str = "release-1.25",
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
        r = subprocess.run(
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
            "from aiohttp import ClientSession",
        ]
    )

    specs_dir = kubernetes_dir / "api" / "openapi-spec" / "v3"

    pod_file = specs_dir / "api__v1_openapi.json"

    api: OpenAPI = OpenAPI.parse_file(pod_file)
    for path, spec in api.paths.items():
        if "watch" in path:
            continue
        chunks.extend(generate_functions(path, spec))

    code = "\n".join(c for c in chunks if c)

    console.print(Syntax(code, lexer="python"))


RE_PARAMS = re.compile(r"\{(\w+)\}")


def path_to_name(path: str) -> tuple[str, list[str]]:
    params = RE_PARAMS.findall(path)
    name = (
        path.removeprefix("/api/")
        .replace("/", "_")
        .replace("namespaces_{namespace}", "namespaced")
        .replace("{name}", "")
        .replace("{path}", "")
        .replace("__", "_")
        .rstrip("_")
    )

    return name, params


def object_ref_to_name(ref: str) -> str:
    #     #/components/schemas/io.k8s.api.core.v1.ComponentStatus'
    return (
        ref.replace("#/components/schemas/io.k8s.api.core.", "Core")
        .replace("#/components/schemas/io.k8s.apimachinery.pkg.apis.meta.", "Core")
        .replace("v1", "V1")
        .replace(".", "")
    )


def camel_to_snake(s: str) -> str:
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def generate_functions(path: str, spec: PathItem) -> Iterable[str]:
    print(path)
    name, params = path_to_name(path)
    args = ["session: ClientSession"] + [f"{p}: str" for p in params]
    fmt_args = ", ".join(args)
    if spec.get is not None:
        op_id = spec.get.operationId
        response_types = spec.get.responses["200"].content
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
                    Original path: {path}
                    Op ID: {op_id}
                    Derived name: {name}
                    Derived params: {params}
                    \"\"\"
                    async with session.get(f"{path}", ssl=sslcontext) as response:
                        {return_line}
                """
            )


if __name__ == "__main__":
    cli()
