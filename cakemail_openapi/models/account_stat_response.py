# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.3.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class AccountStatResponse(object):
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
        'active_contacts': 'int',
        'sent_emails': 'int',
        'sent_campaign_emails': 'int',
        'sent_action_emails': 'int',
        'sent_email_emails': 'int',
        'open_rate': 'float',
        'bounce_rate': 'float',
        'click_rate': 'float',
        'spam_rate': 'float',
        'unsubscribe_rate': 'float',
        'emails_usage': 'float',
        'contacts_usage': 'float',
        'bounces_hard': 'int',
        'bounce_hard_rate': 'float',
        'spams': 'int',
        'current_lists': 'int'
    }

    attribute_map = {
        'active_contacts': 'active_contacts',
        'sent_emails': 'sent_emails',
        'sent_campaign_emails': 'sent_campaign_emails',
        'sent_action_emails': 'sent_action_emails',
        'sent_email_emails': 'sent_email_emails',
        'open_rate': 'open_rate',
        'bounce_rate': 'bounce_rate',
        'click_rate': 'click_rate',
        'spam_rate': 'spam_rate',
        'unsubscribe_rate': 'unsubscribe_rate',
        'emails_usage': 'emails_usage',
        'contacts_usage': 'contacts_usage',
        'bounces_hard': 'bounces_hard',
        'bounce_hard_rate': 'bounce_hard_rate',
        'spams': 'spams',
        'current_lists': 'current_lists'
    }

    def __init__(self, active_contacts=None, sent_emails=None, sent_campaign_emails=None, sent_action_emails=None, sent_email_emails=None, open_rate=None, bounce_rate=None, click_rate=None, spam_rate=None, unsubscribe_rate=None, emails_usage=None, contacts_usage=None, bounces_hard=None, bounce_hard_rate=None, spams=None, current_lists=None, local_vars_configuration=None):  # noqa: E501
        """AccountStatResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_contacts = None
        self._sent_emails = None
        self._sent_campaign_emails = None
        self._sent_action_emails = None
        self._sent_email_emails = None
        self._open_rate = None
        self._bounce_rate = None
        self._click_rate = None
        self._spam_rate = None
        self._unsubscribe_rate = None
        self._emails_usage = None
        self._contacts_usage = None
        self._bounces_hard = None
        self._bounce_hard_rate = None
        self._spams = None
        self._current_lists = None
        self.discriminator = None

        self.active_contacts = active_contacts
        self.sent_emails = sent_emails
        self.sent_campaign_emails = sent_campaign_emails
        self.sent_action_emails = sent_action_emails
        self.sent_email_emails = sent_email_emails
        self.open_rate = open_rate
        self.bounce_rate = bounce_rate
        self.click_rate = click_rate
        self.spam_rate = spam_rate
        self.unsubscribe_rate = unsubscribe_rate
        self.emails_usage = emails_usage
        self.contacts_usage = contacts_usage
        self.bounces_hard = bounces_hard
        self.bounce_hard_rate = bounce_hard_rate
        self.spams = spams
        self.current_lists = current_lists

    @property
    def active_contacts(self):
        """Gets the active_contacts of this AccountStatResponse.  # noqa: E501


        :return: The active_contacts of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._active_contacts

    @active_contacts.setter
    def active_contacts(self, active_contacts):
        """Sets the active_contacts of this AccountStatResponse.


        :param active_contacts: The active_contacts of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and active_contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `active_contacts`, must not be `None`")  # noqa: E501

        self._active_contacts = active_contacts

    @property
    def sent_emails(self):
        """Gets the sent_emails of this AccountStatResponse.  # noqa: E501


        :return: The sent_emails of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails

    @sent_emails.setter
    def sent_emails(self, sent_emails):
        """Sets the sent_emails of this AccountStatResponse.


        :param sent_emails: The sent_emails of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_emails`, must not be `None`")  # noqa: E501

        self._sent_emails = sent_emails

    @property
    def sent_campaign_emails(self):
        """Gets the sent_campaign_emails of this AccountStatResponse.  # noqa: E501


        :return: The sent_campaign_emails of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_campaign_emails

    @sent_campaign_emails.setter
    def sent_campaign_emails(self, sent_campaign_emails):
        """Sets the sent_campaign_emails of this AccountStatResponse.


        :param sent_campaign_emails: The sent_campaign_emails of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_campaign_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_campaign_emails`, must not be `None`")  # noqa: E501

        self._sent_campaign_emails = sent_campaign_emails

    @property
    def sent_action_emails(self):
        """Gets the sent_action_emails of this AccountStatResponse.  # noqa: E501


        :return: The sent_action_emails of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_action_emails

    @sent_action_emails.setter
    def sent_action_emails(self, sent_action_emails):
        """Sets the sent_action_emails of this AccountStatResponse.


        :param sent_action_emails: The sent_action_emails of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_action_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_action_emails`, must not be `None`")  # noqa: E501

        self._sent_action_emails = sent_action_emails

    @property
    def sent_email_emails(self):
        """Gets the sent_email_emails of this AccountStatResponse.  # noqa: E501


        :return: The sent_email_emails of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_email_emails

    @sent_email_emails.setter
    def sent_email_emails(self, sent_email_emails):
        """Sets the sent_email_emails of this AccountStatResponse.


        :param sent_email_emails: The sent_email_emails of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_email_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_email_emails`, must not be `None`")  # noqa: E501

        self._sent_email_emails = sent_email_emails

    @property
    def open_rate(self):
        """Gets the open_rate of this AccountStatResponse.  # noqa: E501


        :return: The open_rate of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._open_rate

    @open_rate.setter
    def open_rate(self, open_rate):
        """Sets the open_rate of this AccountStatResponse.


        :param open_rate: The open_rate of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and open_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `open_rate`, must not be `None`")  # noqa: E501

        self._open_rate = open_rate

    @property
    def bounce_rate(self):
        """Gets the bounce_rate of this AccountStatResponse.  # noqa: E501


        :return: The bounce_rate of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._bounce_rate

    @bounce_rate.setter
    def bounce_rate(self, bounce_rate):
        """Sets the bounce_rate of this AccountStatResponse.


        :param bounce_rate: The bounce_rate of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and bounce_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_rate`, must not be `None`")  # noqa: E501

        self._bounce_rate = bounce_rate

    @property
    def click_rate(self):
        """Gets the click_rate of this AccountStatResponse.  # noqa: E501


        :return: The click_rate of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """Sets the click_rate of this AccountStatResponse.


        :param click_rate: The click_rate of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and click_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `click_rate`, must not be `None`")  # noqa: E501

        self._click_rate = click_rate

    @property
    def spam_rate(self):
        """Gets the spam_rate of this AccountStatResponse.  # noqa: E501


        :return: The spam_rate of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._spam_rate

    @spam_rate.setter
    def spam_rate(self, spam_rate):
        """Sets the spam_rate of this AccountStatResponse.


        :param spam_rate: The spam_rate of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and spam_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `spam_rate`, must not be `None`")  # noqa: E501

        self._spam_rate = spam_rate

    @property
    def unsubscribe_rate(self):
        """Gets the unsubscribe_rate of this AccountStatResponse.  # noqa: E501


        :return: The unsubscribe_rate of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._unsubscribe_rate

    @unsubscribe_rate.setter
    def unsubscribe_rate(self, unsubscribe_rate):
        """Sets the unsubscribe_rate of this AccountStatResponse.


        :param unsubscribe_rate: The unsubscribe_rate of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unsubscribe_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `unsubscribe_rate`, must not be `None`")  # noqa: E501

        self._unsubscribe_rate = unsubscribe_rate

    @property
    def emails_usage(self):
        """Gets the emails_usage of this AccountStatResponse.  # noqa: E501


        :return: The emails_usage of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._emails_usage

    @emails_usage.setter
    def emails_usage(self, emails_usage):
        """Sets the emails_usage of this AccountStatResponse.


        :param emails_usage: The emails_usage of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and emails_usage is None:  # noqa: E501
            raise ValueError("Invalid value for `emails_usage`, must not be `None`")  # noqa: E501

        self._emails_usage = emails_usage

    @property
    def contacts_usage(self):
        """Gets the contacts_usage of this AccountStatResponse.  # noqa: E501


        :return: The contacts_usage of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._contacts_usage

    @contacts_usage.setter
    def contacts_usage(self, contacts_usage):
        """Sets the contacts_usage of this AccountStatResponse.


        :param contacts_usage: The contacts_usage of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and contacts_usage is None:  # noqa: E501
            raise ValueError("Invalid value for `contacts_usage`, must not be `None`")  # noqa: E501

        self._contacts_usage = contacts_usage

    @property
    def bounces_hard(self):
        """Gets the bounces_hard of this AccountStatResponse.  # noqa: E501


        :return: The bounces_hard of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_hard

    @bounces_hard.setter
    def bounces_hard(self, bounces_hard):
        """Sets the bounces_hard of this AccountStatResponse.


        :param bounces_hard: The bounces_hard of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_hard is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_hard`, must not be `None`")  # noqa: E501

        self._bounces_hard = bounces_hard

    @property
    def bounce_hard_rate(self):
        """Gets the bounce_hard_rate of this AccountStatResponse.  # noqa: E501


        :return: The bounce_hard_rate of this AccountStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._bounce_hard_rate

    @bounce_hard_rate.setter
    def bounce_hard_rate(self, bounce_hard_rate):
        """Sets the bounce_hard_rate of this AccountStatResponse.


        :param bounce_hard_rate: The bounce_hard_rate of this AccountStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and bounce_hard_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_hard_rate`, must not be `None`")  # noqa: E501

        self._bounce_hard_rate = bounce_hard_rate

    @property
    def spams(self):
        """Gets the spams of this AccountStatResponse.  # noqa: E501


        :return: The spams of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._spams

    @spams.setter
    def spams(self, spams):
        """Sets the spams of this AccountStatResponse.


        :param spams: The spams of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and spams is None:  # noqa: E501
            raise ValueError("Invalid value for `spams`, must not be `None`")  # noqa: E501

        self._spams = spams

    @property
    def current_lists(self):
        """Gets the current_lists of this AccountStatResponse.  # noqa: E501


        :return: The current_lists of this AccountStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._current_lists

    @current_lists.setter
    def current_lists(self, current_lists):
        """Sets the current_lists of this AccountStatResponse.


        :param current_lists: The current_lists of this AccountStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and current_lists is None:  # noqa: E501
            raise ValueError("Invalid value for `current_lists`, must not be `None`")  # noqa: E501

        self._current_lists = current_lists

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
        if not isinstance(other, AccountStatResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountStatResponse):
            return True

        return self.to_dict() != other.to_dict()
