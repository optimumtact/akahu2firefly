# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from firefly_iii_client.configuration import Configuration


class LinkType(object):
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
        'editable': 'bool',
        'inward': 'str',
        'name': 'str',
        'outward': 'str'
    }

    attribute_map = {
        'editable': 'editable',
        'inward': 'inward',
        'name': 'name',
        'outward': 'outward'
    }

    def __init__(self, editable=None, inward=None, name=None, outward=None, local_vars_configuration=None):  # noqa: E501
        """LinkType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._editable = None
        self._inward = None
        self._name = None
        self._outward = None
        self.discriminator = None

        if editable is not None:
            self.editable = editable
        self.inward = inward
        self.name = name
        self.outward = outward

    @property
    def editable(self):
        """Gets the editable of this LinkType.  # noqa: E501


        :return: The editable of this LinkType.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this LinkType.


        :param editable: The editable of this LinkType.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def inward(self):
        """Gets the inward of this LinkType.  # noqa: E501


        :return: The inward of this LinkType.  # noqa: E501
        :rtype: str
        """
        return self._inward

    @inward.setter
    def inward(self, inward):
        """Sets the inward of this LinkType.


        :param inward: The inward of this LinkType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inward is None:  # noqa: E501
            raise ValueError("Invalid value for `inward`, must not be `None`")  # noqa: E501

        self._inward = inward

    @property
    def name(self):
        """Gets the name of this LinkType.  # noqa: E501


        :return: The name of this LinkType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LinkType.


        :param name: The name of this LinkType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outward(self):
        """Gets the outward of this LinkType.  # noqa: E501


        :return: The outward of this LinkType.  # noqa: E501
        :rtype: str
        """
        return self._outward

    @outward.setter
    def outward(self, outward):
        """Sets the outward of this LinkType.


        :param outward: The outward of this LinkType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and outward is None:  # noqa: E501
            raise ValueError("Invalid value for `outward`, must not be `None`")  # noqa: E501

        self._outward = outward

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LinkType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkType):
            return True

        return self.to_dict() != other.to_dict()