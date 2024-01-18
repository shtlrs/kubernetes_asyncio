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


class V1StatefulSetStatus(object):
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
        'available_replicas': 'int',
        'collision_count': 'int',
        'conditions': 'list[V1StatefulSetCondition]',
        'current_replicas': 'int',
        'current_revision': 'str',
        'observed_generation': 'int',
        'ready_replicas': 'int',
        'replicas': 'int',
        'update_revision': 'str',
        'updated_replicas': 'int'
    }

    attribute_map = {
        'available_replicas': 'availableReplicas',
        'collision_count': 'collisionCount',
        'conditions': 'conditions',
        'current_replicas': 'currentReplicas',
        'current_revision': 'currentRevision',
        'observed_generation': 'observedGeneration',
        'ready_replicas': 'readyReplicas',
        'replicas': 'replicas',
        'update_revision': 'updateRevision',
        'updated_replicas': 'updatedReplicas'
    }

    def __init__(self, available_replicas=None, collision_count=None, conditions=None, current_replicas=None, current_revision=None, observed_generation=None, ready_replicas=None, replicas=None, update_revision=None, updated_replicas=None, local_vars_configuration=None):  # noqa: E501
        """V1StatefulSetStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._available_replicas = None
        self._collision_count = None
        self._conditions = None
        self._current_replicas = None
        self._current_revision = None
        self._observed_generation = None
        self._ready_replicas = None
        self._replicas = None
        self._update_revision = None
        self._updated_replicas = None
        self.discriminator = None

        if available_replicas is not None:
            self.available_replicas = available_replicas
        if collision_count is not None:
            self.collision_count = collision_count
        if conditions is not None:
            self.conditions = conditions
        if current_replicas is not None:
            self.current_replicas = current_replicas
        if current_revision is not None:
            self.current_revision = current_revision
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if ready_replicas is not None:
            self.ready_replicas = ready_replicas
        self.replicas = replicas
        if update_revision is not None:
            self.update_revision = update_revision
        if updated_replicas is not None:
            self.updated_replicas = updated_replicas

    @property
    def available_replicas(self):
        """Gets the available_replicas of this V1StatefulSetStatus.  # noqa: E501

        Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset.  # noqa: E501

        :return: The available_replicas of this V1StatefulSetStatus.  # noqa: E501
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """Sets the available_replicas of this V1StatefulSetStatus.

        Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset.  # noqa: E501

        :param available_replicas: The available_replicas of this V1StatefulSetStatus.  # noqa: E501
        :type available_replicas: int
        """

        self._available_replicas = available_replicas

    @property
    def collision_count(self):
        """Gets the collision_count of this V1StatefulSetStatus.  # noqa: E501

        collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.  # noqa: E501

        :return: The collision_count of this V1StatefulSetStatus.  # noqa: E501
        :rtype: int
        """
        return self._collision_count

    @collision_count.setter
    def collision_count(self, collision_count):
        """Sets the collision_count of this V1StatefulSetStatus.

        collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.  # noqa: E501

        :param collision_count: The collision_count of this V1StatefulSetStatus.  # noqa: E501
        :type collision_count: int
        """

        self._collision_count = collision_count

    @property
    def conditions(self):
        """Gets the conditions of this V1StatefulSetStatus.  # noqa: E501

        Represents the latest available observations of a statefulset's current state.  # noqa: E501

        :return: The conditions of this V1StatefulSetStatus.  # noqa: E501
        :rtype: list[V1StatefulSetCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1StatefulSetStatus.

        Represents the latest available observations of a statefulset's current state.  # noqa: E501

        :param conditions: The conditions of this V1StatefulSetStatus.  # noqa: E501
        :type conditions: list[V1StatefulSetCondition]
        """

        self._conditions = conditions

    @property
    def current_replicas(self):
        """Gets the current_replicas of this V1StatefulSetStatus.  # noqa: E501

        currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.  # noqa: E501

        :return: The current_replicas of this V1StatefulSetStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """Sets the current_replicas of this V1StatefulSetStatus.

        currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.  # noqa: E501

        :param current_replicas: The current_replicas of this V1StatefulSetStatus.  # noqa: E501
        :type current_replicas: int
        """

        self._current_replicas = current_replicas

    @property
    def current_revision(self):
        """Gets the current_revision of this V1StatefulSetStatus.  # noqa: E501

        currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).  # noqa: E501

        :return: The current_revision of this V1StatefulSetStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_revision

    @current_revision.setter
    def current_revision(self, current_revision):
        """Sets the current_revision of this V1StatefulSetStatus.

        currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).  # noqa: E501

        :param current_revision: The current_revision of this V1StatefulSetStatus.  # noqa: E501
        :type current_revision: str
        """

        self._current_revision = current_revision

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1StatefulSetStatus.  # noqa: E501

        observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.  # noqa: E501

        :return: The observed_generation of this V1StatefulSetStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1StatefulSetStatus.

        observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.  # noqa: E501

        :param observed_generation: The observed_generation of this V1StatefulSetStatus.  # noqa: E501
        :type observed_generation: int
        """

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self):
        """Gets the ready_replicas of this V1StatefulSetStatus.  # noqa: E501

        readyReplicas is the number of pods created for this StatefulSet with a Ready Condition.  # noqa: E501

        :return: The ready_replicas of this V1StatefulSetStatus.  # noqa: E501
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """Sets the ready_replicas of this V1StatefulSetStatus.

        readyReplicas is the number of pods created for this StatefulSet with a Ready Condition.  # noqa: E501

        :param ready_replicas: The ready_replicas of this V1StatefulSetStatus.  # noqa: E501
        :type ready_replicas: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """Gets the replicas of this V1StatefulSetStatus.  # noqa: E501

        replicas is the number of Pods created by the StatefulSet controller.  # noqa: E501

        :return: The replicas of this V1StatefulSetStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this V1StatefulSetStatus.

        replicas is the number of Pods created by the StatefulSet controller.  # noqa: E501

        :param replicas: The replicas of this V1StatefulSetStatus.  # noqa: E501
        :type replicas: int
        """
        if self.local_vars_configuration.client_side_validation and replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas

    @property
    def update_revision(self):
        """Gets the update_revision of this V1StatefulSetStatus.  # noqa: E501

        updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)  # noqa: E501

        :return: The update_revision of this V1StatefulSetStatus.  # noqa: E501
        :rtype: str
        """
        return self._update_revision

    @update_revision.setter
    def update_revision(self, update_revision):
        """Sets the update_revision of this V1StatefulSetStatus.

        updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)  # noqa: E501

        :param update_revision: The update_revision of this V1StatefulSetStatus.  # noqa: E501
        :type update_revision: str
        """

        self._update_revision = update_revision

    @property
    def updated_replicas(self):
        """Gets the updated_replicas of this V1StatefulSetStatus.  # noqa: E501

        updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.  # noqa: E501

        :return: The updated_replicas of this V1StatefulSetStatus.  # noqa: E501
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas):
        """Sets the updated_replicas of this V1StatefulSetStatus.

        updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.  # noqa: E501

        :param updated_replicas: The updated_replicas of this V1StatefulSetStatus.  # noqa: E501
        :type updated_replicas: int
        """

        self._updated_replicas = updated_replicas

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
        if not isinstance(other, V1StatefulSetStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1StatefulSetStatus):
            return True

        return self.to_dict() != other.to_dict()
