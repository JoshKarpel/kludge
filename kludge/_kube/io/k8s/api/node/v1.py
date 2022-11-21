# generated by datamodel-codegen:
#   filename:  v3

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from ...apimachinery.pkg.api import resource
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class Scheduling(BaseModel):
    """
    Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.
    """

    nodeSelector: Optional[dict[str, str]] = Field(
        None,
        description="nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.",
    )
    tolerations: Optional[list[v1.TolerationModel]] = Field(
        None,
        description="tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.",
    )


class Overhead(BaseModel):
    """
    Overhead structure represents the resource overhead associated with running a pod.
    """

    podFixed: Optional[dict[str, resource.QuantityModel3]] = Field(
        None,
        description="PodFixed represents the fixed resource overhead associated with running a pod.",
    )


class RuntimeClass(BaseModel):
    """
    RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used to determine which container runtime is used to run all containers in a pod. RuntimeClasses are manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is responsible for resolving the RuntimeClassName reference before running the pod.  For more details, see https://kubernetes.io/docs/concepts/containers/runtime-class/
    """

    apiVersion: Optional[str] = Field(
        None,
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    handler: str = Field(
        ...,
        description='Handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.',
    )
    kind: Optional[str] = Field(
        None,
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: v1_1.ObjectMetaModel8 = Field(
        {},
        description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    overhead: Optional[Overhead] = Field(
        None,
        description="Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see\n https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/",
    )
    scheduling: Optional[Scheduling] = Field(
        None,
        description="Scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.",
    )


class RuntimeClassList(BaseModel):
    """
    RuntimeClassList is a list of RuntimeClass objects.
    """

    apiVersion: Optional[str] = Field(
        None,
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: list[RuntimeClass] = Field(..., description="Items is a list of schema objects.")
    kind: Optional[str] = Field(
        None,
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: v1_1.ListMetaModel8 = Field(
        {},
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
