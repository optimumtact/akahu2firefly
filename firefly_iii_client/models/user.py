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


class User(object):
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
        'blocked': 'bool',
        'blocked_code': 'str',
        'created_at': 'datetime',
        'email': 'str',
        'role': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'blocked': 'blocked',
        'blocked_code': 'blocked_code',
        'created_at': 'created_at',
        'email': 'email',
        'role': 'role',
        'updated_at': 'updated_at'
    }

    def __init__(self, blocked=None, blocked_code=None, created_at=None, email=None, role=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._blocked = None
        self._blocked_code = None
        self._created_at = None
        self._email = None
        self._role = None
        self._updated_at = None
        self.discriminator = None

        if blocked is not None:
            self.blocked = blocked
        self.blocked_code = blocked_code
        if created_at is not None:
            self.created_at = created_at
        self.email = email
        self.role = role
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def blocked(self):
        """Gets the blocked of this User.  # noqa: E501

        Boolean to indicate if the user is blocked.  # noqa: E501

        :return: The blocked of this User.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this User.

        Boolean to indicate if the user is blocked.  # noqa: E501

        :param blocked: The blocked of this User.  # noqa: E501
        :type: bool
        """

        self._blocked = blocked

    @property
    def blocked_code(self):
        """Gets the blocked_code of this User.  # noqa: E501

        If you say the user must be blocked, this will be the reason code.  # noqa: E501

        :return: The blocked_code of this User.  # noqa: E501
        :rtype: str
        """
        return self._blocked_code

    @blocked_code.setter
    def blocked_code(self, blocked_code):
        """Sets the blocked_code of this User.

        If you say the user must be blocked, this will be the reason code.  # noqa: E501

        :param blocked_code: The blocked_code of this User.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"email_changed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and blocked_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `blocked_code` ({0}), must be one of {1}"  # noqa: E501
                .format(blocked_code, allowed_values)
            )

        self._blocked_code = blocked_code

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501


        :return: The created_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.


        :param created_at: The created_at of this User.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        The new users email address.  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        The new users email address.  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def role(self):
        """Gets the role of this User.  # noqa: E501

        Role for the new user. Can be empty or omitted.  # noqa: E501

        :return: The role of this User.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.

        Role for the new user. Can be empty or omitted.  # noqa: E501

        :param role: The role of this User.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"owner", "demo"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and role not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501


        :return: The updated_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.


        :param updated_at: The updated_at of this User.  # noqa: E501
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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()