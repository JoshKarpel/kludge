from asyncio import sleep
from typing import ClassVar

from counterweight.components import component
from counterweight.elements import Div, Text
from counterweight.events import KeyPressed
from counterweight.hooks import use_effect, use_state
from counterweight.keys import Key
from counterweight.styles.utilities import *
from pydantic import BaseModel, ConfigDict
from structlog import get_logger

from kludge.klient import Klient
from kludge.konfig import Konfig

logger = get_logger()

FOCUS_ORDER = {
    "resources": "namespaces",
    "namespaces": "resources",
}


@component
def root() -> Div:
    names_to_resources, set_names_to_resources = use_state(())  # type: ignore[var-annotated]
    resource_filter, set_resource_filter = use_state("pods")
    selected_resource, set_selected_resource = use_state(None)
    namespace_filter, set_namespace_filter = use_state("default")
    selected_namespace, set_selected_namespace = use_state("default")
    namespaces, set_namespaces = use_state(())
    instances, set_instances = use_state(())  # type: ignore[var-annotated]
    focus, set_focus = use_state("resources")

    def on_key(event: KeyPressed) -> None:
        match focus, event.key:
            case "resources", Key.Backspace:
                rf = resource_filter[:-1]
                set_resource_filter(rf)
                if rf in names_to_resources:
                    set_selected_resource(names_to_resources[rf])
            case "namespaces", Key.Backspace:
                nf = namespace_filter[:-1]
                set_namespace_filter(nf)
                if nf in namespaces:
                    set_selected_namespace(nf)
            case "resources", c if c.isprintable() and len(c) == 1:
                rf = resource_filter + c
                set_resource_filter(rf)
                if rf in names_to_resources:
                    set_selected_resource(names_to_resources[rf])
            case "namespaces", c if c.isprintable() and len(c) == 1:
                nf = namespace_filter + c
                set_namespace_filter(nf)
                if nf in namespaces:
                    set_selected_namespace(nf)
            case _, Key.Tab:
                set_focus(lambda f: FOCUS_ORDER[f])

    async def watch_resources() -> None:
        async with Klient(Konfig.build()) as klient:
            while True:
                discovered_resources = await discover_resources(klient)
                names_to_resources = {}
                for r in discovered_resources:
                    for n in r.names:
                        names_to_resources[n] = r
                set_names_to_resources(names_to_resources)
                set_selected_resource(lambda sr: names_to_resources["pods"] if sr is None else sr)
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
                    path=selected_resource.collection_url(selected_namespace),
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
                style=row | weight_none,
                children=[
                    Text(
                        style=weight_none
                        | border_lightrounded
                        | (border_amber_600 if focus == "resources" else None),
                        content=f"Resource: {resource_filter}",
                    ),
                    Text(
                        style=weight_none
                        | border_lightrounded
                        | (border_amber_600 if focus == "namespaces" else None),
                        content=f"Namespace: {namespace_filter}",
                    ),
                ],
            ),
            Div(
                style=col | border_lightrounded | pad_x_1 | align_self_stretch,
                children=[
                    Text(
                        style=weight_none,
                        content=instance["metadata"]["name"],
                    )
                    for instance in instances
                ],
            ),
        ],
    )


class Resource(BaseModel):
    group: str | None
    groupVersion: str
    name: str
    kind: str
    singularName: str
    namespaced: bool
    shortNames: tuple[str, ...] = ()
    verbs: tuple[str, ...]

    model_config: ClassVar[ConfigDict] = {
        "frozen": True,
        "extras": "ignore",
    }

    def collection_url(self, namespace: str) -> str:
        parts = []

        if self.group is None:
            parts.append("api")
        else:
            raise NotImplementedError

        parts.append(self.groupVersion)

        if self.namespaced:
            parts.append("namespaces")
            parts.append(namespace)

        parts.append(self.name)

        return "/" + "/".join(parts)

    def instance_url(self, namespace: str, name: str) -> str:
        return "/".join((self.collection_url(namespace), name))

    @property
    def names(self) -> set[str]:
        return {self.name, self.singularName, *self.shortNames} - {""}


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
                Resource.model_validate(resource | {"group": None, "groupVersion": version})
            )

    return tuple(resources)
