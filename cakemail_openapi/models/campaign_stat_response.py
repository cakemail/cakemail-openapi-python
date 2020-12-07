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


class CampaignStatResponse(object):
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
        'active_emails': 'int',
        'bounces': 'int',
        'bounce_rate': 'float',
        'bounces_address_changed': 'int',
        'bounces_challenge_response': 'int',
        'bounces_dns_failure': 'int',
        'bounces_full_mailbox': 'int',
        'bounces_hard': 'int',
        'bounces_mail_blocked': 'int',
        'bounces_soft': 'int',
        'bounces_transient': 'int',
        'clicks': 'int',
        'click_rate': 'float',
        'forwards': 'int',
        'implied_opens': 'int',
        'opens': 'int',
        'open_rate': 'float',
        'spams': 'int',
        'unique_clicks': 'int',
        'unique_opens': 'int',
        'unopens': 'int',
        'unopen_rate': 'float',
        'unsubscribes': 'int',
        'unsubscribe_rate': 'float',
        'spam_rate': 'float',
        'sent_emails': 'int',
        'sent_rate': 'float'
    }

    attribute_map = {
        'active_emails': 'active_emails',
        'bounces': 'bounces',
        'bounce_rate': 'bounce_rate',
        'bounces_address_changed': 'bounces_address_changed',
        'bounces_challenge_response': 'bounces_challenge_response',
        'bounces_dns_failure': 'bounces_dns_failure',
        'bounces_full_mailbox': 'bounces_full_mailbox',
        'bounces_hard': 'bounces_hard',
        'bounces_mail_blocked': 'bounces_mail_blocked',
        'bounces_soft': 'bounces_soft',
        'bounces_transient': 'bounces_transient',
        'clicks': 'clicks',
        'click_rate': 'click_rate',
        'forwards': 'forwards',
        'implied_opens': 'implied_opens',
        'opens': 'opens',
        'open_rate': 'open_rate',
        'spams': 'spams',
        'unique_clicks': 'unique_clicks',
        'unique_opens': 'unique_opens',
        'unopens': 'unopens',
        'unopen_rate': 'unopen_rate',
        'unsubscribes': 'unsubscribes',
        'unsubscribe_rate': 'unsubscribe_rate',
        'spam_rate': 'spam_rate',
        'sent_emails': 'sent_emails',
        'sent_rate': 'sent_rate'
    }

    def __init__(self, active_emails=None, bounces=None, bounce_rate=None, bounces_address_changed=None, bounces_challenge_response=None, bounces_dns_failure=None, bounces_full_mailbox=None, bounces_hard=None, bounces_mail_blocked=None, bounces_soft=None, bounces_transient=None, clicks=None, click_rate=None, forwards=None, implied_opens=None, opens=None, open_rate=None, spams=None, unique_clicks=None, unique_opens=None, unopens=None, unopen_rate=None, unsubscribes=None, unsubscribe_rate=None, spam_rate=None, sent_emails=None, sent_rate=None, local_vars_configuration=None):  # noqa: E501
        """CampaignStatResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_emails = None
        self._bounces = None
        self._bounce_rate = None
        self._bounces_address_changed = None
        self._bounces_challenge_response = None
        self._bounces_dns_failure = None
        self._bounces_full_mailbox = None
        self._bounces_hard = None
        self._bounces_mail_blocked = None
        self._bounces_soft = None
        self._bounces_transient = None
        self._clicks = None
        self._click_rate = None
        self._forwards = None
        self._implied_opens = None
        self._opens = None
        self._open_rate = None
        self._spams = None
        self._unique_clicks = None
        self._unique_opens = None
        self._unopens = None
        self._unopen_rate = None
        self._unsubscribes = None
        self._unsubscribe_rate = None
        self._spam_rate = None
        self._sent_emails = None
        self._sent_rate = None
        self.discriminator = None

        self.active_emails = active_emails
        self.bounces = bounces
        self.bounce_rate = bounce_rate
        self.bounces_address_changed = bounces_address_changed
        self.bounces_challenge_response = bounces_challenge_response
        self.bounces_dns_failure = bounces_dns_failure
        self.bounces_full_mailbox = bounces_full_mailbox
        self.bounces_hard = bounces_hard
        self.bounces_mail_blocked = bounces_mail_blocked
        self.bounces_soft = bounces_soft
        self.bounces_transient = bounces_transient
        self.clicks = clicks
        self.click_rate = click_rate
        self.forwards = forwards
        self.implied_opens = implied_opens
        self.opens = opens
        self.open_rate = open_rate
        self.spams = spams
        self.unique_clicks = unique_clicks
        self.unique_opens = unique_opens
        self.unopens = unopens
        self.unopen_rate = unopen_rate
        self.unsubscribes = unsubscribes
        self.unsubscribe_rate = unsubscribe_rate
        self.spam_rate = spam_rate
        self.sent_emails = sent_emails
        self.sent_rate = sent_rate

    @property
    def active_emails(self):
        """Gets the active_emails of this CampaignStatResponse.  # noqa: E501


        :return: The active_emails of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._active_emails

    @active_emails.setter
    def active_emails(self, active_emails):
        """Sets the active_emails of this CampaignStatResponse.


        :param active_emails: The active_emails of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and active_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `active_emails`, must not be `None`")  # noqa: E501

        self._active_emails = active_emails

    @property
    def bounces(self):
        """Gets the bounces of this CampaignStatResponse.  # noqa: E501


        :return: The bounces of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces

    @bounces.setter
    def bounces(self, bounces):
        """Sets the bounces of this CampaignStatResponse.


        :param bounces: The bounces of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces`, must not be `None`")  # noqa: E501

        self._bounces = bounces

    @property
    def bounce_rate(self):
        """Gets the bounce_rate of this CampaignStatResponse.  # noqa: E501


        :return: The bounce_rate of this CampaignStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._bounce_rate

    @bounce_rate.setter
    def bounce_rate(self, bounce_rate):
        """Sets the bounce_rate of this CampaignStatResponse.


        :param bounce_rate: The bounce_rate of this CampaignStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and bounce_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_rate`, must not be `None`")  # noqa: E501

        self._bounce_rate = bounce_rate

    @property
    def bounces_address_changed(self):
        """Gets the bounces_address_changed of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_address_changed of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_address_changed

    @bounces_address_changed.setter
    def bounces_address_changed(self, bounces_address_changed):
        """Sets the bounces_address_changed of this CampaignStatResponse.


        :param bounces_address_changed: The bounces_address_changed of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_address_changed is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_address_changed`, must not be `None`")  # noqa: E501

        self._bounces_address_changed = bounces_address_changed

    @property
    def bounces_challenge_response(self):
        """Gets the bounces_challenge_response of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_challenge_response of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_challenge_response

    @bounces_challenge_response.setter
    def bounces_challenge_response(self, bounces_challenge_response):
        """Sets the bounces_challenge_response of this CampaignStatResponse.


        :param bounces_challenge_response: The bounces_challenge_response of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_challenge_response is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_challenge_response`, must not be `None`")  # noqa: E501

        self._bounces_challenge_response = bounces_challenge_response

    @property
    def bounces_dns_failure(self):
        """Gets the bounces_dns_failure of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_dns_failure of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_dns_failure

    @bounces_dns_failure.setter
    def bounces_dns_failure(self, bounces_dns_failure):
        """Sets the bounces_dns_failure of this CampaignStatResponse.


        :param bounces_dns_failure: The bounces_dns_failure of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_dns_failure is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_dns_failure`, must not be `None`")  # noqa: E501

        self._bounces_dns_failure = bounces_dns_failure

    @property
    def bounces_full_mailbox(self):
        """Gets the bounces_full_mailbox of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_full_mailbox of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_full_mailbox

    @bounces_full_mailbox.setter
    def bounces_full_mailbox(self, bounces_full_mailbox):
        """Sets the bounces_full_mailbox of this CampaignStatResponse.


        :param bounces_full_mailbox: The bounces_full_mailbox of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_full_mailbox is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_full_mailbox`, must not be `None`")  # noqa: E501

        self._bounces_full_mailbox = bounces_full_mailbox

    @property
    def bounces_hard(self):
        """Gets the bounces_hard of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_hard of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_hard

    @bounces_hard.setter
    def bounces_hard(self, bounces_hard):
        """Sets the bounces_hard of this CampaignStatResponse.


        :param bounces_hard: The bounces_hard of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_hard is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_hard`, must not be `None`")  # noqa: E501

        self._bounces_hard = bounces_hard

    @property
    def bounces_mail_blocked(self):
        """Gets the bounces_mail_blocked of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_mail_blocked of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_mail_blocked

    @bounces_mail_blocked.setter
    def bounces_mail_blocked(self, bounces_mail_blocked):
        """Sets the bounces_mail_blocked of this CampaignStatResponse.


        :param bounces_mail_blocked: The bounces_mail_blocked of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_mail_blocked is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_mail_blocked`, must not be `None`")  # noqa: E501

        self._bounces_mail_blocked = bounces_mail_blocked

    @property
    def bounces_soft(self):
        """Gets the bounces_soft of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_soft of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_soft

    @bounces_soft.setter
    def bounces_soft(self, bounces_soft):
        """Sets the bounces_soft of this CampaignStatResponse.


        :param bounces_soft: The bounces_soft of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_soft is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_soft`, must not be `None`")  # noqa: E501

        self._bounces_soft = bounces_soft

    @property
    def bounces_transient(self):
        """Gets the bounces_transient of this CampaignStatResponse.  # noqa: E501


        :return: The bounces_transient of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_transient

    @bounces_transient.setter
    def bounces_transient(self, bounces_transient):
        """Sets the bounces_transient of this CampaignStatResponse.


        :param bounces_transient: The bounces_transient of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_transient is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_transient`, must not be `None`")  # noqa: E501

        self._bounces_transient = bounces_transient

    @property
    def clicks(self):
        """Gets the clicks of this CampaignStatResponse.  # noqa: E501


        :return: The clicks of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this CampaignStatResponse.


        :param clicks: The clicks of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and clicks is None:  # noqa: E501
            raise ValueError("Invalid value for `clicks`, must not be `None`")  # noqa: E501

        self._clicks = clicks

    @property
    def click_rate(self):
        """Gets the click_rate of this CampaignStatResponse.  # noqa: E501


        :return: The click_rate of this CampaignStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """Sets the click_rate of this CampaignStatResponse.


        :param click_rate: The click_rate of this CampaignStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and click_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `click_rate`, must not be `None`")  # noqa: E501

        self._click_rate = click_rate

    @property
    def forwards(self):
        """Gets the forwards of this CampaignStatResponse.  # noqa: E501


        :return: The forwards of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards):
        """Sets the forwards of this CampaignStatResponse.


        :param forwards: The forwards of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and forwards is None:  # noqa: E501
            raise ValueError("Invalid value for `forwards`, must not be `None`")  # noqa: E501

        self._forwards = forwards

    @property
    def implied_opens(self):
        """Gets the implied_opens of this CampaignStatResponse.  # noqa: E501


        :return: The implied_opens of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._implied_opens

    @implied_opens.setter
    def implied_opens(self, implied_opens):
        """Sets the implied_opens of this CampaignStatResponse.


        :param implied_opens: The implied_opens of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and implied_opens is None:  # noqa: E501
            raise ValueError("Invalid value for `implied_opens`, must not be `None`")  # noqa: E501

        self._implied_opens = implied_opens

    @property
    def opens(self):
        """Gets the opens of this CampaignStatResponse.  # noqa: E501


        :return: The opens of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this CampaignStatResponse.


        :param opens: The opens of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and opens is None:  # noqa: E501
            raise ValueError("Invalid value for `opens`, must not be `None`")  # noqa: E501

        self._opens = opens

    @property
    def open_rate(self):
        """Gets the open_rate of this CampaignStatResponse.  # noqa: E501


        :return: The open_rate of this CampaignStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._open_rate

    @open_rate.setter
    def open_rate(self, open_rate):
        """Sets the open_rate of this CampaignStatResponse.


        :param open_rate: The open_rate of this CampaignStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and open_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `open_rate`, must not be `None`")  # noqa: E501

        self._open_rate = open_rate

    @property
    def spams(self):
        """Gets the spams of this CampaignStatResponse.  # noqa: E501


        :return: The spams of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._spams

    @spams.setter
    def spams(self, spams):
        """Sets the spams of this CampaignStatResponse.


        :param spams: The spams of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and spams is None:  # noqa: E501
            raise ValueError("Invalid value for `spams`, must not be `None`")  # noqa: E501

        self._spams = spams

    @property
    def unique_clicks(self):
        """Gets the unique_clicks of this CampaignStatResponse.  # noqa: E501


        :return: The unique_clicks of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unique_clicks

    @unique_clicks.setter
    def unique_clicks(self, unique_clicks):
        """Sets the unique_clicks of this CampaignStatResponse.


        :param unique_clicks: The unique_clicks of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unique_clicks is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_clicks`, must not be `None`")  # noqa: E501

        self._unique_clicks = unique_clicks

    @property
    def unique_opens(self):
        """Gets the unique_opens of this CampaignStatResponse.  # noqa: E501


        :return: The unique_opens of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unique_opens

    @unique_opens.setter
    def unique_opens(self, unique_opens):
        """Sets the unique_opens of this CampaignStatResponse.


        :param unique_opens: The unique_opens of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unique_opens is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_opens`, must not be `None`")  # noqa: E501

        self._unique_opens = unique_opens

    @property
    def unopens(self):
        """Gets the unopens of this CampaignStatResponse.  # noqa: E501


        :return: The unopens of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unopens

    @unopens.setter
    def unopens(self, unopens):
        """Sets the unopens of this CampaignStatResponse.


        :param unopens: The unopens of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unopens is None:  # noqa: E501
            raise ValueError("Invalid value for `unopens`, must not be `None`")  # noqa: E501

        self._unopens = unopens

    @property
    def unopen_rate(self):
        """Gets the unopen_rate of this CampaignStatResponse.  # noqa: E501


        :return: The unopen_rate of this CampaignStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._unopen_rate

    @unopen_rate.setter
    def unopen_rate(self, unopen_rate):
        """Sets the unopen_rate of this CampaignStatResponse.


        :param unopen_rate: The unopen_rate of this CampaignStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unopen_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `unopen_rate`, must not be `None`")  # noqa: E501

        self._unopen_rate = unopen_rate

    @property
    def unsubscribes(self):
        """Gets the unsubscribes of this CampaignStatResponse.  # noqa: E501


        :return: The unsubscribes of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribes

    @unsubscribes.setter
    def unsubscribes(self, unsubscribes):
        """Sets the unsubscribes of this CampaignStatResponse.


        :param unsubscribes: The unsubscribes of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unsubscribes is None:  # noqa: E501
            raise ValueError("Invalid value for `unsubscribes`, must not be `None`")  # noqa: E501

        self._unsubscribes = unsubscribes

    @property
    def unsubscribe_rate(self):
        """Gets the unsubscribe_rate of this CampaignStatResponse.  # noqa: E501


        :return: The unsubscribe_rate of this CampaignStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._unsubscribe_rate

    @unsubscribe_rate.setter
    def unsubscribe_rate(self, unsubscribe_rate):
        """Sets the unsubscribe_rate of this CampaignStatResponse.


        :param unsubscribe_rate: The unsubscribe_rate of this CampaignStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unsubscribe_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `unsubscribe_rate`, must not be `None`")  # noqa: E501

        self._unsubscribe_rate = unsubscribe_rate

    @property
    def spam_rate(self):
        """Gets the spam_rate of this CampaignStatResponse.  # noqa: E501


        :return: The spam_rate of this CampaignStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._spam_rate

    @spam_rate.setter
    def spam_rate(self, spam_rate):
        """Sets the spam_rate of this CampaignStatResponse.


        :param spam_rate: The spam_rate of this CampaignStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and spam_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `spam_rate`, must not be `None`")  # noqa: E501

        self._spam_rate = spam_rate

    @property
    def sent_emails(self):
        """Gets the sent_emails of this CampaignStatResponse.  # noqa: E501


        :return: The sent_emails of this CampaignStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails

    @sent_emails.setter
    def sent_emails(self, sent_emails):
        """Sets the sent_emails of this CampaignStatResponse.


        :param sent_emails: The sent_emails of this CampaignStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_emails`, must not be `None`")  # noqa: E501

        self._sent_emails = sent_emails

    @property
    def sent_rate(self):
        """Gets the sent_rate of this CampaignStatResponse.  # noqa: E501


        :return: The sent_rate of this CampaignStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._sent_rate

    @sent_rate.setter
    def sent_rate(self, sent_rate):
        """Sets the sent_rate of this CampaignStatResponse.


        :param sent_rate: The sent_rate of this CampaignStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and sent_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_rate`, must not be `None`")  # noqa: E501

        self._sent_rate = sent_rate

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
        if not isinstance(other, CampaignStatResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignStatResponse):
            return True

        return self.to_dict() != other.to_dict()
