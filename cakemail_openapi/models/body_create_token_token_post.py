# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class BodyCreateTokenTokenPost(object):
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
        'grant_type': 'PasswordGrantType',
        'username': 'str',
        'password': 'str',
        'account_id': 'int'
    }

    attribute_map = {
        'grant_type': 'grant_type',
        'username': 'username',
        'password': 'password',
        'account_id': 'account_id'
    }

    def __init__(self, grant_type=None, username=None, password=None, account_id=None, local_vars_configuration=None):  # noqa: E501
        """BodyCreateTokenTokenPost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._grant_type = None
        self._username = None
        self._password = None
        self._account_id = None
        self.discriminator = None

        if grant_type is not None:
            self.grant_type = grant_type
        self.username = username
        self.password = password
        if account_id is not None:
            self.account_id = account_id

    @property
    def grant_type(self):
        """Gets the grant_type of this BodyCreateTokenTokenPost.  # noqa: E501


        :return: The grant_type of this BodyCreateTokenTokenPost.  # noqa: E501
        :rtype: PasswordGrantType
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this BodyCreateTokenTokenPost.


        :param grant_type: The grant_type of this BodyCreateTokenTokenPost.  # noqa: E501
        :type: PasswordGrantType
        """

        self._grant_type = grant_type

    @property
    def username(self):
        """Gets the username of this BodyCreateTokenTokenPost.  # noqa: E501


        :return: The username of this BodyCreateTokenTokenPost.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this BodyCreateTokenTokenPost.


        :param username: The username of this BodyCreateTokenTokenPost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this BodyCreateTokenTokenPost.  # noqa: E501


        :return: The password of this BodyCreateTokenTokenPost.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BodyCreateTokenTokenPost.


        :param password: The password of this BodyCreateTokenTokenPost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def account_id(self):
        """Gets the account_id of this BodyCreateTokenTokenPost.  # noqa: E501


        :return: The account_id of this BodyCreateTokenTokenPost.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BodyCreateTokenTokenPost.


        :param account_id: The account_id of this BodyCreateTokenTokenPost.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

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
        if not isinstance(other, BodyCreateTokenTokenPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BodyCreateTokenTokenPost):
            return True

        return self.to_dict() != other.to_dict()
