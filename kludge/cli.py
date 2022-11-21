import os
from textwrap import dedent

from rich.console import Console
from rich.style import Style
from typer import Typer

from kludge.app import KludgeApp
from kludge.constants import PACKAGE_NAME, __version__

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
    """
    Present a deck.
    """
    os.environ["TEXTUAL"] = ",".join(sorted(["debug", "devtools"]))

    app = KludgeApp()
    app.run()


@cli.command()
def version() -> None:
    """
    Display version and debugging information.
    """

    console.print(__version__, style=Style())
