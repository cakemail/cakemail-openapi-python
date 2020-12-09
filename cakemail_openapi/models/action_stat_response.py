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


class ActionStatResponse(object):
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
        'bounces': 'int',
        'bounces_address_changed': 'int',
        'bounces_challenge_response': 'int',
        'bounces_dns_failure': 'int',
        'bounces_full_mailbox': 'int',
        'bounces_hard': 'int',
        'bounces_mail_blocked': 'int',
        'bounces_soft': 'int',
        'bounces_transient': 'int',
        'unique_clicks': 'int',
        'forwards': 'int',
        'implied_opens': 'int',
        'unique_opens': 'int',
        'unopens': 'int',
        'clicks': 'int',
        'opens': 'int',
        'spams': 'int',
        'spam_rate': 'float',
        'unsubscribes': 'int',
        'sent_emails': 'int'
    }

    attribute_map = {
        'bounces': 'bounces',
        'bounces_address_changed': 'bounces_address_changed',
        'bounces_challenge_response': 'bounces_challenge_response',
        'bounces_dns_failure': 'bounces_dns_failure',
        'bounces_full_mailbox': 'bounces_full_mailbox',
        'bounces_hard': 'bounces_hard',
        'bounces_mail_blocked': 'bounces_mail_blocked',
        'bounces_soft': 'bounces_soft',
        'bounces_transient': 'bounces_transient',
        'unique_clicks': 'unique_clicks',
        'forwards': 'forwards',
        'implied_opens': 'implied_opens',
        'unique_opens': 'unique_opens',
        'unopens': 'unopens',
        'clicks': 'clicks',
        'opens': 'opens',
        'spams': 'spams',
        'spam_rate': 'spam_rate',
        'unsubscribes': 'unsubscribes',
        'sent_emails': 'sent_emails'
    }

    def __init__(self, bounces=None, bounces_address_changed=None, bounces_challenge_response=None, bounces_dns_failure=None, bounces_full_mailbox=None, bounces_hard=None, bounces_mail_blocked=None, bounces_soft=None, bounces_transient=None, unique_clicks=None, forwards=None, implied_opens=None, unique_opens=None, unopens=None, clicks=None, opens=None, spams=None, spam_rate=None, unsubscribes=None, sent_emails=None, local_vars_configuration=None):  # noqa: E501
        """ActionStatResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bounces = None
        self._bounces_address_changed = None
        self._bounces_challenge_response = None
        self._bounces_dns_failure = None
        self._bounces_full_mailbox = None
        self._bounces_hard = None
        self._bounces_mail_blocked = None
        self._bounces_soft = None
        self._bounces_transient = None
        self._unique_clicks = None
        self._forwards = None
        self._implied_opens = None
        self._unique_opens = None
        self._unopens = None
        self._clicks = None
        self._opens = None
        self._spams = None
        self._spam_rate = None
        self._unsubscribes = None
        self._sent_emails = None
        self.discriminator = None

        self.bounces = bounces
        self.bounces_address_changed = bounces_address_changed
        self.bounces_challenge_response = bounces_challenge_response
        self.bounces_dns_failure = bounces_dns_failure
        self.bounces_full_mailbox = bounces_full_mailbox
        self.bounces_hard = bounces_hard
        self.bounces_mail_blocked = bounces_mail_blocked
        self.bounces_soft = bounces_soft
        self.bounces_transient = bounces_transient
        self.unique_clicks = unique_clicks
        self.forwards = forwards
        self.implied_opens = implied_opens
        self.unique_opens = unique_opens
        self.unopens = unopens
        self.clicks = clicks
        self.opens = opens
        self.spams = spams
        self.spam_rate = spam_rate
        self.unsubscribes = unsubscribes
        self.sent_emails = sent_emails

    @property
    def bounces(self):
        """Gets the bounces of this ActionStatResponse.  # noqa: E501


        :return: The bounces of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces

    @bounces.setter
    def bounces(self, bounces):
        """Sets the bounces of this ActionStatResponse.


        :param bounces: The bounces of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces`, must not be `None`")  # noqa: E501

        self._bounces = bounces

    @property
    def bounces_address_changed(self):
        """Gets the bounces_address_changed of this ActionStatResponse.  # noqa: E501


        :return: The bounces_address_changed of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_address_changed

    @bounces_address_changed.setter
    def bounces_address_changed(self, bounces_address_changed):
        """Sets the bounces_address_changed of this ActionStatResponse.


        :param bounces_address_changed: The bounces_address_changed of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_address_changed is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_address_changed`, must not be `None`")  # noqa: E501

        self._bounces_address_changed = bounces_address_changed

    @property
    def bounces_challenge_response(self):
        """Gets the bounces_challenge_response of this ActionStatResponse.  # noqa: E501


        :return: The bounces_challenge_response of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_challenge_response

    @bounces_challenge_response.setter
    def bounces_challenge_response(self, bounces_challenge_response):
        """Sets the bounces_challenge_response of this ActionStatResponse.


        :param bounces_challenge_response: The bounces_challenge_response of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_challenge_response is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_challenge_response`, must not be `None`")  # noqa: E501

        self._bounces_challenge_response = bounces_challenge_response

    @property
    def bounces_dns_failure(self):
        """Gets the bounces_dns_failure of this ActionStatResponse.  # noqa: E501


        :return: The bounces_dns_failure of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_dns_failure

    @bounces_dns_failure.setter
    def bounces_dns_failure(self, bounces_dns_failure):
        """Sets the bounces_dns_failure of this ActionStatResponse.


        :param bounces_dns_failure: The bounces_dns_failure of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_dns_failure is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_dns_failure`, must not be `None`")  # noqa: E501

        self._bounces_dns_failure = bounces_dns_failure

    @property
    def bounces_full_mailbox(self):
        """Gets the bounces_full_mailbox of this ActionStatResponse.  # noqa: E501


        :return: The bounces_full_mailbox of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_full_mailbox

    @bounces_full_mailbox.setter
    def bounces_full_mailbox(self, bounces_full_mailbox):
        """Sets the bounces_full_mailbox of this ActionStatResponse.


        :param bounces_full_mailbox: The bounces_full_mailbox of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_full_mailbox is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_full_mailbox`, must not be `None`")  # noqa: E501

        self._bounces_full_mailbox = bounces_full_mailbox

    @property
    def bounces_hard(self):
        """Gets the bounces_hard of this ActionStatResponse.  # noqa: E501


        :return: The bounces_hard of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_hard

    @bounces_hard.setter
    def bounces_hard(self, bounces_hard):
        """Sets the bounces_hard of this ActionStatResponse.


        :param bounces_hard: The bounces_hard of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_hard is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_hard`, must not be `None`")  # noqa: E501

        self._bounces_hard = bounces_hard

    @property
    def bounces_mail_blocked(self):
        """Gets the bounces_mail_blocked of this ActionStatResponse.  # noqa: E501


        :return: The bounces_mail_blocked of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_mail_blocked

    @bounces_mail_blocked.setter
    def bounces_mail_blocked(self, bounces_mail_blocked):
        """Sets the bounces_mail_blocked of this ActionStatResponse.


        :param bounces_mail_blocked: The bounces_mail_blocked of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_mail_blocked is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_mail_blocked`, must not be `None`")  # noqa: E501

        self._bounces_mail_blocked = bounces_mail_blocked

    @property
    def bounces_soft(self):
        """Gets the bounces_soft of this ActionStatResponse.  # noqa: E501


        :return: The bounces_soft of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_soft

    @bounces_soft.setter
    def bounces_soft(self, bounces_soft):
        """Sets the bounces_soft of this ActionStatResponse.


        :param bounces_soft: The bounces_soft of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_soft is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_soft`, must not be `None`")  # noqa: E501

        self._bounces_soft = bounces_soft

    @property
    def bounces_transient(self):
        """Gets the bounces_transient of this ActionStatResponse.  # noqa: E501


        :return: The bounces_transient of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_transient

    @bounces_transient.setter
    def bounces_transient(self, bounces_transient):
        """Sets the bounces_transient of this ActionStatResponse.


        :param bounces_transient: The bounces_transient of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_transient is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_transient`, must not be `None`")  # noqa: E501

        self._bounces_transient = bounces_transient

    @property
    def unique_clicks(self):
        """Gets the unique_clicks of this ActionStatResponse.  # noqa: E501


        :return: The unique_clicks of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unique_clicks

    @unique_clicks.setter
    def unique_clicks(self, unique_clicks):
        """Sets the unique_clicks of this ActionStatResponse.


        :param unique_clicks: The unique_clicks of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unique_clicks is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_clicks`, must not be `None`")  # noqa: E501

        self._unique_clicks = unique_clicks

    @property
    def forwards(self):
        """Gets the forwards of this ActionStatResponse.  # noqa: E501


        :return: The forwards of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards):
        """Sets the forwards of this ActionStatResponse.


        :param forwards: The forwards of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and forwards is None:  # noqa: E501
            raise ValueError("Invalid value for `forwards`, must not be `None`")  # noqa: E501

        self._forwards = forwards

    @property
    def implied_opens(self):
        """Gets the implied_opens of this ActionStatResponse.  # noqa: E501


        :return: The implied_opens of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._implied_opens

    @implied_opens.setter
    def implied_opens(self, implied_opens):
        """Sets the implied_opens of this ActionStatResponse.


        :param implied_opens: The implied_opens of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and implied_opens is None:  # noqa: E501
            raise ValueError("Invalid value for `implied_opens`, must not be `None`")  # noqa: E501

        self._implied_opens = implied_opens

    @property
    def unique_opens(self):
        """Gets the unique_opens of this ActionStatResponse.  # noqa: E501


        :return: The unique_opens of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unique_opens

    @unique_opens.setter
    def unique_opens(self, unique_opens):
        """Sets the unique_opens of this ActionStatResponse.


        :param unique_opens: The unique_opens of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unique_opens is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_opens`, must not be `None`")  # noqa: E501

        self._unique_opens = unique_opens

    @property
    def unopens(self):
        """Gets the unopens of this ActionStatResponse.  # noqa: E501


        :return: The unopens of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unopens

    @unopens.setter
    def unopens(self, unopens):
        """Sets the unopens of this ActionStatResponse.


        :param unopens: The unopens of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unopens is None:  # noqa: E501
            raise ValueError("Invalid value for `unopens`, must not be `None`")  # noqa: E501

        self._unopens = unopens

    @property
    def clicks(self):
        """Gets the clicks of this ActionStatResponse.  # noqa: E501


        :return: The clicks of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this ActionStatResponse.


        :param clicks: The clicks of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and clicks is None:  # noqa: E501
            raise ValueError("Invalid value for `clicks`, must not be `None`")  # noqa: E501

        self._clicks = clicks

    @property
    def opens(self):
        """Gets the opens of this ActionStatResponse.  # noqa: E501


        :return: The opens of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this ActionStatResponse.


        :param opens: The opens of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and opens is None:  # noqa: E501
            raise ValueError("Invalid value for `opens`, must not be `None`")  # noqa: E501

        self._opens = opens

    @property
    def spams(self):
        """Gets the spams of this ActionStatResponse.  # noqa: E501


        :return: The spams of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._spams

    @spams.setter
    def spams(self, spams):
        """Sets the spams of this ActionStatResponse.


        :param spams: The spams of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and spams is None:  # noqa: E501
            raise ValueError("Invalid value for `spams`, must not be `None`")  # noqa: E501

        self._spams = spams

    @property
    def spam_rate(self):
        """Gets the spam_rate of this ActionStatResponse.  # noqa: E501


        :return: The spam_rate of this ActionStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._spam_rate

    @spam_rate.setter
    def spam_rate(self, spam_rate):
        """Sets the spam_rate of this ActionStatResponse.


        :param spam_rate: The spam_rate of this ActionStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and spam_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `spam_rate`, must not be `None`")  # noqa: E501

        self._spam_rate = spam_rate

    @property
    def unsubscribes(self):
        """Gets the unsubscribes of this ActionStatResponse.  # noqa: E501


        :return: The unsubscribes of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribes

    @unsubscribes.setter
    def unsubscribes(self, unsubscribes):
        """Sets the unsubscribes of this ActionStatResponse.


        :param unsubscribes: The unsubscribes of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unsubscribes is None:  # noqa: E501
            raise ValueError("Invalid value for `unsubscribes`, must not be `None`")  # noqa: E501

        self._unsubscribes = unsubscribes

    @property
    def sent_emails(self):
        """Gets the sent_emails of this ActionStatResponse.  # noqa: E501


        :return: The sent_emails of this ActionStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails

    @sent_emails.setter
    def sent_emails(self, sent_emails):
        """Sets the sent_emails of this ActionStatResponse.


        :param sent_emails: The sent_emails of this ActionStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_emails`, must not be `None`")  # noqa: E501

        self._sent_emails = sent_emails

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
        if not isinstance(other, ActionStatResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionStatResponse):
            return True

        return self.to_dict() != other.to_dict()
