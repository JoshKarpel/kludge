from __future__ import annotations

from kubernetes_asyncio.client import ApiClient, CoreV1Api, V1NodeList, V1PodList
from kubernetes_asyncio.config import load_kube_config
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DataTable, Footer, Header, Input


class ResourcesTable(Widget):
    resource: str = reactive("pods")
    filter: str = reactive("")
    results: list[object] = reactive(list)

    async def api(self) -> ApiClient:
        return await self.app.api()

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Input(name="Command", id="command", value="pods"),
            Input(name="Filter", id="filter"),
            id="inputs",
        )
        dt = DataTable()
        dt.add_column("name")
        dt.focus()
        yield dt

    def watch_resource(self, command) -> None:
        pass  # needed to make the compute fire?

    async def compute_results(self) -> list[object]:
        self.log(f"compute results {self.resource}")
        api = await self.api()
        self.log(api)
        if self.resource == "pods":
            core = CoreV1Api(api)
            pod_list: V1PodList = await core.list_pod_for_all_namespaces()
            return pod_list.items
        elif self.resource == "nodes":
            core = CoreV1Api(api)
            node_list: V1NodeList = await core.list_node()
            return node_list.items
        else:
            self.app.bell()
            return []

    def watch_results(self, resources: list[object]) -> None:
        self.log(f"watch results")
        dt = self.query_one(DataTable)
        dt.clear()
        self.log(dt)
        for o in resources:
            self.log(o.metadata.name)
            dt.add_row(o.metadata.name)
        self.log(dt)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.log("before", self.resource, self.filter)
        if event.input.id == "command":
            self.resource = event.value
        elif event.input.id == "filter":
            self.filter = event.value
        self.log("after", self.resource, self.filter)


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
