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


class AccountTypeProperty(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DEFAULT_ACCOUNT = "Default account"
    CASH_ACCOUNT = "Cash account"
    ASSET_ACCOUNT = "Asset account"
    EXPENSE_ACCOUNT = "Expense account"
    REVENUE_ACCOUNT = "Revenue account"
    INITIAL_BALANCE_ACCOUNT = "Initial balance account"
    BENEFICIARY_ACCOUNT = "Beneficiary account"
    IMPORT_ACCOUNT = "Import account"
    RECONCILIATION_ACCOUNT = "Reconciliation account"
    LOAN = "Loan"
    DEBT = "Debt"
    MORTGAGE = "Mortgage"

    allowable_values = [DEFAULT_ACCOUNT, CASH_ACCOUNT, ASSET_ACCOUNT, EXPENSE_ACCOUNT, REVENUE_ACCOUNT, INITIAL_BALANCE_ACCOUNT, BENEFICIARY_ACCOUNT, IMPORT_ACCOUNT, RECONCILIATION_ACCOUNT, LOAN, DEBT, MORTGAGE]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """AccountTypeProperty - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, AccountTypeProperty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountTypeProperty):
            return True

        return self.to_dict() != other.to_dict()
