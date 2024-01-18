# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.29.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1JobSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'active_deadline_seconds': 'int',
        'backoff_limit': 'int',
        'backoff_limit_per_index': 'int',
        'completion_mode': 'str',
        'completions': 'int',
        'manual_selector': 'bool',
        'max_failed_indexes': 'int',
        'parallelism': 'int',
        'pod_failure_policy': 'V1PodFailurePolicy',
        'pod_replacement_policy': 'str',
        'selector': 'V1LabelSelector',
        'suspend': 'bool',
        'template': 'V1PodTemplateSpec',
        'ttl_seconds_after_finished': 'int'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'backoff_limit': 'backoffLimit',
        'backoff_limit_per_index': 'backoffLimitPerIndex',
        'completion_mode': 'completionMode',
        'completions': 'completions',
        'manual_selector': 'manualSelector',
        'max_failed_indexes': 'maxFailedIndexes',
        'parallelism': 'parallelism',
        'pod_failure_policy': 'podFailurePolicy',
        'pod_replacement_policy': 'podReplacementPolicy',
        'selector': 'selector',
        'suspend': 'suspend',
        'template': 'template',
        'ttl_seconds_after_finished': 'ttlSecondsAfterFinished'
    }

    def __init__(self, active_deadline_seconds=None, backoff_limit=None, backoff_limit_per_index=None, completion_mode=None, completions=None, manual_selector=None, max_failed_indexes=None, parallelism=None, pod_failure_policy=None, pod_replacement_policy=None, selector=None, suspend=None, template=None, ttl_seconds_after_finished=None, local_vars_configuration=None):  # noqa: E501
        """V1JobSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active_deadline_seconds = None
        self._backoff_limit = None
        self._backoff_limit_per_index = None
        self._completion_mode = None
        self._completions = None
        self._manual_selector = None
        self._max_failed_indexes = None
        self._parallelism = None
        self._pod_failure_policy = None
        self._pod_replacement_policy = None
        self._selector = None
        self._suspend = None
        self._template = None
        self._ttl_seconds_after_finished = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if backoff_limit is not None:
            self.backoff_limit = backoff_limit
        if backoff_limit_per_index is not None:
            self.backoff_limit_per_index = backoff_limit_per_index
        if completion_mode is not None:
            self.completion_mode = completion_mode
        if completions is not None:
            self.completions = completions
        if manual_selector is not None:
            self.manual_selector = manual_selector
        if max_failed_indexes is not None:
            self.max_failed_indexes = max_failed_indexes
        if parallelism is not None:
            self.parallelism = parallelism
        if pod_failure_policy is not None:
            self.pod_failure_policy = pod_failure_policy
        if pod_replacement_policy is not None:
            self.pod_replacement_policy = pod_replacement_policy
        if selector is not None:
            self.selector = selector
        if suspend is not None:
            self.suspend = suspend
        self.template = template
        if ttl_seconds_after_finished is not None:
            self.ttl_seconds_after_finished = ttl_seconds_after_finished

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this V1JobSpec.  # noqa: E501

        Specifies the duration in seconds relative to the startTime that the job may be continuously active before the system tries to terminate it; value must be positive integer. If a Job is suspended (at creation or through an update), this timer will effectively be stopped and reset when the Job is resumed again.  # noqa: E501

        :return: The active_deadline_seconds of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this V1JobSpec.

        Specifies the duration in seconds relative to the startTime that the job may be continuously active before the system tries to terminate it; value must be positive integer. If a Job is suspended (at creation or through an update), this timer will effectively be stopped and reset when the Job is resumed again.  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this V1JobSpec.  # noqa: E501
        :type active_deadline_seconds: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def backoff_limit(self):
        """Gets the backoff_limit of this V1JobSpec.  # noqa: E501

        Specifies the number of retries before marking this job failed. Defaults to 6  # noqa: E501

        :return: The backoff_limit of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._backoff_limit

    @backoff_limit.setter
    def backoff_limit(self, backoff_limit):
        """Sets the backoff_limit of this V1JobSpec.

        Specifies the number of retries before marking this job failed. Defaults to 6  # noqa: E501

        :param backoff_limit: The backoff_limit of this V1JobSpec.  # noqa: E501
        :type backoff_limit: int
        """

        self._backoff_limit = backoff_limit

    @property
    def backoff_limit_per_index(self):
        """Gets the backoff_limit_per_index of this V1JobSpec.  # noqa: E501

        Specifies the limit for the number of retries within an index before marking this index as failed. When enabled the number of failures per index is kept in the pod's batch.kubernetes.io/job-index-failure-count annotation. It can only be set when Job's completionMode=Indexed, and the Pod's restart policy is Never. The field is immutable. This field is beta-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (enabled by default).  # noqa: E501

        :return: The backoff_limit_per_index of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._backoff_limit_per_index

    @backoff_limit_per_index.setter
    def backoff_limit_per_index(self, backoff_limit_per_index):
        """Sets the backoff_limit_per_index of this V1JobSpec.

        Specifies the limit for the number of retries within an index before marking this index as failed. When enabled the number of failures per index is kept in the pod's batch.kubernetes.io/job-index-failure-count annotation. It can only be set when Job's completionMode=Indexed, and the Pod's restart policy is Never. The field is immutable. This field is beta-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (enabled by default).  # noqa: E501

        :param backoff_limit_per_index: The backoff_limit_per_index of this V1JobSpec.  # noqa: E501
        :type backoff_limit_per_index: int
        """

        self._backoff_limit_per_index = backoff_limit_per_index

    @property
    def completion_mode(self):
        """Gets the completion_mode of this V1JobSpec.  # noqa: E501

        completionMode specifies how Pod completions are tracked. It can be `NonIndexed` (default) or `Indexed`.  `NonIndexed` means that the Job is considered complete when there have been .spec.completions successfully completed Pods. Each Pod completion is homologous to each other.  `Indexed` means that the Pods of a Job get an associated completion index from 0 to (.spec.completions - 1), available in the annotation batch.kubernetes.io/job-completion-index. The Job is considered complete when there is one successfully completed Pod for each index. When value is `Indexed`, .spec.completions must be specified and `.spec.parallelism` must be less than or equal to 10^5. In addition, The Pod name takes the form `$(job-name)-$(index)-$(random-string)`, the Pod hostname takes the form `$(job-name)-$(index)`.  More completion modes can be added in the future. If the Job controller observes a mode that it doesn't recognize, which is possible during upgrades due to version skew, the controller skips updates for the Job.  # noqa: E501

        :return: The completion_mode of this V1JobSpec.  # noqa: E501
        :rtype: str
        """
        return self._completion_mode

    @completion_mode.setter
    def completion_mode(self, completion_mode):
        """Sets the completion_mode of this V1JobSpec.

        completionMode specifies how Pod completions are tracked. It can be `NonIndexed` (default) or `Indexed`.  `NonIndexed` means that the Job is considered complete when there have been .spec.completions successfully completed Pods. Each Pod completion is homologous to each other.  `Indexed` means that the Pods of a Job get an associated completion index from 0 to (.spec.completions - 1), available in the annotation batch.kubernetes.io/job-completion-index. The Job is considered complete when there is one successfully completed Pod for each index. When value is `Indexed`, .spec.completions must be specified and `.spec.parallelism` must be less than or equal to 10^5. In addition, The Pod name takes the form `$(job-name)-$(index)-$(random-string)`, the Pod hostname takes the form `$(job-name)-$(index)`.  More completion modes can be added in the future. If the Job controller observes a mode that it doesn't recognize, which is possible during upgrades due to version skew, the controller skips updates for the Job.  # noqa: E501

        :param completion_mode: The completion_mode of this V1JobSpec.  # noqa: E501
        :type completion_mode: str
        """

        self._completion_mode = completion_mode

    @property
    def completions(self):
        """Gets the completions of this V1JobSpec.  # noqa: E501

        Specifies the desired number of successfully finished pods the job should be run with.  Setting to null means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The completions of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """Sets the completions of this V1JobSpec.

        Specifies the desired number of successfully finished pods the job should be run with.  Setting to null means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param completions: The completions of this V1JobSpec.  # noqa: E501
        :type completions: int
        """

        self._completions = completions

    @property
    def manual_selector(self):
        """Gets the manual_selector of this V1JobSpec.  # noqa: E501

        manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector  # noqa: E501

        :return: The manual_selector of this V1JobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._manual_selector

    @manual_selector.setter
    def manual_selector(self, manual_selector):
        """Sets the manual_selector of this V1JobSpec.

        manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector  # noqa: E501

        :param manual_selector: The manual_selector of this V1JobSpec.  # noqa: E501
        :type manual_selector: bool
        """

        self._manual_selector = manual_selector

    @property
    def max_failed_indexes(self):
        """Gets the max_failed_indexes of this V1JobSpec.  # noqa: E501

        Specifies the maximal number of failed indexes before marking the Job as failed, when backoffLimitPerIndex is set. Once the number of failed indexes exceeds this number the entire Job is marked as Failed and its execution is terminated. When left as null the job continues execution of all of its indexes and is marked with the `Complete` Job condition. It can only be specified when backoffLimitPerIndex is set. It can be null or up to completions. It is required and must be less than or equal to 10^4 when is completions greater than 10^5. This field is beta-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (enabled by default).  # noqa: E501

        :return: The max_failed_indexes of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_failed_indexes

    @max_failed_indexes.setter
    def max_failed_indexes(self, max_failed_indexes):
        """Sets the max_failed_indexes of this V1JobSpec.

        Specifies the maximal number of failed indexes before marking the Job as failed, when backoffLimitPerIndex is set. Once the number of failed indexes exceeds this number the entire Job is marked as Failed and its execution is terminated. When left as null the job continues execution of all of its indexes and is marked with the `Complete` Job condition. It can only be specified when backoffLimitPerIndex is set. It can be null or up to completions. It is required and must be less than or equal to 10^4 when is completions greater than 10^5. This field is beta-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (enabled by default).  # noqa: E501

        :param max_failed_indexes: The max_failed_indexes of this V1JobSpec.  # noqa: E501
        :type max_failed_indexes: int
        """

        self._max_failed_indexes = max_failed_indexes

    @property
    def parallelism(self):
        """Gets the parallelism of this V1JobSpec.  # noqa: E501

        Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The parallelism of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this V1JobSpec.

        Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param parallelism: The parallelism of this V1JobSpec.  # noqa: E501
        :type parallelism: int
        """

        self._parallelism = parallelism

    @property
    def pod_failure_policy(self):
        """Gets the pod_failure_policy of this V1JobSpec.  # noqa: E501


        :return: The pod_failure_policy of this V1JobSpec.  # noqa: E501
        :rtype: V1PodFailurePolicy
        """
        return self._pod_failure_policy

    @pod_failure_policy.setter
    def pod_failure_policy(self, pod_failure_policy):
        """Sets the pod_failure_policy of this V1JobSpec.


        :param pod_failure_policy: The pod_failure_policy of this V1JobSpec.  # noqa: E501
        :type pod_failure_policy: V1PodFailurePolicy
        """

        self._pod_failure_policy = pod_failure_policy

    @property
    def pod_replacement_policy(self):
        """Gets the pod_replacement_policy of this V1JobSpec.  # noqa: E501

        podReplacementPolicy specifies when to create replacement Pods. Possible values are: - TerminatingOrFailed means that we recreate pods   when they are terminating (has a metadata.deletionTimestamp) or failed. - Failed means to wait until a previously created Pod is fully terminated (has phase   Failed or Succeeded) before creating a replacement Pod.  When using podFailurePolicy, Failed is the the only allowed value. TerminatingOrFailed and Failed are allowed values when podFailurePolicy is not in use. This is an beta field. To use this, enable the JobPodReplacementPolicy feature toggle. This is on by default.  # noqa: E501

        :return: The pod_replacement_policy of this V1JobSpec.  # noqa: E501
        :rtype: str
        """
        return self._pod_replacement_policy

    @pod_replacement_policy.setter
    def pod_replacement_policy(self, pod_replacement_policy):
        """Sets the pod_replacement_policy of this V1JobSpec.

        podReplacementPolicy specifies when to create replacement Pods. Possible values are: - TerminatingOrFailed means that we recreate pods   when they are terminating (has a metadata.deletionTimestamp) or failed. - Failed means to wait until a previously created Pod is fully terminated (has phase   Failed or Succeeded) before creating a replacement Pod.  When using podFailurePolicy, Failed is the the only allowed value. TerminatingOrFailed and Failed are allowed values when podFailurePolicy is not in use. This is an beta field. To use this, enable the JobPodReplacementPolicy feature toggle. This is on by default.  # noqa: E501

        :param pod_replacement_policy: The pod_replacement_policy of this V1JobSpec.  # noqa: E501
        :type pod_replacement_policy: str
        """

        self._pod_replacement_policy = pod_replacement_policy

    @property
    def selector(self):
        """Gets the selector of this V1JobSpec.  # noqa: E501


        :return: The selector of this V1JobSpec.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1JobSpec.


        :param selector: The selector of this V1JobSpec.  # noqa: E501
        :type selector: V1LabelSelector
        """

        self._selector = selector

    @property
    def suspend(self):
        """Gets the suspend of this V1JobSpec.  # noqa: E501

        suspend specifies whether the Job controller should create Pods or not. If a Job is created with suspend set to true, no Pods are created by the Job controller. If a Job is suspended after creation (i.e. the flag goes from false to true), the Job controller will delete all active Pods associated with this Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the Job, effectively resetting the ActiveDeadlineSeconds timer too. Defaults to false.  # noqa: E501

        :return: The suspend of this V1JobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1JobSpec.

        suspend specifies whether the Job controller should create Pods or not. If a Job is created with suspend set to true, no Pods are created by the Job controller. If a Job is suspended after creation (i.e. the flag goes from false to true), the Job controller will delete all active Pods associated with this Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the Job, effectively resetting the ActiveDeadlineSeconds timer too. Defaults to false.  # noqa: E501

        :param suspend: The suspend of this V1JobSpec.  # noqa: E501
        :type suspend: bool
        """

        self._suspend = suspend

    @property
    def template(self):
        """Gets the template of this V1JobSpec.  # noqa: E501


        :return: The template of this V1JobSpec.  # noqa: E501
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1JobSpec.


        :param template: The template of this V1JobSpec.  # noqa: E501
        :type template: V1PodTemplateSpec
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def ttl_seconds_after_finished(self):
        """Gets the ttl_seconds_after_finished of this V1JobSpec.  # noqa: E501

        ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes.  # noqa: E501

        :return: The ttl_seconds_after_finished of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished):
        """Sets the ttl_seconds_after_finished of this V1JobSpec.

        ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes.  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this V1JobSpec.  # noqa: E501
        :type ttl_seconds_after_finished: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1JobSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1JobSpec):
            return True

        return self.to_dict() != other.to_dict()
