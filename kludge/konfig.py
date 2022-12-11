from __future__ import annotations

import os
from pathlib import Path

from pydantic import BaseModel, Field
from yaml import safe_load


class ClusterInfo(BaseModel):
    certificate_authority: Path = Field(..., alias="certificate-authority")
    server: str


class Cluster(BaseModel):
    name: str
    cluster: ClusterInfo


class UserInfo(BaseModel):
    client_certificate: str = Field(..., alias="client-certificate")
    client_key: str = Field(..., alias="client-key")


class User(BaseModel):
    name: str
    user: UserInfo


class Konfig(BaseModel):
    apiVersion: str
    clusters: list[Cluster]
    users: list[User]

    @classmethod
    def build(cls) -> Konfig:
        path = Path(os.getenv("KUBECONFIG", Path.home() / ".kube" / "config"))

        y = safe_load(path.read_text())

        return cls.parse_obj(y)
