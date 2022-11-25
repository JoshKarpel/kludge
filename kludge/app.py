from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime, timezone
from fnmatch import fnmatch
from typing import Callable, Literal

from kubernetes_asyncio.client import ApiClient, CoreV1Api
from kubernetes_asyncio.config import load_kube_config
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DataTable, Footer, Header, Input

RESOURCE = Literal[
    "pod",
    "node",
    "namespace",
]

RESOURCE_ALIASES: Mapping[str, RESOURCE] = {
    "pod": "pod",
    "pods": "pod",
    "node": "node",
    "nodes": "node",
    "namespace": "namespace",
    "ns": "namespace",
}


def item_by_attr(collections: list[object], attr: str, value: object) -> object | None:
    for c in collections:
        if getattr(c, attr) == value:
            return c
    return None


def time_since(timestamp: datetime) -> str:
    td = datetime.now(timezone.utc) - timestamp

    parts = []
    if td.days > 0:
        parts.append(f"{td.days}d")

    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        parts.append(f"{hours}h")

    if minutes > 0:
        parts.append(f"{minutes}m")

    if seconds > 0:
        parts.append(f"{seconds}s")

    return " ".join(parts)


NODE_STATUS_MAP = {
    "True": "Ready",
    "False": "Unready",
    "Unknown": "Unknown",
}


def name(obj) -> str:
    return obj.metadata.name


def namespace(obj) -> str:
    return obj.metadata.namespace


def age(obj) -> str:
    return time_since(obj.metadata.creation_timestamp)


RESOURCE_COLS: Mapping[RESOURCE, Mapping[str, Callable[[object], str]]] = {
    "pod": {
        "name": name,
        "namespace": namespace,
        "age": age,
    },
    "node": {
        "name": name,
        "status": lambda obj: NODE_STATUS_MAP[
            item_by_attr(obj.status.conditions, "type", "Ready").status
        ],
        "age": age,
    },
    "namespace": {
        "name": name,
        "age": age,
    },
}


class ResourcesTable(Widget):
    namespace: str | None = reactive(None)
    resource: RESOURCE = reactive("pod")
    filter: str = reactive("*")
    raw_results: list[object] = reactive(list, always_update=True)
    results: list[object] = reactive(list, always_update=True)

    async def api(self) -> ApiClient:
        return await self.app.api()

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Input(name="Resource", id="resource", value="pod"),
            Input(name="Namespace", id="namespace", value="", placeholder=""),
            Input(name="Filter", id="filter", value="", placeholder="*"),
            id="inputs",
        )
        yield DataTable()

    def on_mount(self):
        self.set_interval(1, self.refresh_query)
        self.query_one(DataTable).focus()

    def validate_resource(self, resource: str) -> RESOURCE:
        return RESOURCE_ALIASES[resource]

    async def watch_namespace(self, namespace: str) -> None:
        self.raw_results = await self._query(self.resource, namespace)

    async def watch_resource(self, resource: RESOURCE) -> None:
        self.raw_results = await self._query(resource, self.namespace)

    async def refresh_query(self) -> None:
        self.raw_results = await self._query(self.resource, self.namespace)

    def watch_filter(self, filter: str) -> None:
        self.results = [r for r in self.raw_results if fnmatch(r.metadata.name, f"{filter}*")]

    def watch_raw_results(self, raw_results: list[object]) -> None:
        self.results = [r for r in raw_results if fnmatch(r.metadata.name, f"{self.filter}*")]

    async def _query(self, resource: RESOURCE, namespace: str) -> list[object]:
        api = await self.api()

        match resource, namespace:
            case "node", _:
                return (await CoreV1Api(api).list_node()).items
            case "pod", None:
                return (await CoreV1Api(api).list_pod_for_all_namespaces()).items
            case "pod", namespace:
                return (await CoreV1Api(api).list_namespaced_pod(namespace)).items
            case "namespace", _:
                return (await CoreV1Api(api).list_namespace()).items
            case _:
                self.app.bell()
                return []

    def watch_results(self, results: list[object]) -> None:
        dt = self.query_one(DataTable)
        dt.clear()
        dt.columns.clear()

        cols = RESOURCE_COLS[self.resource]
        dt.add_columns(*(c.upper() for c in cols.keys()))

        for o in results:
            dt.add_row(*(get(o) for get in cols.values()))

    async def namespace_names(self) -> set[str]:
        return {
            ns.metadata.name for ns in (await CoreV1Api(await self.api()).list_namespace()).items
        }

    async def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "resource":
            if event.value in RESOURCE_ALIASES:
                self.resource = event.value
        elif event.input.id == "filter":
            self.filter = event.value
        elif event.input.id == "namespace":
            if event.value == "":
                self.namespace = None
            elif event.value in (await self.namespace_names()):
                self.namespace = event.value


class KludgeApp(App[None]):
    CSS_PATH = "kludge.css"
    BINDINGS = []
    SCREENS = {}

    async def api(self) -> ApiClient:
        if hasattr(self, "_api"):
            return self._api

        await load_kube_config()
        self._api = ApiClient()
        return self._api

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        yield ResourcesTable()
