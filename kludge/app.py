from asyncio import sleep
from typing import ClassVar, Literal

from counterweight.components import component
from counterweight.elements import Div, Text
from counterweight.events import KeyPressed
from counterweight.hooks import Setter, use_effect, use_state
from counterweight.keys import Key
from counterweight.styles.utilities import *
from pydantic import BaseModel, ConfigDict
from structlog import get_logger

from kludge.klient import Klient
from kludge.konfig import Konfig

logger = get_logger()

FOCUS = {
    0: "resources",
    1: "namespaces",
}


@component
def root() -> Div:
    names_to_resources, set_names_to_resources = use_state({})
    resource_filter, set_resource_filter = use_state("pods")
    selected_resource, set_selected_resource = use_state(None)
    namespace_filter, set_namespace_filter = use_state("default")
    selected_namespace, set_selected_namespace = use_state("default")
    namespaces, set_namespaces = use_state(())
    instances, set_instances = use_state(())
    focus, set_focus = use_state(0)

    def on_key(event: KeyPressed) -> None:
        match event.key:
            case Key.Tab:
                set_focus(lambda f: (f + 1) % len(FOCUS))
            case Key.BackTab:
                set_focus(lambda f: (f - 1) % len(FOCUS))

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
                set_selected_resource(lambda sr: "pods" if sr is None else sr)
                logger.debug("watch_resources", names_to_resources=names_to_resources)

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
                logger.debug("watch_namespaces", namespaces=ns)

                await sleep(60)

    async def watch_resource() -> None:
        logger.debug(
            "watch_resource",
            selected_resource=selected_resource,
            selected_namespace=selected_namespace,
        )

        if selected_resource is None:
            return

        async with Klient(Konfig.build()) as klient:
            while True:
                async with await klient.request(
                    method="get",
                    path=names_to_resources[selected_resource].collection_url(selected_namespace),
                ) as response:
                    j = await response.json()

                logger.debug("watch_resource", j=j)
                set_instances(j["items"])

                await sleep(5)

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
            Div(
                style=col | border_lightrounded | pad_x_1 | align_self_stretch,
                children=[
                    Text(
                        style=inset_top_center | absolute(y=-1),
                        content=f" {names_to_resources[selected_resource].kind} in {selected_namespace} "
                        if selected_resource
                        else "",
                    )
                ]
                + [
                    Text(
                        style=weight_none,
                        content=instance["metadata"]["name"],
                    )
                    for instance in instances
                ],
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
    b = border_lightrounded | (border_amber_600 if focused else None)

    def on_key(event: KeyPressed) -> None:
        if not focused:
            return

        match event.key:
            case Key.Backspace:
                new_filter_text = filter_text[:-1]
                set_filter_text(new_filter_text)

                if new_filter_text in options:
                    set_selected_option(new_filter_text)

            case c if c.isprintable() and len(c) == 1:
                new_filter_text = filter_text + c
                set_filter_text(new_filter_text)

                if new_filter_text in options:
                    set_selected_option(new_filter_text)

    is_valid = filter_text in options

    children = [
        Text(
            style=weight_none | pad_x_1 | (text_gray_500 if not is_valid else None),
            content=filter_text,
        )
    ]
    typeahead = {o for o in options if o.startswith(filter_text)}
    if focused and not is_valid and typeahead:
        children.append(
            Text(
                style=pad_x_1 | b | absolute(x=-1, y=1),
                content="\n".join(sorted(typeahead, key=lambda o: (len(o), o))[:10]),
            )
        )

    return Div(
        on_key=on_key,
        style=row | b | style,
        children=[
            Text(
                style=weight_none | b | border_right | pad_x_1,
                content=title,
            ),
            Div(
                style=row,
                children=children,
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
        logger.debug("foo", j=j)

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

        logger.debug("group", v=v)

        async with await klient.request(
            method="get", path=f"/apis/{v['groupVersion']}"
        ) as response:
            j = await response.json()
            logger.debug("group", j=j)
            for resource in j["resources"]:
                if "/" in resource["name"]:
                    continue  # TODO: handle subresources

                resources.append(
                    Resource.model_validate(
                        resource | {"core": False, "groupVersion": v["groupVersion"]}
                    )
                )

    return tuple(resources)
