# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.4.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class AccountOwnerUser(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'title': 'str',
        'office_phone': 'str',
        'mobile_phone': 'str',
        'language': 'Languages',
        'timezone': 'str',
        'email': 'str',
        'password': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'title': 'title',
        'office_phone': 'office_phone',
        'mobile_phone': 'mobile_phone',
        'language': 'language',
        'timezone': 'timezone',
        'email': 'email',
        'password': 'password'
    }

    def __init__(self, first_name=None, last_name=None, title=None, office_phone=None, mobile_phone=None, language=None, timezone=None, email=None, password=None, local_vars_configuration=None):  # noqa: E501
        """AccountOwnerUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._first_name = None
        self._last_name = None
        self._title = None
        self._office_phone = None
        self._mobile_phone = None
        self._language = None
        self._timezone = None
        self._email = None
        self._password = None
        self.discriminator = None

        self.first_name = first_name
        self.last_name = last_name
        if title is not None:
            self.title = title
        if office_phone is not None:
            self.office_phone = office_phone
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if language is not None:
            self.language = language
        if timezone is not None:
            self.timezone = timezone
        self.email = email
        if password is not None:
            self.password = password

    @property
    def first_name(self):
        """Gets the first_name of this AccountOwnerUser.  # noqa: E501


        :return: The first_name of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AccountOwnerUser.


        :param first_name: The first_name of this AccountOwnerUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this AccountOwnerUser.  # noqa: E501


        :return: The last_name of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AccountOwnerUser.


        :param last_name: The last_name of this AccountOwnerUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and last_name is None:  # noqa: E501
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def title(self):
        """Gets the title of this AccountOwnerUser.  # noqa: E501


        :return: The title of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AccountOwnerUser.


        :param title: The title of this AccountOwnerUser.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def office_phone(self):
        """Gets the office_phone of this AccountOwnerUser.  # noqa: E501


        :return: The office_phone of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._office_phone

    @office_phone.setter
    def office_phone(self, office_phone):
        """Sets the office_phone of this AccountOwnerUser.


        :param office_phone: The office_phone of this AccountOwnerUser.  # noqa: E501
        :type: str
        """

        self._office_phone = office_phone

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this AccountOwnerUser.  # noqa: E501


        :return: The mobile_phone of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this AccountOwnerUser.


        :param mobile_phone: The mobile_phone of this AccountOwnerUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mobile_phone is not None and not re.search(r'[0-9]+', mobile_phone)):  # noqa: E501
            raise ValueError(r"Invalid value for `mobile_phone`, must be a follow pattern or equal to `/[0-9]+/`")  # noqa: E501

        self._mobile_phone = mobile_phone

    @property
    def language(self):
        """Gets the language of this AccountOwnerUser.  # noqa: E501


        :return: The language of this AccountOwnerUser.  # noqa: E501
        :rtype: Languages
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AccountOwnerUser.


        :param language: The language of this AccountOwnerUser.  # noqa: E501
        :type: Languages
        """

        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this AccountOwnerUser.  # noqa: E501

        Based on tz database  # noqa: E501

        :return: The timezone of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this AccountOwnerUser.

        Based on tz database  # noqa: E501

        :param timezone: The timezone of this AccountOwnerUser.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def email(self):
        """Gets the email of this AccountOwnerUser.  # noqa: E501


        :return: The email of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountOwnerUser.


        :param email: The email of this AccountOwnerUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this AccountOwnerUser.  # noqa: E501


        :return: The password of this AccountOwnerUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AccountOwnerUser.


        :param password: The password of this AccountOwnerUser.  # noqa: E501
        :type: str
        """
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
        if not isinstance(other, AccountOwnerUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountOwnerUser):
            return True

        return self.to_dict() != other.to_dict()
