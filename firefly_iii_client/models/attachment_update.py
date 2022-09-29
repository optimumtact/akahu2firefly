# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 0.10.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AttachmentUpdate(object):
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
        'filename': 'str',
        'model': 'str',
        'model_id': 'int',
        'notes': 'str',
        'title': 'str'
    }

    attribute_map = {
        'filename': 'filename',
        'model': 'model',
        'model_id': 'model_id',
        'notes': 'notes',
        'title': 'title'
    }

    def __init__(self, filename=None, model=None, model_id=None, notes=None, title=None):  # noqa: E501
        """AttachmentUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._filename = None
        self._model = None
        self._model_id = None
        self._notes = None
        self._title = None
        self.discriminator = None

        self.filename = filename
        self.model = model
        self.model_id = model_id
        if notes is not None:
            self.notes = notes
        if title is not None:
            self.title = title

    @property
    def filename(self):
        """Gets the filename of this AttachmentUpdate.  # noqa: E501


        :return: The filename of this AttachmentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this AttachmentUpdate.


        :param filename: The filename of this AttachmentUpdate.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def model(self):
        """Gets the model of this AttachmentUpdate.  # noqa: E501

        The object class to which the attachment must be linked.  # noqa: E501

        :return: The model of this AttachmentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this AttachmentUpdate.

        The object class to which the attachment must be linked.  # noqa: E501

        :param model: The model of this AttachmentUpdate.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        allowed_values = ["Bill", "Transaction", "TransactionJournal", "ImportJob"]  # noqa: E501
        if model not in allowed_values:
            raise ValueError(
                "Invalid value for `model` ({0}), must be one of {1}"  # noqa: E501
                .format(model, allowed_values)
            )

        self._model = model

    @property
    def model_id(self):
        """Gets the model_id of this AttachmentUpdate.  # noqa: E501


        :return: The model_id of this AttachmentUpdate.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this AttachmentUpdate.


        :param model_id: The model_id of this AttachmentUpdate.  # noqa: E501
        :type: int
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

    @property
    def notes(self):
        """Gets the notes of this AttachmentUpdate.  # noqa: E501


        :return: The notes of this AttachmentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AttachmentUpdate.


        :param notes: The notes of this AttachmentUpdate.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def title(self):
        """Gets the title of this AttachmentUpdate.  # noqa: E501


        :return: The title of this AttachmentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AttachmentUpdate.


        :param title: The title of this AttachmentUpdate.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, AttachmentUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
