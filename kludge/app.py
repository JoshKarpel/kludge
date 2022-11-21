from __future__ import annotations

from textual.app import App


class KludgeApp(App[None]):
    CSS_PATH = "kludge.css"
    BINDINGS = []
    SCREENS = {}
