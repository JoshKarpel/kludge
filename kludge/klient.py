# cluster = config.clusters[0].cluster
# user = config.users[0].user
#
# sslcontext = ssl.create_default_context(cafile=cluster.certificate_authority)
# sslcontext.load_cert_chain(certfile=user.client_certificate, keyfile=user.client_key)
#
# async with ClientSession() as session:
#     async with session.get(
#             f"{cluster.server}/apis/apps/v1/deployments", ssl=sslcontext
#     ) as response:
#         j = await response.json()
#         console.print(j)
#         console.print(DeploymentList.parse_obj(j))
#
from __future__ import annotations

import ssl
from functools import cached_property
from types import TracebackType
from typing import Type
from urllib.parse import urljoin

from aiohttp import ClientSession
from aiohttp.client import _RequestContextManager

from kludge.konfig import Konfig


class Klient:
    def __init__(self, konfig: Konfig):
        self.konfig = konfig
        self._session = None

    async def session(self) -> ClientSession:
        if self._session is not None:
            return self._session

        self._session = ClientSession()
        return self._session

    async def __aenter__(self) -> Klient:
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await (await self.session()).close()

    @cached_property
    def sslcontext(self):
        cluster = self.konfig.clusters[0].cluster
        user = self.konfig.users[0].user

        sslcontext = ssl.create_default_context(cafile=cluster.certificate_authority)
        sslcontext.load_cert_chain(certfile=user.client_certificate, keyfile=user.client_key)

        return sslcontext

    def url(self, path: str) -> str:
        return urljoin(self.konfig.clusters[0].cluster.server, path)

    async def get(self, path: str) -> _RequestContextManager:
        return (await self.session()).get(url=self.url(path), ssl=self.sslcontext)
