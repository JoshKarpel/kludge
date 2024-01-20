from __future__ import annotations

from asyncio import sleep
from datetime import datetime, timezone
from typing import ClassVar, Literal

from counterweight.components import component
from counterweight.elements import Chunk, Div, Text
from counterweight.events import KeyPressed
from counterweight.hooks import Setter, use_effect, use_state
from counterweight.keys import Key
from counterweight.styles.utilities import *
from more_itertools import intersperse
from pydantic import BaseModel, ConfigDict
from structlog import get_logger

from kludge.klient import Klient
from kludge.konfig import Konfig

logger = get_logger()

FOCUS = {
    0: "resources",
    1: "namespaces",
}

DEFAULT_SELECTED_RESOURCE = "pod"


def now() -> datetime:
    return datetime.now(timezone.utc)


@component
def root() -> Div:
    names_to_resources, set_names_to_resources = use_state({})
    resource_filter, set_resource_filter = use_state(DEFAULT_SELECTED_RESOURCE)
    selected_resource, set_selected_resource = use_state(None)
    namespace_filter, set_namespace_filter = use_state("default")
    selected_namespace, set_selected_namespace = use_state("default")
    namespaces, set_namespaces = use_state(())
    resources, set_resources = use_state({"columnDefinitions": [], "items": []})
    last_fetch, set_last_fetch = use_state(None)
    focus, set_focus = use_state(0)
    wide, set_wide = use_state(False)
    use_utc, set_use_utc = use_state(True)

    def on_key(event: KeyPressed) -> None:
        match event.key:
            case Key.Tab:
                set_focus(lambda f: (f + 1) % len(FOCUS))
            case Key.BackTab:
                set_focus(lambda f: (f - 1) % len(FOCUS))
            case Key.ControlW:
                set_wide(lambda w: not w)
            case Key.ControlU:
                set_use_utc(lambda u: not u)

    async def watch_resources() -> None:
        async with Klient(Konfig.build()) as klient:
            while True:
                discovered_resources = await discover_resources(klient)
                names_to_resources = {}
                for r in discovered_resources:
                    if "list" in r.verbs:
                        for n in r.names:
                            names_to_resources[n] = r
                set_names_to_resources(names_to_resources)
                set_selected_resource(
                    lambda sr: DEFAULT_SELECTED_RESOURCE
                    if sr is None and DEFAULT_SELECTED_RESOURCE in names_to_resources
                    else sr
                )

                await sleep(60)

    async def watch_namespaces() -> None:
        async with Klient(Konfig.build()) as klient:
            while True:
                async with await klient.request(
                    method="get", path="/api/v1/namespaces"
                ) as response:
                    j = await response.json()

                ns = tuple(ns["metadata"]["name"] for ns in j["items"])
                set_namespaces(ns)

                await sleep(60)

    async def watch_resource() -> None:
        if selected_resource is None:
            return

        async with Klient(Konfig.build()) as klient:
            while True:
                async with await klient.request(
                    method="get",
                    path=names_to_resources[selected_resource].collection_url(selected_namespace),
                    headers={
                        "Accept": "application/json;as=Table;g=meta.k8s.io;v=v1",  # https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables
                    },
                ) as response:
                    j = await response.json()

                set_resources(j)
                set_last_fetch(now())

                await sleep(1)

    use_effect(watch_resources, ())
    use_effect(watch_namespaces, ())
    use_effect(watch_resource, (selected_resource, selected_namespace))

    return Div(
        style=col,
        on_key=on_key,
        children=[
            Div(
                style=row | weight_none | align_self_stretch,
                children=[
                    filter_pad(
                        title="Resource",
                        filter_text=resource_filter,
                        set_filter_text=set_resource_filter,
                        options=set(names_to_resources.keys()),
                        set_selected_option=set_selected_resource,
                        focused=FOCUS[focus] == "resources",
                        style=weight_1,
                    ),
                    filter_pad(
                        title="Namespace",
                        filter_text=namespace_filter,
                        set_filter_text=set_namespace_filter,
                        options=set(namespaces),
                        set_selected_option=set_selected_namespace,
                        focused=FOCUS[focus] == "namespaces",
                        style=weight_1,
                    ),
                ],
            ),
            resource_table(
                names_to_resources=names_to_resources,
                selected_resource=selected_resource,
                selected_namespace=selected_namespace,
                resources=resources,
                last_fetch=last_fetch,
                use_utc=use_utc,
                wide=wide,
            ),
        ],
    )


@component
def filter_pad(
    title: str,
    filter_text: str,
    set_filter_text: Setter[str],
    options: set[str],
    set_selected_option: Setter[object],
    focused: bool,
    style: Style,
) -> Div:
    typeahead_idx, set_typeahead_idx = use_state(0)

    b = border_lightrounded

    typeahead = sorted(
        (o for o in options if o.startswith(filter_text)),
        key=lambda o: (len(o), o),
    )[:15]
    typeahead_idx = clamp(0, typeahead_idx, len(typeahead) - 1)

    def on_key(event: KeyPressed) -> None:
        if not focused:
            return

        match event.key:
            case Key.Backspace:
                new_filter_text = filter_text[:-1]
                set_filter_text(new_filter_text)

                if new_filter_text in options:
                    set_selected_option(new_filter_text)
                    set_typeahead_idx(0)

            case c if c.isprintable() and len(c) == 1:
                new_filter_text = filter_text + c
                set_filter_text(new_filter_text)

                if new_filter_text in options:
                    set_selected_option(new_filter_text)
                    set_typeahead_idx(0)

            case Key.Down if not is_valid:
                set_typeahead_idx(clamp(0, typeahead_idx + 1, len(typeahead) - 1))

            case Key.Up if not is_valid:
                set_typeahead_idx(clamp(0, typeahead_idx - 1, len(typeahead) - 1))

            case Key.Enter if typeahead_idx is not None:
                set_filter_text(typeahead[typeahead_idx])
                set_selected_option(typeahead[typeahead_idx])
                set_typeahead_idx(0)

    is_valid = filter_text in options

    children = [
        Text(
            style=weight_none | pad_x_1 | (text_gray_500 if not is_valid else None),
            content=filter_text,
        )
    ]
    if focused and not is_valid and typeahead:
        children.append(
            Text(
                style=pad_x_1 | b | absolute(x=-1, y=1) | z(10),
                content=list(
                    intersperse(
                        Chunk.newline(),
                        (
                            Chunk(
                                style=CellStyle(
                                    foreground=cyan_400
                                    if idx == typeahead_idx
                                    else Color.from_name("white")
                                ),
                                content=t,
                            )
                            for idx, t in enumerate(typeahead)
                        ),
                    ),
                ),
            )
        )

    return Div(
        on_key=on_key,
        style=row | b | style,
        children=[
            Text(
                style=weight_none
                | b
                | border_right
                | pad_x_1
                | (text_cyan_400 if focused else None),
                content=title,
            ),
            Div(
                style=row,
                children=children,
            ),
        ],
    )


@component
def resource_table(
    names_to_resources: dict[str, Resource],
    selected_resource: str | None,
    selected_namespace: str,
    resources: dict[str, object],
    last_fetch: datetime | None,
    use_utc: bool,
    wide: bool,
) -> Div:
    return Div(
        style=row | border_lightrounded | pad_x_1 | gap_children_2 | align_self_stretch,
        children=[
            Text(
                style=inset_top_center
                | absolute(y=-1)
                | z(1),  # TODO: z(1) should not be needed here
                content=(
                    f" {names_to_resources[selected_resource].kind} in {selected_namespace} "
                    if names_to_resources[selected_resource].namespaced
                    else f" {names_to_resources[selected_resource].kind} "
                )
                if selected_resource is not None
                else "",
            ),
            Text(
                style=inset_bottom_center | absolute(y=1) | z(1),
                content=f" {last_fetch if use_utc else last_fetch.astimezone():%Y-%m-%d %H:%M:%S %z} "
                if last_fetch is not None
                else " Waiting for first fetch ... ",
            ),
            *(
                Text(
                    style=weight_none,
                    content=list(
                        intersperse(
                            Chunk.newline(),
                            (
                                Chunk(
                                    content=col_def["name"].upper(),
                                    style=CellStyle(bold=True),
                                ),
                                *(
                                    Chunk(content=str(r["cells"][col_idx]))
                                    for r in resources["rows"]
                                ),
                            ),
                        )
                    ),
                )
                for col_idx, col_def in enumerate(resources["columnDefinitions"])
                if wide or col_def["priority"] == 0
            ),
        ],
    )


Verb = Literal[
    "create",
    "delete",
    "deletecollection",
    "get",
    "list",
    "patch",
    "update",
    "watch",
]


class Resource(BaseModel):
    core: bool
    groupVersion: str
    name: str
    kind: str
    singularName: str
    namespaced: bool
    shortNames: tuple[str, ...] = ()
    verbs: tuple[Verb, ...]

    model_config: ClassVar[ConfigDict] = {
        "frozen": True,
        "extras": "ignore",
    }

    def collection_url(self, namespace: str) -> str:
        parts = ["api" if self.core else "apis", self.groupVersion]

        if self.namespaced:
            parts.append("namespaces")
            parts.append(namespace)

        parts.append(self.name)

        return "/" + "/".join(parts)

    def instance_url(self, namespace: str, name: str) -> str:
        return "/".join((self.collection_url(namespace), name))

    @property
    def names(self) -> set[str]:
        return {
            f"{self.groupVersion}/{self.name}" if not self.core else self.name,
            self.singularName,
            *self.shortNames,
        } - {""}


async def discover_resources(klient: Klient) -> tuple[Resource, ...]:
    resources = []

    # Core API
    async with await klient.request(method="get", path="/api") as response:
        j = await response.json()

    for version in j["versions"]:
        async with await klient.request(method="get", path=f"/api/{version}") as response:
            j = await response.json()

        for resource in j["resources"]:
            if "/" in resource["name"]:
                continue  # TODO: handle subresources

            resources.append(
                Resource.model_validate(resource | {"core": True, "groupVersion": version})
            )

    # Everything else
    async with await klient.request(method="get", path="/apis") as response:
        j = await response.json()

    for group in j["groups"]:
        v = group["preferredVersion"]

        async with await klient.request(
            method="get", path=f"/apis/{v['groupVersion']}"
        ) as response:
            j = await response.json()
            for resource in j["resources"]:
                if "/" in resource["name"]:
                    continue  # TODO: handle subresources

                resources.append(
                    Resource.model_validate(
                        resource | {"core": False, "groupVersion": v["groupVersion"]}
                    )
                )

    return tuple(resources)


def clamp(min_: int, val: int, max_: int) -> int:
    return max(min_, min(val, max_))
