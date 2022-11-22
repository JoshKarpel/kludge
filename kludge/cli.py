import os
import ssl
from asyncio import run
from textwrap import dedent

from aiohttp import ClientSession
from rich.console import Console
from typer import Typer

from kludge._kube.io.k8s.api.apps.v1 import DeploymentList
from kludge.constants import PACKAGE_NAME
from kludge.kubeconfig import KubeConfig

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

    config = KubeConfig.build()
    console.print(config)

    run(run_app(config))


async def run_app(config: KubeConfig) -> None:
    cluster = config.clusters[0].cluster
    user = config.users[0].user

    sslcontext = ssl.create_default_context(cafile=cluster.certificate_authority)
    sslcontext.load_cert_chain(certfile=user.client_certificate, keyfile=user.client_key)

    async with ClientSession() as session:
        async with session.get(
            f"{cluster.server}/apis/apps/v1/deployments", ssl=sslcontext
        ) as response:
            j = await response.json()
            console.print(j)
            console.print(DeploymentList.parse_obj(j))

    # app = KludgeApp()
    # app.run()
