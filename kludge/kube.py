from __future__ import annotations

from aiohttp import ClientSession
from pydantic import BaseModel, Field


class AuthenticationV1BoundObjectReference(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("BoundObjectReference", alias="kind")
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")


class AuthenticationV1TokenRequest(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("TokenRequest", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: AuthenticationV1TokenRequestSpec = Field(
        default_factory=AuthenticationV1TokenRequestSpec, alias="spec"
    )
    status: AuthenticationV1TokenRequestStatus = Field(
        default_factory=AuthenticationV1TokenRequestStatus, alias="status"
    )


class AuthenticationV1TokenRequestStatus(BaseModel):
    expiration_timestamp: MetaV1Time = Field(
        default_factory=MetaV1Time, alias="expirationTimestamp"
    )
    token: str = Field(default="", alias="token")


class iok8sapiautoscalingV1Scale(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("Scale", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: iok8sapiautoscalingV1ScaleSpec = Field(
        default_factory=iok8sapiautoscalingV1ScaleSpec, alias="spec"
    )
    status: iok8sapiautoscalingV1ScaleStatus = Field(
        default_factory=iok8sapiautoscalingV1ScaleStatus, alias="status"
    )


class iok8sapiautoscalingV1ScaleSpec(BaseModel):
    replicas: int = Field(..., alias="replicas")


class iok8sapiautoscalingV1ScaleStatus(BaseModel):
    replicas: int = Field(default=0, alias="replicas")
    selector: str = Field(..., alias="selector")


class CoreV1AWSElasticBlockStoreVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    partition: int = Field(..., alias="partition")
    read_only: bool = Field(..., alias="readOnly")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1Affinity(BaseModel):
    node_affinity: CoreV1NodeAffinity = Field(..., alias="nodeAffinity")
    pod_affinity: CoreV1PodAffinity = Field(..., alias="podAffinity")
    pod_anti_affinity: CoreV1PodAntiAffinity = Field(..., alias="podAntiAffinity")


class CoreV1AttachedVolume(BaseModel):
    device_path: str = Field(default="", alias="devicePath")
    name: str = Field(default="", alias="name")


class CoreV1AzureDiskVolumeSource(BaseModel):
    caching_mode: str = Field(..., alias="cachingMode")
    disk_name: str = Field(default="", alias="diskName")
    disk_uri: str = Field(default="", alias="diskURI")
    fs_type: str = Field(..., alias="fsType")
    kind: str = Field("AzureDiskVolumeSource", alias="kind")
    read_only: bool = Field(..., alias="readOnly")


class CoreV1AzureFilePersistentVolumeSource(BaseModel):
    read_only: bool = Field(..., alias="readOnly")
    secret_name: str = Field(default="", alias="secretName")
    secret_namespace: str = Field(..., alias="secretNamespace")
    share_name: str = Field(default="", alias="shareName")


class CoreV1AzureFileVolumeSource(BaseModel):
    read_only: bool = Field(..., alias="readOnly")
    secret_name: str = Field(default="", alias="secretName")
    share_name: str = Field(default="", alias="shareName")


class CoreV1Binding(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("Binding", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    target: CoreV1ObjectReference = Field(default_factory=CoreV1ObjectReference, alias="target")


class CoreV1CinderPersistentVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    read_only: bool = Field(..., alias="readOnly")
    secret_ref: CoreV1SecretReference = Field(..., alias="secretRef")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1CinderVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    read_only: bool = Field(..., alias="readOnly")
    secret_ref: CoreV1LocalObjectReference = Field(..., alias="secretRef")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1ClientIPConfig(BaseModel):
    timeout_seconds: int = Field(..., alias="timeoutSeconds")


class CoreV1ComponentCondition(BaseModel):
    error: str = Field(..., alias="error")
    message: str = Field(..., alias="message")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1ComponentStatus(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    conditions: list[CoreV1ComponentCondition] = Field(..., alias="conditions")
    kind: str = Field("ComponentStatus", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")


class CoreV1ComponentStatusList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1ComponentStatus] = Field(..., alias="items")
    kind: str = Field("ComponentStatusList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1ConfigMapEnvSource(BaseModel):
    name: str = Field(..., alias="name")
    optional: bool = Field(..., alias="optional")


class CoreV1ConfigMapKeySelector(BaseModel):
    key: str = Field(default="", alias="key")
    name: str = Field(..., alias="name")
    optional: bool = Field(..., alias="optional")


class CoreV1ConfigMapList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1ConfigMap] = Field(..., alias="items")
    kind: str = Field("ConfigMapList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1ConfigMapNodeConfigSource(BaseModel):
    kubelet_config_key: str = Field(default="", alias="kubeletConfigKey")
    name: str = Field(default="", alias="name")
    namespace: str = Field(default="", alias="namespace")
    resource_version: str = Field(..., alias="resourceVersion")
    uid: str = Field(..., alias="uid")


class CoreV1ConfigMapProjection(BaseModel):
    items: list[CoreV1KeyToPath] = Field(..., alias="items")
    name: str = Field(..., alias="name")
    optional: bool = Field(..., alias="optional")


class CoreV1ConfigMapVolumeSource(BaseModel):
    default_mode: int = Field(..., alias="defaultMode")
    items: list[CoreV1KeyToPath] = Field(..., alias="items")
    name: str = Field(..., alias="name")
    optional: bool = Field(..., alias="optional")


class CoreV1ContainerPort(BaseModel):
    container_port: int = Field(default=0, alias="containerPort")
    host_ip: str = Field(..., alias="hostIP")
    host_port: int = Field(..., alias="hostPort")
    name: str = Field(..., alias="name")
    protocol: str = Field(default="TCP", alias="protocol")


class CoreV1ContainerState(BaseModel):
    running: CoreV1ContainerStateRunning = Field(..., alias="running")
    terminated: CoreV1ContainerStateTerminated = Field(..., alias="terminated")
    waiting: CoreV1ContainerStateWaiting = Field(..., alias="waiting")


class CoreV1ContainerStateRunning(BaseModel):
    started_at: MetaV1Time = Field(default_factory=MetaV1Time, alias="startedAt")


class CoreV1ContainerStateTerminated(BaseModel):
    container_id: str = Field(..., alias="containerID")
    exit_code: int = Field(default=0, alias="exitCode")
    finished_at: MetaV1Time = Field(default_factory=MetaV1Time, alias="finishedAt")
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")
    signal: int = Field(..., alias="signal")
    started_at: MetaV1Time = Field(default_factory=MetaV1Time, alias="startedAt")


class CoreV1ContainerStateWaiting(BaseModel):
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")


class CoreV1ContainerStatus(BaseModel):
    container_id: str = Field(..., alias="containerID")
    image: str = Field(default="", alias="image")
    image_id: str = Field(default="", alias="imageID")
    last_state: CoreV1ContainerState = Field(
        default_factory=CoreV1ContainerState, alias="lastState"
    )
    name: str = Field(default="", alias="name")
    ready: bool = Field(default=False, alias="ready")
    restart_count: int = Field(default=0, alias="restartCount")
    started: bool = Field(..., alias="started")
    state: CoreV1ContainerState = Field(default_factory=CoreV1ContainerState, alias="state")


class CoreV1DaemonEndpoint(BaseModel):
    port: int = Field(default=0, alias="Port")


class CoreV1DownwardAPIProjection(BaseModel):
    items: list[CoreV1DownwardAPIVolumeFile] = Field(..., alias="items")


class CoreV1DownwardAPIVolumeFile(BaseModel):
    field_ref: CoreV1ObjectFieldSelector = Field(..., alias="fieldRef")
    mode: int = Field(..., alias="mode")
    path: str = Field(default="", alias="path")
    resource_field_ref: CoreV1ResourceFieldSelector = Field(..., alias="resourceFieldRef")


class CoreV1DownwardAPIVolumeSource(BaseModel):
    default_mode: int = Field(..., alias="defaultMode")
    items: list[CoreV1DownwardAPIVolumeFile] = Field(..., alias="items")


class CoreV1EmptyDirVolumeSource(BaseModel):
    medium: str = Field(..., alias="medium")
    size_limit: iok8sapimachinerypkgapiresourceQuantity = Field(..., alias="sizeLimit")


class CoreV1EndpointAddress(BaseModel):
    hostname: str = Field(..., alias="hostname")
    ip: str = Field(default="", alias="ip")
    node_name: str = Field(..., alias="nodeName")
    target_ref: CoreV1ObjectReference = Field(..., alias="targetRef")


class CoreV1EndpointPort(BaseModel):
    app_protocol: str = Field(..., alias="appProtocol")
    name: str = Field(..., alias="name")
    port: int = Field(default=0, alias="port")
    protocol: str = Field(..., alias="protocol")


class CoreV1EndpointSubset(BaseModel):
    addresses: list[CoreV1EndpointAddress] = Field(..., alias="addresses")
    not_ready_addresses: list[CoreV1EndpointAddress] = Field(..., alias="notReadyAddresses")
    ports: list[CoreV1EndpointPort] = Field(..., alias="ports")


class CoreV1Endpoints(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("Endpoints", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    subsets: list[CoreV1EndpointSubset] = Field(..., alias="subsets")


class CoreV1EndpointsList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1Endpoints] = Field(..., alias="items")
    kind: str = Field("EndpointsList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1EnvFromSource(BaseModel):
    config_map_ref: CoreV1ConfigMapEnvSource = Field(..., alias="configMapRef")
    prefix: str = Field(..., alias="prefix")
    secret_ref: CoreV1SecretEnvSource = Field(..., alias="secretRef")


class CoreV1EnvVar(BaseModel):
    name: str = Field(default="", alias="name")
    value: str = Field(..., alias="value")
    value_from: CoreV1EnvVarSource = Field(..., alias="valueFrom")


class CoreV1EnvVarSource(BaseModel):
    config_map_key_ref: CoreV1ConfigMapKeySelector = Field(..., alias="configMapKeyRef")
    field_ref: CoreV1ObjectFieldSelector = Field(..., alias="fieldRef")
    resource_field_ref: CoreV1ResourceFieldSelector = Field(..., alias="resourceFieldRef")
    secret_key_ref: CoreV1SecretKeySelector = Field(..., alias="secretKeyRef")


class CoreV1EphemeralVolumeSource(BaseModel):
    volume_claim_template: CoreV1PersistentVolumeClaimTemplate = Field(
        ..., alias="volumeClaimTemplate"
    )


class CoreV1Event(BaseModel):
    action: str = Field(..., alias="action")
    api_version: str = Field("v1", alias="apiVersion")
    count: int = Field(..., alias="count")
    event_time: MetaV1MicroTime = Field(default_factory=MetaV1MicroTime, alias="eventTime")
    first_timestamp: MetaV1Time = Field(default_factory=MetaV1Time, alias="firstTimestamp")
    involved_object: CoreV1ObjectReference = Field(
        default_factory=CoreV1ObjectReference, alias="involvedObject"
    )
    kind: str = Field("Event", alias="kind")
    last_timestamp: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastTimestamp")
    message: str = Field(..., alias="message")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    reason: str = Field(..., alias="reason")
    related: CoreV1ObjectReference = Field(..., alias="related")
    reporting_component: str = Field(default="", alias="reportingComponent")
    reporting_instance: str = Field(default="", alias="reportingInstance")
    series: CoreV1EventSeries = Field(..., alias="series")
    source: CoreV1EventSource = Field(default_factory=CoreV1EventSource, alias="source")
    type: str = Field(..., alias="type")


class CoreV1EventList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1Event] = Field(..., alias="items")
    kind: str = Field("EventList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1EventSeries(BaseModel):
    count: int = Field(..., alias="count")
    last_observed_time: MetaV1MicroTime = Field(
        default_factory=MetaV1MicroTime, alias="lastObservedTime"
    )


class CoreV1EventSource(BaseModel):
    component: str = Field(..., alias="component")
    host: str = Field(..., alias="host")


class CoreV1FlockerVolumeSource(BaseModel):
    dataset_name: str = Field(..., alias="datasetName")
    dataset_uuid: str = Field(..., alias="datasetUUID")


class CoreV1GCEPersistentDiskVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    partition: int = Field(..., alias="partition")
    pd_name: str = Field(default="", alias="pdName")
    read_only: bool = Field(..., alias="readOnly")


class CoreV1GRPCAction(BaseModel):
    port: int = Field(default=0, alias="port")
    service: str = Field(default="", alias="service")


class CoreV1GitRepoVolumeSource(BaseModel):
    directory: str = Field(..., alias="directory")
    repository: str = Field(default="", alias="repository")
    revision: str = Field(..., alias="revision")


class CoreV1GlusterfsPersistentVolumeSource(BaseModel):
    endpoints: str = Field(default="", alias="endpoints")
    endpoints_namespace: str = Field(..., alias="endpointsNamespace")
    path: str = Field(default="", alias="path")
    read_only: bool = Field(..., alias="readOnly")


class CoreV1GlusterfsVolumeSource(BaseModel):
    endpoints: str = Field(default="", alias="endpoints")
    path: str = Field(default="", alias="path")
    read_only: bool = Field(..., alias="readOnly")


class CoreV1HTTPGetAction(BaseModel):
    host: str = Field(..., alias="host")
    http_headers: list[CoreV1HTTPHeader] = Field(..., alias="httpHeaders")
    path: str = Field(..., alias="path")
    port: iok8sapimachinerypkgutilintstrIntOrString = Field(
        default_factory=iok8sapimachinerypkgutilintstrIntOrString, alias="port"
    )
    scheme: str = Field(..., alias="scheme")


class CoreV1HTTPHeader(BaseModel):
    name: str = Field(default="", alias="name")
    value: str = Field(default="", alias="value")


class CoreV1HostPathVolumeSource(BaseModel):
    path: str = Field(default="", alias="path")
    type: str = Field(..., alias="type")


class CoreV1KeyToPath(BaseModel):
    key: str = Field(default="", alias="key")
    mode: int = Field(..., alias="mode")
    path: str = Field(default="", alias="path")


class CoreV1Lifecycle(BaseModel):
    post_start: CoreV1LifecycleHandler = Field(..., alias="postStart")
    pre_stop: CoreV1LifecycleHandler = Field(..., alias="preStop")


class CoreV1LifecycleHandler(BaseModel):
    exec: CoreV1ExecAction = Field(..., alias="exec")
    http_get: CoreV1HTTPGetAction = Field(..., alias="httpGet")
    tcp_socket: CoreV1TCPSocketAction = Field(..., alias="tcpSocket")


class CoreV1LimitRange(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("LimitRange", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1LimitRangeSpec = Field(default_factory=CoreV1LimitRangeSpec, alias="spec")


class CoreV1LimitRangeList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1LimitRange] = Field(..., alias="items")
    kind: str = Field("LimitRangeList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1LimitRangeSpec(BaseModel):
    limits: list[CoreV1LimitRangeItem] = Field(..., alias="limits")


class CoreV1LoadBalancerIngress(BaseModel):
    hostname: str = Field(..., alias="hostname")
    ip: str = Field(..., alias="ip")
    ports: list[CoreV1PortStatus] = Field(..., alias="ports")


class CoreV1LoadBalancerStatus(BaseModel):
    ingress: list[CoreV1LoadBalancerIngress] = Field(..., alias="ingress")


class CoreV1LocalObjectReference(BaseModel):
    name: str = Field(..., alias="name")


class CoreV1LocalVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    path: str = Field(default="", alias="path")


class CoreV1NFSVolumeSource(BaseModel):
    path: str = Field(default="", alias="path")
    read_only: bool = Field(..., alias="readOnly")
    server: str = Field(default="", alias="server")


class CoreV1Namespace(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("Namespace", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1NamespaceSpec = Field(default_factory=CoreV1NamespaceSpec, alias="spec")
    status: CoreV1NamespaceStatus = Field(default_factory=CoreV1NamespaceStatus, alias="status")


class CoreV1NamespaceCondition(BaseModel):
    last_transition_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastTransitionTime")
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1NamespaceList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1Namespace] = Field(..., alias="items")
    kind: str = Field("NamespaceList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1NamespaceStatus(BaseModel):
    conditions: list[CoreV1NamespaceCondition] = Field(..., alias="conditions")
    phase: str = Field(..., alias="phase")


class CoreV1Node(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("Node", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1NodeSpec = Field(default_factory=CoreV1NodeSpec, alias="spec")
    status: CoreV1NodeStatus = Field(default_factory=CoreV1NodeStatus, alias="status")


class CoreV1NodeAddress(BaseModel):
    address: str = Field(default="", alias="address")
    type: str = Field(default="", alias="type")


class CoreV1NodeAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1PreferredSchedulingTerm
    ] = Field(..., alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: CoreV1NodeSelector = Field(
        ..., alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1NodeCondition(BaseModel):
    last_heartbeat_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastHeartbeatTime")
    last_transition_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastTransitionTime")
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1NodeConfigSource(BaseModel):
    config_map: CoreV1ConfigMapNodeConfigSource = Field(..., alias="configMap")


class CoreV1NodeConfigStatus(BaseModel):
    active: CoreV1NodeConfigSource = Field(..., alias="active")
    assigned: CoreV1NodeConfigSource = Field(..., alias="assigned")
    error: str = Field(..., alias="error")
    last_known_good: CoreV1NodeConfigSource = Field(..., alias="lastKnownGood")


class CoreV1NodeDaemonEndpoints(BaseModel):
    kubelet_endpoint: CoreV1DaemonEndpoint = Field(
        default_factory=CoreV1DaemonEndpoint, alias="kubeletEndpoint"
    )


class CoreV1NodeList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1Node] = Field(..., alias="items")
    kind: str = Field("NodeList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1NodeSelector(BaseModel):
    node_selector_terms: list[CoreV1NodeSelectorTerm] = Field(..., alias="nodeSelectorTerms")


class CoreV1NodeSelectorTerm(BaseModel):
    match_expressions: list[CoreV1NodeSelectorRequirement] = Field(..., alias="matchExpressions")
    match_fields: list[CoreV1NodeSelectorRequirement] = Field(..., alias="matchFields")


class CoreV1NodeSystemInfo(BaseModel):
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
    api_version: str = Field("v1", alias="apiVersion")
    field_path: str = Field(default="", alias="fieldPath")


class CoreV1ObjectReference(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    field_path: str = Field(..., alias="fieldPath")
    kind: str = Field("ObjectReference", alias="kind")
    name: str = Field(..., alias="name")
    namespace: str = Field(..., alias="namespace")
    resource_version: str = Field(..., alias="resourceVersion")
    uid: str = Field(..., alias="uid")


class CoreV1PersistentVolume(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("PersistentVolume", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1PersistentVolumeSpec = Field(
        default_factory=CoreV1PersistentVolumeSpec, alias="spec"
    )
    status: CoreV1PersistentVolumeStatus = Field(
        default_factory=CoreV1PersistentVolumeStatus, alias="status"
    )


class CoreV1PersistentVolumeClaim(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("PersistentVolumeClaim", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1PersistentVolumeClaimSpec = Field(
        default_factory=CoreV1PersistentVolumeClaimSpec, alias="spec"
    )
    status: CoreV1PersistentVolumeClaimStatus = Field(
        default_factory=CoreV1PersistentVolumeClaimStatus, alias="status"
    )


class CoreV1PersistentVolumeClaimCondition(BaseModel):
    last_probe_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastProbeTime")
    last_transition_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastTransitionTime")
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1PersistentVolumeClaimList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1PersistentVolumeClaim] = Field(..., alias="items")
    kind: str = Field("PersistentVolumeClaimList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1PersistentVolumeClaimTemplate(BaseModel):
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1PersistentVolumeClaimSpec = Field(
        default_factory=CoreV1PersistentVolumeClaimSpec, alias="spec"
    )


class CoreV1PersistentVolumeClaimVolumeSource(BaseModel):
    claim_name: str = Field(default="", alias="claimName")
    read_only: bool = Field(..., alias="readOnly")


class CoreV1PersistentVolumeList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1PersistentVolume] = Field(..., alias="items")
    kind: str = Field("PersistentVolumeList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1PersistentVolumeStatus(BaseModel):
    message: str = Field(..., alias="message")
    phase: str = Field(..., alias="phase")
    reason: str = Field(..., alias="reason")


class CoreV1PhotonPersistentDiskVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    pd_id: str = Field(default="", alias="pdID")


class CoreV1Pod(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("Pod", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1PodSpec = Field(default_factory=CoreV1PodSpec, alias="spec")
    status: CoreV1PodStatus = Field(default_factory=CoreV1PodStatus, alias="status")


class CoreV1PodAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1WeightedPodAffinityTerm
    ] = Field(..., alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: list[CoreV1PodAffinityTerm] = Field(
        ..., alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1PodAntiAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1WeightedPodAffinityTerm
    ] = Field(..., alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: list[CoreV1PodAffinityTerm] = Field(
        ..., alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1PodCondition(BaseModel):
    last_probe_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastProbeTime")
    last_transition_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastTransitionTime")
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1PodDNSConfigOption(BaseModel):
    name: str = Field(..., alias="name")
    value: str = Field(..., alias="value")


class CoreV1PodIP(BaseModel):
    ip: str = Field(..., alias="ip")


class CoreV1PodList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1Pod] = Field(..., alias="items")
    kind: str = Field("PodList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1PodOS(BaseModel):
    name: str = Field(default="", alias="name")


class CoreV1PodReadinessGate(BaseModel):
    condition_type: str = Field(default="", alias="conditionType")


class CoreV1PodStatus(BaseModel):
    conditions: list[CoreV1PodCondition] = Field(..., alias="conditions")
    container_statuses: list[CoreV1ContainerStatus] = Field(..., alias="containerStatuses")
    ephemeral_container_statuses: list[CoreV1ContainerStatus] = Field(
        ..., alias="ephemeralContainerStatuses"
    )
    host_ip: str = Field(..., alias="hostIP")
    init_container_statuses: list[CoreV1ContainerStatus] = Field(..., alias="initContainerStatuses")
    message: str = Field(..., alias="message")
    nominated_node_name: str = Field(..., alias="nominatedNodeName")
    phase: str = Field(..., alias="phase")
    pod_ip: str = Field(..., alias="podIP")
    pod_i_ps: list[CoreV1PodIP] = Field(..., alias="podIPs")
    qos_class: str = Field(..., alias="qosClass")
    reason: str = Field(..., alias="reason")
    start_time: MetaV1Time = Field(..., alias="startTime")


class CoreV1PodTemplate(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("PodTemplate", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    template: CoreV1PodTemplateSpec = Field(default_factory=CoreV1PodTemplateSpec, alias="template")


class CoreV1PodTemplateList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1PodTemplate] = Field(..., alias="items")
    kind: str = Field("PodTemplateList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1PodTemplateSpec(BaseModel):
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1PodSpec = Field(default_factory=CoreV1PodSpec, alias="spec")


class CoreV1PortStatus(BaseModel):
    error: str = Field(..., alias="error")
    port: int = Field(default=0, alias="port")
    protocol: str = Field(default="", alias="protocol")


class CoreV1PortworxVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    read_only: bool = Field(..., alias="readOnly")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1PreferredSchedulingTerm(BaseModel):
    preference: CoreV1NodeSelectorTerm = Field(
        default_factory=CoreV1NodeSelectorTerm, alias="preference"
    )
    weight: int = Field(default=0, alias="weight")


class CoreV1Probe(BaseModel):
    exec: CoreV1ExecAction = Field(..., alias="exec")
    failure_threshold: int = Field(..., alias="failureThreshold")
    grpc: CoreV1GRPCAction = Field(..., alias="grpc")
    http_get: CoreV1HTTPGetAction = Field(..., alias="httpGet")
    initial_delay_seconds: int = Field(..., alias="initialDelaySeconds")
    period_seconds: int = Field(..., alias="periodSeconds")
    success_threshold: int = Field(..., alias="successThreshold")
    tcp_socket: CoreV1TCPSocketAction = Field(..., alias="tcpSocket")
    termination_grace_period_seconds: int = Field(..., alias="terminationGracePeriodSeconds")
    timeout_seconds: int = Field(..., alias="timeoutSeconds")


class CoreV1ProjectedVolumeSource(BaseModel):
    default_mode: int = Field(..., alias="defaultMode")
    sources: list[CoreV1VolumeProjection] = Field(..., alias="sources")


class CoreV1QuobyteVolumeSource(BaseModel):
    group: str = Field(..., alias="group")
    read_only: bool = Field(..., alias="readOnly")
    registry: str = Field(default="", alias="registry")
    tenant: str = Field(..., alias="tenant")
    user: str = Field(..., alias="user")
    volume: str = Field(default="", alias="volume")


class CoreV1ReplicationController(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("ReplicationController", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1ReplicationControllerSpec = Field(
        default_factory=CoreV1ReplicationControllerSpec, alias="spec"
    )
    status: CoreV1ReplicationControllerStatus = Field(
        default_factory=CoreV1ReplicationControllerStatus, alias="status"
    )


class CoreV1ReplicationControllerCondition(BaseModel):
    last_transition_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastTransitionTime")
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class CoreV1ReplicationControllerList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1ReplicationController] = Field(..., alias="items")
    kind: str = Field("ReplicationControllerList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1ReplicationControllerStatus(BaseModel):
    available_replicas: int = Field(..., alias="availableReplicas")
    conditions: list[CoreV1ReplicationControllerCondition] = Field(..., alias="conditions")
    fully_labeled_replicas: int = Field(..., alias="fullyLabeledReplicas")
    observed_generation: int = Field(..., alias="observedGeneration")
    ready_replicas: int = Field(..., alias="readyReplicas")
    replicas: int = Field(default=0, alias="replicas")


class CoreV1ResourceFieldSelector(BaseModel):
    container_name: str = Field(..., alias="containerName")
    divisor: iok8sapimachinerypkgapiresourceQuantity = Field(
        default_factory=iok8sapimachinerypkgapiresourceQuantity, alias="divisor"
    )
    resource: str = Field(default="", alias="resource")


class CoreV1ResourceQuota(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("ResourceQuota", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1ResourceQuotaSpec = Field(default_factory=CoreV1ResourceQuotaSpec, alias="spec")
    status: CoreV1ResourceQuotaStatus = Field(
        default_factory=CoreV1ResourceQuotaStatus, alias="status"
    )


class CoreV1ResourceQuotaList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1ResourceQuota] = Field(..., alias="items")
    kind: str = Field("ResourceQuotaList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1SELinuxOptions(BaseModel):
    level: str = Field(..., alias="level")
    role: str = Field(..., alias="role")
    type: str = Field(..., alias="type")
    user: str = Field(..., alias="user")


class CoreV1ScaleIOPersistentVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    gateway: str = Field(default="", alias="gateway")
    protection_domain: str = Field(..., alias="protectionDomain")
    read_only: bool = Field(..., alias="readOnly")
    secret_ref: CoreV1SecretReference = Field(..., alias="secretRef")
    ssl_enabled: bool = Field(..., alias="sslEnabled")
    storage_mode: str = Field(..., alias="storageMode")
    storage_pool: str = Field(..., alias="storagePool")
    system: str = Field(default="", alias="system")
    volume_name: str = Field(..., alias="volumeName")


class CoreV1ScaleIOVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    gateway: str = Field(default="", alias="gateway")
    protection_domain: str = Field(..., alias="protectionDomain")
    read_only: bool = Field(..., alias="readOnly")
    secret_ref: CoreV1LocalObjectReference = Field(..., alias="secretRef")
    ssl_enabled: bool = Field(..., alias="sslEnabled")
    storage_mode: str = Field(..., alias="storageMode")
    storage_pool: str = Field(..., alias="storagePool")
    system: str = Field(default="", alias="system")
    volume_name: str = Field(..., alias="volumeName")


class CoreV1ScopeSelector(BaseModel):
    match_expressions: list[CoreV1ScopedResourceSelectorRequirement] = Field(
        ..., alias="matchExpressions"
    )


class CoreV1SeccompProfile(BaseModel):
    localhost_profile: str = Field(..., alias="localhostProfile")
    type: str = Field(default="", alias="type")


class CoreV1SecretEnvSource(BaseModel):
    name: str = Field(..., alias="name")
    optional: bool = Field(..., alias="optional")


class CoreV1SecretKeySelector(BaseModel):
    key: str = Field(default="", alias="key")
    name: str = Field(..., alias="name")
    optional: bool = Field(..., alias="optional")


class CoreV1SecretList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1Secret] = Field(..., alias="items")
    kind: str = Field("SecretList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1SecretProjection(BaseModel):
    items: list[CoreV1KeyToPath] = Field(..., alias="items")
    name: str = Field(..., alias="name")
    optional: bool = Field(..., alias="optional")


class CoreV1SecretReference(BaseModel):
    name: str = Field(..., alias="name")
    namespace: str = Field(..., alias="namespace")


class CoreV1SecretVolumeSource(BaseModel):
    default_mode: int = Field(..., alias="defaultMode")
    items: list[CoreV1KeyToPath] = Field(..., alias="items")
    optional: bool = Field(..., alias="optional")
    secret_name: str = Field(..., alias="secretName")


class CoreV1SecurityContext(BaseModel):
    allow_privilege_escalation: bool = Field(..., alias="allowPrivilegeEscalation")
    capabilities: CoreV1Capabilities = Field(..., alias="capabilities")
    privileged: bool = Field(..., alias="privileged")
    proc_mount: str = Field(..., alias="procMount")
    read_only_root_filesystem: bool = Field(..., alias="readOnlyRootFilesystem")
    run_as_group: int = Field(..., alias="runAsGroup")
    run_as_non_root: bool = Field(..., alias="runAsNonRoot")
    run_as_user: int = Field(..., alias="runAsUser")
    se_linux_options: CoreV1SELinuxOptions = Field(..., alias="seLinuxOptions")
    seccomp_profile: CoreV1SeccompProfile = Field(..., alias="seccompProfile")
    windows_options: CoreV1WindowsSecurityContextOptions = Field(..., alias="windowsOptions")


class CoreV1Service(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    kind: str = Field("Service", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    spec: CoreV1ServiceSpec = Field(default_factory=CoreV1ServiceSpec, alias="spec")
    status: CoreV1ServiceStatus = Field(default_factory=CoreV1ServiceStatus, alias="status")


class CoreV1ServiceAccount(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    automount_service_account_token: bool = Field(..., alias="automountServiceAccountToken")
    image_pull_secrets: list[CoreV1LocalObjectReference] = Field(..., alias="imagePullSecrets")
    kind: str = Field("ServiceAccount", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")
    secrets: list[CoreV1ObjectReference] = Field(..., alias="secrets")


class CoreV1ServiceAccountList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1ServiceAccount] = Field(..., alias="items")
    kind: str = Field("ServiceAccountList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1ServiceAccountTokenProjection(BaseModel):
    audience: str = Field(..., alias="audience")
    expiration_seconds: int = Field(..., alias="expirationSeconds")
    path: str = Field(default="", alias="path")


class CoreV1ServiceList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    items: list[CoreV1Service] = Field(..., alias="items")
    kind: str = Field("ServiceList", alias="kind")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")


class CoreV1ServicePort(BaseModel):
    app_protocol: str = Field(..., alias="appProtocol")
    name: str = Field(..., alias="name")
    node_port: int = Field(..., alias="nodePort")
    port: int = Field(default=0, alias="port")
    protocol: str = Field(default="TCP", alias="protocol")
    target_port: iok8sapimachinerypkgutilintstrIntOrString = Field(
        default_factory=iok8sapimachinerypkgutilintstrIntOrString, alias="targetPort"
    )


class CoreV1ServiceStatus(BaseModel):
    conditions: list[MetaV1Condition] = Field(..., alias="conditions")
    load_balancer: CoreV1LoadBalancerStatus = Field(
        default_factory=CoreV1LoadBalancerStatus, alias="loadBalancer"
    )


class CoreV1SessionAffinityConfig(BaseModel):
    client_ip: CoreV1ClientIPConfig = Field(..., alias="clientIP")


class CoreV1StorageOSPersistentVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    read_only: bool = Field(..., alias="readOnly")
    secret_ref: CoreV1ObjectReference = Field(..., alias="secretRef")
    volume_name: str = Field(..., alias="volumeName")
    volume_namespace: str = Field(..., alias="volumeNamespace")


class CoreV1StorageOSVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    read_only: bool = Field(..., alias="readOnly")
    secret_ref: CoreV1LocalObjectReference = Field(..., alias="secretRef")
    volume_name: str = Field(..., alias="volumeName")
    volume_namespace: str = Field(..., alias="volumeNamespace")


class CoreV1Sysctl(BaseModel):
    name: str = Field(default="", alias="name")
    value: str = Field(default="", alias="value")


class CoreV1TCPSocketAction(BaseModel):
    host: str = Field(..., alias="host")
    port: iok8sapimachinerypkgutilintstrIntOrString = Field(
        default_factory=iok8sapimachinerypkgutilintstrIntOrString, alias="port"
    )


class CoreV1Taint(BaseModel):
    effect: str = Field(default="", alias="effect")
    key: str = Field(default="", alias="key")
    time_added: MetaV1Time = Field(..., alias="timeAdded")
    value: str = Field(..., alias="value")


class CoreV1Toleration(BaseModel):
    effect: str = Field(..., alias="effect")
    key: str = Field(..., alias="key")
    operator: str = Field(..., alias="operator")
    toleration_seconds: int = Field(..., alias="tolerationSeconds")
    value: str = Field(..., alias="value")


class CoreV1TypedLocalObjectReference(BaseModel):
    api_group: str = Field(..., alias="apiGroup")
    kind: str = Field(default="", alias="kind")
    name: str = Field(default="", alias="name")


class CoreV1Volume(BaseModel):
    aws_elastic_block_store: CoreV1AWSElasticBlockStoreVolumeSource = Field(
        ..., alias="awsElasticBlockStore"
    )
    azure_disk: CoreV1AzureDiskVolumeSource = Field(..., alias="azureDisk")
    azure_file: CoreV1AzureFileVolumeSource = Field(..., alias="azureFile")
    cephfs: CoreV1CephFSVolumeSource = Field(..., alias="cephfs")
    cinder: CoreV1CinderVolumeSource = Field(..., alias="cinder")
    config_map: CoreV1ConfigMapVolumeSource = Field(..., alias="configMap")
    csi: CoreV1CSIVolumeSource = Field(..., alias="csi")
    downward_api: CoreV1DownwardAPIVolumeSource = Field(..., alias="downwardAPI")
    empty_dir: CoreV1EmptyDirVolumeSource = Field(..., alias="emptyDir")
    ephemeral: CoreV1EphemeralVolumeSource = Field(..., alias="ephemeral")
    fc: CoreV1FCVolumeSource = Field(..., alias="fc")
    flex_volume: CoreV1FlexVolumeSource = Field(..., alias="flexVolume")
    flocker: CoreV1FlockerVolumeSource = Field(..., alias="flocker")
    gce_persistent_disk: CoreV1GCEPersistentDiskVolumeSource = Field(..., alias="gcePersistentDisk")
    git_repo: CoreV1GitRepoVolumeSource = Field(..., alias="gitRepo")
    glusterfs: CoreV1GlusterfsVolumeSource = Field(..., alias="glusterfs")
    host_path: CoreV1HostPathVolumeSource = Field(..., alias="hostPath")
    iscsi: CoreV1ISCSIVolumeSource = Field(..., alias="iscsi")
    name: str = Field(default="", alias="name")
    nfs: CoreV1NFSVolumeSource = Field(..., alias="nfs")
    persistent_volume_claim: CoreV1PersistentVolumeClaimVolumeSource = Field(
        ..., alias="persistentVolumeClaim"
    )
    photon_persistent_disk: CoreV1PhotonPersistentDiskVolumeSource = Field(
        ..., alias="photonPersistentDisk"
    )
    portworx_volume: CoreV1PortworxVolumeSource = Field(..., alias="portworxVolume")
    projected: CoreV1ProjectedVolumeSource = Field(..., alias="projected")
    quobyte: CoreV1QuobyteVolumeSource = Field(..., alias="quobyte")
    rbd: CoreV1RBDVolumeSource = Field(..., alias="rbd")
    scale_io: CoreV1ScaleIOVolumeSource = Field(..., alias="scaleIO")
    secret: CoreV1SecretVolumeSource = Field(..., alias="secret")
    storageos: CoreV1StorageOSVolumeSource = Field(..., alias="storageos")
    vsphere_volume: CoreV1VsphereVirtualDiskVolumeSource = Field(..., alias="vsphereVolume")


class CoreV1VolumeDevice(BaseModel):
    device_path: str = Field(default="", alias="devicePath")
    name: str = Field(default="", alias="name")


class CoreV1VolumeMount(BaseModel):
    mount_path: str = Field(default="", alias="mountPath")
    mount_propagation: str = Field(..., alias="mountPropagation")
    name: str = Field(default="", alias="name")
    read_only: bool = Field(..., alias="readOnly")
    sub_path: str = Field(..., alias="subPath")
    sub_path_expr: str = Field(..., alias="subPathExpr")


class CoreV1VolumeNodeAffinity(BaseModel):
    required: CoreV1NodeSelector = Field(..., alias="required")


class CoreV1VolumeProjection(BaseModel):
    config_map: CoreV1ConfigMapProjection = Field(..., alias="configMap")
    downward_api: CoreV1DownwardAPIProjection = Field(..., alias="downwardAPI")
    secret: CoreV1SecretProjection = Field(..., alias="secret")
    service_account_token: CoreV1ServiceAccountTokenProjection = Field(
        ..., alias="serviceAccountToken"
    )


class CoreV1VsphereVirtualDiskVolumeSource(BaseModel):
    fs_type: str = Field(..., alias="fsType")
    storage_policy_id: str = Field(..., alias="storagePolicyID")
    storage_policy_name: str = Field(..., alias="storagePolicyName")
    volume_path: str = Field(default="", alias="volumePath")


class CoreV1WeightedPodAffinityTerm(BaseModel):
    pod_affinity_term: CoreV1PodAffinityTerm = Field(
        default_factory=CoreV1PodAffinityTerm, alias="podAffinityTerm"
    )
    weight: int = Field(default=0, alias="weight")


class CoreV1WindowsSecurityContextOptions(BaseModel):
    gmsa_credential_spec: str = Field(..., alias="gmsaCredentialSpec")
    gmsa_credential_spec_name: str = Field(..., alias="gmsaCredentialSpecName")
    host_process: bool = Field(..., alias="hostProcess")
    run_as_user_name: str = Field(..., alias="runAsUserName")


class iok8sapipolicyV1Eviction(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    delete_options: MetaV1DeleteOptions = Field(..., alias="deleteOptions")
    kind: str = Field("Eviction", alias="kind")
    metadata: MetaV1ObjectMeta = Field(default_factory=MetaV1ObjectMeta, alias="metadata")


class MetaV1APIResourceList(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    group_version: str = Field(default="", alias="groupVersion")
    kind: str = Field("APIResourceList", alias="kind")
    resources: list[MetaV1APIResource] = Field(..., alias="resources")


class MetaV1Condition(BaseModel):
    last_transition_time: MetaV1Time = Field(default_factory=MetaV1Time, alias="lastTransitionTime")
    message: str = Field(default="", alias="message")
    observed_generation: int = Field(..., alias="observedGeneration")
    reason: str = Field(default="", alias="reason")
    status: str = Field(default="", alias="status")
    type: str = Field(default="", alias="type")


class MetaV1ListMeta(BaseModel):
    continue_: str = Field(..., alias="continue_")
    remaining_item_count: int = Field(..., alias="remainingItemCount")
    resource_version: str = Field(..., alias="resourceVersion")
    self_link: str = Field(..., alias="selfLink")


class MetaV1ManagedFieldsEntry(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    fields_type: str = Field(..., alias="fieldsType")
    fields_v1: MetaV1FieldsV1 = Field(..., alias="fieldsV1")
    manager: str = Field(..., alias="manager")
    operation: str = Field(..., alias="operation")
    subresource: str = Field(..., alias="subresource")
    time: MetaV1Time = Field(..., alias="time")


class MetaV1OwnerReference(BaseModel):
    api_version: str = Field(default="", alias="apiVersion")
    block_owner_deletion: bool = Field(..., alias="blockOwnerDeletion")
    controller: bool = Field(..., alias="controller")
    kind: str = Field(default="", alias="kind")
    name: str = Field(default="", alias="name")
    uid: str = Field(default="", alias="uid")


class MetaV1Preconditions(BaseModel):
    resource_version: str = Field(..., alias="resourceVersion")
    uid: str = Field(..., alias="uid")


class MetaV1Status(BaseModel):
    api_version: str = Field("v1", alias="apiVersion")
    code: int = Field(..., alias="code")
    details: MetaV1StatusDetails = Field(..., alias="details")
    kind: str = Field("Status", alias="kind")
    message: str = Field(..., alias="message")
    metadata: MetaV1ListMeta = Field(default_factory=MetaV1ListMeta, alias="metadata")
    reason: str = Field(..., alias="reason")
    status: str = Field(..., alias="status")


class MetaV1StatusCause(BaseModel):
    field: str = Field(..., alias="field")
    message: str = Field(..., alias="message")
    reason: str = Field(..., alias="reason")


class MetaV1StatusDetails(BaseModel):
    causes: list[MetaV1StatusCause] = Field(..., alias="causes")
    group: str = Field(..., alias="group")
    kind: str = Field("StatusDetails", alias="kind")
    name: str = Field(..., alias="name")
    retry_after_seconds: int = Field(..., alias="retryAfterSeconds")
    uid: str = Field(..., alias="uid")


class MetaV1WatchEvent(BaseModel):
    object: iok8sapimachinerypkgruntimeRawExtension = Field(
        default_factory=iok8sapimachinerypkgruntimeRawExtension, alias="object"
    )
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
) -> iok8sapiautoscalingV1Scale:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale
    Op ID: readCoreV1NamespacedReplicationControllerScale
    Derived params: ['namespace', 'name']
    """
    async with session.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale"
    ) as response:
        return iok8sapiautoscalingV1Scale.parse_obj(await response.json())


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
