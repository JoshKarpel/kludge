from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from fnmatch import fnmatch
from typing import Callable, Generic, Iterable, Literal, TypeVar

from kubernetes_asyncio.client import ApiClient, CoreV1Api, V1Namespace, V1Node, V1Pod, V1Service
from rich.console import RenderableType
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.events import Key
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DataTable, Input

from kludge.klient import Klient
from kludge.konfig import Konfig
from kludge.kube import (
    list_core_v1_namespace,
    list_core_v1_namespaced_pod,
    list_core_v1_namespaced_service,
    list_core_v1_node,
    list_core_v1_pod_for_all_namespaces,
    list_core_v1_service_for_all_namespaces,
)

RESOURCE = Literal[
    "node",
    "namespace",
    "pod",
    "service",
]

_RESOURCE_ALIASES: Mapping[RESOURCE, set[str]] = {
    "node": {"nodes"},
    "namespace": {"ns"},
    "pod": {"pods", "po"},
    "service": {"services", "svc"},
}

RESOURCE_ALIASES: Mapping[str, RESOURCE] = {
    alias: resource
    for resource, aliases in _RESOURCE_ALIASES.items()
    for alias in (*aliases, resource)
}

T = TypeVar("T")


def first_item_with_attr_value(items: Iterable[T], attr: str, value: object) -> T | None:
    for c in items:
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


def pod_containers_ready(pod: V1Pod) -> str:
    container_statuses = pod.status.container_statuses

    num_total = len(container_statuses)
    num_ready = sum(cs.ready for cs in container_statuses)

    return f"{num_ready}/{num_total}"


class ColumnVerbosity(int, Enum):
    Normal = 0
    Wide = 1


R = TypeVar("R")


@dataclass(frozen=True)
class Col(Generic[R]):
    header: str
    getter: Callable[[R], RenderableType]
    verbosity: ColumnVerbosity = ColumnVerbosity.Normal


NODE_COLS: list[Col[V1Node]] = [
    Col(header="name", getter=name),
    Col(
        header="status",
        getter=lambda obj: NODE_STATUS_MAP[
            first_item_with_attr_value(obj.status.conditions, "type", "Ready").status
        ],
    ),
    Col(header="age", getter=age),
]

NAMESPACE_COLS: list[Col[V1Namespace]] = [
    Col(header="name", getter=name),
    Col(header="age", getter=age),
]

POD_COLS: list[Col[V1Pod]] = [
    Col(header="namespace", getter=namespace),
    Col(header="name", getter=name),
    Col(header="ready", getter=pod_containers_ready),
    Col(header="status", getter=lambda pod: pod.status.phase),
    Col(header="age", getter=age),
    Col(header="pod-ip", getter=lambda pod: pod.status.pod_ip, verbosity=ColumnVerbosity.Wide),
]

SERVICE_COLS: list[Col[V1Service]] = [
    Col(header="namespace", getter=namespace),
    Col(header="name", getter=name),
    Col(header="cluster-ip", getter=lambda service: service.spec.cluster_ip),
    Col(
        header="ports",
        getter=lambda obj: ", ".join(
            f"{port.name}:{port.port}/{port.protocol}" for port in obj.spec.ports
        ),
    ),
    Col(header="age", getter=age),
]

RESOURCE_COLS: Mapping[RESOURCE, list[Col]] = {
    "node": NODE_COLS,
    "namespace": NAMESPACE_COLS,
    "pod": POD_COLS,
    "service": SERVICE_COLS,
}


class ResourcesTable(Widget):
    namespace: str | None = reactive(None)
    resource: RESOURCE = reactive("pod")
    filter: str = reactive("*")
    raw_results: list[object] = reactive(list, always_update=True)
    results: list[object] = reactive(list, always_update=True)
    col_verbosity: ColumnVerbosity = reactive(ColumnVerbosity.Normal)

    BINDINGS = [
        Binding("w", "cycle_col_verbosity", "Cycle column verbosity"),
    ]

    async def api(self) -> ApiClient:
        return await self.app.api()

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Input(name="Namespace", id="namespace", value="", placeholder="all"),
            Input(name="Resource", id="resource", value="pod"),
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
        match resource, namespace:
            case "node", _:
                return (await list_core_v1_node(self.app.klient)).items
            case "namespace", _:
                return (await list_core_v1_namespace(self.app.klient)).items
            case "pod", None:
                return (await list_core_v1_pod_for_all_namespaces(self.app.klient)).items
            case "pod", namespace:
                return (
                    await list_core_v1_namespaced_pod(self.app.klient, namespace=namespace)
                ).items
            case "service", None:
                return (await list_core_v1_service_for_all_namespaces(self.app.klient)).items
            case "service", namespace:
                return (
                    await list_core_v1_namespaced_service(self.app.klient, namespace=namespace)
                ).items
            case _:
                self.app.bell()
                return []

    def watch_results(self, results: list[object]) -> None:
        dt = self.query_one(DataTable)
        dt.clear()
        dt.columns.clear()

        cols = [
            c for c in RESOURCE_COLS[self.resource] if int(c.verbosity) <= int(self.col_verbosity)
        ]

        dt.add_columns(*(c.header.upper() for c in cols))

        for o in results:
            dt.add_row(*(c.getter(o) for c in cols))

    async def namespace_names(self) -> set[str]:
        return {
            ns.metadata.name for ns in (await CoreV1Api(await self.api()).list_namespace()).items
        }

    def selected_resource(self) -> object:
        return self.results[self.query_one(DataTable).cursor_cell.row]

    def on_key(self, event: Key) -> None:
        if event.key == "slash":
            self.get_widget_by_id("filter").focus()
        elif event.key == "semicolon":
            self.get_widget_by_id("resource").focus()
        elif event.key == "apostrophe":
            self.get_widget_by_id("namespace").focus()
        elif event.key == "escape":
            self.query_one(DataTable).focus()

        if self.query_one(DataTable).has_focus:
            if self.resource == "namespace" and event.key == "enter":
                self.get_widget_by_id("namespace").value = self.selected_resource().metadata.name
                self.get_widget_by_id("resource").value = "pod"

    async def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "resource":
            if event.value in RESOURCE_ALIASES:
                self.resource = event.value
                self.get_widget_by_id("filter").value = ""
                event.input.remove_class("bad")
            else:
                event.input.add_class("bad")
        elif event.input.id == "filter":
            self.filter = event.value
        elif event.input.id == "namespace":
            if event.value == "":
                self.namespace = None
                event.input.remove_class("bad")
            elif event.value in (await self.namespace_names()):
                self.namespace = event.value
                event.input.remove_class("bad")
            else:
                event.input.add_class("bad")

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one(DataTable).focus()

    def action_cycle_col_verbosity(self) -> None:
        self.col_verbosity = ColumnVerbosity((self.col_verbosity + 1) % (max(ColumnVerbosity) + 1))
        self.results = self.results  # force results watcher to run


class KludgeApp(App[None]):
    CSS_PATH = "kludge.css"
    BINDINGS = []
    SCREENS = {}

    def __init__(self):
        super().__init__()

        self.klient = Klient(Konfig.build())

    def compose(self) -> ComposeResult:
        yield ResourcesTable()
