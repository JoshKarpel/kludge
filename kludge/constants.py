from importlib import metadata
from pathlib import Path

PACKAGE_NAME = "kludge"
__version__ = metadata.version(PACKAGE_NAME)


PACKAGE_DIR = Path(__file__).resolve().parent
