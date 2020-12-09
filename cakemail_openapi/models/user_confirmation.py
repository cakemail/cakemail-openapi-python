# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.3.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class UserConfirmation(object):
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
        'confirmation': 'str',
        'password': 'str'
    }

    attribute_map = {
        'confirmation': 'confirmation',
        'password': 'password'
    }

    def __init__(self, confirmation=None, password=None, local_vars_configuration=None):  # noqa: E501
        """UserConfirmation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._confirmation = None
        self._password = None
        self.discriminator = None

        self.confirmation = confirmation
        self.password = password

    @property
    def confirmation(self):
        """Gets the confirmation of this UserConfirmation.  # noqa: E501


        :return: The confirmation of this UserConfirmation.  # noqa: E501
        :rtype: str
        """
        return self._confirmation

    @confirmation.setter
    def confirmation(self, confirmation):
        """Sets the confirmation of this UserConfirmation.


        :param confirmation: The confirmation of this UserConfirmation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and confirmation is None:  # noqa: E501
            raise ValueError("Invalid value for `confirmation`, must not be `None`")  # noqa: E501

        self._confirmation = confirmation

    @property
    def password(self):
        """Gets the password of this UserConfirmation.  # noqa: E501


        :return: The password of this UserConfirmation.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserConfirmation.


        :param password: The password of this UserConfirmation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 8):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `8`")  # noqa: E501

        self._password = password

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
        if not isinstance(other, UserConfirmation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserConfirmation):
            return True

        return self.to_dict() != other.to_dict()
