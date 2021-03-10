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


class ListStatResponse(object):
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
        'pending_contacts': 'int',
        'invalid_contacts': 'int',
        'unsubscribed_contacts': 'int',
        'flagged_contacts': 'int',
        'deleted_contacts': 'int',
        'sent_emails': 'int',
        'open_rate': 'float',
        'bounce_rate': 'float',
        'click_rate': 'float',
        'unsubscribe_rate': 'float',
        'spam_rate': 'float'
    }

    attribute_map = {
        'active_contacts': 'active_contacts',
        'pending_contacts': 'pending_contacts',
        'invalid_contacts': 'invalid_contacts',
        'unsubscribed_contacts': 'unsubscribed_contacts',
        'flagged_contacts': 'flagged_contacts',
        'deleted_contacts': 'deleted_contacts',
        'sent_emails': 'sent_emails',
        'open_rate': 'open_rate',
        'bounce_rate': 'bounce_rate',
        'click_rate': 'click_rate',
        'unsubscribe_rate': 'unsubscribe_rate',
        'spam_rate': 'spam_rate'
    }

    def __init__(self, active_contacts=None, pending_contacts=None, invalid_contacts=None, unsubscribed_contacts=None, flagged_contacts=None, deleted_contacts=None, sent_emails=None, open_rate=None, bounce_rate=None, click_rate=None, unsubscribe_rate=None, spam_rate=None, local_vars_configuration=None):  # noqa: E501
        """ListStatResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_contacts = None
        self._pending_contacts = None
        self._invalid_contacts = None
        self._unsubscribed_contacts = None
        self._flagged_contacts = None
        self._deleted_contacts = None
        self._sent_emails = None
        self._open_rate = None
        self._bounce_rate = None
        self._click_rate = None
        self._unsubscribe_rate = None
        self._spam_rate = None
        self.discriminator = None

        self.active_contacts = active_contacts
        self.pending_contacts = pending_contacts
        self.invalid_contacts = invalid_contacts
        self.unsubscribed_contacts = unsubscribed_contacts
        self.flagged_contacts = flagged_contacts
        self.deleted_contacts = deleted_contacts
        self.sent_emails = sent_emails
        self.open_rate = open_rate
        self.bounce_rate = bounce_rate
        self.click_rate = click_rate
        self.unsubscribe_rate = unsubscribe_rate
        self.spam_rate = spam_rate

    @property
    def active_contacts(self):
        """Gets the active_contacts of this ListStatResponse.  # noqa: E501


        :return: The active_contacts of this ListStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._active_contacts

    @active_contacts.setter
    def active_contacts(self, active_contacts):
        """Sets the active_contacts of this ListStatResponse.


        :param active_contacts: The active_contacts of this ListStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and active_contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `active_contacts`, must not be `None`")  # noqa: E501

        self._active_contacts = active_contacts

    @property
    def pending_contacts(self):
        """Gets the pending_contacts of this ListStatResponse.  # noqa: E501


        :return: The pending_contacts of this ListStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._pending_contacts

    @pending_contacts.setter
    def pending_contacts(self, pending_contacts):
        """Sets the pending_contacts of this ListStatResponse.


        :param pending_contacts: The pending_contacts of this ListStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pending_contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `pending_contacts`, must not be `None`")  # noqa: E501

        self._pending_contacts = pending_contacts

    @property
    def invalid_contacts(self):
        """Gets the invalid_contacts of this ListStatResponse.  # noqa: E501


        :return: The invalid_contacts of this ListStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._invalid_contacts

    @invalid_contacts.setter
    def invalid_contacts(self, invalid_contacts):
        """Sets the invalid_contacts of this ListStatResponse.


        :param invalid_contacts: The invalid_contacts of this ListStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and invalid_contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `invalid_contacts`, must not be `None`")  # noqa: E501

        self._invalid_contacts = invalid_contacts

    @property
    def unsubscribed_contacts(self):
        """Gets the unsubscribed_contacts of this ListStatResponse.  # noqa: E501


        :return: The unsubscribed_contacts of this ListStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribed_contacts

    @unsubscribed_contacts.setter
    def unsubscribed_contacts(self, unsubscribed_contacts):
        """Sets the unsubscribed_contacts of this ListStatResponse.


        :param unsubscribed_contacts: The unsubscribed_contacts of this ListStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and unsubscribed_contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `unsubscribed_contacts`, must not be `None`")  # noqa: E501

        self._unsubscribed_contacts = unsubscribed_contacts

    @property
    def flagged_contacts(self):
        """Gets the flagged_contacts of this ListStatResponse.  # noqa: E501


        :return: The flagged_contacts of this ListStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._flagged_contacts

    @flagged_contacts.setter
    def flagged_contacts(self, flagged_contacts):
        """Sets the flagged_contacts of this ListStatResponse.


        :param flagged_contacts: The flagged_contacts of this ListStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and flagged_contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `flagged_contacts`, must not be `None`")  # noqa: E501

        self._flagged_contacts = flagged_contacts

    @property
    def deleted_contacts(self):
        """Gets the deleted_contacts of this ListStatResponse.  # noqa: E501


        :return: The deleted_contacts of this ListStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._deleted_contacts

    @deleted_contacts.setter
    def deleted_contacts(self, deleted_contacts):
        """Sets the deleted_contacts of this ListStatResponse.


        :param deleted_contacts: The deleted_contacts of this ListStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and deleted_contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_contacts`, must not be `None`")  # noqa: E501

        self._deleted_contacts = deleted_contacts

    @property
    def sent_emails(self):
        """Gets the sent_emails of this ListStatResponse.  # noqa: E501


        :return: The sent_emails of this ListStatResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_emails

    @sent_emails.setter
    def sent_emails(self, sent_emails):
        """Sets the sent_emails of this ListStatResponse.


        :param sent_emails: The sent_emails of this ListStatResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_emails is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_emails`, must not be `None`")  # noqa: E501

        self._sent_emails = sent_emails

    @property
    def open_rate(self):
        """Gets the open_rate of this ListStatResponse.  # noqa: E501


        :return: The open_rate of this ListStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._open_rate

    @open_rate.setter
    def open_rate(self, open_rate):
        """Sets the open_rate of this ListStatResponse.


        :param open_rate: The open_rate of this ListStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and open_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `open_rate`, must not be `None`")  # noqa: E501

        self._open_rate = open_rate

    @property
    def bounce_rate(self):
        """Gets the bounce_rate of this ListStatResponse.  # noqa: E501


        :return: The bounce_rate of this ListStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._bounce_rate

    @bounce_rate.setter
    def bounce_rate(self, bounce_rate):
        """Sets the bounce_rate of this ListStatResponse.


        :param bounce_rate: The bounce_rate of this ListStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and bounce_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_rate`, must not be `None`")  # noqa: E501

        self._bounce_rate = bounce_rate

    @property
    def click_rate(self):
        """Gets the click_rate of this ListStatResponse.  # noqa: E501


        :return: The click_rate of this ListStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """Sets the click_rate of this ListStatResponse.


        :param click_rate: The click_rate of this ListStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and click_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `click_rate`, must not be `None`")  # noqa: E501

        self._click_rate = click_rate

    @property
    def unsubscribe_rate(self):
        """Gets the unsubscribe_rate of this ListStatResponse.  # noqa: E501


        :return: The unsubscribe_rate of this ListStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._unsubscribe_rate

    @unsubscribe_rate.setter
    def unsubscribe_rate(self, unsubscribe_rate):
        """Sets the unsubscribe_rate of this ListStatResponse.


        :param unsubscribe_rate: The unsubscribe_rate of this ListStatResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unsubscribe_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `unsubscribe_rate`, must not be `None`")  # noqa: E501

        self._unsubscribe_rate = unsubscribe_rate

    @property
    def spam_rate(self):
        """Gets the spam_rate of this ListStatResponse.  # noqa: E501


        :return: The spam_rate of this ListStatResponse.  # noqa: E501
        :rtype: float
        """
        return self._spam_rate

    @spam_rate.setter
    def spam_rate(self, spam_rate):
        """Sets the spam_rate of this ListStatResponse.


        :param spam_rate: The spam_rate of this ListStatResponse.  # noqa: E501
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
        if not isinstance(other, ListStatResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListStatResponse):
            return True

        return self.to_dict() != other.to_dict()
