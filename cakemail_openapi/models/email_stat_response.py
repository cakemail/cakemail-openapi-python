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


class EmailStatResponse(object):
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
        'date': 'int',
        'sent_emails': 'int',
        'open_rate': 'float',
        'bounce_rate': 'float',
        'click_rate': 'float',
        'spam_rate': 'float'
    }

    attribute_map = {
        'date': 'date',
        'sent_emails': 'sent_emails',
        'open_rate': 'open_rate',
        'bounce_rate': 'bounce_rate',
        'click_rate': 'click_rate',
        'spam_rate': 'spam_rate'
    }

    def __init__(self, date=None, sent_emails=None, open_rate=None, bounce_rate=None, click_rate=None, spam_rate=None, local_vars_configuration=None):  # noqa: E501
        """EmailStatResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._sent_emails = None
        self._open_rate = None
        self._bounce_rate = None
        self._click_rate = None
        self._spam_rate = None
        self.discriminator = None

        self.date = date
        self.sent_emails = sent_emails
        self.open_rate = open_rate
        self.bounce_rate = bounce_rate
        self.click_rate = click_rate
        self.spam_rate = spam_rate

    @property
    def date(self):
        """Gets the date of this EmailStatResponse.  # noqa: E501


        :return: The date of this EmailStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EmailStatResponse.


        :param date: The date of this EmailStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def sent_emails(self):
        """Gets the sent_emails of this EmailStatResponse.  # noqa: E501


        :return: The sent_emails of this EmailStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails

    @sent_emails.setter
    def sent_emails(self, sent_emails):
        """Sets the sent_emails of this EmailStatResponse.


        :param sent_emails: The sent_emails of this EmailStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_emails`, must not be `None`")  # noqa: E501

        self._sent_emails = sent_emails

    @property
    def open_rate(self):
        """Gets the open_rate of this EmailStatResponse.  # noqa: E501


        :return: The open_rate of this EmailStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._open_rate

    @open_rate.setter
    def open_rate(self, open_rate):
        """Sets the open_rate of this EmailStatResponse.


        :param open_rate: The open_rate of this EmailStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and open_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `open_rate`, must not be `None`")  # noqa: E501

        self._open_rate = open_rate

    @property
    def bounce_rate(self):
        """Gets the bounce_rate of this EmailStatResponse.  # noqa: E501


        :return: The bounce_rate of this EmailStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._bounce_rate

    @bounce_rate.setter
    def bounce_rate(self, bounce_rate):
        """Sets the bounce_rate of this EmailStatResponse.


        :param bounce_rate: The bounce_rate of this EmailStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and bounce_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_rate`, must not be `None`")  # noqa: E501

        self._bounce_rate = bounce_rate

    @property
    def click_rate(self):
        """Gets the click_rate of this EmailStatResponse.  # noqa: E501


        :return: The click_rate of this EmailStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """Sets the click_rate of this EmailStatResponse.


        :param click_rate: The click_rate of this EmailStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and click_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `click_rate`, must not be `None`")  # noqa: E501

        self._click_rate = click_rate

    @property
    def spam_rate(self):
        """Gets the spam_rate of this EmailStatResponse.  # noqa: E501


        :return: The spam_rate of this EmailStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._spam_rate

    @spam_rate.setter
    def spam_rate(self, spam_rate):
        """Sets the spam_rate of this EmailStatResponse.


        :param spam_rate: The spam_rate of this EmailStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and spam_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `spam_rate`, must not be `None`")  # noqa: E501

        self._spam_rate = spam_rate

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
        if not isinstance(other, EmailStatResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailStatResponse):
            return True

        return self.to_dict() != other.to_dict()
