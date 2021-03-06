# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.4.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class ResetPasswordConfirmResponse(object):
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
        'object': 'str',
        'password_reset': 'bool'
    }

    attribute_map = {
        'object': 'object',
        'password_reset': 'password_reset'
    }

    def __init__(self, object='user', password_reset=True, local_vars_configuration=None):  # noqa: E501
        """ResetPasswordConfirmResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object = None
        self._password_reset = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if password_reset is not None:
            self.password_reset = password_reset

    @property
    def object(self):
        """Gets the object of this ResetPasswordConfirmResponse.  # noqa: E501


        :return: The object of this ResetPasswordConfirmResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ResetPasswordConfirmResponse.


        :param object: The object of this ResetPasswordConfirmResponse.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def password_reset(self):
        """Gets the password_reset of this ResetPasswordConfirmResponse.  # noqa: E501


        :return: The password_reset of this ResetPasswordConfirmResponse.  # noqa: E501
        :rtype: bool
        """
        return self._password_reset

    @password_reset.setter
    def password_reset(self, password_reset):
        """Sets the password_reset of this ResetPasswordConfirmResponse.


        :param password_reset: The password_reset of this ResetPasswordConfirmResponse.  # noqa: E501
        :type: bool
        """

        self._password_reset = password_reset

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
        if not isinstance(other, ResetPasswordConfirmResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetPasswordConfirmResponse):
            return True

        return self.to_dict() != other.to_dict()
