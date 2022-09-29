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


class TransactionLink(object):
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
        'inward_id': 'int',
        'link_type_id': 'int',
        'link_type_name': 'str',
        'notes': 'str',
        'outward_id': 'int',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'created_at': 'created_at',
        'inward_id': 'inward_id',
        'link_type_id': 'link_type_id',
        'link_type_name': 'link_type_name',
        'notes': 'notes',
        'outward_id': 'outward_id',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, inward_id=None, link_type_id=None, link_type_name=None, notes=None, outward_id=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """TransactionLink - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._inward_id = None
        self._link_type_id = None
        self._link_type_name = None
        self._notes = None
        self._outward_id = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        self.inward_id = inward_id
        self.link_type_id = link_type_id
        if link_type_name is not None:
            self.link_type_name = link_type_name
        if notes is not None:
            self.notes = notes
        self.outward_id = outward_id
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this TransactionLink.  # noqa: E501


        :return: The created_at of this TransactionLink.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransactionLink.


        :param created_at: The created_at of this TransactionLink.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def inward_id(self):
        """Gets the inward_id of this TransactionLink.  # noqa: E501

        The inward transaction transaction_journal_id for the link. This becomes the 'is paid by' transaction of the set.  # noqa: E501

        :return: The inward_id of this TransactionLink.  # noqa: E501
        :rtype: int
        """
        return self._inward_id

    @inward_id.setter
    def inward_id(self, inward_id):
        """Sets the inward_id of this TransactionLink.

        The inward transaction transaction_journal_id for the link. This becomes the 'is paid by' transaction of the set.  # noqa: E501

        :param inward_id: The inward_id of this TransactionLink.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and inward_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inward_id`, must not be `None`")  # noqa: E501

        self._inward_id = inward_id

    @property
    def link_type_id(self):
        """Gets the link_type_id of this TransactionLink.  # noqa: E501

        The link type ID to use. You can also use the link_type_name field.  # noqa: E501

        :return: The link_type_id of this TransactionLink.  # noqa: E501
        :rtype: int
        """
        return self._link_type_id

    @link_type_id.setter
    def link_type_id(self, link_type_id):
        """Sets the link_type_id of this TransactionLink.

        The link type ID to use. You can also use the link_type_name field.  # noqa: E501

        :param link_type_id: The link_type_id of this TransactionLink.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and link_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `link_type_id`, must not be `None`")  # noqa: E501

        self._link_type_id = link_type_id

    @property
    def link_type_name(self):
        """Gets the link_type_name of this TransactionLink.  # noqa: E501

        The link type name to use. You can also use the link_type_id field.  # noqa: E501

        :return: The link_type_name of this TransactionLink.  # noqa: E501
        :rtype: str
        """
        return self._link_type_name

    @link_type_name.setter
    def link_type_name(self, link_type_name):
        """Sets the link_type_name of this TransactionLink.

        The link type name to use. You can also use the link_type_id field.  # noqa: E501

        :param link_type_name: The link_type_name of this TransactionLink.  # noqa: E501
        :type: str
        """

        self._link_type_name = link_type_name

    @property
    def notes(self):
        """Gets the notes of this TransactionLink.  # noqa: E501

        Optional. Some notes.  # noqa: E501

        :return: The notes of this TransactionLink.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this TransactionLink.

        Optional. Some notes.  # noqa: E501

        :param notes: The notes of this TransactionLink.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def outward_id(self):
        """Gets the outward_id of this TransactionLink.  # noqa: E501

        The outward transaction transaction_journal_id for the link. This becomes the 'pays for' transaction of the set.  # noqa: E501

        :return: The outward_id of this TransactionLink.  # noqa: E501
        :rtype: int
        """
        return self._outward_id

    @outward_id.setter
    def outward_id(self, outward_id):
        """Sets the outward_id of this TransactionLink.

        The outward transaction transaction_journal_id for the link. This becomes the 'pays for' transaction of the set.  # noqa: E501

        :param outward_id: The outward_id of this TransactionLink.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and outward_id is None:  # noqa: E501
            raise ValueError("Invalid value for `outward_id`, must not be `None`")  # noqa: E501

        self._outward_id = outward_id

    @property
    def updated_at(self):
        """Gets the updated_at of this TransactionLink.  # noqa: E501


        :return: The updated_at of this TransactionLink.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TransactionLink.


        :param updated_at: The updated_at of this TransactionLink.  # noqa: E501
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
        if not isinstance(other, TransactionLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionLink):
            return True

        return self.to_dict() != other.to_dict()