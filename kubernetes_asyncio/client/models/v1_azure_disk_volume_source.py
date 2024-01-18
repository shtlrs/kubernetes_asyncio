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


class V1AzureDiskVolumeSource(object):
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
        'caching_mode': 'str',
        'disk_name': 'str',
        'disk_uri': 'str',
        'fs_type': 'str',
        'kind': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'caching_mode': 'cachingMode',
        'disk_name': 'diskName',
        'disk_uri': 'diskURI',
        'fs_type': 'fsType',
        'kind': 'kind',
        'read_only': 'readOnly'
    }

    def __init__(self, caching_mode=None, disk_name=None, disk_uri=None, fs_type=None, kind=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        """V1AzureDiskVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._caching_mode = None
        self._disk_name = None
        self._disk_uri = None
        self._fs_type = None
        self._kind = None
        self._read_only = None
        self.discriminator = None

        if caching_mode is not None:
            self.caching_mode = caching_mode
        self.disk_name = disk_name
        self.disk_uri = disk_uri
        if fs_type is not None:
            self.fs_type = fs_type
        if kind is not None:
            self.kind = kind
        if read_only is not None:
            self.read_only = read_only

    @property
    def caching_mode(self):
        """Gets the caching_mode of this V1AzureDiskVolumeSource.  # noqa: E501

        cachingMode is the Host Caching mode: None, Read Only, Read Write.  # noqa: E501

        :return: The caching_mode of this V1AzureDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._caching_mode

    @caching_mode.setter
    def caching_mode(self, caching_mode):
        """Sets the caching_mode of this V1AzureDiskVolumeSource.

        cachingMode is the Host Caching mode: None, Read Only, Read Write.  # noqa: E501

        :param caching_mode: The caching_mode of this V1AzureDiskVolumeSource.  # noqa: E501
        :type caching_mode: str
        """

        self._caching_mode = caching_mode

    @property
    def disk_name(self):
        """Gets the disk_name of this V1AzureDiskVolumeSource.  # noqa: E501

        diskName is the Name of the data disk in the blob storage  # noqa: E501

        :return: The disk_name of this V1AzureDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        """Sets the disk_name of this V1AzureDiskVolumeSource.

        diskName is the Name of the data disk in the blob storage  # noqa: E501

        :param disk_name: The disk_name of this V1AzureDiskVolumeSource.  # noqa: E501
        :type disk_name: str
        """
        if self.local_vars_configuration.client_side_validation and disk_name is None:  # noqa: E501
            raise ValueError("Invalid value for `disk_name`, must not be `None`")  # noqa: E501

        self._disk_name = disk_name

    @property
    def disk_uri(self):
        """Gets the disk_uri of this V1AzureDiskVolumeSource.  # noqa: E501

        diskURI is the URI of data disk in the blob storage  # noqa: E501

        :return: The disk_uri of this V1AzureDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._disk_uri

    @disk_uri.setter
    def disk_uri(self, disk_uri):
        """Sets the disk_uri of this V1AzureDiskVolumeSource.

        diskURI is the URI of data disk in the blob storage  # noqa: E501

        :param disk_uri: The disk_uri of this V1AzureDiskVolumeSource.  # noqa: E501
        :type disk_uri: str
        """
        if self.local_vars_configuration.client_side_validation and disk_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `disk_uri`, must not be `None`")  # noqa: E501

        self._disk_uri = disk_uri

    @property
    def fs_type(self):
        """Gets the fs_type of this V1AzureDiskVolumeSource.  # noqa: E501

        fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :return: The fs_type of this V1AzureDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1AzureDiskVolumeSource.

        fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :param fs_type: The fs_type of this V1AzureDiskVolumeSource.  # noqa: E501
        :type fs_type: str
        """

        self._fs_type = fs_type

    @property
    def kind(self):
        """Gets the kind of this V1AzureDiskVolumeSource.  # noqa: E501

        kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared  # noqa: E501

        :return: The kind of this V1AzureDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1AzureDiskVolumeSource.

        kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared  # noqa: E501

        :param kind: The kind of this V1AzureDiskVolumeSource.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def read_only(self):
        """Gets the read_only of this V1AzureDiskVolumeSource.  # noqa: E501

        readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :return: The read_only of this V1AzureDiskVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1AzureDiskVolumeSource.

        readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :param read_only: The read_only of this V1AzureDiskVolumeSource.  # noqa: E501
        :type read_only: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, V1AzureDiskVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AzureDiskVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
