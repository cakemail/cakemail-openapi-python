# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class PatchSelfAccount(object):
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
        'address': 'Address',
        'name': 'str',
        'account_owner': 'AccountOwner',
        'fax': 'str',
        'phone': 'str',
        'domains': 'Domains',
        'website': 'str'
    }

    attribute_map = {
        'address': 'address',
        'name': 'name',
        'account_owner': 'account_owner',
        'fax': 'fax',
        'phone': 'phone',
        'domains': 'domains',
        'website': 'website'
    }

    def __init__(self, address=None, name=None, account_owner=None, fax=None, phone=None, domains=None, website=None, local_vars_configuration=None):  # noqa: E501
        """PatchSelfAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._name = None
        self._account_owner = None
        self._fax = None
        self._phone = None
        self._domains = None
        self._website = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if name is not None:
            self.name = name
        if account_owner is not None:
            self.account_owner = account_owner
        if fax is not None:
            self.fax = fax
        if phone is not None:
            self.phone = phone
        if domains is not None:
            self.domains = domains
        if website is not None:
            self.website = website

    @property
    def address(self):
        """Gets the address of this PatchSelfAccount.  # noqa: E501


        :return: The address of this PatchSelfAccount.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PatchSelfAccount.


        :param address: The address of this PatchSelfAccount.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def name(self):
        """Gets the name of this PatchSelfAccount.  # noqa: E501


        :return: The name of this PatchSelfAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchSelfAccount.


        :param name: The name of this PatchSelfAccount.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def account_owner(self):
        """Gets the account_owner of this PatchSelfAccount.  # noqa: E501


        :return: The account_owner of this PatchSelfAccount.  # noqa: E501
        :rtype: AccountOwner
        """
        return self._account_owner

    @account_owner.setter
    def account_owner(self, account_owner):
        """Sets the account_owner of this PatchSelfAccount.


        :param account_owner: The account_owner of this PatchSelfAccount.  # noqa: E501
        :type: AccountOwner
        """

        self._account_owner = account_owner

    @property
    def fax(self):
        """Gets the fax of this PatchSelfAccount.  # noqa: E501


        :return: The fax of this PatchSelfAccount.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this PatchSelfAccount.


        :param fax: The fax of this PatchSelfAccount.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fax is not None and len(fax) < 10):
            raise ValueError("Invalid value for `fax`, length must be greater than or equal to `10`")  # noqa: E501

        self._fax = fax

    @property
    def phone(self):
        """Gets the phone of this PatchSelfAccount.  # noqa: E501


        :return: The phone of this PatchSelfAccount.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PatchSelfAccount.


        :param phone: The phone of this PatchSelfAccount.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone is not None and len(phone) < 10):
            raise ValueError("Invalid value for `phone`, length must be greater than or equal to `10`")  # noqa: E501

        self._phone = phone

    @property
    def domains(self):
        """Gets the domains of this PatchSelfAccount.  # noqa: E501


        :return: The domains of this PatchSelfAccount.  # noqa: E501
        :rtype: Domains
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this PatchSelfAccount.


        :param domains: The domains of this PatchSelfAccount.  # noqa: E501
        :type: Domains
        """

        self._domains = domains

    @property
    def website(self):
        """Gets the website of this PatchSelfAccount.  # noqa: E501


        :return: The website of this PatchSelfAccount.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this PatchSelfAccount.


        :param website: The website of this PatchSelfAccount.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                website is not None and len(website) > 2083):
            raise ValueError("Invalid value for `website`, length must be less than or equal to `2083`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                website is not None and len(website) < 1):
            raise ValueError("Invalid value for `website`, length must be greater than or equal to `1`")  # noqa: E501

        self._website = website

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
        if not isinstance(other, PatchSelfAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchSelfAccount):
            return True

        return self.to_dict() != other.to_dict()
