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


class V1alpha2ResourceClaimSpec(object):
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
        'allocation_mode': 'str',
        'parameters_ref': 'V1alpha2ResourceClaimParametersReference',
        'resource_class_name': 'str'
    }

    attribute_map = {
        'allocation_mode': 'allocationMode',
        'parameters_ref': 'parametersRef',
        'resource_class_name': 'resourceClassName'
    }

    def __init__(self, allocation_mode=None, parameters_ref=None, resource_class_name=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2ResourceClaimSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allocation_mode = None
        self._parameters_ref = None
        self._resource_class_name = None
        self.discriminator = None

        if allocation_mode is not None:
            self.allocation_mode = allocation_mode
        if parameters_ref is not None:
            self.parameters_ref = parameters_ref
        self.resource_class_name = resource_class_name

    @property
    def allocation_mode(self):
        """Gets the allocation_mode of this V1alpha2ResourceClaimSpec.  # noqa: E501

        Allocation can start immediately or when a Pod wants to use the resource. \"WaitForFirstConsumer\" is the default.  # noqa: E501

        :return: The allocation_mode of this V1alpha2ResourceClaimSpec.  # noqa: E501
        :rtype: str
        """
        return self._allocation_mode

    @allocation_mode.setter
    def allocation_mode(self, allocation_mode):
        """Sets the allocation_mode of this V1alpha2ResourceClaimSpec.

        Allocation can start immediately or when a Pod wants to use the resource. \"WaitForFirstConsumer\" is the default.  # noqa: E501

        :param allocation_mode: The allocation_mode of this V1alpha2ResourceClaimSpec.  # noqa: E501
        :type allocation_mode: str
        """

        self._allocation_mode = allocation_mode

    @property
    def parameters_ref(self):
        """Gets the parameters_ref of this V1alpha2ResourceClaimSpec.  # noqa: E501


        :return: The parameters_ref of this V1alpha2ResourceClaimSpec.  # noqa: E501
        :rtype: V1alpha2ResourceClaimParametersReference
        """
        return self._parameters_ref

    @parameters_ref.setter
    def parameters_ref(self, parameters_ref):
        """Sets the parameters_ref of this V1alpha2ResourceClaimSpec.


        :param parameters_ref: The parameters_ref of this V1alpha2ResourceClaimSpec.  # noqa: E501
        :type parameters_ref: V1alpha2ResourceClaimParametersReference
        """

        self._parameters_ref = parameters_ref

    @property
    def resource_class_name(self):
        """Gets the resource_class_name of this V1alpha2ResourceClaimSpec.  # noqa: E501

        ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment.  # noqa: E501

        :return: The resource_class_name of this V1alpha2ResourceClaimSpec.  # noqa: E501
        :rtype: str
        """
        return self._resource_class_name

    @resource_class_name.setter
    def resource_class_name(self, resource_class_name):
        """Sets the resource_class_name of this V1alpha2ResourceClaimSpec.

        ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment.  # noqa: E501

        :param resource_class_name: The resource_class_name of this V1alpha2ResourceClaimSpec.  # noqa: E501
        :type resource_class_name: str
        """
        if self.local_vars_configuration.client_side_validation and resource_class_name is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_class_name`, must not be `None`")  # noqa: E501

        self._resource_class_name = resource_class_name

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
        if not isinstance(other, V1alpha2ResourceClaimSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2ResourceClaimSpec):
            return True

        return self.to_dict() != other.to_dict()
