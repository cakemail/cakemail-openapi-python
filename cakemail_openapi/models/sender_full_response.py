# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class SenderFullResponse(object):
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
        'id': 'str',
        'name': 'str',
        'email': 'str',
        'confirmed': 'bool',
        'confirmed_on': 'int',
        'last_confirmation_sent_on': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'email': 'email',
        'confirmed': 'confirmed',
        'confirmed_on': 'confirmed_on',
        'last_confirmation_sent_on': 'last_confirmation_sent_on'
    }

    def __init__(self, id=None, name=None, email=None, confirmed=None, confirmed_on=None, last_confirmation_sent_on=None, local_vars_configuration=None):  # noqa: E501
        """SenderFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._email = None
        self._confirmed = None
        self._confirmed_on = None
        self._last_confirmation_sent_on = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.email = email
        self.confirmed = confirmed
        if confirmed_on is not None:
            self.confirmed_on = confirmed_on
        if last_confirmation_sent_on is not None:
            self.last_confirmation_sent_on = last_confirmation_sent_on

    @property
    def id(self):
        """Gets the id of this SenderFullResponse.  # noqa: E501


        :return: The id of this SenderFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SenderFullResponse.


        :param id: The id of this SenderFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SenderFullResponse.  # noqa: E501


        :return: The name of this SenderFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SenderFullResponse.


        :param name: The name of this SenderFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this SenderFullResponse.  # noqa: E501


        :return: The email of this SenderFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SenderFullResponse.


        :param email: The email of this SenderFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def confirmed(self):
        """Gets the confirmed of this SenderFullResponse.  # noqa: E501


        :return: The confirmed of this SenderFullResponse.  # noqa: E501
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this SenderFullResponse.


        :param confirmed: The confirmed of this SenderFullResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and confirmed is None:  # noqa: E501
            raise ValueError("Invalid value for `confirmed`, must not be `None`")  # noqa: E501

        self._confirmed = confirmed

    @property
    def confirmed_on(self):
        """Gets the confirmed_on of this SenderFullResponse.  # noqa: E501


        :return: The confirmed_on of this SenderFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._confirmed_on

    @confirmed_on.setter
    def confirmed_on(self, confirmed_on):
        """Sets the confirmed_on of this SenderFullResponse.


        :param confirmed_on: The confirmed_on of this SenderFullResponse.  # noqa: E501
        :type: int
        """

        self._confirmed_on = confirmed_on

    @property
    def last_confirmation_sent_on(self):
        """Gets the last_confirmation_sent_on of this SenderFullResponse.  # noqa: E501


        :return: The last_confirmation_sent_on of this SenderFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_confirmation_sent_on

    @last_confirmation_sent_on.setter
    def last_confirmation_sent_on(self, last_confirmation_sent_on):
        """Sets the last_confirmation_sent_on of this SenderFullResponse.


        :param last_confirmation_sent_on: The last_confirmation_sent_on of this SenderFullResponse.  # noqa: E501
        :type: int
        """

        self._last_confirmation_sent_on = last_confirmation_sent_on

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
        if not isinstance(other, SenderFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SenderFullResponse):
            return True

        return self.to_dict() != other.to_dict()
