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


class UserSummaryResponse(object):
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
        'email': 'str',
        'status': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'last_activity_on': 'int',
        'created_on': 'int',
        'expires_on': 'int'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'status': 'status',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'last_activity_on': 'last_activity_on',
        'created_on': 'created_on',
        'expires_on': 'expires_on'
    }

    def __init__(self, id=None, email=None, status=None, first_name=None, last_name=None, last_activity_on=None, created_on=None, expires_on=None, local_vars_configuration=None):  # noqa: E501
        """UserSummaryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._status = None
        self._first_name = None
        self._last_name = None
        self._last_activity_on = None
        self._created_on = None
        self._expires_on = None
        self.discriminator = None

        self.id = id
        self.email = email
        if status is not None:
            self.status = status
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if last_activity_on is not None:
            self.last_activity_on = last_activity_on
        if created_on is not None:
            self.created_on = created_on
        if expires_on is not None:
            self.expires_on = expires_on

    @property
    def id(self):
        """Gets the id of this UserSummaryResponse.  # noqa: E501


        :return: The id of this UserSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSummaryResponse.


        :param id: The id of this UserSummaryResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this UserSummaryResponse.  # noqa: E501


        :return: The email of this UserSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserSummaryResponse.


        :param email: The email of this UserSummaryResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def status(self):
        """Gets the status of this UserSummaryResponse.  # noqa: E501


        :return: The status of this UserSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserSummaryResponse.


        :param status: The status of this UserSummaryResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def first_name(self):
        """Gets the first_name of this UserSummaryResponse.  # noqa: E501


        :return: The first_name of this UserSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserSummaryResponse.


        :param first_name: The first_name of this UserSummaryResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserSummaryResponse.  # noqa: E501


        :return: The last_name of this UserSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserSummaryResponse.


        :param last_name: The last_name of this UserSummaryResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def last_activity_on(self):
        """Gets the last_activity_on of this UserSummaryResponse.  # noqa: E501


        :return: The last_activity_on of this UserSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_activity_on

    @last_activity_on.setter
    def last_activity_on(self, last_activity_on):
        """Sets the last_activity_on of this UserSummaryResponse.


        :param last_activity_on: The last_activity_on of this UserSummaryResponse.  # noqa: E501
        :type: int
        """

        self._last_activity_on = last_activity_on

    @property
    def created_on(self):
        """Gets the created_on of this UserSummaryResponse.  # noqa: E501


        :return: The created_on of this UserSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this UserSummaryResponse.


        :param created_on: The created_on of this UserSummaryResponse.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def expires_on(self):
        """Gets the expires_on of this UserSummaryResponse.  # noqa: E501


        :return: The expires_on of this UserSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """Sets the expires_on of this UserSummaryResponse.


        :param expires_on: The expires_on of this UserSummaryResponse.  # noqa: E501
        :type: int
        """

        self._expires_on = expires_on

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
        if not isinstance(other, UserSummaryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSummaryResponse):
            return True

        return self.to_dict() != other.to_dict()
