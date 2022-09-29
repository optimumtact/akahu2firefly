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


class Category(object):
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
        'created_at': 'datetime',
        'earned': 'list[CategoryEarned]',
        'name': 'str',
        'spent': 'list[CategorySpent]',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'created_at': 'created_at',
        'earned': 'earned',
        'name': 'name',
        'spent': 'spent',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, earned=None, name=None, spent=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Category - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._earned = None
        self._name = None
        self._spent = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if earned is not None:
            self.earned = earned
        self.name = name
        if spent is not None:
            self.spent = spent
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this Category.  # noqa: E501


        :return: The created_at of this Category.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Category.


        :param created_at: The created_at of this Category.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def earned(self):
        """Gets the earned of this Category.  # noqa: E501


        :return: The earned of this Category.  # noqa: E501
        :rtype: list[CategoryEarned]
        """
        return self._earned

    @earned.setter
    def earned(self, earned):
        """Sets the earned of this Category.


        :param earned: The earned of this Category.  # noqa: E501
        :type: list[CategoryEarned]
        """

        self._earned = earned

    @property
    def name(self):
        """Gets the name of this Category.  # noqa: E501


        :return: The name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.


        :param name: The name of this Category.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def spent(self):
        """Gets the spent of this Category.  # noqa: E501


        :return: The spent of this Category.  # noqa: E501
        :rtype: list[CategorySpent]
        """
        return self._spent

    @spent.setter
    def spent(self, spent):
        """Sets the spent of this Category.


        :param spent: The spent of this Category.  # noqa: E501
        :type: list[CategorySpent]
        """

        self._spent = spent

    @property
    def updated_at(self):
        """Gets the updated_at of this Category.  # noqa: E501


        :return: The updated_at of this Category.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Category.


        :param updated_at: The updated_at of this Category.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Category):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Category):
            return True

        return self.to_dict() != other.to_dict()
