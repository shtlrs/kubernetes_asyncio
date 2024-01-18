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


class CoreV1Event(object):
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
        'action': 'str',
        'api_version': 'str',
        'count': 'int',
        'event_time': 'datetime',
        'first_timestamp': 'datetime',
        'involved_object': 'V1ObjectReference',
        'kind': 'str',
        'last_timestamp': 'datetime',
        'message': 'str',
        'metadata': 'V1ObjectMeta',
        'reason': 'str',
        'related': 'V1ObjectReference',
        'reporting_component': 'str',
        'reporting_instance': 'str',
        'series': 'CoreV1EventSeries',
        'source': 'V1EventSource',
        'type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'api_version': 'apiVersion',
        'count': 'count',
        'event_time': 'eventTime',
        'first_timestamp': 'firstTimestamp',
        'involved_object': 'involvedObject',
        'kind': 'kind',
        'last_timestamp': 'lastTimestamp',
        'message': 'message',
        'metadata': 'metadata',
        'reason': 'reason',
        'related': 'related',
        'reporting_component': 'reportingComponent',
        'reporting_instance': 'reportingInstance',
        'series': 'series',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, action=None, api_version=None, count=None, event_time=None, first_timestamp=None, involved_object=None, kind=None, last_timestamp=None, message=None, metadata=None, reason=None, related=None, reporting_component=None, reporting_instance=None, series=None, source=None, type=None, local_vars_configuration=None):  # noqa: E501
        """CoreV1Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._api_version = None
        self._count = None
        self._event_time = None
        self._first_timestamp = None
        self._involved_object = None
        self._kind = None
        self._last_timestamp = None
        self._message = None
        self._metadata = None
        self._reason = None
        self._related = None
        self._reporting_component = None
        self._reporting_instance = None
        self._series = None
        self._source = None
        self._type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if api_version is not None:
            self.api_version = api_version
        if count is not None:
            self.count = count
        if event_time is not None:
            self.event_time = event_time
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        self.involved_object = involved_object
        if kind is not None:
            self.kind = kind
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if message is not None:
            self.message = message
        self.metadata = metadata
        if reason is not None:
            self.reason = reason
        if related is not None:
            self.related = related
        if reporting_component is not None:
            self.reporting_component = reporting_component
        if reporting_instance is not None:
            self.reporting_instance = reporting_instance
        if series is not None:
            self.series = series
        if source is not None:
            self.source = source
        if type is not None:
            self.type = type

    @property
    def action(self):
        """Gets the action of this CoreV1Event.  # noqa: E501

        What action was taken/failed regarding to the Regarding object.  # noqa: E501

        :return: The action of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CoreV1Event.

        What action was taken/failed regarding to the Regarding object.  # noqa: E501

        :param action: The action of this CoreV1Event.  # noqa: E501
        :type action: str
        """

        self._action = action

    @property
    def api_version(self):
        """Gets the api_version of this CoreV1Event.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this CoreV1Event.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this CoreV1Event.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def count(self):
        """Gets the count of this CoreV1Event.  # noqa: E501

        The number of times this event has occurred.  # noqa: E501

        :return: The count of this CoreV1Event.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CoreV1Event.

        The number of times this event has occurred.  # noqa: E501

        :param count: The count of this CoreV1Event.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def event_time(self):
        """Gets the event_time of this CoreV1Event.  # noqa: E501

        Time when this Event was first observed.  # noqa: E501

        :return: The event_time of this CoreV1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this CoreV1Event.

        Time when this Event was first observed.  # noqa: E501

        :param event_time: The event_time of this CoreV1Event.  # noqa: E501
        :type event_time: datetime
        """

        self._event_time = event_time

    @property
    def first_timestamp(self):
        """Gets the first_timestamp of this CoreV1Event.  # noqa: E501

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :return: The first_timestamp of this CoreV1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """Sets the first_timestamp of this CoreV1Event.

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :param first_timestamp: The first_timestamp of this CoreV1Event.  # noqa: E501
        :type first_timestamp: datetime
        """

        self._first_timestamp = first_timestamp

    @property
    def involved_object(self):
        """Gets the involved_object of this CoreV1Event.  # noqa: E501


        :return: The involved_object of this CoreV1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """Sets the involved_object of this CoreV1Event.


        :param involved_object: The involved_object of this CoreV1Event.  # noqa: E501
        :type involved_object: V1ObjectReference
        """
        if self.local_vars_configuration.client_side_validation and involved_object is None:  # noqa: E501
            raise ValueError("Invalid value for `involved_object`, must not be `None`")  # noqa: E501

        self._involved_object = involved_object

    @property
    def kind(self):
        """Gets the kind of this CoreV1Event.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CoreV1Event.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this CoreV1Event.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this CoreV1Event.  # noqa: E501

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :return: The last_timestamp of this CoreV1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this CoreV1Event.

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :param last_timestamp: The last_timestamp of this CoreV1Event.  # noqa: E501
        :type last_timestamp: datetime
        """

        self._last_timestamp = last_timestamp

    @property
    def message(self):
        """Gets the message of this CoreV1Event.  # noqa: E501

        A human-readable description of the status of this operation.  # noqa: E501

        :return: The message of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CoreV1Event.

        A human-readable description of the status of this operation.  # noqa: E501

        :param message: The message of this CoreV1Event.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def metadata(self):
        """Gets the metadata of this CoreV1Event.  # noqa: E501


        :return: The metadata of this CoreV1Event.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CoreV1Event.


        :param metadata: The metadata of this CoreV1Event.  # noqa: E501
        :type metadata: V1ObjectMeta
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def reason(self):
        """Gets the reason of this CoreV1Event.  # noqa: E501

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :return: The reason of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CoreV1Event.

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :param reason: The reason of this CoreV1Event.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def related(self):
        """Gets the related of this CoreV1Event.  # noqa: E501


        :return: The related of this CoreV1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this CoreV1Event.


        :param related: The related of this CoreV1Event.  # noqa: E501
        :type related: V1ObjectReference
        """

        self._related = related

    @property
    def reporting_component(self):
        """Gets the reporting_component of this CoreV1Event.  # noqa: E501

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :return: The reporting_component of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_component

    @reporting_component.setter
    def reporting_component(self, reporting_component):
        """Sets the reporting_component of this CoreV1Event.

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :param reporting_component: The reporting_component of this CoreV1Event.  # noqa: E501
        :type reporting_component: str
        """

        self._reporting_component = reporting_component

    @property
    def reporting_instance(self):
        """Gets the reporting_instance of this CoreV1Event.  # noqa: E501

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :return: The reporting_instance of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_instance

    @reporting_instance.setter
    def reporting_instance(self, reporting_instance):
        """Sets the reporting_instance of this CoreV1Event.

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :param reporting_instance: The reporting_instance of this CoreV1Event.  # noqa: E501
        :type reporting_instance: str
        """

        self._reporting_instance = reporting_instance

    @property
    def series(self):
        """Gets the series of this CoreV1Event.  # noqa: E501


        :return: The series of this CoreV1Event.  # noqa: E501
        :rtype: CoreV1EventSeries
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this CoreV1Event.


        :param series: The series of this CoreV1Event.  # noqa: E501
        :type series: CoreV1EventSeries
        """

        self._series = series

    @property
    def source(self):
        """Gets the source of this CoreV1Event.  # noqa: E501


        :return: The source of this CoreV1Event.  # noqa: E501
        :rtype: V1EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CoreV1Event.


        :param source: The source of this CoreV1Event.  # noqa: E501
        :type source: V1EventSource
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this CoreV1Event.  # noqa: E501

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :return: The type of this CoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoreV1Event.

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :param type: The type of this CoreV1Event.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, CoreV1Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoreV1Event):
            return True

        return self.to_dict() != other.to_dict()
