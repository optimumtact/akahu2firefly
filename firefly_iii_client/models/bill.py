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


class Bill(object):
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
        'active': 'bool',
        'amount_max': 'str',
        'amount_min': 'str',
        'created_at': 'datetime',
        'currency_code': 'str',
        'currency_decimal_places': 'int',
        'currency_id': 'int',
        'currency_symbol': 'str',
        'date': 'date',
        'name': 'str',
        'next_expected_match': 'date',
        'notes': 'str',
        'object_group_id': 'int',
        'object_group_order': 'int',
        'object_group_title': 'str',
        'paid_dates': 'list[BillPaidDates]',
        'pay_dates': 'list[date]',
        'repeat_freq': 'str',
        'skip': 'int',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'amount_max': 'amount_max',
        'amount_min': 'amount_min',
        'created_at': 'created_at',
        'currency_code': 'currency_code',
        'currency_decimal_places': 'currency_decimal_places',
        'currency_id': 'currency_id',
        'currency_symbol': 'currency_symbol',
        'date': 'date',
        'name': 'name',
        'next_expected_match': 'next_expected_match',
        'notes': 'notes',
        'object_group_id': 'object_group_id',
        'object_group_order': 'object_group_order',
        'object_group_title': 'object_group_title',
        'paid_dates': 'paid_dates',
        'pay_dates': 'pay_dates',
        'repeat_freq': 'repeat_freq',
        'skip': 'skip',
        'updated_at': 'updated_at'
    }

    def __init__(self, active=None, amount_max=None, amount_min=None, created_at=None, currency_code=None, currency_decimal_places=None, currency_id=None, currency_symbol=None, date=None, name=None, next_expected_match=None, notes=None, object_group_id=None, object_group_order=None, object_group_title=None, paid_dates=None, pay_dates=None, repeat_freq=None, skip=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Bill - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._amount_max = None
        self._amount_min = None
        self._created_at = None
        self._currency_code = None
        self._currency_decimal_places = None
        self._currency_id = None
        self._currency_symbol = None
        self._date = None
        self._name = None
        self._next_expected_match = None
        self._notes = None
        self._object_group_id = None
        self._object_group_order = None
        self._object_group_title = None
        self._paid_dates = None
        self._pay_dates = None
        self._repeat_freq = None
        self._skip = None
        self._updated_at = None
        self.discriminator = None

        if active is not None:
            self.active = active
        self.amount_max = amount_max
        self.amount_min = amount_min
        if created_at is not None:
            self.created_at = created_at
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_decimal_places is not None:
            self.currency_decimal_places = currency_decimal_places
        if currency_id is not None:
            self.currency_id = currency_id
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        self.date = date
        self.name = name
        if next_expected_match is not None:
            self.next_expected_match = next_expected_match
        if notes is not None:
            self.notes = notes
        if object_group_id is not None:
            self.object_group_id = object_group_id
        if object_group_order is not None:
            self.object_group_order = object_group_order
        if object_group_title is not None:
            self.object_group_title = object_group_title
        if paid_dates is not None:
            self.paid_dates = paid_dates
        if pay_dates is not None:
            self.pay_dates = pay_dates
        self.repeat_freq = repeat_freq
        if skip is not None:
            self.skip = skip
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def active(self):
        """Gets the active of this Bill.  # noqa: E501

        If the bill is active.  # noqa: E501

        :return: The active of this Bill.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Bill.

        If the bill is active.  # noqa: E501

        :param active: The active of this Bill.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def amount_max(self):
        """Gets the amount_max of this Bill.  # noqa: E501


        :return: The amount_max of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._amount_max

    @amount_max.setter
    def amount_max(self, amount_max):
        """Sets the amount_max of this Bill.


        :param amount_max: The amount_max of this Bill.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount_max is None:  # noqa: E501
            raise ValueError("Invalid value for `amount_max`, must not be `None`")  # noqa: E501

        self._amount_max = amount_max

    @property
    def amount_min(self):
        """Gets the amount_min of this Bill.  # noqa: E501


        :return: The amount_min of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._amount_min

    @amount_min.setter
    def amount_min(self, amount_min):
        """Sets the amount_min of this Bill.


        :param amount_min: The amount_min of this Bill.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount_min is None:  # noqa: E501
            raise ValueError("Invalid value for `amount_min`, must not be `None`")  # noqa: E501

        self._amount_min = amount_min

    @property
    def created_at(self):
        """Gets the created_at of this Bill.  # noqa: E501


        :return: The created_at of this Bill.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Bill.


        :param created_at: The created_at of this Bill.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def currency_code(self):
        """Gets the currency_code of this Bill.  # noqa: E501

        Use either currency_id or currency_code  # noqa: E501

        :return: The currency_code of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Bill.

        Use either currency_id or currency_code  # noqa: E501

        :param currency_code: The currency_code of this Bill.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_decimal_places(self):
        """Gets the currency_decimal_places of this Bill.  # noqa: E501


        :return: The currency_decimal_places of this Bill.  # noqa: E501
        :rtype: int
        """
        return self._currency_decimal_places

    @currency_decimal_places.setter
    def currency_decimal_places(self, currency_decimal_places):
        """Sets the currency_decimal_places of this Bill.


        :param currency_decimal_places: The currency_decimal_places of this Bill.  # noqa: E501
        :type: int
        """

        self._currency_decimal_places = currency_decimal_places

    @property
    def currency_id(self):
        """Gets the currency_id of this Bill.  # noqa: E501

        Use either currency_id or currency_code  # noqa: E501

        :return: The currency_id of this Bill.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this Bill.

        Use either currency_id or currency_code  # noqa: E501

        :param currency_id: The currency_id of this Bill.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this Bill.  # noqa: E501


        :return: The currency_symbol of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this Bill.


        :param currency_symbol: The currency_symbol of this Bill.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def date(self):
        """Gets the date of this Bill.  # noqa: E501


        :return: The date of this Bill.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Bill.


        :param date: The date of this Bill.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def name(self):
        """Gets the name of this Bill.  # noqa: E501


        :return: The name of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bill.


        :param name: The name of this Bill.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def next_expected_match(self):
        """Gets the next_expected_match of this Bill.  # noqa: E501

        When the bill is expected to be due.  # noqa: E501

        :return: The next_expected_match of this Bill.  # noqa: E501
        :rtype: date
        """
        return self._next_expected_match

    @next_expected_match.setter
    def next_expected_match(self, next_expected_match):
        """Sets the next_expected_match of this Bill.

        When the bill is expected to be due.  # noqa: E501

        :param next_expected_match: The next_expected_match of this Bill.  # noqa: E501
        :type: date
        """

        self._next_expected_match = next_expected_match

    @property
    def notes(self):
        """Gets the notes of this Bill.  # noqa: E501


        :return: The notes of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Bill.


        :param notes: The notes of this Bill.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def object_group_id(self):
        """Gets the object_group_id of this Bill.  # noqa: E501

        The group ID of the group this object is part of. NULL if no group.  # noqa: E501

        :return: The object_group_id of this Bill.  # noqa: E501
        :rtype: int
        """
        return self._object_group_id

    @object_group_id.setter
    def object_group_id(self, object_group_id):
        """Sets the object_group_id of this Bill.

        The group ID of the group this object is part of. NULL if no group.  # noqa: E501

        :param object_group_id: The object_group_id of this Bill.  # noqa: E501
        :type: int
        """

        self._object_group_id = object_group_id

    @property
    def object_group_order(self):
        """Gets the object_group_order of this Bill.  # noqa: E501

        The order of the group. At least 1, for the highest sorting.  # noqa: E501

        :return: The object_group_order of this Bill.  # noqa: E501
        :rtype: int
        """
        return self._object_group_order

    @object_group_order.setter
    def object_group_order(self, object_group_order):
        """Sets the object_group_order of this Bill.

        The order of the group. At least 1, for the highest sorting.  # noqa: E501

        :param object_group_order: The object_group_order of this Bill.  # noqa: E501
        :type: int
        """

        self._object_group_order = object_group_order

    @property
    def object_group_title(self):
        """Gets the object_group_title of this Bill.  # noqa: E501

        The name of the group. NULL if no group.  # noqa: E501

        :return: The object_group_title of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._object_group_title

    @object_group_title.setter
    def object_group_title(self, object_group_title):
        """Sets the object_group_title of this Bill.

        The name of the group. NULL if no group.  # noqa: E501

        :param object_group_title: The object_group_title of this Bill.  # noqa: E501
        :type: str
        """

        self._object_group_title = object_group_title

    @property
    def paid_dates(self):
        """Gets the paid_dates of this Bill.  # noqa: E501

        Array of past transactions when the bill was paid.  # noqa: E501

        :return: The paid_dates of this Bill.  # noqa: E501
        :rtype: list[BillPaidDates]
        """
        return self._paid_dates

    @paid_dates.setter
    def paid_dates(self, paid_dates):
        """Sets the paid_dates of this Bill.

        Array of past transactions when the bill was paid.  # noqa: E501

        :param paid_dates: The paid_dates of this Bill.  # noqa: E501
        :type: list[BillPaidDates]
        """

        self._paid_dates = paid_dates

    @property
    def pay_dates(self):
        """Gets the pay_dates of this Bill.  # noqa: E501

        Array of future dates when the bill is expected to be paid. Autogenerated.  # noqa: E501

        :return: The pay_dates of this Bill.  # noqa: E501
        :rtype: list[date]
        """
        return self._pay_dates

    @pay_dates.setter
    def pay_dates(self, pay_dates):
        """Sets the pay_dates of this Bill.

        Array of future dates when the bill is expected to be paid. Autogenerated.  # noqa: E501

        :param pay_dates: The pay_dates of this Bill.  # noqa: E501
        :type: list[date]
        """

        self._pay_dates = pay_dates

    @property
    def repeat_freq(self):
        """Gets the repeat_freq of this Bill.  # noqa: E501

        How often the bill must be paid.  # noqa: E501

        :return: The repeat_freq of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._repeat_freq

    @repeat_freq.setter
    def repeat_freq(self, repeat_freq):
        """Sets the repeat_freq of this Bill.

        How often the bill must be paid.  # noqa: E501

        :param repeat_freq: The repeat_freq of this Bill.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and repeat_freq is None:  # noqa: E501
            raise ValueError("Invalid value for `repeat_freq`, must not be `None`")  # noqa: E501
        allowed_values = ["weekly", "monthly", "quarterly", "half-year", "yearly"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and repeat_freq not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `repeat_freq` ({0}), must be one of {1}"  # noqa: E501
                .format(repeat_freq, allowed_values)
            )

        self._repeat_freq = repeat_freq

    @property
    def skip(self):
        """Gets the skip of this Bill.  # noqa: E501

        How often the bill must be skipped. 1 means a bi-monthly bill.  # noqa: E501

        :return: The skip of this Bill.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this Bill.

        How often the bill must be skipped. 1 means a bi-monthly bill.  # noqa: E501

        :param skip: The skip of this Bill.  # noqa: E501
        :type: int
        """

        self._skip = skip

    @property
    def updated_at(self):
        """Gets the updated_at of this Bill.  # noqa: E501


        :return: The updated_at of this Bill.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Bill.


        :param updated_at: The updated_at of this Bill.  # noqa: E501
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
        if not isinstance(other, Bill):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Bill):
            return True

        return self.to_dict() != other.to_dict()