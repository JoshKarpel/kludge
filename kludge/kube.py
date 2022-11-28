from __future__ import annotations

from aiohttp import ClientSession
from pydantic import BaseModel, Field


class AuthenticationV1BoundObjectReference(BaseModel):
    """
    Original name: io.k8s.api.authentication.v1.BoundObjectReference
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("BoundObjectReference", alias="kind")
    name: str | None = Field(..., alias="name")
    uid: str | None = Field(..., alias="uid")


class AuthenticationV1TokenRequest(BaseModel):
    """
    Original name: io.k8s.api.authentication.v1.TokenRequest
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("TokenRequest", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: AuthenticationV1TokenRequestSpec = Field(default={}, alias="spec")
    status: AuthenticationV1TokenRequestStatus = Field(default={}, alias="status")


class AuthenticationV1TokenRequestStatus(BaseModel):
    """
    Original name: io.k8s.api.authentication.v1.TokenRequestStatus
    """

    expiration_timestamp: MetaV1Time = Field(default={}, alias="expirationTimestamp")
    token: str = Field(default="", alias="token")


class AutoscalingV1Scale(BaseModel):
    """
    Original name: io.k8s.api.autoscaling.v1.Scale
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("Scale", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: AutoscalingV1ScaleSpec = Field(default={}, alias="spec")
    status: AutoscalingV1ScaleStatus = Field(default={}, alias="status")


class AutoscalingV1ScaleSpec(BaseModel):
    """
    Original name: io.k8s.api.autoscaling.v1.ScaleSpec
    """

    replicas: int | None = Field(..., alias="replicas")


class AutoscalingV1ScaleStatus(BaseModel):
    """
    Original name: io.k8s.api.autoscaling.v1.ScaleStatus
    """

    replicas: int = Field(default=0, alias="replicas")
    selector: str | None = Field(..., alias="selector")


class CoreV1AWSElasticBlockStoreVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AWSElasticBlockStoreVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    partition: int | None = Field(..., alias="partition")
    read_only: bool | None = Field(..., alias="readOnly")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1Affinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Affinity
    """

    node_affinity: CoreV1NodeAffinity | None = Field(..., alias="nodeAffinity")
    pod_affinity: CoreV1PodAffinity | None = Field(..., alias="podAffinity")
    pod_anti_affinity: CoreV1PodAntiAffinity | None = Field(..., alias="podAntiAffinity")


class CoreV1AttachedVolume(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AttachedVolume
    """

    device_path: str = Field(default="", alias="devicePath")
    name: str = Field(default="", alias="name")


class CoreV1AzureDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AzureDiskVolumeSource
    """

    caching_mode: str | None = Field(..., alias="cachingMode")
    disk_name: str = Field(default="", alias="diskName")
    disk_uri: str = Field(default="", alias="diskURI")
    fs_type: str | None = Field(..., alias="fsType")
    kind: str | None = Field("AzureDiskVolumeSource", alias="kind")
    read_only: bool | None = Field(..., alias="readOnly")


class CoreV1AzureFilePersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AzureFilePersistentVolumeSource
    """

    read_only: bool | None = Field(..., alias="readOnly")
    secret_name: str = Field(default="", alias="secretName")
    secret_namespace: str | None = Field(..., alias="secretNamespace")
    share_name: str = Field(default="", alias="shareName")


class CoreV1AzureFileVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AzureFileVolumeSource
    """

    read_only: bool | None = Field(..., alias="readOnly")
    secret_name: str = Field(default="", alias="secretName")
    share_name: str = Field(default="", alias="shareName")


class CoreV1Binding(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Binding
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("Binding", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    target: CoreV1ObjectReference = Field(default={}, alias="target")


class CoreV1CinderPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CinderPersistentVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    read_only: bool | None = Field(..., alias="readOnly")
    secret_ref: CoreV1SecretReference | None = Field(..., alias="secretRef")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1CinderVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CinderVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    read_only: bool | None = Field(..., alias="readOnly")
    secret_ref: CoreV1LocalObjectReference | None = Field(..., alias="secretRef")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1ClientIPConfig(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ClientIPConfig
    """

    timeout_seconds: int | None = Field(..., alias="timeoutSeconds")


class CoreV1ComponentCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ComponentCondition
    """

    error: str | None = Field(..., alias="error")
    message: str | None = Field(..., alias="message")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1ComponentStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ComponentStatus
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    conditions: list[CoreV1ComponentCondition] | None = Field(..., alias="conditions")
    kind: str | None = Field("ComponentStatus", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")


class CoreV1ComponentStatusList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ComponentStatusList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1ComponentStatus] = Field(..., alias="items")
    kind: str | None = Field("ComponentStatusList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1ConfigMapEnvSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapEnvSource
    """

    name: str | None = Field(..., alias="name")
    optional: bool | None = Field(..., alias="optional")


class CoreV1ConfigMapKeySelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapKeySelector
    """

    key: str = Field(default="", alias="key")
    name: str | None = Field(..., alias="name")
    optional: bool | None = Field(..., alias="optional")


class CoreV1ConfigMapList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1ConfigMap] = Field(..., alias="items")
    kind: str | None = Field("ConfigMapList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1ConfigMapNodeConfigSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapNodeConfigSource
    """

    kubelet_config_key: str = Field(default="", alias="kubeletConfigKey")
    name: str = Field(default="", alias="name")
    namespace: str = Field(default="", alias="namespace")
    resource_version: str | None = Field(..., alias="resourceVersion")
    uid: str | None = Field(..., alias="uid")


class CoreV1ConfigMapProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapProjection
    """

    items: list[CoreV1KeyToPath] | None = Field(..., alias="items")
    name: str | None = Field(..., alias="name")
    optional: bool | None = Field(..., alias="optional")


class CoreV1ConfigMapVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapVolumeSource
    """

    default_mode: int | None = Field(..., alias="defaultMode")
    items: list[CoreV1KeyToPath] | None = Field(..., alias="items")
    name: str | None = Field(..., alias="name")
    optional: bool | None = Field(..., alias="optional")


class CoreV1ContainerPort(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerPort
    """

    container_port: int = Field(default=0, alias="containerPort")
    host_ip: str | None = Field(..., alias="hostIP")
    host_port: int | None = Field(..., alias="hostPort")
    name: str | None = Field(..., alias="name")
    protocol: str = Field(default="TCP", alias="protocol")


class CoreV1ContainerState(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerState
    """

    running: CoreV1ContainerStateRunning | None = Field(..., alias="running")
    terminated: CoreV1ContainerStateTerminated | None = Field(..., alias="terminated")
    waiting: CoreV1ContainerStateWaiting | None = Field(..., alias="waiting")


class CoreV1ContainerStateRunning(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStateRunning
    """

    started_at: MetaV1Time = Field(default={}, alias="startedAt")


class CoreV1ContainerStateTerminated(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStateTerminated
    """

    container_id: str | None = Field(..., alias="containerID")
    exit_code: int = Field(default=0, alias="exitCode")
    finished_at: MetaV1Time = Field(default={}, alias="finishedAt")
    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")
    signal: int | None = Field(..., alias="signal")
    started_at: MetaV1Time = Field(default={}, alias="startedAt")


class CoreV1ContainerStateWaiting(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStateWaiting
    """

    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")


class CoreV1ContainerStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStatus
    """

    container_id: str | None = Field(..., alias="containerID")
    image: str = Field(default="", alias="image")
    image_id: str = Field(default="", alias="imageID")
    last_state: CoreV1ContainerState = Field(default={}, alias="lastState")
    name: str = Field(default="", alias="name")
    ready: bool = Field(default=False, alias="ready")
    restart_count: int = Field(default=0, alias="restartCount")
    started: bool | None = Field(..., alias="started")
    state: CoreV1ContainerState = Field(default={}, alias="state")


class CoreV1DaemonEndpoint(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DaemonEndpoint
    """

    port: int = Field(default=0, alias="Port")


class CoreV1DownwardAPIProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DownwardAPIProjection
    """

    items: list[CoreV1DownwardAPIVolumeFile] | None = Field(..., alias="items")


class CoreV1DownwardAPIVolumeFile(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DownwardAPIVolumeFile
    """

    field_ref: CoreV1ObjectFieldSelector | None = Field(..., alias="fieldRef")
    mode: int | None = Field(..., alias="mode")
    path: str = Field(default="", alias="path")
    resource_field_ref: CoreV1ResourceFieldSelector | None = Field(..., alias="resourceFieldRef")


class CoreV1DownwardAPIVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DownwardAPIVolumeSource
    """

    default_mode: int | None = Field(..., alias="defaultMode")
    items: list[CoreV1DownwardAPIVolumeFile] | None = Field(..., alias="items")


class CoreV1EmptyDirVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EmptyDirVolumeSource
    """

    medium: str | None = Field(..., alias="medium")
    size_limit: iok8sapimachinerypkgapiresourceQuantity | None = Field(..., alias="sizeLimit")


class CoreV1EndpointAddress(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointAddress
    """

    hostname: str | None = Field(..., alias="hostname")
    ip: str = Field(default="", alias="ip")
    node_name: str | None = Field(..., alias="nodeName")
    target_ref: CoreV1ObjectReference | None = Field(..., alias="targetRef")


class CoreV1EndpointPort(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointPort
    """

    app_protocol: str | None = Field(..., alias="appProtocol")
    name: str | None = Field(..., alias="name")
    port: int = Field(default=0, alias="port")
    protocol: str | None = Field(..., alias="protocol")


class CoreV1EndpointSubset(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointSubset
    """

    addresses: list[CoreV1EndpointAddress] | None = Field(..., alias="addresses")
    not_ready_addresses: list[CoreV1EndpointAddress] | None = Field(..., alias="notReadyAddresses")
    ports: list[CoreV1EndpointPort] | None = Field(..., alias="ports")


class CoreV1Endpoints(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Endpoints
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("Endpoints", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    subsets: list[CoreV1EndpointSubset] | None = Field(..., alias="subsets")


class CoreV1EndpointsList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointsList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1Endpoints] = Field(..., alias="items")
    kind: str | None = Field("EndpointsList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1EnvFromSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EnvFromSource
    """

    config_map_ref: CoreV1ConfigMapEnvSource | None = Field(..., alias="configMapRef")
    prefix: str | None = Field(..., alias="prefix")
    secret_ref: CoreV1SecretEnvSource | None = Field(..., alias="secretRef")


class CoreV1EnvVar(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EnvVar
    """

    name: str = Field(default="", alias="name")
    value: str | None = Field(..., alias="value")
    value_from: CoreV1EnvVarSource | None = Field(..., alias="valueFrom")


class CoreV1EnvVarSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EnvVarSource
    """

    config_map_key_ref: CoreV1ConfigMapKeySelector | None = Field(..., alias="configMapKeyRef")
    field_ref: CoreV1ObjectFieldSelector | None = Field(..., alias="fieldRef")
    resource_field_ref: CoreV1ResourceFieldSelector | None = Field(..., alias="resourceFieldRef")
    secret_key_ref: CoreV1SecretKeySelector | None = Field(..., alias="secretKeyRef")


class CoreV1EphemeralVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EphemeralVolumeSource
    """

    volume_claim_template: CoreV1PersistentVolumeClaimTemplate | None = Field(
        ..., alias="volumeClaimTemplate"
    )


class CoreV1Event(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Event
    """

    action: str | None = Field(..., alias="action")
    api_version: str | None = Field("v1", alias="apiVersion")
    count: int | None = Field(..., alias="count")
    event_time: MetaV1MicroTime = Field(default={}, alias="eventTime")
    first_timestamp: MetaV1Time = Field(default={}, alias="firstTimestamp")
    involved_object: CoreV1ObjectReference = Field(default={}, alias="involvedObject")
    kind: str | None = Field("Event", alias="kind")
    last_timestamp: MetaV1Time = Field(default={}, alias="lastTimestamp")
    message: str | None = Field(..., alias="message")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    reason: str | None = Field(..., alias="reason")
    related: CoreV1ObjectReference | None = Field(..., alias="related")
    reporting_component: str = Field(default="", alias="reportingComponent")
    reporting_instance: str = Field(default="", alias="reportingInstance")
    series: CoreV1EventSeries | None = Field(..., alias="series")
    source: CoreV1EventSource = Field(default={}, alias="source")
    type: str | None = Field(..., alias="type")


class CoreV1EventList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EventList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1Event] = Field(..., alias="items")
    kind: str | None = Field("EventList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1EventSeries(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EventSeries
    """

    count: int | None = Field(..., alias="count")
    last_observed_time: MetaV1MicroTime = Field(default={}, alias="lastObservedTime")


class CoreV1EventSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EventSource
    """

    component: str | None = Field(..., alias="component")
    host: str | None = Field(..., alias="host")


class CoreV1FlockerVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.FlockerVolumeSource
    """

    dataset_name: str | None = Field(..., alias="datasetName")
    dataset_uuid: str | None = Field(..., alias="datasetUUID")


class CoreV1GCEPersistentDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GCEPersistentDiskVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    partition: int | None = Field(..., alias="partition")
    pd_name: str = Field(default="", alias="pdName")
    read_only: bool | None = Field(..., alias="readOnly")


class CoreV1GRPCAction(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GRPCAction
    """

    port: int = Field(default=0, alias="port")
    service: str = Field(default="", alias="service")


class CoreV1GitRepoVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GitRepoVolumeSource
    """

    directory: str | None = Field(..., alias="directory")
    repository: str = Field(default="", alias="repository")
    revision: str | None = Field(..., alias="revision")


class CoreV1GlusterfsPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GlusterfsPersistentVolumeSource
    """

    endpoints: str = Field(default="", alias="endpoints")
    endpoints_namespace: str | None = Field(..., alias="endpointsNamespace")
    path: str = Field(default="", alias="path")
    read_only: bool | None = Field(..., alias="readOnly")


class CoreV1GlusterfsVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GlusterfsVolumeSource
    """

    endpoints: str = Field(default="", alias="endpoints")
    path: str = Field(default="", alias="path")
    read_only: bool | None = Field(..., alias="readOnly")


class CoreV1HTTPGetAction(BaseModel):
    """
    Original name: io.k8s.api.core.v1.HTTPGetAction
    """

    host: str | None = Field(..., alias="host")
    http_headers: list[CoreV1HTTPHeader] | None = Field(..., alias="httpHeaders")
    path: str | None = Field(..., alias="path")
    port: iok8sapimachinerypkgutilintstrIntOrString = Field(default={}, alias="port")
    scheme: str | None = Field(..., alias="scheme")


class CoreV1HTTPHeader(BaseModel):
    """
    Original name: io.k8s.api.core.v1.HTTPHeader
    """

    name: str = Field(default="", alias="name")
    value: str = Field(default="", alias="value")


class CoreV1HostPathVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.HostPathVolumeSource
    """

    path: str = Field(default="", alias="path")
    type: str | None = Field(..., alias="type")


class CoreV1KeyToPath(BaseModel):
    """
    Original name: io.k8s.api.core.v1.KeyToPath
    """

    key: str = Field(default="", alias="key")
    mode: int | None = Field(..., alias="mode")
    path: str = Field(default="", alias="path")


class CoreV1Lifecycle(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Lifecycle
    """

    post_start: CoreV1LifecycleHandler | None = Field(..., alias="postStart")
    pre_stop: CoreV1LifecycleHandler | None = Field(..., alias="preStop")


class CoreV1LifecycleHandler(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LifecycleHandler
    """

    exec: CoreV1ExecAction | None = Field(..., alias="exec")
    http_get: CoreV1HTTPGetAction | None = Field(..., alias="httpGet")
    tcp_socket: CoreV1TCPSocketAction | None = Field(..., alias="tcpSocket")


class CoreV1LimitRange(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LimitRange
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("LimitRange", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1LimitRangeSpec = Field(default={}, alias="spec")


class CoreV1LimitRangeList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LimitRangeList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1LimitRange] = Field(..., alias="items")
    kind: str | None = Field("LimitRangeList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1LimitRangeSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LimitRangeSpec
    """

    limits: list[CoreV1LimitRangeItem] = Field(..., alias="limits")


class CoreV1LoadBalancerIngress(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LoadBalancerIngress
    """

    hostname: str | None = Field(..., alias="hostname")
    ip: str | None = Field(..., alias="ip")
    ports: list[CoreV1PortStatus] | None = Field(..., alias="ports")


class CoreV1LoadBalancerStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LoadBalancerStatus
    """

    ingress: list[CoreV1LoadBalancerIngress] | None = Field(..., alias="ingress")


class CoreV1LocalObjectReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LocalObjectReference
    """

    name: str | None = Field(..., alias="name")


class CoreV1LocalVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LocalVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    path: str = Field(default="", alias="path")


class CoreV1NFSVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NFSVolumeSource
    """

    path: str = Field(default="", alias="path")
    read_only: bool | None = Field(..., alias="readOnly")
    server: str = Field(default="", alias="server")


class CoreV1Namespace(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Namespace
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("Namespace", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1NamespaceSpec = Field(default={}, alias="spec")
    status: CoreV1NamespaceStatus = Field(default={}, alias="status")


class CoreV1NamespaceCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NamespaceCondition
    """

    last_transition_time: MetaV1Time = Field(default={}, alias="lastTransitionTime")
    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1NamespaceList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NamespaceList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1Namespace] = Field(..., alias="items")
    kind: str | None = Field("NamespaceList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1NamespaceStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NamespaceStatus
    """

    conditions: list[CoreV1NamespaceCondition] | None = Field(..., alias="conditions")
    phase: str | None = Field(..., alias="phase")


class CoreV1Node(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Node
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("Node", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1NodeSpec = Field(default={}, alias="spec")
    status: CoreV1NodeStatus = Field(default={}, alias="status")


class CoreV1NodeAddress(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeAddress
    """

    address: str = Field(default="", alias="address")
    type: str = Field(default="", alias="type")


class CoreV1NodeAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeAffinity
    """

    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1PreferredSchedulingTerm
    ] | None = Field(..., alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: CoreV1NodeSelector | None = Field(
        ..., alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1NodeCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeCondition
    """

    last_heartbeat_time: MetaV1Time = Field(default={}, alias="lastHeartbeatTime")
    last_transition_time: MetaV1Time = Field(default={}, alias="lastTransitionTime")
    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1NodeConfigSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeConfigSource
    """

    config_map: CoreV1ConfigMapNodeConfigSource | None = Field(..., alias="configMap")


class CoreV1NodeConfigStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeConfigStatus
    """

    active: CoreV1NodeConfigSource | None = Field(..., alias="active")
    assigned: CoreV1NodeConfigSource | None = Field(..., alias="assigned")
    error: str | None = Field(..., alias="error")
    last_known_good: CoreV1NodeConfigSource | None = Field(..., alias="lastKnownGood")


class CoreV1NodeDaemonEndpoints(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeDaemonEndpoints
    """

    kubelet_endpoint: CoreV1DaemonEndpoint = Field(default={}, alias="kubeletEndpoint")


class CoreV1NodeList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1Node] = Field(..., alias="items")
    kind: str | None = Field("NodeList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1NodeSelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSelector
    """

    node_selector_terms: list[CoreV1NodeSelectorTerm] = Field(..., alias="nodeSelectorTerms")


class CoreV1NodeSelectorTerm(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSelectorTerm
    """

    match_expressions: list[CoreV1NodeSelectorRequirement] | None = Field(
        ..., alias="matchExpressions"
    )
    match_fields: list[CoreV1NodeSelectorRequirement] | None = Field(..., alias="matchFields")


class CoreV1NodeSystemInfo(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSystemInfo
    """

    architecture: str = Field(default="", alias="architecture")
    boot_id: str = Field(default="", alias="bootID")
    container_runtime_version: str = Field(default="", alias="containerRuntimeVersion")
    kernel_version: str = Field(default="", alias="kernelVersion")
    kube_proxy_version: str = Field(default="", alias="kubeProxyVersion")
    kubelet_version: str = Field(default="", alias="kubeletVersion")
    machine_id: str = Field(default="", alias="machineID")
    operating_system: str = Field(default="", alias="operatingSystem")
    os_image: str = Field(default="", alias="osImage")
    system_uuid: str = Field(default="", alias="systemUUID")


class CoreV1ObjectFieldSelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ObjectFieldSelector
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    field_path: str = Field(default="", alias="fieldPath")


class CoreV1ObjectReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ObjectReference
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    field_path: str | None = Field(..., alias="fieldPath")
    kind: str | None = Field("ObjectReference", alias="kind")
    name: str | None = Field(..., alias="name")
    namespace: str | None = Field(..., alias="namespace")
    resource_version: str | None = Field(..., alias="resourceVersion")
    uid: str | None = Field(..., alias="uid")


class CoreV1PersistentVolume(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolume
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("PersistentVolume", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1PersistentVolumeSpec = Field(default={}, alias="spec")
    status: CoreV1PersistentVolumeStatus = Field(default={}, alias="status")


class CoreV1PersistentVolumeClaim(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaim
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("PersistentVolumeClaim", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1PersistentVolumeClaimSpec = Field(default={}, alias="spec")
    status: CoreV1PersistentVolumeClaimStatus = Field(default={}, alias="status")


class CoreV1PersistentVolumeClaimCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimCondition
    """

    last_probe_time: MetaV1Time = Field(default={}, alias="lastProbeTime")
    last_transition_time: MetaV1Time = Field(default={}, alias="lastTransitionTime")
    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1PersistentVolumeClaimList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1PersistentVolumeClaim] = Field(..., alias="items")
    kind: str | None = Field("PersistentVolumeClaimList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1PersistentVolumeClaimTemplate(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimTemplate
    """

    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1PersistentVolumeClaimSpec = Field(default={}, alias="spec")


class CoreV1PersistentVolumeClaimVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimVolumeSource
    """

    claim_name: str = Field(default="", alias="claimName")
    read_only: bool | None = Field(..., alias="readOnly")


class CoreV1PersistentVolumeList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1PersistentVolume] = Field(..., alias="items")
    kind: str | None = Field("PersistentVolumeList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1PersistentVolumeStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeStatus
    """

    message: str | None = Field(..., alias="message")
    phase: str | None = Field(..., alias="phase")
    reason: str | None = Field(..., alias="reason")


class CoreV1PhotonPersistentDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PhotonPersistentDiskVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    pd_id: str = Field(default="", alias="pdID")


class CoreV1Pod(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Pod
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("Pod", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1PodSpec = Field(default={}, alias="spec")
    status: CoreV1PodStatus = Field(default={}, alias="status")


class CoreV1PodAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodAffinity
    """

    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1WeightedPodAffinityTerm
    ] | None = Field(..., alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: list[CoreV1PodAffinityTerm] | None = Field(
        ..., alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1PodAntiAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodAntiAffinity
    """

    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1WeightedPodAffinityTerm
    ] | None = Field(..., alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: list[CoreV1PodAffinityTerm] | None = Field(
        ..., alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1PodCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodCondition
    """

    last_probe_time: MetaV1Time = Field(default={}, alias="lastProbeTime")
    last_transition_time: MetaV1Time = Field(default={}, alias="lastTransitionTime")
    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1PodDNSConfigOption(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodDNSConfigOption
    """

    name: str | None = Field(..., alias="name")
    value: str | None = Field(..., alias="value")


class CoreV1PodIP(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodIP
    """

    ip: str | None = Field(..., alias="ip")


class CoreV1PodList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1Pod] = Field(..., alias="items")
    kind: str | None = Field("PodList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1PodOS(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodOS
    """

    name: str = Field(default="", alias="name")


class CoreV1PodReadinessGate(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodReadinessGate
    """

    condition_type: str = Field(default="", alias="conditionType")


class CoreV1PodStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodStatus
    """

    conditions: list[CoreV1PodCondition] | None = Field(..., alias="conditions")
    container_statuses: list[CoreV1ContainerStatus] | None = Field(..., alias="containerStatuses")
    ephemeral_container_statuses: list[CoreV1ContainerStatus] | None = Field(
        ..., alias="ephemeralContainerStatuses"
    )
    host_ip: str | None = Field(..., alias="hostIP")
    init_container_statuses: list[CoreV1ContainerStatus] | None = Field(
        ..., alias="initContainerStatuses"
    )
    message: str | None = Field(..., alias="message")
    nominated_node_name: str | None = Field(..., alias="nominatedNodeName")
    phase: str | None = Field(..., alias="phase")
    pod_ip: str | None = Field(..., alias="podIP")
    pod_i_ps: list[CoreV1PodIP] | None = Field(..., alias="podIPs")
    qos_class: str | None = Field(..., alias="qosClass")
    reason: str | None = Field(..., alias="reason")
    start_time: MetaV1Time | None = Field(..., alias="startTime")


class CoreV1PodTemplate(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodTemplate
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("PodTemplate", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    template: CoreV1PodTemplateSpec = Field(default={}, alias="template")


class CoreV1PodTemplateList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodTemplateList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1PodTemplate] = Field(..., alias="items")
    kind: str | None = Field("PodTemplateList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1PodTemplateSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodTemplateSpec
    """

    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1PodSpec = Field(default={}, alias="spec")


class CoreV1PortStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PortStatus
    """

    error: str | None = Field(..., alias="error")
    port: int = Field(default=0, alias="port")
    protocol: str = Field(default="", alias="protocol")


class CoreV1PortworxVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PortworxVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    read_only: bool | None = Field(..., alias="readOnly")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1PreferredSchedulingTerm(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PreferredSchedulingTerm
    """

    preference: CoreV1NodeSelectorTerm = Field(default={}, alias="preference")
    weight: int = Field(default=0, alias="weight")


class CoreV1Probe(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Probe
    """

    exec: CoreV1ExecAction | None = Field(..., alias="exec")
    failure_threshold: int | None = Field(..., alias="failureThreshold")
    grpc: CoreV1GRPCAction | None = Field(..., alias="grpc")
    http_get: CoreV1HTTPGetAction | None = Field(..., alias="httpGet")
    initial_delay_seconds: int | None = Field(..., alias="initialDelaySeconds")
    period_seconds: int | None = Field(..., alias="periodSeconds")
    success_threshold: int | None = Field(..., alias="successThreshold")
    tcp_socket: CoreV1TCPSocketAction | None = Field(..., alias="tcpSocket")
    termination_grace_period_seconds: int | None = Field(..., alias="terminationGracePeriodSeconds")
    timeout_seconds: int | None = Field(..., alias="timeoutSeconds")


class CoreV1ProjectedVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ProjectedVolumeSource
    """

    default_mode: int | None = Field(..., alias="defaultMode")
    sources: list[CoreV1VolumeProjection] | None = Field(..., alias="sources")


class CoreV1QuobyteVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.QuobyteVolumeSource
    """

    group: str | None = Field(..., alias="group")
    read_only: bool | None = Field(..., alias="readOnly")
    registry: str = Field(default="", alias="registry")
    tenant: str | None = Field(..., alias="tenant")
    user: str | None = Field(..., alias="user")
    volume: str = Field(default="", alias="volume")


class CoreV1ReplicationController(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationController
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("ReplicationController", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1ReplicationControllerSpec = Field(default={}, alias="spec")
    status: CoreV1ReplicationControllerStatus = Field(default={}, alias="status")


class CoreV1ReplicationControllerCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationControllerCondition
    """

    last_transition_time: MetaV1Time = Field(default={}, alias="lastTransitionTime")
    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1ReplicationControllerList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationControllerList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1ReplicationController] = Field(..., alias="items")
    kind: str | None = Field("ReplicationControllerList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1ReplicationControllerStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationControllerStatus
    """

    available_replicas: int | None = Field(..., alias="availableReplicas")
    conditions: list[CoreV1ReplicationControllerCondition] | None = Field(..., alias="conditions")
    fully_labeled_replicas: int | None = Field(..., alias="fullyLabeledReplicas")
    observed_generation: int | None = Field(..., alias="observedGeneration")
    ready_replicas: int | None = Field(..., alias="readyReplicas")
    replicas: int = Field(default=0, alias="replicas")


class CoreV1ResourceFieldSelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceFieldSelector
    """

    container_name: str | None = Field(..., alias="containerName")
    divisor: iok8sapimachinerypkgapiresourceQuantity = Field(default={}, alias="divisor")
    resource: str = Field(default="", alias="resource")


class CoreV1ResourceQuota(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceQuota
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("ResourceQuota", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1ResourceQuotaSpec = Field(default={}, alias="spec")
    status: CoreV1ResourceQuotaStatus = Field(default={}, alias="status")


class CoreV1ResourceQuotaList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceQuotaList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1ResourceQuota] = Field(..., alias="items")
    kind: str | None = Field("ResourceQuotaList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1SELinuxOptions(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SELinuxOptions
    """

    level: str | None = Field(..., alias="level")
    role: str | None = Field(..., alias="role")
    type: str | None = Field(..., alias="type")
    user: str | None = Field(..., alias="user")


class CoreV1ScaleIOPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ScaleIOPersistentVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    gateway: str = Field(default="", alias="gateway")
    protection_domain: str | None = Field(..., alias="protectionDomain")
    read_only: bool | None = Field(..., alias="readOnly")
    secret_ref: CoreV1SecretReference = Field(..., alias="secretRef")
    ssl_enabled: bool | None = Field(..., alias="sslEnabled")
    storage_mode: str | None = Field(..., alias="storageMode")
    storage_pool: str | None = Field(..., alias="storagePool")
    system: str = Field(default="", alias="system")
    volume_name: str | None = Field(..., alias="volumeName")


class CoreV1ScaleIOVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ScaleIOVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    gateway: str = Field(default="", alias="gateway")
    protection_domain: str | None = Field(..., alias="protectionDomain")
    read_only: bool | None = Field(..., alias="readOnly")
    secret_ref: CoreV1LocalObjectReference = Field(..., alias="secretRef")
    ssl_enabled: bool | None = Field(..., alias="sslEnabled")
    storage_mode: str | None = Field(..., alias="storageMode")
    storage_pool: str | None = Field(..., alias="storagePool")
    system: str = Field(default="", alias="system")
    volume_name: str | None = Field(..., alias="volumeName")


class CoreV1ScopeSelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ScopeSelector
    """

    match_expressions: list[CoreV1ScopedResourceSelectorRequirement] | None = Field(
        ..., alias="matchExpressions"
    )


class CoreV1SeccompProfile(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SeccompProfile
    """

    localhost_profile: str | None = Field(..., alias="localhostProfile")
    type: str = Field(default="", alias="type")


class CoreV1SecretEnvSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretEnvSource
    """

    name: str | None = Field(..., alias="name")
    optional: bool | None = Field(..., alias="optional")


class CoreV1SecretKeySelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretKeySelector
    """

    key: str = Field(default="", alias="key")
    name: str | None = Field(..., alias="name")
    optional: bool | None = Field(..., alias="optional")


class CoreV1SecretList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1Secret] = Field(..., alias="items")
    kind: str | None = Field("SecretList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1SecretProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretProjection
    """

    items: list[CoreV1KeyToPath] | None = Field(..., alias="items")
    name: str | None = Field(..., alias="name")
    optional: bool | None = Field(..., alias="optional")


class CoreV1SecretReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretReference
    """

    name: str | None = Field(..., alias="name")
    namespace: str | None = Field(..., alias="namespace")


class CoreV1SecretVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretVolumeSource
    """

    default_mode: int | None = Field(..., alias="defaultMode")
    items: list[CoreV1KeyToPath] | None = Field(..., alias="items")
    optional: bool | None = Field(..., alias="optional")
    secret_name: str | None = Field(..., alias="secretName")


class CoreV1SecurityContext(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecurityContext
    """

    allow_privilege_escalation: bool | None = Field(..., alias="allowPrivilegeEscalation")
    capabilities: CoreV1Capabilities | None = Field(..., alias="capabilities")
    privileged: bool | None = Field(..., alias="privileged")
    proc_mount: str | None = Field(..., alias="procMount")
    read_only_root_filesystem: bool | None = Field(..., alias="readOnlyRootFilesystem")
    run_as_group: int | None = Field(..., alias="runAsGroup")
    run_as_non_root: bool | None = Field(..., alias="runAsNonRoot")
    run_as_user: int | None = Field(..., alias="runAsUser")
    se_linux_options: CoreV1SELinuxOptions | None = Field(..., alias="seLinuxOptions")
    seccomp_profile: CoreV1SeccompProfile | None = Field(..., alias="seccompProfile")
    windows_options: CoreV1WindowsSecurityContextOptions | None = Field(..., alias="windowsOptions")


class CoreV1Service(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Service
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    kind: str | None = Field("Service", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    spec: CoreV1ServiceSpec = Field(default={}, alias="spec")
    status: CoreV1ServiceStatus = Field(default={}, alias="status")


class CoreV1ServiceAccount(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceAccount
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    automount_service_account_token: bool | None = Field(..., alias="automountServiceAccountToken")
    image_pull_secrets: list[CoreV1LocalObjectReference] | None = Field(
        ..., alias="imagePullSecrets"
    )
    kind: str | None = Field("ServiceAccount", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")
    secrets: list[CoreV1ObjectReference] | None = Field(..., alias="secrets")


class CoreV1ServiceAccountList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceAccountList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1ServiceAccount] = Field(..., alias="items")
    kind: str | None = Field("ServiceAccountList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1ServiceAccountTokenProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceAccountTokenProjection
    """

    audience: str | None = Field(..., alias="audience")
    expiration_seconds: int | None = Field(..., alias="expirationSeconds")
    path: str = Field(default="", alias="path")


class CoreV1ServiceList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    items: list[CoreV1Service] = Field(..., alias="items")
    kind: str | None = Field("ServiceList", alias="kind")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")


class CoreV1ServicePort(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServicePort
    """

    app_protocol: str | None = Field(..., alias="appProtocol")
    name: str | None = Field(..., alias="name")
    node_port: int | None = Field(..., alias="nodePort")
    port: int = Field(default=0, alias="port")
    protocol: str = Field(default="TCP", alias="protocol")
    target_port: iok8sapimachinerypkgutilintstrIntOrString = Field(default={}, alias="targetPort")


class CoreV1ServiceStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceStatus
    """

    conditions: list[MetaV1Condition] | None = Field(..., alias="conditions")
    load_balancer: CoreV1LoadBalancerStatus = Field(default={}, alias="loadBalancer")


class CoreV1SessionAffinityConfig(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SessionAffinityConfig
    """

    client_ip: CoreV1ClientIPConfig | None = Field(..., alias="clientIP")


class CoreV1StorageOSPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.StorageOSPersistentVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    read_only: bool | None = Field(..., alias="readOnly")
    secret_ref: CoreV1ObjectReference | None = Field(..., alias="secretRef")
    volume_name: str | None = Field(..., alias="volumeName")
    volume_namespace: str | None = Field(..., alias="volumeNamespace")


class CoreV1StorageOSVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.StorageOSVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    read_only: bool | None = Field(..., alias="readOnly")
    secret_ref: CoreV1LocalObjectReference | None = Field(..., alias="secretRef")
    volume_name: str | None = Field(..., alias="volumeName")
    volume_namespace: str | None = Field(..., alias="volumeNamespace")


class CoreV1Sysctl(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Sysctl
    """

    name: str = Field(default="", alias="name")
    value: str = Field(default="", alias="value")


class CoreV1TCPSocketAction(BaseModel):
    """
    Original name: io.k8s.api.core.v1.TCPSocketAction
    """

    host: str | None = Field(..., alias="host")
    port: iok8sapimachinerypkgutilintstrIntOrString = Field(default={}, alias="port")


class CoreV1Taint(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Taint
    """

    effect: str = Field(default="", alias="effect")
    key: str = Field(default="", alias="key")
    time_added: MetaV1Time | None = Field(..., alias="timeAdded")
    value: str | None = Field(..., alias="value")


class CoreV1Toleration(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Toleration
    """

    effect: str | None = Field(..., alias="effect")
    key: str | None = Field(..., alias="key")
    operator: str | None = Field(..., alias="operator")
    toleration_seconds: int | None = Field(..., alias="tolerationSeconds")
    value: str | None = Field(..., alias="value")


class CoreV1TypedLocalObjectReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.TypedLocalObjectReference
    """

    api_group: str | None = Field(..., alias="apiGroup")
    kind: str = Field(default="", alias="kind")
    name: str = Field(default="", alias="name")


class CoreV1Volume(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Volume
    """

    aws_elastic_block_store: CoreV1AWSElasticBlockStoreVolumeSource | None = Field(
        ..., alias="awsElasticBlockStore"
    )
    azure_disk: CoreV1AzureDiskVolumeSource | None = Field(..., alias="azureDisk")
    azure_file: CoreV1AzureFileVolumeSource | None = Field(..., alias="azureFile")
    cephfs: CoreV1CephFSVolumeSource | None = Field(..., alias="cephfs")
    cinder: CoreV1CinderVolumeSource | None = Field(..., alias="cinder")
    config_map: CoreV1ConfigMapVolumeSource | None = Field(..., alias="configMap")
    csi: CoreV1CSIVolumeSource | None = Field(..., alias="csi")
    downward_api: CoreV1DownwardAPIVolumeSource | None = Field(..., alias="downwardAPI")
    empty_dir: CoreV1EmptyDirVolumeSource | None = Field(..., alias="emptyDir")
    ephemeral: CoreV1EphemeralVolumeSource | None = Field(..., alias="ephemeral")
    fc: CoreV1FCVolumeSource | None = Field(..., alias="fc")
    flex_volume: CoreV1FlexVolumeSource | None = Field(..., alias="flexVolume")
    flocker: CoreV1FlockerVolumeSource | None = Field(..., alias="flocker")
    gce_persistent_disk: CoreV1GCEPersistentDiskVolumeSource | None = Field(
        ..., alias="gcePersistentDisk"
    )
    git_repo: CoreV1GitRepoVolumeSource | None = Field(..., alias="gitRepo")
    glusterfs: CoreV1GlusterfsVolumeSource | None = Field(..., alias="glusterfs")
    host_path: CoreV1HostPathVolumeSource | None = Field(..., alias="hostPath")
    iscsi: CoreV1ISCSIVolumeSource | None = Field(..., alias="iscsi")
    name: str = Field(default="", alias="name")
    nfs: CoreV1NFSVolumeSource | None = Field(..., alias="nfs")
    persistent_volume_claim: CoreV1PersistentVolumeClaimVolumeSource | None = Field(
        ..., alias="persistentVolumeClaim"
    )
    photon_persistent_disk: CoreV1PhotonPersistentDiskVolumeSource | None = Field(
        ..., alias="photonPersistentDisk"
    )
    portworx_volume: CoreV1PortworxVolumeSource | None = Field(..., alias="portworxVolume")
    projected: CoreV1ProjectedVolumeSource | None = Field(..., alias="projected")
    quobyte: CoreV1QuobyteVolumeSource | None = Field(..., alias="quobyte")
    rbd: CoreV1RBDVolumeSource | None = Field(..., alias="rbd")
    scale_io: CoreV1ScaleIOVolumeSource | None = Field(..., alias="scaleIO")
    secret: CoreV1SecretVolumeSource | None = Field(..., alias="secret")
    storageos: CoreV1StorageOSVolumeSource | None = Field(..., alias="storageos")
    vsphere_volume: CoreV1VsphereVirtualDiskVolumeSource | None = Field(..., alias="vsphereVolume")


class CoreV1VolumeDevice(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeDevice
    """

    device_path: str = Field(default="", alias="devicePath")
    name: str = Field(default="", alias="name")


class CoreV1VolumeMount(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeMount
    """

    mount_path: str = Field(default="", alias="mountPath")
    mount_propagation: str | None = Field(..., alias="mountPropagation")
    name: str = Field(default="", alias="name")
    read_only: bool | None = Field(..., alias="readOnly")
    sub_path: str | None = Field(..., alias="subPath")
    sub_path_expr: str | None = Field(..., alias="subPathExpr")


class CoreV1VolumeNodeAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeNodeAffinity
    """

    required: CoreV1NodeSelector | None = Field(..., alias="required")


class CoreV1VolumeProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeProjection
    """

    config_map: CoreV1ConfigMapProjection | None = Field(..., alias="configMap")
    downward_api: CoreV1DownwardAPIProjection | None = Field(..., alias="downwardAPI")
    secret: CoreV1SecretProjection | None = Field(..., alias="secret")
    service_account_token: CoreV1ServiceAccountTokenProjection | None = Field(
        ..., alias="serviceAccountToken"
    )


class CoreV1VsphereVirtualDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VsphereVirtualDiskVolumeSource
    """

    fs_type: str | None = Field(..., alias="fsType")
    storage_policy_id: str | None = Field(..., alias="storagePolicyID")
    storage_policy_name: str | None = Field(..., alias="storagePolicyName")
    volume_path: str = Field(default="", alias="volumePath")


class CoreV1WeightedPodAffinityTerm(BaseModel):
    """
    Original name: io.k8s.api.core.v1.WeightedPodAffinityTerm
    """

    pod_affinity_term: CoreV1PodAffinityTerm = Field(default={}, alias="podAffinityTerm")
    weight: int = Field(default=0, alias="weight")


class CoreV1WindowsSecurityContextOptions(BaseModel):
    """
    Original name: io.k8s.api.core.v1.WindowsSecurityContextOptions
    """

    gmsa_credential_spec: str | None = Field(..., alias="gmsaCredentialSpec")
    gmsa_credential_spec_name: str | None = Field(..., alias="gmsaCredentialSpecName")
    host_process: bool | None = Field(..., alias="hostProcess")
    run_as_user_name: str | None = Field(..., alias="runAsUserName")


class iok8sapipolicyV1Eviction(BaseModel):
    """
    Original name: io.k8s.api.policy.v1.Eviction
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    delete_options: MetaV1DeleteOptions | None = Field(..., alias="deleteOptions")
    kind: str | None = Field("Eviction", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default={}, alias="metadata")


class MetaV1APIResourceList(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.APIResourceList
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    group_version: str = Field(default="", alias="groupVersion")
    kind: str | None = Field("APIResourceList", alias="kind")
    resources: list[MetaV1APIResource] = Field(..., alias="resources")


class MetaV1Condition(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.Condition
    """

    last_transition_time: MetaV1Time = Field(default={}, alias="lastTransitionTime")
    message: str = Field(default="", alias="message")
    observed_generation: int | None = Field(..., alias="observedGeneration")
    reason: str = Field(default="", alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class MetaV1ListMeta(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta
    """

    continue_: str | None = Field(..., alias="continue_")
    remaining_item_count: int | None = Field(..., alias="remainingItemCount")
    resource_version: str | None = Field(..., alias="resourceVersion")
    self_link: str | None = Field(..., alias="selfLink")


class MetaV1ManagedFieldsEntry(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.ManagedFieldsEntry
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    fields_type: str | None = Field(..., alias="fieldsType")
    fields_v1: MetaV1FieldsV1 | None = Field(..., alias="fieldsV1")
    manager: str | None = Field(..., alias="manager")
    operation: str | None = Field(..., alias="operation")
    subresource: str | None = Field(..., alias="subresource")
    time: MetaV1Time | None = Field(..., alias="time")


class MetaV1OwnerReference(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.OwnerReference
    """

    api_version: str = Field(default="", alias="apiVersion")
    block_owner_deletion: bool | None = Field(..., alias="blockOwnerDeletion")
    controller: bool | None = Field(..., alias="controller")
    kind: str = Field(default="", alias="kind")
    name: str = Field(default="", alias="name")
    uid: str = Field(default="", alias="uid")


class MetaV1Preconditions(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.Preconditions
    """

    resource_version: str | None = Field(..., alias="resourceVersion")
    uid: str | None = Field(..., alias="uid")


class MetaV1Status(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.Status
    """

    api_version: str | None = Field("v1", alias="apiVersion")
    code: int | None = Field(..., alias="code")
    details: MetaV1StatusDetails | None = Field(..., alias="details")
    kind: str | None = Field("Status", alias="kind")
    message: str | None = Field(..., alias="message")
    metadata: MetaV1ListMeta = Field(default={}, alias="metadata")
    reason: str | None = Field(..., alias="reason")
    status: str | None = Field(..., alias="status")


class MetaV1StatusCause(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.StatusCause
    """

    field: str | None = Field(..., alias="field")
    message: str | None = Field(..., alias="message")
    reason: str | None = Field(..., alias="reason")


class MetaV1StatusDetails(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.StatusDetails
    """

    causes: list[MetaV1StatusCause] | None = Field(..., alias="causes")
    group: str | None = Field(..., alias="group")
    kind: str | None = Field("StatusDetails", alias="kind")
    name: str | None = Field(..., alias="name")
    retry_after_seconds: int | None = Field(..., alias="retryAfterSeconds")
    uid: str | None = Field(..., alias="uid")


class MetaV1WatchEvent(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.WatchEvent
    """

    object: iok8sapimachinerypkgruntimeRawExtension = Field(default={}, alias="object")
    type: str = Field(default="", alias="type")


async def get_core_v1_api_resources(session: ClientSession) -> MetaV1APIResourceList:
    """
    Original path: /api/v1/
    Op ID: getCoreV1APIResources
    Derived params: []
    """
    async with session.get(f"/api/v1/") as response:
        return MetaV1APIResourceList.parse_obj(await response.json())


async def list_core_v1_component_status(session: ClientSession) -> CoreV1ComponentStatusList:
    """
    Original path: /api/v1/componentstatuses
    Op ID: listCoreV1ComponentStatus
    Derived params: []
    """
    async with session.get(f"/api/v1/componentstatuses") as response:
        return CoreV1ComponentStatusList.parse_obj(await response.json())


async def read_core_v1_component_status(session: ClientSession, name: str) -> CoreV1ComponentStatus:
    """
    Original path: /api/v1/componentstatuses/{name}
    Op ID: readCoreV1ComponentStatus
    Derived params: ['name']
    """
    async with session.get(f"/api/v1/componentstatuses/{name}") as response:
        return CoreV1ComponentStatus.parse_obj(await response.json())


async def list_core_v1_config_map_for_all_namespaces(session: ClientSession) -> CoreV1ConfigMapList:
    """
    Original path: /api/v1/configmaps
    Op ID: listCoreV1ConfigMapForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/configmaps") as response:
        return CoreV1ConfigMapList.parse_obj(await response.json())


async def list_core_v1_endpoints_for_all_namespaces(session: ClientSession) -> CoreV1EndpointsList:
    """
    Original path: /api/v1/endpoints
    Op ID: listCoreV1EndpointsForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/endpoints") as response:
        return CoreV1EndpointsList.parse_obj(await response.json())


async def list_core_v1_event_for_all_namespaces(session: ClientSession) -> CoreV1EventList:
    """
    Original path: /api/v1/events
    Op ID: listCoreV1EventForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/events") as response:
        return CoreV1EventList.parse_obj(await response.json())


async def list_core_v1_limit_range_for_all_namespaces(
    session: ClientSession,
) -> CoreV1LimitRangeList:
    """
    Original path: /api/v1/limitranges
    Op ID: listCoreV1LimitRangeForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/limitranges") as response:
        return CoreV1LimitRangeList.parse_obj(await response.json())


async def list_core_v1_namespace(session: ClientSession) -> CoreV1NamespaceList:
    """
    Original path: /api/v1/namespaces
    Op ID: listCoreV1Namespace
    Derived params: []
    """
    async with session.get(f"/api/v1/namespaces") as response:
        return CoreV1NamespaceList.parse_obj(await response.json())


async def list_core_v1_namespaced_config_map(
    session: ClientSession, namespace: str
) -> CoreV1ConfigMapList:
    """
    Original path: /api/v1/namespaces/{namespace}/configmaps
    Op ID: listCoreV1NamespacedConfigMap
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/configmaps") as response:
        return CoreV1ConfigMapList.parse_obj(await response.json())


async def read_core_v1_namespaced_config_map(
    session: ClientSession, namespace: str, name: str
) -> CoreV1ConfigMap:
    """
    Original path: /api/v1/namespaces/{namespace}/configmaps/{name}
    Op ID: readCoreV1NamespacedConfigMap
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/configmaps/{name}") as response:
        return CoreV1ConfigMap.parse_obj(await response.json())


async def list_core_v1_namespaced_endpoints(
    session: ClientSession, namespace: str
) -> CoreV1EndpointsList:
    """
    Original path: /api/v1/namespaces/{namespace}/endpoints
    Op ID: listCoreV1NamespacedEndpoints
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/endpoints") as response:
        return CoreV1EndpointsList.parse_obj(await response.json())


async def read_core_v1_namespaced_endpoints(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Endpoints:
    """
    Original path: /api/v1/namespaces/{namespace}/endpoints/{name}
    Op ID: readCoreV1NamespacedEndpoints
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/endpoints/{name}") as response:
        return CoreV1Endpoints.parse_obj(await response.json())


async def list_core_v1_namespaced_event(session: ClientSession, namespace: str) -> CoreV1EventList:
    """
    Original path: /api/v1/namespaces/{namespace}/events
    Op ID: listCoreV1NamespacedEvent
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/events") as response:
        return CoreV1EventList.parse_obj(await response.json())


async def read_core_v1_namespaced_event(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Event:
    """
    Original path: /api/v1/namespaces/{namespace}/events/{name}
    Op ID: readCoreV1NamespacedEvent
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/events/{name}") as response:
        return CoreV1Event.parse_obj(await response.json())


async def list_core_v1_namespaced_limit_range(
    session: ClientSession, namespace: str
) -> CoreV1LimitRangeList:
    """
    Original path: /api/v1/namespaces/{namespace}/limitranges
    Op ID: listCoreV1NamespacedLimitRange
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/limitranges") as response:
        return CoreV1LimitRangeList.parse_obj(await response.json())


async def read_core_v1_namespaced_limit_range(
    session: ClientSession, namespace: str, name: str
) -> CoreV1LimitRange:
    """
    Original path: /api/v1/namespaces/{namespace}/limitranges/{name}
    Op ID: readCoreV1NamespacedLimitRange
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/limitranges/{name}") as response:
        return CoreV1LimitRange.parse_obj(await response.json())


async def list_core_v1_namespaced_persistent_volume_claim(
    session: ClientSession, namespace: str
) -> CoreV1PersistentVolumeClaimList:
    """
    Original path: /api/v1/namespaces/{namespace}/persistentvolumeclaims
    Op ID: listCoreV1NamespacedPersistentVolumeClaim
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/persistentvolumeclaims") as response:
        return CoreV1PersistentVolumeClaimList.parse_obj(await response.json())


async def read_core_v1_namespaced_persistent_volume_claim(
    session: ClientSession, namespace: str, name: str
) -> CoreV1PersistentVolumeClaim:
    """
    Original path: /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}
    Op ID: readCoreV1NamespacedPersistentVolumeClaim
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}"
    ) as response:
        return CoreV1PersistentVolumeClaim.parse_obj(await response.json())


async def read_core_v1_namespaced_persistent_volume_claim_status(
    session: ClientSession, namespace: str, name: str
) -> CoreV1PersistentVolumeClaim:
    """
    Original path: /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status
    Op ID: readCoreV1NamespacedPersistentVolumeClaimStatus
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status"
    ) as response:
        return CoreV1PersistentVolumeClaim.parse_obj(await response.json())


async def list_core_v1_namespaced_pod(session: ClientSession, namespace: str) -> CoreV1PodList:
    """
    Original path: /api/v1/namespaces/{namespace}/pods
    Op ID: listCoreV1NamespacedPod
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/pods") as response:
        return CoreV1PodList.parse_obj(await response.json())


async def read_core_v1_namespaced_pod(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Pod:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}
    Op ID: readCoreV1NamespacedPod
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/pods/{name}") as response:
        return CoreV1Pod.parse_obj(await response.json())


async def read_core_v1_namespaced_pod_ephemeralcontainers(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Pod:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers
    Op ID: readCoreV1NamespacedPodEphemeralcontainers
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers"
    ) as response:
        return CoreV1Pod.parse_obj(await response.json())


async def read_core_v1_namespaced_pod_log(
    session: ClientSession, namespace: str, name: str
) -> string:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}/log
    Op ID: readCoreV1NamespacedPodLog
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/pods/{name}/log") as response:
        return await response.text()


async def read_core_v1_namespaced_pod_status(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Pod:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}/status
    Op ID: readCoreV1NamespacedPodStatus
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/pods/{name}/status") as response:
        return CoreV1Pod.parse_obj(await response.json())


async def list_core_v1_namespaced_pod_template(
    session: ClientSession, namespace: str
) -> CoreV1PodTemplateList:
    """
    Original path: /api/v1/namespaces/{namespace}/podtemplates
    Op ID: listCoreV1NamespacedPodTemplate
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/podtemplates") as response:
        return CoreV1PodTemplateList.parse_obj(await response.json())


async def read_core_v1_namespaced_pod_template(
    session: ClientSession, namespace: str, name: str
) -> CoreV1PodTemplate:
    """
    Original path: /api/v1/namespaces/{namespace}/podtemplates/{name}
    Op ID: readCoreV1NamespacedPodTemplate
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/podtemplates/{name}") as response:
        return CoreV1PodTemplate.parse_obj(await response.json())


async def list_core_v1_namespaced_replication_controller(
    session: ClientSession, namespace: str
) -> CoreV1ReplicationControllerList:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers
    Op ID: listCoreV1NamespacedReplicationController
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/replicationcontrollers") as response:
        return CoreV1ReplicationControllerList.parse_obj(await response.json())


async def read_core_v1_namespaced_replication_controller(
    session: ClientSession, namespace: str, name: str
) -> CoreV1ReplicationController:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers/{name}
    Op ID: readCoreV1NamespacedReplicationController
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers/{name}"
    ) as response:
        return CoreV1ReplicationController.parse_obj(await response.json())


async def read_core_v1_namespaced_replication_controller_scale(
    session: ClientSession, namespace: str, name: str
) -> AutoscalingV1Scale:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale
    Op ID: readCoreV1NamespacedReplicationControllerScale
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale"
    ) as response:
        return AutoscalingV1Scale.parse_obj(await response.json())


async def read_core_v1_namespaced_replication_controller_status(
    session: ClientSession, namespace: str, name: str
) -> CoreV1ReplicationController:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status
    Op ID: readCoreV1NamespacedReplicationControllerStatus
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status"
    ) as response:
        return CoreV1ReplicationController.parse_obj(await response.json())


async def list_core_v1_namespaced_resource_quota(
    session: ClientSession, namespace: str
) -> CoreV1ResourceQuotaList:
    """
    Original path: /api/v1/namespaces/{namespace}/resourcequotas
    Op ID: listCoreV1NamespacedResourceQuota
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/resourcequotas") as response:
        return CoreV1ResourceQuotaList.parse_obj(await response.json())


async def read_core_v1_namespaced_resource_quota(
    session: ClientSession, namespace: str, name: str
) -> CoreV1ResourceQuota:
    """
    Original path: /api/v1/namespaces/{namespace}/resourcequotas/{name}
    Op ID: readCoreV1NamespacedResourceQuota
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/resourcequotas/{name}") as response:
        return CoreV1ResourceQuota.parse_obj(await response.json())


async def read_core_v1_namespaced_resource_quota_status(
    session: ClientSession, namespace: str, name: str
) -> CoreV1ResourceQuota:
    """
    Original path: /api/v1/namespaces/{namespace}/resourcequotas/{name}/status
    Op ID: readCoreV1NamespacedResourceQuotaStatus
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/resourcequotas/{name}/status"
    ) as response:
        return CoreV1ResourceQuota.parse_obj(await response.json())


async def list_core_v1_namespaced_secret(
    session: ClientSession, namespace: str
) -> CoreV1SecretList:
    """
    Original path: /api/v1/namespaces/{namespace}/secrets
    Op ID: listCoreV1NamespacedSecret
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/secrets") as response:
        return CoreV1SecretList.parse_obj(await response.json())


async def read_core_v1_namespaced_secret(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Secret:
    """
    Original path: /api/v1/namespaces/{namespace}/secrets/{name}
    Op ID: readCoreV1NamespacedSecret
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/secrets/{name}") as response:
        return CoreV1Secret.parse_obj(await response.json())


async def list_core_v1_namespaced_service_account(
    session: ClientSession, namespace: str
) -> CoreV1ServiceAccountList:
    """
    Original path: /api/v1/namespaces/{namespace}/serviceaccounts
    Op ID: listCoreV1NamespacedServiceAccount
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/serviceaccounts") as response:
        return CoreV1ServiceAccountList.parse_obj(await response.json())


async def read_core_v1_namespaced_service_account(
    session: ClientSession, namespace: str, name: str
) -> CoreV1ServiceAccount:
    """
    Original path: /api/v1/namespaces/{namespace}/serviceaccounts/{name}
    Op ID: readCoreV1NamespacedServiceAccount
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/serviceaccounts/{name}") as response:
        return CoreV1ServiceAccount.parse_obj(await response.json())


async def list_core_v1_namespaced_service(
    session: ClientSession, namespace: str
) -> CoreV1ServiceList:
    """
    Original path: /api/v1/namespaces/{namespace}/services
    Op ID: listCoreV1NamespacedService
    Derived params: ['namespace']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/services") as response:
        return CoreV1ServiceList.parse_obj(await response.json())


async def read_core_v1_namespaced_service(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Service:
    """
    Original path: /api/v1/namespaces/{namespace}/services/{name}
    Op ID: readCoreV1NamespacedService
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/services/{name}") as response:
        return CoreV1Service.parse_obj(await response.json())


async def read_core_v1_namespaced_service_status(
    session: ClientSession, namespace: str, name: str
) -> CoreV1Service:
    """
    Original path: /api/v1/namespaces/{namespace}/services/{name}/status
    Op ID: readCoreV1NamespacedServiceStatus
    Derived params: ['namespace', 'name']
    """
    async with session.get(f"/api/v1/namespaces/{namespace}/services/{name}/status") as response:
        return CoreV1Service.parse_obj(await response.json())


async def read_core_v1_namespace(session: ClientSession, name: str) -> CoreV1Namespace:
    """
    Original path: /api/v1/namespaces/{name}
    Op ID: readCoreV1Namespace
    Derived params: ['name']
    """
    async with session.get(f"/api/v1/namespaces/{name}") as response:
        return CoreV1Namespace.parse_obj(await response.json())


async def read_core_v1_namespace_status(session: ClientSession, name: str) -> CoreV1Namespace:
    """
    Original path: /api/v1/namespaces/{name}/status
    Op ID: readCoreV1NamespaceStatus
    Derived params: ['name']
    """
    async with session.get(f"/api/v1/namespaces/{name}/status") as response:
        return CoreV1Namespace.parse_obj(await response.json())


async def list_core_v1_node(session: ClientSession) -> CoreV1NodeList:
    """
    Original path: /api/v1/nodes
    Op ID: listCoreV1Node
    Derived params: []
    """
    async with session.get(f"/api/v1/nodes") as response:
        return CoreV1NodeList.parse_obj(await response.json())


async def read_core_v1_node(session: ClientSession, name: str) -> CoreV1Node:
    """
    Original path: /api/v1/nodes/{name}
    Op ID: readCoreV1Node
    Derived params: ['name']
    """
    async with session.get(f"/api/v1/nodes/{name}") as response:
        return CoreV1Node.parse_obj(await response.json())


async def read_core_v1_node_status(session: ClientSession, name: str) -> CoreV1Node:
    """
    Original path: /api/v1/nodes/{name}/status
    Op ID: readCoreV1NodeStatus
    Derived params: ['name']
    """
    async with session.get(f"/api/v1/nodes/{name}/status") as response:
        return CoreV1Node.parse_obj(await response.json())


async def list_core_v1_persistent_volume_claim_for_all_namespaces(
    session: ClientSession,
) -> CoreV1PersistentVolumeClaimList:
    """
    Original path: /api/v1/persistentvolumeclaims
    Op ID: listCoreV1PersistentVolumeClaimForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/persistentvolumeclaims") as response:
        return CoreV1PersistentVolumeClaimList.parse_obj(await response.json())


async def list_core_v1_persistent_volume(session: ClientSession) -> CoreV1PersistentVolumeList:
    """
    Original path: /api/v1/persistentvolumes
    Op ID: listCoreV1PersistentVolume
    Derived params: []
    """
    async with session.get(f"/api/v1/persistentvolumes") as response:
        return CoreV1PersistentVolumeList.parse_obj(await response.json())


async def read_core_v1_persistent_volume(
    session: ClientSession, name: str
) -> CoreV1PersistentVolume:
    """
    Original path: /api/v1/persistentvolumes/{name}
    Op ID: readCoreV1PersistentVolume
    Derived params: ['name']
    """
    async with session.get(f"/api/v1/persistentvolumes/{name}") as response:
        return CoreV1PersistentVolume.parse_obj(await response.json())


async def read_core_v1_persistent_volume_status(
    session: ClientSession, name: str
) -> CoreV1PersistentVolume:
    """
    Original path: /api/v1/persistentvolumes/{name}/status
    Op ID: readCoreV1PersistentVolumeStatus
    Derived params: ['name']
    """
    async with session.get(f"/api/v1/persistentvolumes/{name}/status") as response:
        return CoreV1PersistentVolume.parse_obj(await response.json())


async def list_core_v1_pod_for_all_namespaces(session: ClientSession) -> CoreV1PodList:
    """
    Original path: /api/v1/pods
    Op ID: listCoreV1PodForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/pods") as response:
        return CoreV1PodList.parse_obj(await response.json())


async def list_core_v1_pod_template_for_all_namespaces(
    session: ClientSession,
) -> CoreV1PodTemplateList:
    """
    Original path: /api/v1/podtemplates
    Op ID: listCoreV1PodTemplateForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/podtemplates") as response:
        return CoreV1PodTemplateList.parse_obj(await response.json())


async def list_core_v1_replication_controller_for_all_namespaces(
    session: ClientSession,
) -> CoreV1ReplicationControllerList:
    """
    Original path: /api/v1/replicationcontrollers
    Op ID: listCoreV1ReplicationControllerForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/replicationcontrollers") as response:
        return CoreV1ReplicationControllerList.parse_obj(await response.json())


async def list_core_v1_resource_quota_for_all_namespaces(
    session: ClientSession,
) -> CoreV1ResourceQuotaList:
    """
    Original path: /api/v1/resourcequotas
    Op ID: listCoreV1ResourceQuotaForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/resourcequotas") as response:
        return CoreV1ResourceQuotaList.parse_obj(await response.json())


async def list_core_v1_secret_for_all_namespaces(session: ClientSession) -> CoreV1SecretList:
    """
    Original path: /api/v1/secrets
    Op ID: listCoreV1SecretForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/secrets") as response:
        return CoreV1SecretList.parse_obj(await response.json())


async def list_core_v1_service_account_for_all_namespaces(
    session: ClientSession,
) -> CoreV1ServiceAccountList:
    """
    Original path: /api/v1/serviceaccounts
    Op ID: listCoreV1ServiceAccountForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/serviceaccounts") as response:
        return CoreV1ServiceAccountList.parse_obj(await response.json())


async def list_core_v1_service_for_all_namespaces(session: ClientSession) -> CoreV1ServiceList:
    """
    Original path: /api/v1/services
    Op ID: listCoreV1ServiceForAllNamespaces
    Derived params: []
    """
    async with session.get(f"/api/v1/services") as response:
        return CoreV1ServiceList.parse_obj(await response.json())
