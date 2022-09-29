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


class ValidationErrorErrors(object):
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
        'field1': 'list[str]',
        'field2': 'list[str]'
    }

    attribute_map = {
        'field1': 'field1',
        'field2': 'field2'
    }

    def __init__(self, field1=None, field2=None, local_vars_configuration=None):  # noqa: E501
        """ValidationErrorErrors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field1 = None
        self._field2 = None
        self.discriminator = None

        if field1 is not None:
            self.field1 = field1
        if field2 is not None:
            self.field2 = field2

    @property
    def field1(self):
        """Gets the field1 of this ValidationErrorErrors.  # noqa: E501


        :return: The field1 of this ValidationErrorErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._field1

    @field1.setter
    def field1(self, field1):
        """Sets the field1 of this ValidationErrorErrors.


        :param field1: The field1 of this ValidationErrorErrors.  # noqa: E501
        :type: list[str]
        """

        self._field1 = field1

    @property
    def field2(self):
        """Gets the field2 of this ValidationErrorErrors.  # noqa: E501


        :return: The field2 of this ValidationErrorErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._field2

    @field2.setter
    def field2(self, field2):
        """Sets the field2 of this ValidationErrorErrors.


        :param field2: The field2 of this ValidationErrorErrors.  # noqa: E501
        :type: list[str]
        """

        self._field2 = field2

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
        if not isinstance(other, ValidationErrorErrors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidationErrorErrors):
            return True

        return self.to_dict() != other.to_dict()
