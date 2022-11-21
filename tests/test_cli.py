import subprocess
import sys

from typer.testing import CliRunner

from kludge.cli import cli
from kludge.constants import PACKAGE_NAME, __version__


def test_help(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["--help"])

    assert result.exit_code == 0


def test_help_via_main() -> None:
    result = subprocess.run([sys.executable, "-m", PACKAGE_NAME, "--help"])

    print(result.stdout)
    assert result.returncode == 0


def test_version(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["version"])

    assert result.exit_code == 0
    assert __version__ in result.stdout
