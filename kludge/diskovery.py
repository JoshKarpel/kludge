from __future__ import annotations

from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict

from kludge.klient import Klient

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
        "extra": "ignore",
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

    # TODO: do all of these concurrently, or use more efficient discovery method

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
