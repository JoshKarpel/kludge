import os
from textwrap import dedent

from rich.console import Console
from typer import Typer

from kludge.app import KludgeApp
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

    app = KludgeApp()
    app.run()
