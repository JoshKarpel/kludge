from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field
from textual import log

from kludge.klient import Klient


class AuthenticationV1BoundObjectReference(BaseModel):
    """
    Original name: io.k8s.api.authentication.v1.BoundObjectReference
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    name: str | None = Field(default=None)
    uid: str | None = Field(default=None)


class AuthenticationV1TokenRequest(BaseModel):
    """
    Original name: io.k8s.api.authentication.v1.TokenRequest
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: AuthenticationV1TokenRequestSpec = Field(default={})
    status: AuthenticationV1TokenRequestStatus = Field(default={})


class AuthenticationV1TokenRequestSpec(BaseModel):
    """
    Original name: io.k8s.api.authentication.v1.TokenRequestSpec
    """

    audiences: list[str] = Field(...)
    bound_object_ref: AuthenticationV1BoundObjectReference | None = Field(
        default=None, alias="boundObjectRef"
    )
    expiration_seconds: int | None = Field(default=None, alias="expirationSeconds")


class AuthenticationV1TokenRequestStatus(BaseModel):
    """
    Original name: io.k8s.api.authentication.v1.TokenRequestStatus
    """

    expiration_timestamp: datetime | None = Field(default=None, alias="expirationTimestamp")
    token: str = Field(default="")


class AutoscalingV1Scale(BaseModel):
    """
    Original name: io.k8s.api.autoscaling.v1.Scale
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: AutoscalingV1ScaleSpec = Field(default={})
    status: AutoscalingV1ScaleStatus = Field(default={})


class AutoscalingV1ScaleSpec(BaseModel):
    """
    Original name: io.k8s.api.autoscaling.v1.ScaleSpec
    """

    replicas: int | None = Field(default=None)


class AutoscalingV1ScaleStatus(BaseModel):
    """
    Original name: io.k8s.api.autoscaling.v1.ScaleStatus
    """

    replicas: int = Field(default=0)
    selector: str | None = Field(default=None)


class CoreV1AWSElasticBlockStoreVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AWSElasticBlockStoreVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    partition: int | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1Affinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Affinity
    """

    node_affinity: CoreV1NodeAffinity | None = Field(default=None, alias="nodeAffinity")
    pod_affinity: CoreV1PodAffinity | None = Field(default=None, alias="podAffinity")
    pod_anti_affinity: CoreV1PodAntiAffinity | None = Field(default=None, alias="podAntiAffinity")


class CoreV1AttachedVolume(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AttachedVolume
    """

    device_path: str = Field(default="", alias="devicePath")
    name: str = Field(default="")


class CoreV1AzureDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AzureDiskVolumeSource
    """

    caching_mode: str | None = Field(default=None, alias="cachingMode")
    disk_name: str = Field(default="", alias="diskName")
    disk_uri: str = Field(default="", alias="diskURI")
    fs_type: str | None = Field(default=None, alias="fsType")
    kind: str | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")


class CoreV1AzureFilePersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AzureFilePersistentVolumeSource
    """

    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_name: str = Field(default="", alias="secretName")
    secret_namespace: str | None = Field(default=None, alias="secretNamespace")
    share_name: str = Field(default="", alias="shareName")


class CoreV1AzureFileVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.AzureFileVolumeSource
    """

    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_name: str = Field(default="", alias="secretName")
    share_name: str = Field(default="", alias="shareName")


class CoreV1Binding(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Binding
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    target: CoreV1ObjectReference = Field(default={})


class CoreV1CSIPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CSIPersistentVolumeSource
    """

    controller_expand_secret_ref: CoreV1SecretReference | None = Field(
        default=None, alias="controllerExpandSecretRef"
    )
    controller_publish_secret_ref: CoreV1SecretReference | None = Field(
        default=None, alias="controllerPublishSecretRef"
    )
    driver: str = Field(default="")
    fs_type: str | None = Field(default=None, alias="fsType")
    node_expand_secret_ref: CoreV1SecretReference | None = Field(
        default=None, alias="nodeExpandSecretRef"
    )
    node_publish_secret_ref: CoreV1SecretReference | None = Field(
        default=None, alias="nodePublishSecretRef"
    )
    node_stage_secret_ref: CoreV1SecretReference | None = Field(
        default=None, alias="nodeStageSecretRef"
    )
    read_only: bool | None = Field(default=None, alias="readOnly")
    volume_attributes: dict[str, str] | None = Field(default=None, alias="volumeAttributes")
    volume_handle: str = Field(default="", alias="volumeHandle")


class CoreV1CSIVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CSIVolumeSource
    """

    driver: str = Field(default="")
    fs_type: str | None = Field(default=None, alias="fsType")
    node_publish_secret_ref: CoreV1LocalObjectReference | None = Field(
        default=None, alias="nodePublishSecretRef"
    )
    read_only: bool | None = Field(default=None, alias="readOnly")
    volume_attributes: dict[str, str] | None = Field(default=None, alias="volumeAttributes")


class CoreV1Capabilities(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Capabilities
    """

    add: list[str] | None = Field(default=None)
    drop: list[str] | None = Field(default=None)


class CoreV1CephFSPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CephFSPersistentVolumeSource
    """

    monitors: list[str] = Field(...)
    path: str | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_file: str | None = Field(default=None, alias="secretFile")
    secret_ref: CoreV1SecretReference | None = Field(default=None, alias="secretRef")
    user: str | None = Field(default=None)


class CoreV1CephFSVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CephFSVolumeSource
    """

    monitors: list[str] = Field(...)
    path: str | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_file: str | None = Field(default=None, alias="secretFile")
    secret_ref: CoreV1LocalObjectReference | None = Field(default=None, alias="secretRef")
    user: str | None = Field(default=None)


class CoreV1CinderPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CinderPersistentVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1SecretReference | None = Field(default=None, alias="secretRef")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1CinderVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.CinderVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1LocalObjectReference | None = Field(default=None, alias="secretRef")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1ClientIPConfig(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ClientIPConfig
    """

    timeout_seconds: int | None = Field(default=None, alias="timeoutSeconds")


class CoreV1ComponentCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ComponentCondition
    """

    error: str | None = Field(default=None)
    message: str | None = Field(default=None)
    status: str = Field(default="")
    type: str = Field(default="")


class CoreV1ComponentStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ComponentStatus
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    conditions: list[CoreV1ComponentCondition] | None = Field(default=None)
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})


class CoreV1ComponentStatusList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ComponentStatusList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1ComponentStatus] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1ConfigMap(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMap
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    binary_data: dict[str, str] | None = Field(default=None, alias="binaryData")
    data: dict[str, str] | None = Field(default=None)
    immutable: bool | None = Field(default=None)
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})


class CoreV1ConfigMapEnvSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapEnvSource
    """

    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)


class CoreV1ConfigMapKeySelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapKeySelector
    """

    key: str = Field(default="")
    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)


class CoreV1ConfigMapList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1ConfigMap] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1ConfigMapNodeConfigSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapNodeConfigSource
    """

    kubelet_config_key: str = Field(default="", alias="kubeletConfigKey")
    name: str = Field(default="")
    namespace: str = Field(default="")
    resource_version: str | None = Field(default=None, alias="resourceVersion")
    uid: str | None = Field(default=None)


class CoreV1ConfigMapProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapProjection
    """

    items: list[CoreV1KeyToPath] | None = Field(default=None)
    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)


class CoreV1ConfigMapVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ConfigMapVolumeSource
    """

    default_mode: int | None = Field(default=None, alias="defaultMode")
    items: list[CoreV1KeyToPath] | None = Field(default=None)
    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)


class CoreV1Container(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Container
    """

    args: list[str] | None = Field(default=None)
    command: list[str] | None = Field(default=None)
    env: list[CoreV1EnvVar] | None = Field(default=None)
    env_from: list[CoreV1EnvFromSource] | None = Field(default=None, alias="envFrom")
    image: str | None = Field(default=None)
    image_pull_policy: str | None = Field(default=None, alias="imagePullPolicy")
    lifecycle: CoreV1Lifecycle | None = Field(default=None)
    liveness_probe: CoreV1Probe | None = Field(default=None, alias="livenessProbe")
    name: str = Field(default="")
    ports: list[CoreV1ContainerPort] | None = Field(default=None)
    readiness_probe: CoreV1Probe | None = Field(default=None, alias="readinessProbe")
    resources: CoreV1ResourceRequirements = Field(default={})
    security_context: CoreV1SecurityContext | None = Field(default=None, alias="securityContext")
    startup_probe: CoreV1Probe | None = Field(default=None, alias="startupProbe")
    stdin: bool | None = Field(default=None)
    stdin_once: bool | None = Field(default=None, alias="stdinOnce")
    termination_message_path: str | None = Field(default=None, alias="terminationMessagePath")
    termination_message_policy: str | None = Field(default=None, alias="terminationMessagePolicy")
    tty: bool | None = Field(default=None)
    volume_devices: list[CoreV1VolumeDevice] | None = Field(default=None, alias="volumeDevices")
    volume_mounts: list[CoreV1VolumeMount] | None = Field(default=None, alias="volumeMounts")
    working_dir: str | None = Field(default=None, alias="workingDir")


class CoreV1ContainerImage(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerImage
    """

    names: list[str] | None = Field(default=None)
    size_bytes: int | None = Field(default=None, alias="sizeBytes")


class CoreV1ContainerPort(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerPort
    """

    container_port: int = Field(default=0, alias="containerPort")
    host_ip: str | None = Field(default=None, alias="hostIP")
    host_port: int | None = Field(default=None, alias="hostPort")
    name: str | None = Field(default=None)
    protocol: str = Field(default="TCP")


class CoreV1ContainerState(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerState
    """

    running: CoreV1ContainerStateRunning | None = Field(default=None)
    terminated: CoreV1ContainerStateTerminated | None = Field(default=None)
    waiting: CoreV1ContainerStateWaiting | None = Field(default=None)


class CoreV1ContainerStateRunning(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStateRunning
    """

    started_at: datetime | None = Field(default=None, alias="startedAt")


class CoreV1ContainerStateTerminated(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStateTerminated
    """

    container_id: str | None = Field(default=None, alias="containerID")
    exit_code: int = Field(default=0, alias="exitCode")
    finished_at: datetime | None = Field(default=None, alias="finishedAt")
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    signal: int | None = Field(default=None)
    started_at: datetime | None = Field(default=None, alias="startedAt")


class CoreV1ContainerStateWaiting(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStateWaiting
    """

    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)


class CoreV1ContainerStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ContainerStatus
    """

    container_id: str | None = Field(default=None, alias="containerID")
    image: str = Field(default="")
    image_id: str = Field(default="", alias="imageID")
    last_state: CoreV1ContainerState = Field(default={}, alias="lastState")
    name: str = Field(default="")
    ready: bool = Field(default=False)
    restart_count: int = Field(default=0, alias="restartCount")
    started: bool | None = Field(default=None)
    state: CoreV1ContainerState = Field(default={})


class CoreV1DaemonEndpoint(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DaemonEndpoint
    """

    port: int = Field(default=0, alias="Port")


class CoreV1DownwardAPIProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DownwardAPIProjection
    """

    items: list[CoreV1DownwardAPIVolumeFile] | None = Field(default=None)


class CoreV1DownwardAPIVolumeFile(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DownwardAPIVolumeFile
    """

    field_ref: CoreV1ObjectFieldSelector | None = Field(default=None, alias="fieldRef")
    mode: int | None = Field(default=None)
    path: str = Field(default="")
    resource_field_ref: CoreV1ResourceFieldSelector | None = Field(
        default=None, alias="resourceFieldRef"
    )


class CoreV1DownwardAPIVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.DownwardAPIVolumeSource
    """

    default_mode: int | None = Field(default=None, alias="defaultMode")
    items: list[CoreV1DownwardAPIVolumeFile] | None = Field(default=None)


class CoreV1EmptyDirVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EmptyDirVolumeSource
    """

    medium: str | None = Field(default=None)
    size_limit: iok8sapimachinerypkgapiresourceQuantity | None = Field(
        default=None, alias="sizeLimit"
    )


class CoreV1EndpointAddress(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointAddress
    """

    hostname: str | None = Field(default=None)
    ip: str = Field(default="")
    node_name: str | None = Field(default=None, alias="nodeName")
    target_ref: CoreV1ObjectReference | None = Field(default=None, alias="targetRef")


class CoreV1EndpointPort(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointPort
    """

    app_protocol: str | None = Field(default=None, alias="appProtocol")
    name: str | None = Field(default=None)
    port: int = Field(default=0)
    protocol: str | None = Field(default=None)


class CoreV1EndpointSubset(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointSubset
    """

    addresses: list[CoreV1EndpointAddress] | None = Field(default=None)
    not_ready_addresses: list[CoreV1EndpointAddress] | None = Field(
        default=None, alias="notReadyAddresses"
    )
    ports: list[CoreV1EndpointPort] | None = Field(default=None)


class CoreV1Endpoints(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Endpoints
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    subsets: list[CoreV1EndpointSubset] | None = Field(default=None)


class CoreV1EndpointsList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EndpointsList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1Endpoints] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1EnvFromSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EnvFromSource
    """

    config_map_ref: CoreV1ConfigMapEnvSource | None = Field(default=None, alias="configMapRef")
    prefix: str | None = Field(default=None)
    secret_ref: CoreV1SecretEnvSource | None = Field(default=None, alias="secretRef")


class CoreV1EnvVar(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EnvVar
    """

    name: str = Field(default="")
    value: str | None = Field(default=None)
    value_from: CoreV1EnvVarSource | None = Field(default=None, alias="valueFrom")


class CoreV1EnvVarSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EnvVarSource
    """

    config_map_key_ref: CoreV1ConfigMapKeySelector | None = Field(
        default=None, alias="configMapKeyRef"
    )
    field_ref: CoreV1ObjectFieldSelector | None = Field(default=None, alias="fieldRef")
    resource_field_ref: CoreV1ResourceFieldSelector | None = Field(
        default=None, alias="resourceFieldRef"
    )
    secret_key_ref: CoreV1SecretKeySelector | None = Field(default=None, alias="secretKeyRef")


class CoreV1EphemeralContainer(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EphemeralContainer
    """

    args: list[str] | None = Field(default=None)
    command: list[str] | None = Field(default=None)
    env: list[CoreV1EnvVar] | None = Field(default=None)
    env_from: list[CoreV1EnvFromSource] | None = Field(default=None, alias="envFrom")
    image: str | None = Field(default=None)
    image_pull_policy: str | None = Field(default=None, alias="imagePullPolicy")
    lifecycle: CoreV1Lifecycle | None = Field(default=None)
    liveness_probe: CoreV1Probe | None = Field(default=None, alias="livenessProbe")
    name: str = Field(default="")
    ports: list[CoreV1ContainerPort] | None = Field(default=None)
    readiness_probe: CoreV1Probe | None = Field(default=None, alias="readinessProbe")
    resources: CoreV1ResourceRequirements = Field(default={})
    security_context: CoreV1SecurityContext | None = Field(default=None, alias="securityContext")
    startup_probe: CoreV1Probe | None = Field(default=None, alias="startupProbe")
    stdin: bool | None = Field(default=None)
    stdin_once: bool | None = Field(default=None, alias="stdinOnce")
    target_container_name: str | None = Field(default=None, alias="targetContainerName")
    termination_message_path: str | None = Field(default=None, alias="terminationMessagePath")
    termination_message_policy: str | None = Field(default=None, alias="terminationMessagePolicy")
    tty: bool | None = Field(default=None)
    volume_devices: list[CoreV1VolumeDevice] | None = Field(default=None, alias="volumeDevices")
    volume_mounts: list[CoreV1VolumeMount] | None = Field(default=None, alias="volumeMounts")
    working_dir: str | None = Field(default=None, alias="workingDir")


class CoreV1EphemeralVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EphemeralVolumeSource
    """

    volume_claim_template: CoreV1PersistentVolumeClaimTemplate | None = Field(
        default=None, alias="volumeClaimTemplate"
    )


class CoreV1Event(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Event
    """

    action: str | None = Field(default=None)
    api_version: str | None = Field(default=None, alias="apiVersion")
    count: int | None = Field(default=None)
    event_time: MetaV1MicroTime = Field(default={}, alias="eventTime")
    first_timestamp: datetime | None = Field(default=None, alias="firstTimestamp")
    involved_object: CoreV1ObjectReference = Field(default={}, alias="involvedObject")
    kind: str | None = Field(default=None)
    last_timestamp: datetime | None = Field(default=None, alias="lastTimestamp")
    message: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    reason: str | None = Field(default=None)
    related: CoreV1ObjectReference | None = Field(default=None)
    reporting_component: str = Field(default="", alias="reportingComponent")
    reporting_instance: str = Field(default="", alias="reportingInstance")
    series: CoreV1EventSeries | None = Field(default=None)
    source: CoreV1EventSource = Field(default={})
    type: str | None = Field(default=None)


class CoreV1EventList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EventList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1Event] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1EventSeries(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EventSeries
    """

    count: int | None = Field(default=None)
    last_observed_time: MetaV1MicroTime = Field(default={}, alias="lastObservedTime")


class CoreV1EventSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.EventSource
    """

    component: str | None = Field(default=None)
    host: str | None = Field(default=None)


class CoreV1ExecAction(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ExecAction
    """

    command: list[str] | None = Field(default=None)


class CoreV1FCVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.FCVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    lun: int | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    target_ww_ns: list[str] | None = Field(default=None, alias="targetWWNs")
    wwids: list[str] | None = Field(default=None)


class CoreV1FlexPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.FlexPersistentVolumeSource
    """

    driver: str = Field(default="")
    fs_type: str | None = Field(default=None, alias="fsType")
    options: dict[str, str] | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1SecretReference | None = Field(default=None, alias="secretRef")


class CoreV1FlexVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.FlexVolumeSource
    """

    driver: str = Field(default="")
    fs_type: str | None = Field(default=None, alias="fsType")
    options: dict[str, str] | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1LocalObjectReference | None = Field(default=None, alias="secretRef")


class CoreV1FlockerVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.FlockerVolumeSource
    """

    dataset_name: str | None = Field(default=None, alias="datasetName")
    dataset_uuid: str | None = Field(default=None, alias="datasetUUID")


class CoreV1GCEPersistentDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GCEPersistentDiskVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    partition: int | None = Field(default=None)
    pd_name: str = Field(default="", alias="pdName")
    read_only: bool | None = Field(default=None, alias="readOnly")


class CoreV1GRPCAction(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GRPCAction
    """

    port: int = Field(default=0)
    service: str = Field(default="")


class CoreV1GitRepoVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GitRepoVolumeSource
    """

    directory: str | None = Field(default=None)
    repository: str = Field(default="")
    revision: str | None = Field(default=None)


class CoreV1GlusterfsPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GlusterfsPersistentVolumeSource
    """

    endpoints: str = Field(default="")
    endpoints_namespace: str | None = Field(default=None, alias="endpointsNamespace")
    path: str = Field(default="")
    read_only: bool | None = Field(default=None, alias="readOnly")


class CoreV1GlusterfsVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.GlusterfsVolumeSource
    """

    endpoints: str = Field(default="")
    path: str = Field(default="")
    read_only: bool | None = Field(default=None, alias="readOnly")


class CoreV1HTTPGetAction(BaseModel):
    """
    Original name: io.k8s.api.core.v1.HTTPGetAction
    """

    host: str | None = Field(default=None)
    http_headers: list[CoreV1HTTPHeader] | None = Field(default=None, alias="httpHeaders")
    path: str | None = Field(default=None)
    port: UtilIntOrString = Field(default={})
    scheme: str | None = Field(default=None)


class CoreV1HTTPHeader(BaseModel):
    """
    Original name: io.k8s.api.core.v1.HTTPHeader
    """

    name: str = Field(default="")
    value: str = Field(default="")


class CoreV1HostAlias(BaseModel):
    """
    Original name: io.k8s.api.core.v1.HostAlias
    """

    hostnames: list[str] | None = Field(default=None)
    ip: str | None = Field(default=None)


class CoreV1HostPathVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.HostPathVolumeSource
    """

    path: str = Field(default="")
    type: str | None = Field(default=None)


class CoreV1ISCSIPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ISCSIPersistentVolumeSource
    """

    chap_auth_discovery: bool | None = Field(default=None, alias="chapAuthDiscovery")
    chap_auth_session: bool | None = Field(default=None, alias="chapAuthSession")
    fs_type: str | None = Field(default=None, alias="fsType")
    initiator_name: str | None = Field(default=None, alias="initiatorName")
    iqn: str = Field(default="")
    iscsi_interface: str | None = Field(default=None, alias="iscsiInterface")
    lun: int = Field(default=0)
    portals: list[str] | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1SecretReference | None = Field(default=None, alias="secretRef")
    target_portal: str = Field(default="", alias="targetPortal")


class CoreV1ISCSIVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ISCSIVolumeSource
    """

    chap_auth_discovery: bool | None = Field(default=None, alias="chapAuthDiscovery")
    chap_auth_session: bool | None = Field(default=None, alias="chapAuthSession")
    fs_type: str | None = Field(default=None, alias="fsType")
    initiator_name: str | None = Field(default=None, alias="initiatorName")
    iqn: str = Field(default="")
    iscsi_interface: str | None = Field(default=None, alias="iscsiInterface")
    lun: int = Field(default=0)
    portals: list[str] | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1LocalObjectReference | None = Field(default=None, alias="secretRef")
    target_portal: str = Field(default="", alias="targetPortal")


class CoreV1KeyToPath(BaseModel):
    """
    Original name: io.k8s.api.core.v1.KeyToPath
    """

    key: str = Field(default="")
    mode: int | None = Field(default=None)
    path: str = Field(default="")


class CoreV1Lifecycle(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Lifecycle
    """

    post_start: CoreV1LifecycleHandler | None = Field(default=None, alias="postStart")
    pre_stop: CoreV1LifecycleHandler | None = Field(default=None, alias="preStop")


class CoreV1LifecycleHandler(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LifecycleHandler
    """

    exec: CoreV1ExecAction | None = Field(default=None)
    http_get: CoreV1HTTPGetAction | None = Field(default=None, alias="httpGet")
    tcp_socket: CoreV1TCPSocketAction | None = Field(default=None, alias="tcpSocket")


class CoreV1LimitRange(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LimitRange
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1LimitRangeSpec = Field(default={})


class CoreV1LimitRangeItem(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LimitRangeItem
    """

    default: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    default_request: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(
        default=None, alias="defaultRequest"
    )
    max: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    max_limit_request_ratio: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(
        default=None, alias="maxLimitRequestRatio"
    )
    min: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    type: str = Field(default="")


class CoreV1LimitRangeList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LimitRangeList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1LimitRange] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1LimitRangeSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LimitRangeSpec
    """

    limits: list[CoreV1LimitRangeItem] = Field(...)


class CoreV1LoadBalancerIngress(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LoadBalancerIngress
    """

    hostname: str | None = Field(default=None)
    ip: str | None = Field(default=None)
    ports: list[CoreV1PortStatus] | None = Field(default=None)


class CoreV1LoadBalancerStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LoadBalancerStatus
    """

    ingress: list[CoreV1LoadBalancerIngress] | None = Field(default=None)


class CoreV1LocalObjectReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LocalObjectReference
    """

    name: str | None = Field(default=None)


class CoreV1LocalVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.LocalVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    path: str = Field(default="")


class CoreV1NFSVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NFSVolumeSource
    """

    path: str = Field(default="")
    read_only: bool | None = Field(default=None, alias="readOnly")
    server: str = Field(default="")


class CoreV1Namespace(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Namespace
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1NamespaceSpec = Field(default={})
    status: CoreV1NamespaceStatus = Field(default={})


class CoreV1NamespaceCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NamespaceCondition
    """

    last_transition_time: datetime | None = Field(default=None, alias="lastTransitionTime")
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    status: str = Field(default="")
    type: str = Field(default="")


class CoreV1NamespaceList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NamespaceList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1Namespace] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1NamespaceSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NamespaceSpec
    """

    finalizers: list[str] | None = Field(default=None)


class CoreV1NamespaceStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NamespaceStatus
    """

    conditions: list[CoreV1NamespaceCondition] | None = Field(default=None)
    phase: str | None = Field(default=None)


class CoreV1Node(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Node
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1NodeSpec = Field(default={})
    status: CoreV1NodeStatus = Field(default={})


class CoreV1NodeAddress(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeAddress
    """

    address: str = Field(default="")
    type: str = Field(default="")


class CoreV1NodeAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeAffinity
    """

    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1PreferredSchedulingTerm
    ] | None = Field(default=None, alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: CoreV1NodeSelector | None = Field(
        default=None, alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1NodeCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeCondition
    """

    last_heartbeat_time: datetime | None = Field(default=None, alias="lastHeartbeatTime")
    last_transition_time: datetime | None = Field(default=None, alias="lastTransitionTime")
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    status: str = Field(default="")
    type: str = Field(default="")


class CoreV1NodeConfigSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeConfigSource
    """

    config_map: CoreV1ConfigMapNodeConfigSource | None = Field(default=None, alias="configMap")


class CoreV1NodeConfigStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeConfigStatus
    """

    active: CoreV1NodeConfigSource | None = Field(default=None)
    assigned: CoreV1NodeConfigSource | None = Field(default=None)
    error: str | None = Field(default=None)
    last_known_good: CoreV1NodeConfigSource | None = Field(default=None, alias="lastKnownGood")


class CoreV1NodeDaemonEndpoints(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeDaemonEndpoints
    """

    kubelet_endpoint: CoreV1DaemonEndpoint = Field(default={}, alias="kubeletEndpoint")


class CoreV1NodeList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1Node] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1NodeSelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSelector
    """

    node_selector_terms: list[CoreV1NodeSelectorTerm] = Field(..., alias="nodeSelectorTerms")


class CoreV1NodeSelectorRequirement(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSelectorRequirement
    """

    key: str = Field(default="")
    operator: str = Field(default="")
    values: list[str] | None = Field(default=None)


class CoreV1NodeSelectorTerm(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSelectorTerm
    """

    match_expressions: list[CoreV1NodeSelectorRequirement] | None = Field(
        default=None, alias="matchExpressions"
    )
    match_fields: list[CoreV1NodeSelectorRequirement] | None = Field(
        default=None, alias="matchFields"
    )


class CoreV1NodeSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSpec
    """

    config_source: CoreV1NodeConfigSource | None = Field(default=None, alias="configSource")
    external_id: str | None = Field(default=None, alias="externalID")
    pod_cidr: str | None = Field(default=None, alias="podCIDR")
    pod_cid_rs: list[str] | None = Field(default=None, alias="podCIDRs")
    provider_id: str | None = Field(default=None, alias="providerID")
    taints: list[CoreV1Taint] | None = Field(default=None)
    unschedulable: bool | None = Field(default=None)


class CoreV1NodeStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeStatus
    """

    addresses: list[CoreV1NodeAddress] | None = Field(default=None)
    allocatable: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    capacity: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    conditions: list[CoreV1NodeCondition] | None = Field(default=None)
    config: CoreV1NodeConfigStatus | None = Field(default=None)
    daemon_endpoints: CoreV1NodeDaemonEndpoints = Field(default={}, alias="daemonEndpoints")
    images: list[CoreV1ContainerImage] | None = Field(default=None)
    node_info: CoreV1NodeSystemInfo = Field(default={}, alias="nodeInfo")
    phase: str | None = Field(default=None)
    volumes_attached: list[CoreV1AttachedVolume] | None = Field(
        default=None, alias="volumesAttached"
    )
    volumes_in_use: list[str] | None = Field(default=None, alias="volumesInUse")


class CoreV1NodeSystemInfo(BaseModel):
    """
    Original name: io.k8s.api.core.v1.NodeSystemInfo
    """

    architecture: str = Field(default="")
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

    api_version: str | None = Field(default=None, alias="apiVersion")
    field_path: str = Field(default="", alias="fieldPath")


class CoreV1ObjectReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ObjectReference
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    field_path: str | None = Field(default=None, alias="fieldPath")
    kind: str | None = Field(default=None)
    name: str | None = Field(default=None)
    namespace: str | None = Field(default=None)
    resource_version: str | None = Field(default=None, alias="resourceVersion")
    uid: str | None = Field(default=None)


class CoreV1PersistentVolume(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolume
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1PersistentVolumeSpec = Field(default={})
    status: CoreV1PersistentVolumeStatus = Field(default={})


class CoreV1PersistentVolumeClaim(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaim
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1PersistentVolumeClaimSpec = Field(default={})
    status: CoreV1PersistentVolumeClaimStatus = Field(default={})


class CoreV1PersistentVolumeClaimCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimCondition
    """

    last_probe_time: datetime | None = Field(default=None, alias="lastProbeTime")
    last_transition_time: datetime | None = Field(default=None, alias="lastTransitionTime")
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    status: str = Field(default="")
    type: str = Field(default="")


class CoreV1PersistentVolumeClaimList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1PersistentVolumeClaim] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1PersistentVolumeClaimSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimSpec
    """

    access_modes: list[str] | None = Field(default=None, alias="accessModes")
    data_source: CoreV1TypedLocalObjectReference | None = Field(default=None, alias="dataSource")
    data_source_ref: CoreV1TypedLocalObjectReference | None = Field(
        default=None, alias="dataSourceRef"
    )
    resources: CoreV1ResourceRequirements = Field(default={})
    selector: MetaV1LabelSelector | None = Field(default=None)
    storage_class_name: str | None = Field(default=None, alias="storageClassName")
    volume_mode: str | None = Field(default=None, alias="volumeMode")
    volume_name: str | None = Field(default=None, alias="volumeName")


class CoreV1PersistentVolumeClaimStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimStatus
    """

    access_modes: list[str] | None = Field(default=None, alias="accessModes")
    allocated_resources: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(
        default=None, alias="allocatedResources"
    )
    capacity: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    conditions: list[CoreV1PersistentVolumeClaimCondition] | None = Field(default=None)
    phase: str | None = Field(default=None)
    resize_status: str | None = Field(default=None, alias="resizeStatus")


class CoreV1PersistentVolumeClaimTemplate(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimTemplate
    """

    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1PersistentVolumeClaimSpec = Field(default={})


class CoreV1PersistentVolumeClaimVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeClaimVolumeSource
    """

    claim_name: str = Field(default="", alias="claimName")
    read_only: bool | None = Field(default=None, alias="readOnly")


class CoreV1PersistentVolumeList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1PersistentVolume] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1PersistentVolumeSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeSpec
    """

    access_modes: list[str] | None = Field(default=None, alias="accessModes")
    aws_elastic_block_store: CoreV1AWSElasticBlockStoreVolumeSource | None = Field(
        default=None, alias="awsElasticBlockStore"
    )
    azure_disk: CoreV1AzureDiskVolumeSource | None = Field(default=None, alias="azureDisk")
    azure_file: CoreV1AzureFilePersistentVolumeSource | None = Field(
        default=None, alias="azureFile"
    )
    capacity: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    cephfs: CoreV1CephFSPersistentVolumeSource | None = Field(default=None)
    cinder: CoreV1CinderPersistentVolumeSource | None = Field(default=None)
    claim_ref: CoreV1ObjectReference | None = Field(default=None, alias="claimRef")
    csi: CoreV1CSIPersistentVolumeSource | None = Field(default=None)
    fc: CoreV1FCVolumeSource | None = Field(default=None)
    flex_volume: CoreV1FlexPersistentVolumeSource | None = Field(default=None, alias="flexVolume")
    flocker: CoreV1FlockerVolumeSource | None = Field(default=None)
    gce_persistent_disk: CoreV1GCEPersistentDiskVolumeSource | None = Field(
        default=None, alias="gcePersistentDisk"
    )
    glusterfs: CoreV1GlusterfsPersistentVolumeSource | None = Field(default=None)
    host_path: CoreV1HostPathVolumeSource | None = Field(default=None, alias="hostPath")
    iscsi: CoreV1ISCSIPersistentVolumeSource | None = Field(default=None)
    local: CoreV1LocalVolumeSource | None = Field(default=None)
    mount_options: list[str] | None = Field(default=None, alias="mountOptions")
    nfs: CoreV1NFSVolumeSource | None = Field(default=None)
    node_affinity: CoreV1VolumeNodeAffinity | None = Field(default=None, alias="nodeAffinity")
    persistent_volume_reclaim_policy: str | None = Field(
        default=None, alias="persistentVolumeReclaimPolicy"
    )
    photon_persistent_disk: CoreV1PhotonPersistentDiskVolumeSource | None = Field(
        default=None, alias="photonPersistentDisk"
    )
    portworx_volume: CoreV1PortworxVolumeSource | None = Field(default=None, alias="portworxVolume")
    quobyte: CoreV1QuobyteVolumeSource | None = Field(default=None)
    rbd: CoreV1RBDPersistentVolumeSource | None = Field(default=None)
    scale_io: CoreV1ScaleIOPersistentVolumeSource | None = Field(default=None, alias="scaleIO")
    storage_class_name: str | None = Field(default=None, alias="storageClassName")
    storageos: CoreV1StorageOSPersistentVolumeSource | None = Field(default=None)
    volume_mode: str | None = Field(default=None, alias="volumeMode")
    vsphere_volume: CoreV1VsphereVirtualDiskVolumeSource | None = Field(
        default=None, alias="vsphereVolume"
    )


class CoreV1PersistentVolumeStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PersistentVolumeStatus
    """

    message: str | None = Field(default=None)
    phase: str | None = Field(default=None)
    reason: str | None = Field(default=None)


class CoreV1PhotonPersistentDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PhotonPersistentDiskVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    pd_id: str = Field(default="", alias="pdID")


class CoreV1Pod(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Pod
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1PodSpec = Field(default={})
    status: CoreV1PodStatus = Field(default={})


class CoreV1PodAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodAffinity
    """

    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1WeightedPodAffinityTerm
    ] | None = Field(default=None, alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: list[CoreV1PodAffinityTerm] | None = Field(
        default=None, alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1PodAffinityTerm(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodAffinityTerm
    """

    label_selector: MetaV1LabelSelector | None = Field(default=None, alias="labelSelector")
    namespace_selector: MetaV1LabelSelector | None = Field(default=None, alias="namespaceSelector")
    namespaces: list[str] | None = Field(default=None)
    topology_key: str = Field(default="", alias="topologyKey")


class CoreV1PodAntiAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodAntiAffinity
    """

    preferred_during_scheduling_ignored_during_execution: list[
        CoreV1WeightedPodAffinityTerm
    ] | None = Field(default=None, alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: list[CoreV1PodAffinityTerm] | None = Field(
        default=None, alias="requiredDuringSchedulingIgnoredDuringExecution"
    )


class CoreV1PodCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodCondition
    """

    last_probe_time: datetime | None = Field(default=None, alias="lastProbeTime")
    last_transition_time: datetime | None = Field(default=None, alias="lastTransitionTime")
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    status: str = Field(default="")
    type: str = Field(default="")


class CoreV1PodDNSConfig(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodDNSConfig
    """

    nameservers: list[str] | None = Field(default=None)
    options: list[CoreV1PodDNSConfigOption] | None = Field(default=None)
    searches: list[str] | None = Field(default=None)


class CoreV1PodDNSConfigOption(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodDNSConfigOption
    """

    name: str | None = Field(default=None)
    value: str | None = Field(default=None)


class CoreV1PodIP(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodIP
    """

    ip: str | None = Field(default=None)


class CoreV1PodList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1Pod] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1PodOS(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodOS
    """

    name: str = Field(default="")


class CoreV1PodReadinessGate(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodReadinessGate
    """

    condition_type: str = Field(default="", alias="conditionType")


class CoreV1PodSecurityContext(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodSecurityContext
    """

    fs_group: int | None = Field(default=None, alias="fsGroup")
    fs_group_change_policy: str | None = Field(default=None, alias="fsGroupChangePolicy")
    run_as_group: int | None = Field(default=None, alias="runAsGroup")
    run_as_non_root: bool | None = Field(default=None, alias="runAsNonRoot")
    run_as_user: int | None = Field(default=None, alias="runAsUser")
    se_linux_options: CoreV1SELinuxOptions | None = Field(default=None, alias="seLinuxOptions")
    seccomp_profile: CoreV1SeccompProfile | None = Field(default=None, alias="seccompProfile")
    supplemental_groups: list[int] | None = Field(default=None, alias="supplementalGroups")
    sysctls: list[CoreV1Sysctl] | None = Field(default=None)
    windows_options: CoreV1WindowsSecurityContextOptions | None = Field(
        default=None, alias="windowsOptions"
    )


class CoreV1PodSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodSpec
    """

    active_deadline_seconds: int | None = Field(default=None, alias="activeDeadlineSeconds")
    affinity: CoreV1Affinity | None = Field(default=None)
    automount_service_account_token: bool | None = Field(
        default=None, alias="automountServiceAccountToken"
    )
    containers: list[CoreV1Container] = Field(...)
    dns_config: CoreV1PodDNSConfig | None = Field(default=None, alias="dnsConfig")
    dns_policy: str | None = Field(default=None, alias="dnsPolicy")
    enable_service_links: bool | None = Field(default=None, alias="enableServiceLinks")
    ephemeral_containers: list[CoreV1EphemeralContainer] | None = Field(
        default=None, alias="ephemeralContainers"
    )
    host_aliases: list[CoreV1HostAlias] | None = Field(default=None, alias="hostAliases")
    host_ip_c: bool | None = Field(default=None, alias="hostIPC")
    host_network: bool | None = Field(default=None, alias="hostNetwork")
    host_pid: bool | None = Field(default=None, alias="hostPID")
    host_users: bool | None = Field(default=None, alias="hostUsers")
    hostname: str | None = Field(default=None)
    image_pull_secrets: list[CoreV1LocalObjectReference] | None = Field(
        default=None, alias="imagePullSecrets"
    )
    init_containers: list[CoreV1Container] | None = Field(default=None, alias="initContainers")
    node_name: str | None = Field(default=None, alias="nodeName")
    node_selector: dict[str, str] | None = Field(default=None, alias="nodeSelector")
    os: CoreV1PodOS | None = Field(default=None)
    overhead: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    preemption_policy: str | None = Field(default=None, alias="preemptionPolicy")
    priority: int | None = Field(default=None)
    priority_class_name: str | None = Field(default=None, alias="priorityClassName")
    readiness_gates: list[CoreV1PodReadinessGate] | None = Field(
        default=None, alias="readinessGates"
    )
    restart_policy: str | None = Field(default=None, alias="restartPolicy")
    runtime_class_name: str | None = Field(default=None, alias="runtimeClassName")
    scheduler_name: str | None = Field(default=None, alias="schedulerName")
    security_context: CoreV1PodSecurityContext | None = Field(default=None, alias="securityContext")
    service_account: str | None = Field(default=None, alias="serviceAccount")
    service_account_name: str | None = Field(default=None, alias="serviceAccountName")
    set_hostname_as_fqdn: bool | None = Field(default=None, alias="setHostnameAsFQDN")
    share_process_namespace: bool | None = Field(default=None, alias="shareProcessNamespace")
    subdomain: str | None = Field(default=None)
    termination_grace_period_seconds: int | None = Field(
        default=None, alias="terminationGracePeriodSeconds"
    )
    tolerations: list[CoreV1Toleration] | None = Field(default=None)
    topology_spread_constraints: list[CoreV1TopologySpreadConstraint] | None = Field(
        default=None, alias="topologySpreadConstraints"
    )
    volumes: list[CoreV1Volume] | None = Field(default=None)


class CoreV1PodStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodStatus
    """

    conditions: list[CoreV1PodCondition] | None = Field(default=None)
    container_statuses: list[CoreV1ContainerStatus] | None = Field(
        default=None, alias="containerStatuses"
    )
    ephemeral_container_statuses: list[CoreV1ContainerStatus] | None = Field(
        default=None, alias="ephemeralContainerStatuses"
    )
    host_ip: str | None = Field(default=None, alias="hostIP")
    init_container_statuses: list[CoreV1ContainerStatus] | None = Field(
        default=None, alias="initContainerStatuses"
    )
    message: str | None = Field(default=None)
    nominated_node_name: str | None = Field(default=None, alias="nominatedNodeName")
    phase: str | None = Field(default=None)
    pod_ip: str | None = Field(default=None, alias="podIP")
    pod_ips: list[CoreV1PodIP] | None = Field(default=None, alias="podIPs")
    qos_class: str | None = Field(default=None, alias="qosClass")
    reason: str | None = Field(default=None)
    start_time: datetime | None = Field(default=None, alias="startTime")


class CoreV1PodTemplate(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodTemplate
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    template: CoreV1PodTemplateSpec = Field(default={})


class CoreV1PodTemplateList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodTemplateList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1PodTemplate] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1PodTemplateSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PodTemplateSpec
    """

    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1PodSpec = Field(default={})


class CoreV1PortStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PortStatus
    """

    error: str | None = Field(default=None)
    port: int = Field(default=0)
    protocol: str = Field(default="")


class CoreV1PortworxVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PortworxVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    read_only: bool | None = Field(default=None, alias="readOnly")
    volume_id: str = Field(default="", alias="volumeID")


class CoreV1PreferredSchedulingTerm(BaseModel):
    """
    Original name: io.k8s.api.core.v1.PreferredSchedulingTerm
    """

    preference: CoreV1NodeSelectorTerm = Field(default={})
    weight: int = Field(default=0)


class CoreV1Probe(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Probe
    """

    exec: CoreV1ExecAction | None = Field(default=None)
    failure_threshold: int | None = Field(default=None, alias="failureThreshold")
    grpc: CoreV1GRPCAction | None = Field(default=None)
    http_get: CoreV1HTTPGetAction | None = Field(default=None, alias="httpGet")
    initial_delay_seconds: int | None = Field(default=None, alias="initialDelaySeconds")
    period_seconds: int | None = Field(default=None, alias="periodSeconds")
    success_threshold: int | None = Field(default=None, alias="successThreshold")
    tcp_socket: CoreV1TCPSocketAction | None = Field(default=None, alias="tcpSocket")
    termination_grace_period_seconds: int | None = Field(
        default=None, alias="terminationGracePeriodSeconds"
    )
    timeout_seconds: int | None = Field(default=None, alias="timeoutSeconds")


class CoreV1ProjectedVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ProjectedVolumeSource
    """

    default_mode: int | None = Field(default=None, alias="defaultMode")
    sources: list[CoreV1VolumeProjection] | None = Field(default=None)


class CoreV1QuobyteVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.QuobyteVolumeSource
    """

    group: str | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    registry: str = Field(default="")
    tenant: str | None = Field(default=None)
    user: str | None = Field(default=None)
    volume: str = Field(default="")


class CoreV1RBDPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.RBDPersistentVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    image: str = Field(default="")
    keyring: str | None = Field(default=None)
    monitors: list[str] = Field(...)
    pool: str | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1SecretReference | None = Field(default=None, alias="secretRef")
    user: str | None = Field(default=None)


class CoreV1RBDVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.RBDVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    image: str = Field(default="")
    keyring: str | None = Field(default=None)
    monitors: list[str] = Field(...)
    pool: str | None = Field(default=None)
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1LocalObjectReference | None = Field(default=None, alias="secretRef")
    user: str | None = Field(default=None)


class CoreV1ReplicationController(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationController
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1ReplicationControllerSpec = Field(default={})
    status: CoreV1ReplicationControllerStatus = Field(default={})


class CoreV1ReplicationControllerCondition(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationControllerCondition
    """

    last_transition_time: datetime | None = Field(default=None, alias="lastTransitionTime")
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    status: str = Field(default="")
    type: str = Field(default="")


class CoreV1ReplicationControllerList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationControllerList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1ReplicationController] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1ReplicationControllerSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationControllerSpec
    """

    min_ready_seconds: int | None = Field(default=None, alias="minReadySeconds")
    replicas: int | None = Field(default=None)
    selector: dict[str, str] | None = Field(default=None)
    template: CoreV1PodTemplateSpec | None = Field(default=None)


class CoreV1ReplicationControllerStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ReplicationControllerStatus
    """

    available_replicas: int | None = Field(default=None, alias="availableReplicas")
    conditions: list[CoreV1ReplicationControllerCondition] | None = Field(default=None)
    fully_labeled_replicas: int | None = Field(default=None, alias="fullyLabeledReplicas")
    observed_generation: int | None = Field(default=None, alias="observedGeneration")
    ready_replicas: int | None = Field(default=None, alias="readyReplicas")
    replicas: int = Field(default=0)


class CoreV1ResourceFieldSelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceFieldSelector
    """

    container_name: str | None = Field(default=None, alias="containerName")
    divisor: iok8sapimachinerypkgapiresourceQuantity = Field(default={})
    resource: str = Field(default="")


class CoreV1ResourceQuota(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceQuota
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1ResourceQuotaSpec = Field(default={})
    status: CoreV1ResourceQuotaStatus = Field(default={})


class CoreV1ResourceQuotaList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceQuotaList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1ResourceQuota] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1ResourceQuotaSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceQuotaSpec
    """

    hard: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    scope_selector: CoreV1ScopeSelector | None = Field(default=None, alias="scopeSelector")
    scopes: list[str] | None = Field(default=None)


class CoreV1ResourceQuotaStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceQuotaStatus
    """

    hard: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    used: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)


class CoreV1ResourceRequirements(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ResourceRequirements
    """

    limits: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)
    requests: dict[str, iok8sapimachinerypkgapiresourceQuantity] | None = Field(default=None)


class CoreV1SELinuxOptions(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SELinuxOptions
    """

    level: str | None = Field(default=None)
    role: str | None = Field(default=None)
    type: str | None = Field(default=None)
    user: str | None = Field(default=None)


class CoreV1ScaleIOPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ScaleIOPersistentVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    gateway: str = Field(default="")
    protection_domain: str | None = Field(default=None, alias="protectionDomain")
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1SecretReference = Field(..., alias="secretRef")
    ssl_enabled: bool | None = Field(default=None, alias="sslEnabled")
    storage_mode: str | None = Field(default=None, alias="storageMode")
    storage_pool: str | None = Field(default=None, alias="storagePool")
    system: str = Field(default="")
    volume_name: str | None = Field(default=None, alias="volumeName")


class CoreV1ScaleIOVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ScaleIOVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    gateway: str = Field(default="")
    protection_domain: str | None = Field(default=None, alias="protectionDomain")
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1LocalObjectReference = Field(..., alias="secretRef")
    ssl_enabled: bool | None = Field(default=None, alias="sslEnabled")
    storage_mode: str | None = Field(default=None, alias="storageMode")
    storage_pool: str | None = Field(default=None, alias="storagePool")
    system: str = Field(default="")
    volume_name: str | None = Field(default=None, alias="volumeName")


class CoreV1ScopeSelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ScopeSelector
    """

    match_expressions: list[CoreV1ScopedResourceSelectorRequirement] | None = Field(
        default=None, alias="matchExpressions"
    )


class CoreV1ScopedResourceSelectorRequirement(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ScopedResourceSelectorRequirement
    """

    operator: str = Field(default="")
    scope_name: str = Field(default="", alias="scopeName")
    values: list[str] | None = Field(default=None)


class CoreV1SeccompProfile(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SeccompProfile
    """

    localhost_profile: str | None = Field(default=None, alias="localhostProfile")
    type: str = Field(default="")


class CoreV1Secret(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Secret
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    data: dict[str, str] | None = Field(default=None)
    immutable: bool | None = Field(default=None)
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    string_data: dict[str, str] | None = Field(default=None, alias="stringData")
    type: str | None = Field(default=None)


class CoreV1SecretEnvSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretEnvSource
    """

    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)


class CoreV1SecretKeySelector(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretKeySelector
    """

    key: str = Field(default="")
    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)


class CoreV1SecretList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1Secret] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1SecretProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretProjection
    """

    items: list[CoreV1KeyToPath] | None = Field(default=None)
    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)


class CoreV1SecretReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretReference
    """

    name: str | None = Field(default=None)
    namespace: str | None = Field(default=None)


class CoreV1SecretVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecretVolumeSource
    """

    default_mode: int | None = Field(default=None, alias="defaultMode")
    items: list[CoreV1KeyToPath] | None = Field(default=None)
    optional: bool | None = Field(default=None)
    secret_name: str | None = Field(default=None, alias="secretName")


class CoreV1SecurityContext(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SecurityContext
    """

    allow_privilege_escalation: bool | None = Field(default=None, alias="allowPrivilegeEscalation")
    capabilities: CoreV1Capabilities | None = Field(default=None)
    privileged: bool | None = Field(default=None)
    proc_mount: str | None = Field(default=None, alias="procMount")
    read_only_root_filesystem: bool | None = Field(default=None, alias="readOnlyRootFilesystem")
    run_as_group: int | None = Field(default=None, alias="runAsGroup")
    run_as_non_root: bool | None = Field(default=None, alias="runAsNonRoot")
    run_as_user: int | None = Field(default=None, alias="runAsUser")
    se_linux_options: CoreV1SELinuxOptions | None = Field(default=None, alias="seLinuxOptions")
    seccomp_profile: CoreV1SeccompProfile | None = Field(default=None, alias="seccompProfile")
    windows_options: CoreV1WindowsSecurityContextOptions | None = Field(
        default=None, alias="windowsOptions"
    )


class CoreV1Service(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Service
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    spec: CoreV1ServiceSpec = Field(default={})
    status: CoreV1ServiceStatus = Field(default={})


class CoreV1ServiceAccount(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceAccount
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    automount_service_account_token: bool | None = Field(
        default=None, alias="automountServiceAccountToken"
    )
    image_pull_secrets: list[CoreV1LocalObjectReference] | None = Field(
        default=None, alias="imagePullSecrets"
    )
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})
    secrets: list[CoreV1ObjectReference] | None = Field(default=None)


class CoreV1ServiceAccountList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceAccountList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1ServiceAccount] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1ServiceAccountTokenProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceAccountTokenProjection
    """

    audience: str | None = Field(default=None)
    expiration_seconds: int | None = Field(default=None, alias="expirationSeconds")
    path: str = Field(default="")


class CoreV1ServiceList(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    items: list[CoreV1Service] = Field(...)
    kind: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})


class CoreV1ServicePort(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServicePort
    """

    app_protocol: str | None = Field(default=None, alias="appProtocol")
    name: str | None = Field(default=None)
    node_port: int | None = Field(default=None, alias="nodePort")
    port: int = Field(default=0)
    protocol: str = Field(default="TCP")
    target_port: UtilIntOrString = Field(default={}, alias="targetPort")


class CoreV1ServiceSpec(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceSpec
    """

    allocate_load_balancer_node_ports: bool | None = Field(
        default=None, alias="allocateLoadBalancerNodePorts"
    )
    cluster_ip: str | None = Field(default=None, alias="clusterIP")
    cluster_ips: list[str] | None = Field(default=None, alias="clusterIPs")
    external_ips: list[str] | None = Field(default=None, alias="externalIPs")
    external_name: str | None = Field(default=None, alias="externalName")
    external_traffic_policy: str | None = Field(default=None, alias="externalTrafficPolicy")
    health_check_node_port: int | None = Field(default=None, alias="healthCheckNodePort")
    internal_traffic_policy: str | None = Field(default=None, alias="internalTrafficPolicy")
    ip_families: list[str] | None = Field(default=None, alias="ipFamilies")
    ip_family_policy: str | None = Field(default=None, alias="ipFamilyPolicy")
    load_balancer_class: str | None = Field(default=None, alias="loadBalancerClass")
    load_balancer_ip: str | None = Field(default=None, alias="loadBalancerIP")
    load_balancer_source_ranges: list[str] | None = Field(
        default=None, alias="loadBalancerSourceRanges"
    )
    ports: list[CoreV1ServicePort] | None = Field(default=None)
    publish_not_ready_addresses: bool | None = Field(default=None, alias="publishNotReadyAddresses")
    selector: dict[str, str] | None = Field(default=None)
    session_affinity: str | None = Field(default=None, alias="sessionAffinity")
    session_affinity_config: CoreV1SessionAffinityConfig | None = Field(
        default=None, alias="sessionAffinityConfig"
    )
    type: str | None = Field(default=None)


class CoreV1ServiceStatus(BaseModel):
    """
    Original name: io.k8s.api.core.v1.ServiceStatus
    """

    conditions: list[MetaV1Condition] | None = Field(default=None)
    load_balancer: CoreV1LoadBalancerStatus = Field(default={}, alias="loadBalancer")


class CoreV1SessionAffinityConfig(BaseModel):
    """
    Original name: io.k8s.api.core.v1.SessionAffinityConfig
    """

    client_ip: CoreV1ClientIPConfig | None = Field(default=None, alias="clientIP")


class CoreV1StorageOSPersistentVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.StorageOSPersistentVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1ObjectReference | None = Field(default=None, alias="secretRef")
    volume_name: str | None = Field(default=None, alias="volumeName")
    volume_namespace: str | None = Field(default=None, alias="volumeNamespace")


class CoreV1StorageOSVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.StorageOSVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    read_only: bool | None = Field(default=None, alias="readOnly")
    secret_ref: CoreV1LocalObjectReference | None = Field(default=None, alias="secretRef")
    volume_name: str | None = Field(default=None, alias="volumeName")
    volume_namespace: str | None = Field(default=None, alias="volumeNamespace")


class CoreV1Sysctl(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Sysctl
    """

    name: str = Field(default="")
    value: str = Field(default="")


class CoreV1TCPSocketAction(BaseModel):
    """
    Original name: io.k8s.api.core.v1.TCPSocketAction
    """

    host: str | None = Field(default=None)
    port: UtilIntOrString = Field(default={})


class CoreV1Taint(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Taint
    """

    effect: str = Field(default="")
    key: str = Field(default="")
    time_added: datetime | None = Field(default=None, alias="timeAdded")
    value: str | None = Field(default=None)


class CoreV1Toleration(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Toleration
    """

    effect: str | None = Field(default=None)
    key: str | None = Field(default=None)
    operator: str | None = Field(default=None)
    toleration_seconds: int | None = Field(default=None, alias="tolerationSeconds")
    value: str | None = Field(default=None)


class CoreV1TopologySpreadConstraint(BaseModel):
    """
    Original name: io.k8s.api.core.v1.TopologySpreadConstraint
    """

    label_selector: MetaV1LabelSelector | None = Field(default=None, alias="labelSelector")
    match_label_keys: list[str] | None = Field(default=None, alias="matchLabelKeys")
    max_skew: int = Field(default=0, alias="maxSkew")
    min_domains: int | None = Field(default=None, alias="minDomains")
    node_affinity_policy: str | None = Field(default=None, alias="nodeAffinityPolicy")
    node_taints_policy: str | None = Field(default=None, alias="nodeTaintsPolicy")
    topology_key: str = Field(default="", alias="topologyKey")
    when_unsatisfiable: str = Field(default="", alias="whenUnsatisfiable")


class CoreV1TypedLocalObjectReference(BaseModel):
    """
    Original name: io.k8s.api.core.v1.TypedLocalObjectReference
    """

    api_group: str | None = Field(default=None, alias="apiGroup")
    kind: str = Field(default="")
    name: str = Field(default="")


class CoreV1Volume(BaseModel):
    """
    Original name: io.k8s.api.core.v1.Volume
    """

    aws_elastic_block_store: CoreV1AWSElasticBlockStoreVolumeSource | None = Field(
        default=None, alias="awsElasticBlockStore"
    )
    azure_disk: CoreV1AzureDiskVolumeSource | None = Field(default=None, alias="azureDisk")
    azure_file: CoreV1AzureFileVolumeSource | None = Field(default=None, alias="azureFile")
    cephfs: CoreV1CephFSVolumeSource | None = Field(default=None)
    cinder: CoreV1CinderVolumeSource | None = Field(default=None)
    config_map: CoreV1ConfigMapVolumeSource | None = Field(default=None, alias="configMap")
    csi: CoreV1CSIVolumeSource | None = Field(default=None)
    downward_api: CoreV1DownwardAPIVolumeSource | None = Field(default=None, alias="downwardAPI")
    empty_dir: CoreV1EmptyDirVolumeSource | None = Field(default=None, alias="emptyDir")
    ephemeral: CoreV1EphemeralVolumeSource | None = Field(default=None)
    fc: CoreV1FCVolumeSource | None = Field(default=None)
    flex_volume: CoreV1FlexVolumeSource | None = Field(default=None, alias="flexVolume")
    flocker: CoreV1FlockerVolumeSource | None = Field(default=None)
    gce_persistent_disk: CoreV1GCEPersistentDiskVolumeSource | None = Field(
        default=None, alias="gcePersistentDisk"
    )
    git_repo: CoreV1GitRepoVolumeSource | None = Field(default=None, alias="gitRepo")
    glusterfs: CoreV1GlusterfsVolumeSource | None = Field(default=None)
    host_path: CoreV1HostPathVolumeSource | None = Field(default=None, alias="hostPath")
    iscsi: CoreV1ISCSIVolumeSource | None = Field(default=None)
    name: str = Field(default="")
    nfs: CoreV1NFSVolumeSource | None = Field(default=None)
    persistent_volume_claim: CoreV1PersistentVolumeClaimVolumeSource | None = Field(
        default=None, alias="persistentVolumeClaim"
    )
    photon_persistent_disk: CoreV1PhotonPersistentDiskVolumeSource | None = Field(
        default=None, alias="photonPersistentDisk"
    )
    portworx_volume: CoreV1PortworxVolumeSource | None = Field(default=None, alias="portworxVolume")
    projected: CoreV1ProjectedVolumeSource | None = Field(default=None)
    quobyte: CoreV1QuobyteVolumeSource | None = Field(default=None)
    rbd: CoreV1RBDVolumeSource | None = Field(default=None)
    scale_io: CoreV1ScaleIOVolumeSource | None = Field(default=None, alias="scaleIO")
    secret: CoreV1SecretVolumeSource | None = Field(default=None)
    storageos: CoreV1StorageOSVolumeSource | None = Field(default=None)
    vsphere_volume: CoreV1VsphereVirtualDiskVolumeSource | None = Field(
        default=None, alias="vsphereVolume"
    )


class CoreV1VolumeDevice(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeDevice
    """

    device_path: str = Field(default="", alias="devicePath")
    name: str = Field(default="")


class CoreV1VolumeMount(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeMount
    """

    mount_path: str = Field(default="", alias="mountPath")
    mount_propagation: str | None = Field(default=None, alias="mountPropagation")
    name: str = Field(default="")
    read_only: bool | None = Field(default=None, alias="readOnly")
    sub_path: str | None = Field(default=None, alias="subPath")
    sub_path_expr: str | None = Field(default=None, alias="subPathExpr")


class CoreV1VolumeNodeAffinity(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeNodeAffinity
    """

    required: CoreV1NodeSelector | None = Field(default=None)


class CoreV1VolumeProjection(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VolumeProjection
    """

    config_map: CoreV1ConfigMapProjection | None = Field(default=None, alias="configMap")
    downward_api: CoreV1DownwardAPIProjection | None = Field(default=None, alias="downwardAPI")
    secret: CoreV1SecretProjection | None = Field(default=None)
    service_account_token: CoreV1ServiceAccountTokenProjection | None = Field(
        default=None, alias="serviceAccountToken"
    )


class CoreV1VsphereVirtualDiskVolumeSource(BaseModel):
    """
    Original name: io.k8s.api.core.v1.VsphereVirtualDiskVolumeSource
    """

    fs_type: str | None = Field(default=None, alias="fsType")
    storage_policy_id: str | None = Field(default=None, alias="storagePolicyID")
    storage_policy_name: str | None = Field(default=None, alias="storagePolicyName")
    volume_path: str = Field(default="", alias="volumePath")


class CoreV1WeightedPodAffinityTerm(BaseModel):
    """
    Original name: io.k8s.api.core.v1.WeightedPodAffinityTerm
    """

    pod_affinity_term: CoreV1PodAffinityTerm = Field(default={}, alias="podAffinityTerm")
    weight: int = Field(default=0)


class CoreV1WindowsSecurityContextOptions(BaseModel):
    """
    Original name: io.k8s.api.core.v1.WindowsSecurityContextOptions
    """

    gmsa_credential_spec: str | None = Field(default=None, alias="gmsaCredentialSpec")
    gmsa_credential_spec_name: str | None = Field(default=None, alias="gmsaCredentialSpecName")
    host_process: bool | None = Field(default=None, alias="hostProcess")
    run_as_user_name: str | None = Field(default=None, alias="runAsUserName")


class iok8sapipolicyV1Eviction(BaseModel):
    """
    Original name: io.k8s.api.policy.v1.Eviction
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    delete_options: MetaV1DeleteOptions | None = Field(default=None, alias="deleteOptions")
    kind: str | None = Field(default=None)
    metadata: MetaV1ObjectMeta = Field(default={})


class iok8sapimachinerypkgapiresourceQuantity(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.api.resource.Quantity
    """

    __root__: str | float | None = Field(default=None)


class MetaV1APIResource(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.APIResource
    """

    categories: list[str] | None = Field(default=None)
    group: str | None = Field(default=None)
    kind: str = Field(default="")
    name: str = Field(default="")
    namespaced: bool = Field(default=False)
    short_names: list[str] | None = Field(default=None, alias="shortNames")
    singular_name: str = Field(default="", alias="singularName")
    storage_version_hash: str | None = Field(default=None, alias="storageVersionHash")
    verbs: list[str] = Field(...)
    version: str | None = Field(default=None)


class MetaV1APIResourceList(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.APIResourceList
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    group_version: str = Field(default="", alias="groupVersion")
    kind: str | None = Field(default=None)
    resources: list[MetaV1APIResource] = Field(...)


class MetaV1Condition(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.Condition
    """

    last_transition_time: datetime | None = Field(default=None, alias="lastTransitionTime")
    message: str = Field(default="")
    observed_generation: int | None = Field(default=None, alias="observedGeneration")
    reason: str = Field(default="")
    status: str = Field(default="")
    type: str = Field(default="")


class MetaV1DeleteOptions(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.DeleteOptions
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    dry_run: list[str] | None = Field(default=None, alias="dryRun")
    grace_period_seconds: int | None = Field(default=None, alias="gracePeriodSeconds")
    kind: str | None = Field(default=None)
    orphan_dependents: bool | None = Field(default=None, alias="orphanDependents")
    preconditions: MetaV1Preconditions | None = Field(default=None)
    propagation_policy: str | None = Field(default=None, alias="propagationPolicy")


class MetaV1FieldsV1(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.FieldsV1
    """

    __root__: dict[str, object] | None = Field(default=None)


class MetaV1LabelSelector(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector
    """

    match_expressions: list[MetaV1LabelSelectorRequirement] | None = Field(
        default=None, alias="matchExpressions"
    )
    match_labels: dict[str, str] | None = Field(default=None, alias="matchLabels")


class MetaV1LabelSelectorRequirement(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement
    """

    key: str = Field(default="")
    operator: str = Field(default="")
    values: list[str] | None = Field(default=None)


class MetaV1ListMeta(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta
    """

    continue_: str | None = Field(default=None)
    remaining_item_count: int | None = Field(default=None, alias="remainingItemCount")
    resource_version: str | None = Field(default=None, alias="resourceVersion")
    self_link: str | None = Field(default=None, alias="selfLink")


class MetaV1ManagedFieldsEntry(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.ManagedFieldsEntry
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    fields_type: str | None = Field(default=None, alias="fieldsType")
    fields_v1: MetaV1FieldsV1 | None = Field(default=None, alias="fieldsV1")
    manager: str | None = Field(default=None)
    operation: str | None = Field(default=None)
    subresource: str | None = Field(default=None)
    time: datetime | None = Field(default=None)


class MetaV1MicroTime(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime
    """

    __root__: str | None = Field(default=None)


class MetaV1ObjectMeta(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta
    """

    annotations: dict[str, str] | None = Field(default=None)
    creation_timestamp: datetime | None = Field(default=None, alias="creationTimestamp")
    deletion_grace_period_seconds: int | None = Field(
        default=None, alias="deletionGracePeriodSeconds"
    )
    deletion_timestamp: datetime | None = Field(default=None, alias="deletionTimestamp")
    finalizers: list[str] | None = Field(default=None)
    generate_name: str | None = Field(default=None, alias="generateName")
    generation: int | None = Field(default=None)
    labels: dict[str, str] | None = Field(default=None)
    managed_fields: list[MetaV1ManagedFieldsEntry] | None = Field(
        default=None, alias="managedFields"
    )
    name: str | None = Field(default=None)
    namespace: str | None = Field(default=None)
    owner_references: list[MetaV1OwnerReference] | None = Field(
        default=None, alias="ownerReferences"
    )
    resource_version: str | None = Field(default=None, alias="resourceVersion")
    self_link: str | None = Field(default=None, alias="selfLink")
    uid: str | None = Field(default=None)


class MetaV1OwnerReference(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.OwnerReference
    """

    api_version: str = Field(default="", alias="apiVersion")
    block_owner_deletion: bool | None = Field(default=None, alias="blockOwnerDeletion")
    controller: bool | None = Field(default=None)
    kind: str = Field(default="")
    name: str = Field(default="")
    uid: str = Field(default="")


class MetaV1Preconditions(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.Preconditions
    """

    resource_version: str | None = Field(default=None, alias="resourceVersion")
    uid: str | None = Field(default=None)


class MetaV1Status(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.Status
    """

    api_version: str | None = Field(default=None, alias="apiVersion")
    code: int | None = Field(default=None)
    details: MetaV1StatusDetails | None = Field(default=None)
    kind: str | None = Field(default=None)
    message: str | None = Field(default=None)
    metadata: MetaV1ListMeta = Field(default={})
    reason: str | None = Field(default=None)
    status: str | None = Field(default=None)


class MetaV1StatusCause(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.StatusCause
    """

    field: str | None = Field(default=None)
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)


class MetaV1StatusDetails(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.StatusDetails
    """

    causes: list[MetaV1StatusCause] | None = Field(default=None)
    group: str | None = Field(default=None)
    kind: str | None = Field(default=None)
    name: str | None = Field(default=None)
    retry_after_seconds: int | None = Field(default=None, alias="retryAfterSeconds")
    uid: str | None = Field(default=None)


class MetaV1Time(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.Time
    """

    __root__: str | None = Field(default=None)


class MetaV1WatchEvent(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.apis.meta.v1.WatchEvent
    """

    object: RuntimeRawExtension = Field(default={})
    type: str = Field(default="")


class RuntimeRawExtension(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.runtime.RawExtension
    """

    __root__: dict[str, object] | None = Field(default=None)


class UtilIntOrString(BaseModel):
    """
    Original name: io.k8s.apimachinery.pkg.util.intstr.IntOrString
    """

    __root__: int | str | None = Field(default=None)


async def get_core_v1_api_resources(klient: Klient) -> MetaV1APIResourceList:
    """
    Original path: /api/v1/
    Op ID: getCoreV1APIResources
    Derived params: []
    """
    async with await klient.get(f"/api/v1/") as response:
        log(await response.json())
        return MetaV1APIResourceList.parse_obj(await response.json())


async def list_core_v1_component_status(klient: Klient) -> CoreV1ComponentStatusList:
    """
    Original path: /api/v1/componentstatuses
    Op ID: listCoreV1ComponentStatus
    Derived params: []
    """
    async with await klient.get(f"/api/v1/componentstatuses") as response:
        log(await response.json())
        return CoreV1ComponentStatusList.parse_obj(await response.json())


async def read_core_v1_component_status(klient: Klient, name: str) -> CoreV1ComponentStatus:
    """
    Original path: /api/v1/componentstatuses/{name}
    Op ID: readCoreV1ComponentStatus
    Derived params: ['name']
    """
    async with await klient.get(f"/api/v1/componentstatuses/{name}") as response:
        log(await response.json())
        return CoreV1ComponentStatus.parse_obj(await response.json())


async def list_core_v1_config_map_for_all_namespaces(klient: Klient) -> CoreV1ConfigMapList:
    """
    Original path: /api/v1/configmaps
    Op ID: listCoreV1ConfigMapForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/configmaps") as response:
        log(await response.json())
        return CoreV1ConfigMapList.parse_obj(await response.json())


async def list_core_v1_endpoints_for_all_namespaces(klient: Klient) -> CoreV1EndpointsList:
    """
    Original path: /api/v1/endpoints
    Op ID: listCoreV1EndpointsForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/endpoints") as response:
        log(await response.json())
        return CoreV1EndpointsList.parse_obj(await response.json())


async def list_core_v1_event_for_all_namespaces(klient: Klient) -> CoreV1EventList:
    """
    Original path: /api/v1/events
    Op ID: listCoreV1EventForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/events") as response:
        log(await response.json())
        return CoreV1EventList.parse_obj(await response.json())


async def list_core_v1_limit_range_for_all_namespaces(klient: Klient) -> CoreV1LimitRangeList:
    """
    Original path: /api/v1/limitranges
    Op ID: listCoreV1LimitRangeForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/limitranges") as response:
        log(await response.json())
        return CoreV1LimitRangeList.parse_obj(await response.json())


async def list_core_v1_namespace(klient: Klient) -> CoreV1NamespaceList:
    """
    Original path: /api/v1/namespaces
    Op ID: listCoreV1Namespace
    Derived params: []
    """
    async with await klient.get(f"/api/v1/namespaces") as response:
        log(await response.json())
        return CoreV1NamespaceList.parse_obj(await response.json())


async def list_core_v1_namespaced_config_map(klient: Klient, namespace: str) -> CoreV1ConfigMapList:
    """
    Original path: /api/v1/namespaces/{namespace}/configmaps
    Op ID: listCoreV1NamespacedConfigMap
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/configmaps") as response:
        log(await response.json())
        return CoreV1ConfigMapList.parse_obj(await response.json())


async def read_core_v1_namespaced_config_map(
    klient: Klient, namespace: str, name: str
) -> CoreV1ConfigMap:
    """
    Original path: /api/v1/namespaces/{namespace}/configmaps/{name}
    Op ID: readCoreV1NamespacedConfigMap
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/configmaps/{name}") as response:
        log(await response.json())
        return CoreV1ConfigMap.parse_obj(await response.json())


async def list_core_v1_namespaced_endpoints(klient: Klient, namespace: str) -> CoreV1EndpointsList:
    """
    Original path: /api/v1/namespaces/{namespace}/endpoints
    Op ID: listCoreV1NamespacedEndpoints
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/endpoints") as response:
        log(await response.json())
        return CoreV1EndpointsList.parse_obj(await response.json())


async def read_core_v1_namespaced_endpoints(
    klient: Klient, namespace: str, name: str
) -> CoreV1Endpoints:
    """
    Original path: /api/v1/namespaces/{namespace}/endpoints/{name}
    Op ID: readCoreV1NamespacedEndpoints
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/endpoints/{name}") as response:
        log(await response.json())
        return CoreV1Endpoints.parse_obj(await response.json())


async def list_core_v1_namespaced_event(klient: Klient, namespace: str) -> CoreV1EventList:
    """
    Original path: /api/v1/namespaces/{namespace}/events
    Op ID: listCoreV1NamespacedEvent
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/events") as response:
        log(await response.json())
        return CoreV1EventList.parse_obj(await response.json())


async def read_core_v1_namespaced_event(klient: Klient, namespace: str, name: str) -> CoreV1Event:
    """
    Original path: /api/v1/namespaces/{namespace}/events/{name}
    Op ID: readCoreV1NamespacedEvent
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/events/{name}") as response:
        log(await response.json())
        return CoreV1Event.parse_obj(await response.json())


async def list_core_v1_namespaced_limit_range(
    klient: Klient, namespace: str
) -> CoreV1LimitRangeList:
    """
    Original path: /api/v1/namespaces/{namespace}/limitranges
    Op ID: listCoreV1NamespacedLimitRange
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/limitranges") as response:
        log(await response.json())
        return CoreV1LimitRangeList.parse_obj(await response.json())


async def read_core_v1_namespaced_limit_range(
    klient: Klient, namespace: str, name: str
) -> CoreV1LimitRange:
    """
    Original path: /api/v1/namespaces/{namespace}/limitranges/{name}
    Op ID: readCoreV1NamespacedLimitRange
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/limitranges/{name}") as response:
        log(await response.json())
        return CoreV1LimitRange.parse_obj(await response.json())


async def list_core_v1_namespaced_persistent_volume_claim(
    klient: Klient, namespace: str
) -> CoreV1PersistentVolumeClaimList:
    """
    Original path: /api/v1/namespaces/{namespace}/persistentvolumeclaims
    Op ID: listCoreV1NamespacedPersistentVolumeClaim
    Derived params: ['namespace']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/persistentvolumeclaims"
    ) as response:
        log(await response.json())
        return CoreV1PersistentVolumeClaimList.parse_obj(await response.json())


async def read_core_v1_namespaced_persistent_volume_claim(
    klient: Klient, namespace: str, name: str
) -> CoreV1PersistentVolumeClaim:
    """
    Original path: /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}
    Op ID: readCoreV1NamespacedPersistentVolumeClaim
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}"
    ) as response:
        log(await response.json())
        return CoreV1PersistentVolumeClaim.parse_obj(await response.json())


async def read_core_v1_namespaced_persistent_volume_claim_status(
    klient: Klient, namespace: str, name: str
) -> CoreV1PersistentVolumeClaim:
    """
    Original path: /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status
    Op ID: readCoreV1NamespacedPersistentVolumeClaimStatus
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status"
    ) as response:
        log(await response.json())
        return CoreV1PersistentVolumeClaim.parse_obj(await response.json())


async def list_core_v1_namespaced_pod(klient: Klient, namespace: str) -> CoreV1PodList:
    """
    Original path: /api/v1/namespaces/{namespace}/pods
    Op ID: listCoreV1NamespacedPod
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/pods") as response:
        log(await response.json())
        return CoreV1PodList.parse_obj(await response.json())


async def read_core_v1_namespaced_pod(klient: Klient, namespace: str, name: str) -> CoreV1Pod:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}
    Op ID: readCoreV1NamespacedPod
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/pods/{name}") as response:
        log(await response.json())
        return CoreV1Pod.parse_obj(await response.json())


async def read_core_v1_namespaced_pod_ephemeralcontainers(
    klient: Klient, namespace: str, name: str
) -> CoreV1Pod:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers
    Op ID: readCoreV1NamespacedPodEphemeralcontainers
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers"
    ) as response:
        log(await response.json())
        return CoreV1Pod.parse_obj(await response.json())


async def read_core_v1_namespaced_pod_log(klient: Klient, namespace: str, name: str) -> str:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}/log
    Op ID: readCoreV1NamespacedPodLog
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/pods/{name}/log") as response:
        log(await response.json())
        return await response.text()


async def read_core_v1_namespaced_pod_status(
    klient: Klient, namespace: str, name: str
) -> CoreV1Pod:
    """
    Original path: /api/v1/namespaces/{namespace}/pods/{name}/status
    Op ID: readCoreV1NamespacedPodStatus
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/pods/{name}/status") as response:
        log(await response.json())
        return CoreV1Pod.parse_obj(await response.json())


async def list_core_v1_namespaced_pod_template(
    klient: Klient, namespace: str
) -> CoreV1PodTemplateList:
    """
    Original path: /api/v1/namespaces/{namespace}/podtemplates
    Op ID: listCoreV1NamespacedPodTemplate
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/podtemplates") as response:
        log(await response.json())
        return CoreV1PodTemplateList.parse_obj(await response.json())


async def read_core_v1_namespaced_pod_template(
    klient: Klient, namespace: str, name: str
) -> CoreV1PodTemplate:
    """
    Original path: /api/v1/namespaces/{namespace}/podtemplates/{name}
    Op ID: readCoreV1NamespacedPodTemplate
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/podtemplates/{name}") as response:
        log(await response.json())
        return CoreV1PodTemplate.parse_obj(await response.json())


async def list_core_v1_namespaced_replication_controller(
    klient: Klient, namespace: str
) -> CoreV1ReplicationControllerList:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers
    Op ID: listCoreV1NamespacedReplicationController
    Derived params: ['namespace']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers"
    ) as response:
        log(await response.json())
        return CoreV1ReplicationControllerList.parse_obj(await response.json())


async def read_core_v1_namespaced_replication_controller(
    klient: Klient, namespace: str, name: str
) -> CoreV1ReplicationController:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers/{name}
    Op ID: readCoreV1NamespacedReplicationController
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers/{name}"
    ) as response:
        log(await response.json())
        return CoreV1ReplicationController.parse_obj(await response.json())


async def read_core_v1_namespaced_replication_controller_scale(
    klient: Klient, namespace: str, name: str
) -> AutoscalingV1Scale:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale
    Op ID: readCoreV1NamespacedReplicationControllerScale
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale"
    ) as response:
        log(await response.json())
        return AutoscalingV1Scale.parse_obj(await response.json())


async def read_core_v1_namespaced_replication_controller_status(
    klient: Klient, namespace: str, name: str
) -> CoreV1ReplicationController:
    """
    Original path: /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status
    Op ID: readCoreV1NamespacedReplicationControllerStatus
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status"
    ) as response:
        log(await response.json())
        return CoreV1ReplicationController.parse_obj(await response.json())


async def list_core_v1_namespaced_resource_quota(
    klient: Klient, namespace: str
) -> CoreV1ResourceQuotaList:
    """
    Original path: /api/v1/namespaces/{namespace}/resourcequotas
    Op ID: listCoreV1NamespacedResourceQuota
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/resourcequotas") as response:
        log(await response.json())
        return CoreV1ResourceQuotaList.parse_obj(await response.json())


async def read_core_v1_namespaced_resource_quota(
    klient: Klient, namespace: str, name: str
) -> CoreV1ResourceQuota:
    """
    Original path: /api/v1/namespaces/{namespace}/resourcequotas/{name}
    Op ID: readCoreV1NamespacedResourceQuota
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/resourcequotas/{name}"
    ) as response:
        log(await response.json())
        return CoreV1ResourceQuota.parse_obj(await response.json())


async def read_core_v1_namespaced_resource_quota_status(
    klient: Klient, namespace: str, name: str
) -> CoreV1ResourceQuota:
    """
    Original path: /api/v1/namespaces/{namespace}/resourcequotas/{name}/status
    Op ID: readCoreV1NamespacedResourceQuotaStatus
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/resourcequotas/{name}/status"
    ) as response:
        log(await response.json())
        return CoreV1ResourceQuota.parse_obj(await response.json())


async def list_core_v1_namespaced_secret(klient: Klient, namespace: str) -> CoreV1SecretList:
    """
    Original path: /api/v1/namespaces/{namespace}/secrets
    Op ID: listCoreV1NamespacedSecret
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/secrets") as response:
        log(await response.json())
        return CoreV1SecretList.parse_obj(await response.json())


async def read_core_v1_namespaced_secret(klient: Klient, namespace: str, name: str) -> CoreV1Secret:
    """
    Original path: /api/v1/namespaces/{namespace}/secrets/{name}
    Op ID: readCoreV1NamespacedSecret
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/secrets/{name}") as response:
        log(await response.json())
        return CoreV1Secret.parse_obj(await response.json())


async def list_core_v1_namespaced_service_account(
    klient: Klient, namespace: str
) -> CoreV1ServiceAccountList:
    """
    Original path: /api/v1/namespaces/{namespace}/serviceaccounts
    Op ID: listCoreV1NamespacedServiceAccount
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/serviceaccounts") as response:
        log(await response.json())
        return CoreV1ServiceAccountList.parse_obj(await response.json())


async def read_core_v1_namespaced_service_account(
    klient: Klient, namespace: str, name: str
) -> CoreV1ServiceAccount:
    """
    Original path: /api/v1/namespaces/{namespace}/serviceaccounts/{name}
    Op ID: readCoreV1NamespacedServiceAccount
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/serviceaccounts/{name}"
    ) as response:
        log(await response.json())
        return CoreV1ServiceAccount.parse_obj(await response.json())


async def list_core_v1_namespaced_service(klient: Klient, namespace: str) -> CoreV1ServiceList:
    """
    Original path: /api/v1/namespaces/{namespace}/services
    Op ID: listCoreV1NamespacedService
    Derived params: ['namespace']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/services") as response:
        log(await response.json())
        return CoreV1ServiceList.parse_obj(await response.json())


async def read_core_v1_namespaced_service(
    klient: Klient, namespace: str, name: str
) -> CoreV1Service:
    """
    Original path: /api/v1/namespaces/{namespace}/services/{name}
    Op ID: readCoreV1NamespacedService
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(f"/api/v1/namespaces/{namespace}/services/{name}") as response:
        log(await response.json())
        return CoreV1Service.parse_obj(await response.json())


async def read_core_v1_namespaced_service_status(
    klient: Klient, namespace: str, name: str
) -> CoreV1Service:
    """
    Original path: /api/v1/namespaces/{namespace}/services/{name}/status
    Op ID: readCoreV1NamespacedServiceStatus
    Derived params: ['namespace', 'name']
    """
    async with await klient.get(
        f"/api/v1/namespaces/{namespace}/services/{name}/status"
    ) as response:
        log(await response.json())
        return CoreV1Service.parse_obj(await response.json())


async def read_core_v1_namespace(klient: Klient, name: str) -> CoreV1Namespace:
    """
    Original path: /api/v1/namespaces/{name}
    Op ID: readCoreV1Namespace
    Derived params: ['name']
    """
    async with await klient.get(f"/api/v1/namespaces/{name}") as response:
        log(await response.json())
        return CoreV1Namespace.parse_obj(await response.json())


async def read_core_v1_namespace_status(klient: Klient, name: str) -> CoreV1Namespace:
    """
    Original path: /api/v1/namespaces/{name}/status
    Op ID: readCoreV1NamespaceStatus
    Derived params: ['name']
    """
    async with await klient.get(f"/api/v1/namespaces/{name}/status") as response:
        log(await response.json())
        return CoreV1Namespace.parse_obj(await response.json())


async def list_core_v1_node(klient: Klient) -> CoreV1NodeList:
    """
    Original path: /api/v1/nodes
    Op ID: listCoreV1Node
    Derived params: []
    """
    async with await klient.get(f"/api/v1/nodes") as response:
        log(await response.json())
        return CoreV1NodeList.parse_obj(await response.json())


async def read_core_v1_node(klient: Klient, name: str) -> CoreV1Node:
    """
    Original path: /api/v1/nodes/{name}
    Op ID: readCoreV1Node
    Derived params: ['name']
    """
    async with await klient.get(f"/api/v1/nodes/{name}") as response:
        log(await response.json())
        return CoreV1Node.parse_obj(await response.json())


async def read_core_v1_node_status(klient: Klient, name: str) -> CoreV1Node:
    """
    Original path: /api/v1/nodes/{name}/status
    Op ID: readCoreV1NodeStatus
    Derived params: ['name']
    """
    async with await klient.get(f"/api/v1/nodes/{name}/status") as response:
        log(await response.json())
        return CoreV1Node.parse_obj(await response.json())


async def list_core_v1_persistent_volume_claim_for_all_namespaces(
    klient: Klient,
) -> CoreV1PersistentVolumeClaimList:
    """
    Original path: /api/v1/persistentvolumeclaims
    Op ID: listCoreV1PersistentVolumeClaimForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/persistentvolumeclaims") as response:
        log(await response.json())
        return CoreV1PersistentVolumeClaimList.parse_obj(await response.json())


async def list_core_v1_persistent_volume(klient: Klient) -> CoreV1PersistentVolumeList:
    """
    Original path: /api/v1/persistentvolumes
    Op ID: listCoreV1PersistentVolume
    Derived params: []
    """
    async with await klient.get(f"/api/v1/persistentvolumes") as response:
        log(await response.json())
        return CoreV1PersistentVolumeList.parse_obj(await response.json())


async def read_core_v1_persistent_volume(klient: Klient, name: str) -> CoreV1PersistentVolume:
    """
    Original path: /api/v1/persistentvolumes/{name}
    Op ID: readCoreV1PersistentVolume
    Derived params: ['name']
    """
    async with await klient.get(f"/api/v1/persistentvolumes/{name}") as response:
        log(await response.json())
        return CoreV1PersistentVolume.parse_obj(await response.json())


async def read_core_v1_persistent_volume_status(
    klient: Klient, name: str
) -> CoreV1PersistentVolume:
    """
    Original path: /api/v1/persistentvolumes/{name}/status
    Op ID: readCoreV1PersistentVolumeStatus
    Derived params: ['name']
    """
    async with await klient.get(f"/api/v1/persistentvolumes/{name}/status") as response:
        log(await response.json())
        return CoreV1PersistentVolume.parse_obj(await response.json())


async def list_core_v1_pod_for_all_namespaces(klient: Klient) -> CoreV1PodList:
    """
    Original path: /api/v1/pods
    Op ID: listCoreV1PodForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/pods") as response:
        log(await response.json())
        return CoreV1PodList.parse_obj(await response.json())


async def list_core_v1_pod_template_for_all_namespaces(klient: Klient) -> CoreV1PodTemplateList:
    """
    Original path: /api/v1/podtemplates
    Op ID: listCoreV1PodTemplateForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/podtemplates") as response:
        log(await response.json())
        return CoreV1PodTemplateList.parse_obj(await response.json())


async def list_core_v1_replication_controller_for_all_namespaces(
    klient: Klient,
) -> CoreV1ReplicationControllerList:
    """
    Original path: /api/v1/replicationcontrollers
    Op ID: listCoreV1ReplicationControllerForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/replicationcontrollers") as response:
        log(await response.json())
        return CoreV1ReplicationControllerList.parse_obj(await response.json())


async def list_core_v1_resource_quota_for_all_namespaces(klient: Klient) -> CoreV1ResourceQuotaList:
    """
    Original path: /api/v1/resourcequotas
    Op ID: listCoreV1ResourceQuotaForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/resourcequotas") as response:
        log(await response.json())
        return CoreV1ResourceQuotaList.parse_obj(await response.json())


async def list_core_v1_secret_for_all_namespaces(klient: Klient) -> CoreV1SecretList:
    """
    Original path: /api/v1/secrets
    Op ID: listCoreV1SecretForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/secrets") as response:
        log(await response.json())
        return CoreV1SecretList.parse_obj(await response.json())


async def list_core_v1_service_account_for_all_namespaces(
    klient: Klient,
) -> CoreV1ServiceAccountList:
    """
    Original path: /api/v1/serviceaccounts
    Op ID: listCoreV1ServiceAccountForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/serviceaccounts") as response:
        log(await response.json())
        return CoreV1ServiceAccountList.parse_obj(await response.json())


async def list_core_v1_service_for_all_namespaces(klient: Klient) -> CoreV1ServiceList:
    """
    Original path: /api/v1/services
    Op ID: listCoreV1ServiceForAllNamespaces
    Derived params: []
    """
    async with await klient.get(f"/api/v1/services") as response:
        log(await response.json())
        return CoreV1ServiceList.parse_obj(await response.json())


AuthenticationV1BoundObjectReference.update_forward_refs()
AuthenticationV1TokenRequest.update_forward_refs()
AuthenticationV1TokenRequestSpec.update_forward_refs()
AuthenticationV1TokenRequestStatus.update_forward_refs()
AutoscalingV1Scale.update_forward_refs()
AutoscalingV1ScaleSpec.update_forward_refs()
AutoscalingV1ScaleStatus.update_forward_refs()
CoreV1AWSElasticBlockStoreVolumeSource.update_forward_refs()
CoreV1Affinity.update_forward_refs()
CoreV1AttachedVolume.update_forward_refs()
CoreV1AzureDiskVolumeSource.update_forward_refs()
CoreV1AzureFilePersistentVolumeSource.update_forward_refs()
CoreV1AzureFileVolumeSource.update_forward_refs()
CoreV1Binding.update_forward_refs()
CoreV1CSIPersistentVolumeSource.update_forward_refs()
CoreV1CSIVolumeSource.update_forward_refs()
CoreV1Capabilities.update_forward_refs()
CoreV1CephFSPersistentVolumeSource.update_forward_refs()
CoreV1CephFSVolumeSource.update_forward_refs()
CoreV1CinderPersistentVolumeSource.update_forward_refs()
CoreV1CinderVolumeSource.update_forward_refs()
CoreV1ClientIPConfig.update_forward_refs()
CoreV1ComponentCondition.update_forward_refs()
CoreV1ComponentStatus.update_forward_refs()
CoreV1ComponentStatusList.update_forward_refs()
CoreV1ConfigMap.update_forward_refs()
CoreV1ConfigMapEnvSource.update_forward_refs()
CoreV1ConfigMapKeySelector.update_forward_refs()
CoreV1ConfigMapList.update_forward_refs()
CoreV1ConfigMapNodeConfigSource.update_forward_refs()
CoreV1ConfigMapProjection.update_forward_refs()
CoreV1ConfigMapVolumeSource.update_forward_refs()
CoreV1Container.update_forward_refs()
CoreV1ContainerImage.update_forward_refs()
CoreV1ContainerPort.update_forward_refs()
CoreV1ContainerState.update_forward_refs()
CoreV1ContainerStateRunning.update_forward_refs()
CoreV1ContainerStateTerminated.update_forward_refs()
CoreV1ContainerStateWaiting.update_forward_refs()
CoreV1ContainerStatus.update_forward_refs()
CoreV1DaemonEndpoint.update_forward_refs()
CoreV1DownwardAPIProjection.update_forward_refs()
CoreV1DownwardAPIVolumeFile.update_forward_refs()
CoreV1DownwardAPIVolumeSource.update_forward_refs()
CoreV1EmptyDirVolumeSource.update_forward_refs()
CoreV1EndpointAddress.update_forward_refs()
CoreV1EndpointPort.update_forward_refs()
CoreV1EndpointSubset.update_forward_refs()
CoreV1Endpoints.update_forward_refs()
CoreV1EndpointsList.update_forward_refs()
CoreV1EnvFromSource.update_forward_refs()
CoreV1EnvVar.update_forward_refs()
CoreV1EnvVarSource.update_forward_refs()
CoreV1EphemeralContainer.update_forward_refs()
CoreV1EphemeralVolumeSource.update_forward_refs()
CoreV1Event.update_forward_refs()
CoreV1EventList.update_forward_refs()
CoreV1EventSeries.update_forward_refs()
CoreV1EventSource.update_forward_refs()
CoreV1ExecAction.update_forward_refs()
CoreV1FCVolumeSource.update_forward_refs()
CoreV1FlexPersistentVolumeSource.update_forward_refs()
CoreV1FlexVolumeSource.update_forward_refs()
CoreV1FlockerVolumeSource.update_forward_refs()
CoreV1GCEPersistentDiskVolumeSource.update_forward_refs()
CoreV1GRPCAction.update_forward_refs()
CoreV1GitRepoVolumeSource.update_forward_refs()
CoreV1GlusterfsPersistentVolumeSource.update_forward_refs()
CoreV1GlusterfsVolumeSource.update_forward_refs()
CoreV1HTTPGetAction.update_forward_refs()
CoreV1HTTPHeader.update_forward_refs()
CoreV1HostAlias.update_forward_refs()
CoreV1HostPathVolumeSource.update_forward_refs()
CoreV1ISCSIPersistentVolumeSource.update_forward_refs()
CoreV1ISCSIVolumeSource.update_forward_refs()
CoreV1KeyToPath.update_forward_refs()
CoreV1Lifecycle.update_forward_refs()
CoreV1LifecycleHandler.update_forward_refs()
CoreV1LimitRange.update_forward_refs()
CoreV1LimitRangeItem.update_forward_refs()
CoreV1LimitRangeList.update_forward_refs()
CoreV1LimitRangeSpec.update_forward_refs()
CoreV1LoadBalancerIngress.update_forward_refs()
CoreV1LoadBalancerStatus.update_forward_refs()
CoreV1LocalObjectReference.update_forward_refs()
CoreV1LocalVolumeSource.update_forward_refs()
CoreV1NFSVolumeSource.update_forward_refs()
CoreV1Namespace.update_forward_refs()
CoreV1NamespaceCondition.update_forward_refs()
CoreV1NamespaceList.update_forward_refs()
CoreV1NamespaceSpec.update_forward_refs()
CoreV1NamespaceStatus.update_forward_refs()
CoreV1Node.update_forward_refs()
CoreV1NodeAddress.update_forward_refs()
CoreV1NodeAffinity.update_forward_refs()
CoreV1NodeCondition.update_forward_refs()
CoreV1NodeConfigSource.update_forward_refs()
CoreV1NodeConfigStatus.update_forward_refs()
CoreV1NodeDaemonEndpoints.update_forward_refs()
CoreV1NodeList.update_forward_refs()
CoreV1NodeSelector.update_forward_refs()
CoreV1NodeSelectorRequirement.update_forward_refs()
CoreV1NodeSelectorTerm.update_forward_refs()
CoreV1NodeSpec.update_forward_refs()
CoreV1NodeStatus.update_forward_refs()
CoreV1NodeSystemInfo.update_forward_refs()
CoreV1ObjectFieldSelector.update_forward_refs()
CoreV1ObjectReference.update_forward_refs()
CoreV1PersistentVolume.update_forward_refs()
CoreV1PersistentVolumeClaim.update_forward_refs()
CoreV1PersistentVolumeClaimCondition.update_forward_refs()
CoreV1PersistentVolumeClaimList.update_forward_refs()
CoreV1PersistentVolumeClaimSpec.update_forward_refs()
CoreV1PersistentVolumeClaimStatus.update_forward_refs()
CoreV1PersistentVolumeClaimTemplate.update_forward_refs()
CoreV1PersistentVolumeClaimVolumeSource.update_forward_refs()
CoreV1PersistentVolumeList.update_forward_refs()
CoreV1PersistentVolumeSpec.update_forward_refs()
CoreV1PersistentVolumeStatus.update_forward_refs()
CoreV1PhotonPersistentDiskVolumeSource.update_forward_refs()
CoreV1Pod.update_forward_refs()
CoreV1PodAffinity.update_forward_refs()
CoreV1PodAffinityTerm.update_forward_refs()
CoreV1PodAntiAffinity.update_forward_refs()
CoreV1PodCondition.update_forward_refs()
CoreV1PodDNSConfig.update_forward_refs()
CoreV1PodDNSConfigOption.update_forward_refs()
CoreV1PodIP.update_forward_refs()
CoreV1PodList.update_forward_refs()
CoreV1PodOS.update_forward_refs()
CoreV1PodReadinessGate.update_forward_refs()
CoreV1PodSecurityContext.update_forward_refs()
CoreV1PodSpec.update_forward_refs()
CoreV1PodStatus.update_forward_refs()
CoreV1PodTemplate.update_forward_refs()
CoreV1PodTemplateList.update_forward_refs()
CoreV1PodTemplateSpec.update_forward_refs()
CoreV1PortStatus.update_forward_refs()
CoreV1PortworxVolumeSource.update_forward_refs()
CoreV1PreferredSchedulingTerm.update_forward_refs()
CoreV1Probe.update_forward_refs()
CoreV1ProjectedVolumeSource.update_forward_refs()
CoreV1QuobyteVolumeSource.update_forward_refs()
CoreV1RBDPersistentVolumeSource.update_forward_refs()
CoreV1RBDVolumeSource.update_forward_refs()
CoreV1ReplicationController.update_forward_refs()
CoreV1ReplicationControllerCondition.update_forward_refs()
CoreV1ReplicationControllerList.update_forward_refs()
CoreV1ReplicationControllerSpec.update_forward_refs()
CoreV1ReplicationControllerStatus.update_forward_refs()
CoreV1ResourceFieldSelector.update_forward_refs()
CoreV1ResourceQuota.update_forward_refs()
CoreV1ResourceQuotaList.update_forward_refs()
CoreV1ResourceQuotaSpec.update_forward_refs()
CoreV1ResourceQuotaStatus.update_forward_refs()
CoreV1ResourceRequirements.update_forward_refs()
CoreV1SELinuxOptions.update_forward_refs()
CoreV1ScaleIOPersistentVolumeSource.update_forward_refs()
CoreV1ScaleIOVolumeSource.update_forward_refs()
CoreV1ScopeSelector.update_forward_refs()
CoreV1ScopedResourceSelectorRequirement.update_forward_refs()
CoreV1SeccompProfile.update_forward_refs()
CoreV1Secret.update_forward_refs()
CoreV1SecretEnvSource.update_forward_refs()
CoreV1SecretKeySelector.update_forward_refs()
CoreV1SecretList.update_forward_refs()
CoreV1SecretProjection.update_forward_refs()
CoreV1SecretReference.update_forward_refs()
CoreV1SecretVolumeSource.update_forward_refs()
CoreV1SecurityContext.update_forward_refs()
CoreV1Service.update_forward_refs()
CoreV1ServiceAccount.update_forward_refs()
CoreV1ServiceAccountList.update_forward_refs()
CoreV1ServiceAccountTokenProjection.update_forward_refs()
CoreV1ServiceList.update_forward_refs()
CoreV1ServicePort.update_forward_refs()
CoreV1ServiceSpec.update_forward_refs()
CoreV1ServiceStatus.update_forward_refs()
CoreV1SessionAffinityConfig.update_forward_refs()
CoreV1StorageOSPersistentVolumeSource.update_forward_refs()
CoreV1StorageOSVolumeSource.update_forward_refs()
CoreV1Sysctl.update_forward_refs()
CoreV1TCPSocketAction.update_forward_refs()
CoreV1Taint.update_forward_refs()
CoreV1Toleration.update_forward_refs()
CoreV1TopologySpreadConstraint.update_forward_refs()
CoreV1TypedLocalObjectReference.update_forward_refs()
CoreV1Volume.update_forward_refs()
CoreV1VolumeDevice.update_forward_refs()
CoreV1VolumeMount.update_forward_refs()
CoreV1VolumeNodeAffinity.update_forward_refs()
CoreV1VolumeProjection.update_forward_refs()
CoreV1VsphereVirtualDiskVolumeSource.update_forward_refs()
CoreV1WeightedPodAffinityTerm.update_forward_refs()
CoreV1WindowsSecurityContextOptions.update_forward_refs()
iok8sapipolicyV1Eviction.update_forward_refs()
iok8sapimachinerypkgapiresourceQuantity.update_forward_refs()
MetaV1APIResource.update_forward_refs()
MetaV1APIResourceList.update_forward_refs()
MetaV1Condition.update_forward_refs()
MetaV1DeleteOptions.update_forward_refs()
MetaV1FieldsV1.update_forward_refs()
MetaV1LabelSelector.update_forward_refs()
MetaV1LabelSelectorRequirement.update_forward_refs()
MetaV1ListMeta.update_forward_refs()
MetaV1ManagedFieldsEntry.update_forward_refs()
MetaV1MicroTime.update_forward_refs()
MetaV1ObjectMeta.update_forward_refs()
MetaV1OwnerReference.update_forward_refs()
MetaV1Preconditions.update_forward_refs()
MetaV1Status.update_forward_refs()
MetaV1StatusCause.update_forward_refs()
MetaV1StatusDetails.update_forward_refs()
MetaV1Time.update_forward_refs()
MetaV1WatchEvent.update_forward_refs()
RuntimeRawExtension.update_forward_refs()
UtilIntOrString.update_forward_refs()
