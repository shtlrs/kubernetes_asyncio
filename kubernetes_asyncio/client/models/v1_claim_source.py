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


class V1ClaimSource(object):
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
        'resource_claim_name': 'str',
        'resource_claim_template_name': 'str'
    }

    attribute_map = {
        'resource_claim_name': 'resourceClaimName',
        'resource_claim_template_name': 'resourceClaimTemplateName'
    }

    def __init__(self, resource_claim_name=None, resource_claim_template_name=None, local_vars_configuration=None):  # noqa: E501
        """V1ClaimSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._resource_claim_name = None
        self._resource_claim_template_name = None
        self.discriminator = None

        if resource_claim_name is not None:
            self.resource_claim_name = resource_claim_name
        if resource_claim_template_name is not None:
            self.resource_claim_template_name = resource_claim_template_name

    @property
    def resource_claim_name(self):
        """Gets the resource_claim_name of this V1ClaimSource.  # noqa: E501

        ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.  # noqa: E501

        :return: The resource_claim_name of this V1ClaimSource.  # noqa: E501
        :rtype: str
        """
        return self._resource_claim_name

    @resource_claim_name.setter
    def resource_claim_name(self, resource_claim_name):
        """Sets the resource_claim_name of this V1ClaimSource.

        ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.  # noqa: E501

        :param resource_claim_name: The resource_claim_name of this V1ClaimSource.  # noqa: E501
        :type resource_claim_name: str
        """

        self._resource_claim_name = resource_claim_name

    @property
    def resource_claim_template_name(self):
        """Gets the resource_claim_template_name of this V1ClaimSource.  # noqa: E501

        ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  # noqa: E501

        :return: The resource_claim_template_name of this V1ClaimSource.  # noqa: E501
        :rtype: str
        """
        return self._resource_claim_template_name

    @resource_claim_template_name.setter
    def resource_claim_template_name(self, resource_claim_template_name):
        """Sets the resource_claim_template_name of this V1ClaimSource.

        ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  # noqa: E501

        :param resource_claim_template_name: The resource_claim_template_name of this V1ClaimSource.  # noqa: E501
        :type resource_claim_template_name: str
        """

        self._resource_claim_template_name = resource_claim_template_name

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
        if not isinstance(other, V1ClaimSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ClaimSource):
            return True

        return self.to_dict() != other.to_dict()
