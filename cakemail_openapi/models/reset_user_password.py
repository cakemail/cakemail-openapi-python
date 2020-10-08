# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class ResetUserPassword(object):
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
        'invalidate_current_password': 'bool'
    }

    attribute_map = {
        'invalidate_current_password': 'invalidate_current_password'
    }

    def __init__(self, invalidate_current_password=False, local_vars_configuration=None):  # noqa: E501
        """ResetUserPassword - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._invalidate_current_password = None
        self.discriminator = None

        if invalidate_current_password is not None:
            self.invalidate_current_password = invalidate_current_password

    @property
    def invalidate_current_password(self):
        """Gets the invalidate_current_password of this ResetUserPassword.  # noqa: E501


        :return: The invalidate_current_password of this ResetUserPassword.  # noqa: E501
        :rtype: bool
        """
        return self._invalidate_current_password

    @invalidate_current_password.setter
    def invalidate_current_password(self, invalidate_current_password):
        """Sets the invalidate_current_password of this ResetUserPassword.


        :param invalidate_current_password: The invalidate_current_password of this ResetUserPassword.  # noqa: E501
        :type: bool
        """

        self._invalidate_current_password = invalidate_current_password

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
        if not isinstance(other, ResetUserPassword):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetUserPassword):
            return True

        return self.to_dict() != other.to_dict()
