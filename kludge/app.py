from __future__ import annotations

import sys
from collections.abc import Mapping
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from enum import Enum
from fnmatch import fnmatch
from typing import Callable, Generic, Iterable, Iterator, Literal, TypeVar

import yaml
from click import edit
from pydantic import BaseModel
from rich.console import RenderableType
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.events import Key
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DataTable, Input
from textual_autocomplete import AutoComplete, Dropdown, DropdownItem

from kludge.klient import Klient
from kludge.konfig import Konfig
from kludge.kube import (
    CoreV1Namespace,
    CoreV1Node,
    CoreV1Pod,
    CoreV1Service,
    delete_core_v1_namespace,
    delete_core_v1_namespaced_pod,
    delete_core_v1_namespaced_service,
    delete_core_v1_node,
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


def now() -> datetime:
    return datetime.now(timezone.utc)


def human_time(delta: timedelta) -> str:
    parts = []
    if delta.days > 0:
        parts.append(f"{delta.days}d")

    hours, remainder = divmod(delta.seconds, 3600)
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
    return human_time(now() - obj.metadata.creation_timestamp)


def pod_containers_ready(pod: CoreV1Pod) -> str:
    container_statuses = pod.status.container_statuses
    if container_statuses is None:
        return f"0/0"
    else:
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


NODE_COLS: list[Col[CoreV1Node]] = [
    Col(header="name", getter=name),
    Col(
        header="status",
        getter=lambda obj: NODE_STATUS_MAP[
            first_item_with_attr_value(obj.status.conditions, "type", "Ready").status
        ],
    ),
    Col(header="age", getter=age),
]

NAMESPACE_COLS: list[Col[CoreV1Namespace]] = [
    Col(header="name", getter=name),
    Col(header="age", getter=age),
]

POD_COLS: list[Col[CoreV1Pod]] = [
    Col(header="namespace", getter=namespace),
    Col(header="name", getter=name),
    Col(header="ready", getter=pod_containers_ready),
    Col(
        header="status",
        getter=lambda pod: f"Terminating (grace: {human_time(pod.metadata.deletion_timestamp - now())})"
        if pod.metadata.deletion_timestamp is not None
        else pod.status.phase,
    ),
    Col(header="age", getter=age),
    Col(header="pod-ip", getter=lambda pod: pod.status.pod_ip, verbosity=ColumnVerbosity.Wide),
]

SERVICE_COLS: list[Col[CoreV1Service]] = [
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
    raw_results: list[BaseModel] = reactive(list, always_update=True)
    results: list[BaseModel] = reactive(list, always_update=True)
    col_verbosity: ColumnVerbosity = reactive(ColumnVerbosity.Normal)
    namespaces: list[CoreV1Namespace] = reactive(list)

    BINDINGS = [
        Binding("w", "cycle_col_verbosity", "Cycle column verbosity"),
        Binding("e", "edit_yaml", "Edit YAML for selected resource"),
        Binding("d", "delete_selected_resource", "Delete the selected resource"),
    ]

    def compose(self) -> ComposeResult:
        yield Horizontal(
            AutoComplete(
                Input(name="Namespace", id="namespace", value="", placeholder="all"),
                Dropdown(
                    items=self.namespace_dropdown_items,
                    id="namespace-dropdown",
                ),
                classes="w-1fr",
            ),
            AutoComplete(
                Input(name="Resource", id="resource", value="pod"),
                Dropdown(
                    items=[DropdownItem(k) for k in RESOURCE_ALIASES.keys()],
                    id="resource-dropdown",
                ),
                classes="w-1fr",
            ),
            Input(name="Filter", id="filter", value="", placeholder="*", classes="w-1fr"),
            id="inputs",
        )

        yield DataTable()

    async def on_mount(self):
        self.set_interval(1, self.refresh_query)
        self.set_interval(1, self.refresh_namespaces)
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

    async def refresh_namespaces(self) -> None:
        self.namespaces = (await list_core_v1_namespace(self.app.klient)).items

    def namespace_names(self) -> set[str]:
        return {ns.metadata.name for ns in self.namespaces}

    def namespace_dropdown_items(self, value: str, cursor_position: int) -> list[DropdownItem]:
        filtered = (ns for ns in self.namespace_names() if fnmatch(ns, "*" + "*".join(value) + "*"))
        srted = sorted(filtered, key=lambda ns: longest_match_length(value, ns), reverse=True)
        return [DropdownItem(ns) for ns in srted]

    def selected_resource(self) -> BaseModel:
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
            elif event.value in self.namespace_names():
                self.namespace = event.value
                event.input.remove_class("bad")
            else:
                event.input.add_class("bad")

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one(DataTable).focus()

    def action_cycle_col_verbosity(self) -> None:
        self.col_verbosity = ColumnVerbosity((self.col_verbosity + 1) % (max(ColumnVerbosity) + 1))
        self.results = self.results  # force results watcher to run

    def action_edit_yaml(self) -> None:
        current = yaml.dump(self.selected_resource().dict(by_alias=True, exclude_defaults=True))
        with self.app.suspend():
            new = edit(current)
            self.log(new)
            # TODO: post it back!

    async def action_delete_selected_resource(self) -> None:
        selected_metadata = self.selected_resource().metadata
        name = selected_metadata.name
        namespace = selected_metadata.namespace

        # TODO: ask for confirmation

        match self.resource, self.namespace:
            case "node", _:
                await delete_core_v1_node(self.app.klient, name=name)
            case "namespace", _:
                await delete_core_v1_namespace(self.app.klient, name=name)
            case "pod", None:
                await delete_core_v1_namespaced_pod(self.app.klient, namespace=namespace, name=name)
            case "pod", namespace:
                await delete_core_v1_namespaced_pod(self.app.klient, namespace=namespace, name=name)
            case "service", None:
                await delete_core_v1_namespaced_service(
                    self.app.klient, namespace=namespace, name=name
                )
            case "service", namespace:
                await delete_core_v1_namespaced_service(
                    self.app.klient, namespace=namespace, name=name
                )
            case _:
                self.app.bell()


class KludgeApp(App[None]):
    CSS_PATH = "kludge.css"
    BINDINGS = []
    SCREENS = {}

    def __init__(self):
        super().__init__()

        self.klient = Klient(Konfig.build())

    def compose(self) -> ComposeResult:
        yield ResourcesTable()

    @contextmanager
    def suspend(self) -> Iterator[None]:
        driver = self._driver

        if driver is not None:
            driver.stop_application_mode()
            driver.exit_event.clear()  # type: ignore[attr-defined]
            with redirect_stdout(sys.__stdout__), redirect_stderr(sys.__stderr__):
                yield
            driver.start_application_mode()


def longest_match_length(a: str, b: str) -> int:
    return SequenceMatcher(a=a, b=b).find_longest_match().size
