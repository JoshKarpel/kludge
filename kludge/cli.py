import os
from asyncio import run
from textwrap import dedent

from kubernetes_asyncio import client, config
from kubernetes_asyncio.client import ApiClient
from rich.console import Console
from typer import Typer

from kludge.constants import PACKAGE_NAME

console = Console()

cli = Typer(
    name=PACKAGE_NAME,
    no_args_is_help=True,
    rich_markup_mode="rich",
    help=dedent(
        f"""\
        """
    ),
)


@cli.command()
def kludge() -> None:
    os.environ["TEXTUAL"] = ",".join(sorted(["debug", "devtools"]))

    run(run_app())


async def run_app() -> None:
    await config.load_kube_config()

    # use the context manager to close http sessions automatically
    async with ApiClient() as api:
        core = client.CoreV1Api(api)
        apps = client.AppsV1Api(api)
        pods = await core.list_pod_for_all_namespaces()

        for ns in pods.items:
            print(ns.metadata.name)

    # app = KludgeApp()
    # app.run()
