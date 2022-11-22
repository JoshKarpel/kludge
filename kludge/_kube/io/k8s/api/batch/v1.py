# generated by datamodel-codegen:
#   filename:  v3

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class PodFailurePolicyOnExitCodesRequirement(BaseModel):
    """
    PodFailurePolicyOnExitCodesRequirement describes the requirement for handling a failed pod based on its container exit codes. In particular, it lookups the .state.terminated.exitCode for each app container and init container status, represented by the .status.containerStatuses and .status.initContainerStatuses fields in the Pod status, respectively. Containers completed with success (exit code 0) are excluded from the requirement check.
    """

    containerName: Optional[str] = Field(
        None,
        description="Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template.",
    )
    operator: str = Field(
        ...,
        description="Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are: - In: the requirement is satisfied if at least one container exit code\n  (might be multiple if there are multiple containers not restricted\n  by the 'containerName' field) is in the set of specified values.\n- NotIn: the requirement is satisfied if at least one container exit code\n  (might be multiple if there are multiple containers not restricted\n  by the 'containerName' field) is not in the set of specified values.\nAdditional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied.\n\n",
    )
    values: list[int] = Field(
        ...,
        description="Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In operator. At least one element is required. At most 255 elements are allowed.",
    )


class PodFailurePolicyOnPodConditionsPattern(BaseModel):
    """
    PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type.
    """

    status: str = Field(
        ...,
        description="Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True.",
    )
    type: str = Field(
        ...,
        description="Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type.",
    )


class PodFailurePolicyRule(BaseModel):
    """
    PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of OnExitCodes and onPodConditions, but not both, can be used in each rule.
    """

    action: str = Field(
        ...,
        description="Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod's job is marked as Failed and all\n  running pods are terminated.\n- Ignore: indicates that the counter towards the .backoffLimit is not\n  incremented and a replacement pod is created.\n- Count: indicates that the pod is handled in the default way - the\n  counter towards the .backoffLimit is incremented.\nAdditional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.\n\n",
    )
    onExitCodes: Optional[PodFailurePolicyOnExitCodesRequirement] = Field(
        None, description="Represents the requirement on the container exit codes."
    )
    onPodConditions: list[PodFailurePolicyOnPodConditionsPattern] = Field(
        ...,
        description="Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.",
    )


class UncountedTerminatedPods(BaseModel):
    """
    UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job status counters.
    """

    failed: Optional[list[str]] = Field(None, description="Failed holds UIDs of failed Pods.")
    succeeded: Optional[list[str]] = Field(
        None, description="Succeeded holds UIDs of succeeded Pods."
    )


class CronJobStatus(BaseModel):
    """
    CronJobStatus represents the current state of a cron job.
    """

    active: Optional[list[v1.ObjectReferenceModel3]] = Field(
        None, description="A list of pointers to currently running jobs."
    )
    lastScheduleTime: Optional[v1_1.TimeModel17] = Field(
        None, description="Information when was the last time the job was successfully scheduled."
    )
    lastSuccessfulTime: Optional[v1_1.TimeModel17] = Field(
        None, description="Information when was the last time the job successfully completed."
    )


class JobCondition(BaseModel):
    """
    JobCondition describes current state of a job.
    """

    lastProbeTime: Optional[v1_1.TimeModel17] = Field(
        {}, description="Last time the condition was checked."
    )
    lastTransitionTime: Optional[v1_1.TimeModel17] = Field(
        {}, description="Last time the condition transit from one status to another."
    )
    message: Optional[str] = Field(
        None, description="Human readable message indicating details about last transition."
    )
    reason: Optional[str] = Field(
        None, description="(brief) reason for the condition's last transition."
    )
    status: str = Field(..., description="Status of the condition, one of True, False, Unknown.")
    type: str = Field(..., description="Type of job condition, Complete or Failed.")


class JobStatus(BaseModel):
    """
    JobStatus represents the current state of a Job.
    """

    active: Optional[int] = Field(None, description="The number of pending and running pods.")
    completedIndexes: Optional[str] = Field(
        None,
        description='CompletedIndexes holds the completed indexes when .spec.completionMode = "Indexed" in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as "1,3-5,7".',
    )
    completionTime: Optional[v1_1.TimeModel17] = Field(
        None,
        description="Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is only set when the job finishes successfully.",
    )
    conditions: Optional[list[JobCondition]] = Field(
        None,
        description='The latest available observations of an object\'s current state. When a Job fails, one of the conditions will have type "Failed" and status true. When a Job is suspended, one of the conditions will have type "Suspended" and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type "Complete" and status true. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/',
    )
    failed: Optional[int] = Field(
        None, description="The number of pods which reached phase Failed."
    )
    ready: Optional[int] = Field(
        None,
        description="The number of pods which have a Ready condition.\n\nThis field is beta-level. The job controller populates the field when the feature gate JobReadyPods is enabled (enabled by default).",
    )
    startTime: Optional[v1_1.TimeModel17] = Field(
        None,
        description="Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC.",
    )
    succeeded: Optional[int] = Field(
        None, description="The number of pods which reached phase Succeeded."
    )
    uncountedTerminatedPods: Optional[UncountedTerminatedPods] = Field(
        None,
        description="UncountedTerminatedPods holds the UIDs of Pods that have terminated but the job controller hasn't yet accounted for in the status counters.\n\nThe job controller creates pods with a finalizer. When a pod terminates (succeeded or failed), the controller does three steps to account for it in the job status: (1) Add the pod UID to the arrays in this field. (2) Remove the pod finalizer. (3) Remove the pod UID from the arrays while increasing the corresponding\n    counter.\n\nThis field is beta-level. The job controller only makes use of this field when the feature gate JobTrackingWithFinalizers is enabled (enabled by default). Old jobs might not be tracked using this field, in which case the field remains null.",
    )


class PodFailurePolicy(BaseModel):
    """
    PodFailurePolicy describes how failed pods influence the backoffLimit.
    """

    rules: list[PodFailurePolicyRule] = Field(
        ...,
        description="A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed.",
    )


class JobSpec(BaseModel):
    """
    JobSpec describes how the job execution will look like.
    """

    activeDeadlineSeconds: Optional[int] = Field(
        None,
        description="Specifies the duration in seconds relative to the startTime that the job may be continuously active before the system tries to terminate it; value must be positive integer. If a Job is suspended (at creation or through an update), this timer will effectively be stopped and reset when the Job is resumed again.",
    )
    backoffLimit: Optional[int] = Field(
        None,
        description="Specifies the number of retries before marking this job failed. Defaults to 6",
    )
    completionMode: Optional[str] = Field(
        None,
        description="CompletionMode specifies how Pod completions are tracked. It can be `NonIndexed` (default) or `Indexed`.\n\n`NonIndexed` means that the Job is considered complete when there have been .spec.completions successfully completed Pods. Each Pod completion is homologous to each other.\n\n`Indexed` means that the Pods of a Job get an associated completion index from 0 to (.spec.completions - 1), available in the annotation batch.kubernetes.io/job-completion-index. The Job is considered complete when there is one successfully completed Pod for each index. When value is `Indexed`, .spec.completions must be specified and `.spec.parallelism` must be less than or equal to 10^5. In addition, The Pod name takes the form `$(job-name)-$(index)-$(random-string)`, the Pod hostname takes the form `$(job-name)-$(index)`.\n\nMore completion modes can be added in the future. If the Job controller observes a mode that it doesn't recognize, which is possible during upgrades due to version skew, the controller skips updates for the Job.",
    )
    completions: Optional[int] = Field(
        None,
        description="Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/",
    )
    manualSelector: Optional[bool] = Field(
        None,
        description="manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector",
    )
    parallelism: Optional[int] = Field(
        None,
        description="Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/",
    )
    podFailurePolicy: Optional[PodFailurePolicy] = Field(
        None,
        description="Specifies the policy of handling failed pods. In particular, it allows to specify the set of actions and conditions which need to be satisfied to take the associated action. If empty, the default behaviour applies - the counter of failed pods, represented by the jobs's .status.failed field, is incremented and it is checked against the backoffLimit. This field cannot be used in combination with restartPolicy=OnFailure.\n\nThis field is alpha-level. To use this field, you must enable the `JobPodFailurePolicy` feature gate (disabled by default).",
    )
    selector: Optional[v1_1.LabelSelectorModel6] = Field(
        None,
        description="A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    suspend: Optional[bool] = Field(
        None,
        description="Suspend specifies whether the Job controller should create Pods or not. If a Job is created with suspend set to true, no Pods are created by the Job controller. If a Job is suspended after creation (i.e. the flag goes from false to true), the Job controller will delete all active Pods associated with this Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the Job, effectively resetting the ActiveDeadlineSeconds timer too. Defaults to false.",
    )
    template: v1.PodTemplateSpecModel = Field(
        ...,
        description="Describes the pod that will be created when executing a job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/",
    )
    ttlSecondsAfterFinished: Optional[int] = Field(
        None,
        description="ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes.",
    )


class JobTemplateSpec(BaseModel):
    """
    JobTemplateSpec describes the data a Job should have when created from a template
    """

    metadata: Optional[v1_1.ObjectMetaModel17] = Field(
        {},
        description="Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[JobSpec] = Field(
        {},
        description="Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class CronJobSpec(BaseModel):
    """
    CronJobSpec describes how the job execution will look like and when it will actually run.
    """

    concurrencyPolicy: Optional[str] = Field(
        None,
        description='Specifies how to treat concurrent executions of a Job. Valid values are: - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn\'t finished yet; - "Replace": cancels currently running job and replaces it with a new one\n\n',
    )
    failedJobsHistoryLimit: Optional[int] = Field(
        None,
        description="The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1.",
    )
    jobTemplate: JobTemplateSpec = Field(
        ..., description="Specifies the job that will be created when executing a CronJob."
    )
    schedule: str = Field(
        ..., description="The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron."
    )
    startingDeadlineSeconds: Optional[int] = Field(
        None,
        description="Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.",
    )
    successfulJobsHistoryLimit: Optional[int] = Field(
        None,
        description="The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3.",
    )
    suspend: Optional[bool] = Field(
        None,
        description="This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.",
    )
    timeZone: Optional[str] = Field(
        None,
        description="The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones This is beta field and must be enabled via the `CronJobTimeZone` feature gate.",
    )


class Job(BaseModel):
    """
    Job represents the configuration of a single job.
    """

    apiVersion: Optional[str] = Field(
        None,
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[str] = Field(
        None,
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1_1.ObjectMetaModel17] = Field(
        {},
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[JobSpec] = Field(
        {},
        description="Specification of the desired behavior of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[JobStatus] = Field(
        {},
        description="Current status of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class JobList(BaseModel):
    """
    JobList is a collection of jobs.
    """

    apiVersion: Optional[str] = Field(
        None,
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: list[Job] = Field(..., description="items is the list of Jobs.")
    kind: Optional[str] = Field(
        None,
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1_1.ListMetaModel15] = Field(
        {},
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class CronJob(BaseModel):
    """
    CronJob represents the configuration of a single cron job.
    """

    apiVersion: Optional[str] = Field(
        None,
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[str] = Field(
        None,
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1_1.ObjectMetaModel17] = Field(
        {},
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[CronJobSpec] = Field(
        {},
        description="Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[CronJobStatus] = Field(
        {},
        description="Current status of a cron job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class CronJobList(BaseModel):
    """
    CronJobList is a collection of cron jobs.
    """

    apiVersion: Optional[str] = Field(
        None,
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: list[CronJob] = Field(..., description="items is the list of CronJobs.")
    kind: Optional[str] = Field(
        None,
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1_1.ListMetaModel15] = Field(
        {},
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
