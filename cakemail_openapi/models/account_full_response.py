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


class AccountFullResponse(object):
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
        'lineage': 'str',
        'status': 'AccountStatus',
        'name': 'str',
        'address': 'AddressResponse',
        'account_owner': 'AccountOwnerResponse',
        'fax': 'str',
        'phone': 'str',
        'website': 'str',
        'logo': 'str',
        'usage_limits': 'UsageLimitsResponse',
        'last_activity_on': 'int',
        'created_on': 'int',
        'partner': 'bool',
        'bypass_recaptcha': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'lineage': 'lineage',
        'status': 'status',
        'name': 'name',
        'address': 'address',
        'account_owner': 'account_owner',
        'fax': 'fax',
        'phone': 'phone',
        'website': 'website',
        'logo': 'logo',
        'usage_limits': 'usage_limits',
        'last_activity_on': 'last_activity_on',
        'created_on': 'created_on',
        'partner': 'partner',
        'bypass_recaptcha': 'bypass_recaptcha'
    }

    def __init__(self, id=None, lineage=None, status=None, name=None, address=None, account_owner=None, fax=None, phone=None, website=None, logo=None, usage_limits=None, last_activity_on=None, created_on=None, partner=None, bypass_recaptcha=None, local_vars_configuration=None):  # noqa: E501
        """AccountFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._lineage = None
        self._status = None
        self._name = None
        self._address = None
        self._account_owner = None
        self._fax = None
        self._phone = None
        self._website = None
        self._logo = None
        self._usage_limits = None
        self._last_activity_on = None
        self._created_on = None
        self._partner = None
        self._bypass_recaptcha = None
        self.discriminator = None

        self.id = id
        self.lineage = lineage
        self.status = status
        if name is not None:
            self.name = name
        self.address = address
        self.account_owner = account_owner
        if fax is not None:
            self.fax = fax
        if phone is not None:
            self.phone = phone
        if website is not None:
            self.website = website
        self.logo = logo
        self.usage_limits = usage_limits
        self.last_activity_on = last_activity_on
        self.created_on = created_on
        self.partner = partner
        self.bypass_recaptcha = bypass_recaptcha

    @property
    def id(self):
        """Gets the id of this AccountFullResponse.  # noqa: E501


        :return: The id of this AccountFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountFullResponse.


        :param id: The id of this AccountFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def lineage(self):
        """Gets the lineage of this AccountFullResponse.  # noqa: E501


        :return: The lineage of this AccountFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this AccountFullResponse.


        :param lineage: The lineage of this AccountFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and lineage is None:  # noqa: E501
            raise ValueError("Invalid value for `lineage`, must not be `None`")  # noqa: E501

        self._lineage = lineage

    @property
    def status(self):
        """Gets the status of this AccountFullResponse.  # noqa: E501


        :return: The status of this AccountFullResponse.  # noqa: E501
        :rtype: AccountStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountFullResponse.


        :param status: The status of this AccountFullResponse.  # noqa: E501
        :type: AccountStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def name(self):
        """Gets the name of this AccountFullResponse.  # noqa: E501


        :return: The name of this AccountFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountFullResponse.


        :param name: The name of this AccountFullResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this AccountFullResponse.  # noqa: E501


        :return: The address of this AccountFullResponse.  # noqa: E501
        :rtype: AddressResponse
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AccountFullResponse.


        :param address: The address of this AccountFullResponse.  # noqa: E501
        :type: AddressResponse
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def account_owner(self):
        """Gets the account_owner of this AccountFullResponse.  # noqa: E501


        :return: The account_owner of this AccountFullResponse.  # noqa: E501
        :rtype: AccountOwnerResponse
        """
        return self._account_owner

    @account_owner.setter
    def account_owner(self, account_owner):
        """Sets the account_owner of this AccountFullResponse.


        :param account_owner: The account_owner of this AccountFullResponse.  # noqa: E501
        :type: AccountOwnerResponse
        """
        if self.local_vars_configuration.client_side_validation and account_owner is None:  # noqa: E501
            raise ValueError("Invalid value for `account_owner`, must not be `None`")  # noqa: E501

        self._account_owner = account_owner

    @property
    def fax(self):
        """Gets the fax of this AccountFullResponse.  # noqa: E501


        :return: The fax of this AccountFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this AccountFullResponse.


        :param fax: The fax of this AccountFullResponse.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def phone(self):
        """Gets the phone of this AccountFullResponse.  # noqa: E501


        :return: The phone of this AccountFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AccountFullResponse.


        :param phone: The phone of this AccountFullResponse.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def website(self):
        """Gets the website of this AccountFullResponse.  # noqa: E501


        :return: The website of this AccountFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this AccountFullResponse.


        :param website: The website of this AccountFullResponse.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def logo(self):
        """Gets the logo of this AccountFullResponse.  # noqa: E501


        :return: The logo of this AccountFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this AccountFullResponse.


        :param logo: The logo of this AccountFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and logo is None:  # noqa: E501
            raise ValueError("Invalid value for `logo`, must not be `None`")  # noqa: E501

        self._logo = logo

    @property
    def usage_limits(self):
        """Gets the usage_limits of this AccountFullResponse.  # noqa: E501


        :return: The usage_limits of this AccountFullResponse.  # noqa: E501
        :rtype: UsageLimitsResponse
        """
        return self._usage_limits

    @usage_limits.setter
    def usage_limits(self, usage_limits):
        """Sets the usage_limits of this AccountFullResponse.


        :param usage_limits: The usage_limits of this AccountFullResponse.  # noqa: E501
        :type: UsageLimitsResponse
        """
        if self.local_vars_configuration.client_side_validation and usage_limits is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_limits`, must not be `None`")  # noqa: E501

        self._usage_limits = usage_limits

    @property
    def last_activity_on(self):
        """Gets the last_activity_on of this AccountFullResponse.  # noqa: E501


        :return: The last_activity_on of this AccountFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_activity_on

    @last_activity_on.setter
    def last_activity_on(self, last_activity_on):
        """Sets the last_activity_on of this AccountFullResponse.


        :param last_activity_on: The last_activity_on of this AccountFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and last_activity_on is None:  # noqa: E501
            raise ValueError("Invalid value for `last_activity_on`, must not be `None`")  # noqa: E501

        self._last_activity_on = last_activity_on

    @property
    def created_on(self):
        """Gets the created_on of this AccountFullResponse.  # noqa: E501


        :return: The created_on of this AccountFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AccountFullResponse.


        :param created_on: The created_on of this AccountFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def partner(self):
        """Gets the partner of this AccountFullResponse.  # noqa: E501


        :return: The partner of this AccountFullResponse.  # noqa: E501
        :rtype: bool
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this AccountFullResponse.


        :param partner: The partner of this AccountFullResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and partner is None:  # noqa: E501
            raise ValueError("Invalid value for `partner`, must not be `None`")  # noqa: E501

        self._partner = partner

    @property
    def bypass_recaptcha(self):
        """Gets the bypass_recaptcha of this AccountFullResponse.  # noqa: E501


        :return: The bypass_recaptcha of this AccountFullResponse.  # noqa: E501
        :rtype: bool
        """
        return self._bypass_recaptcha

    @bypass_recaptcha.setter
    def bypass_recaptcha(self, bypass_recaptcha):
        """Sets the bypass_recaptcha of this AccountFullResponse.


        :param bypass_recaptcha: The bypass_recaptcha of this AccountFullResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and bypass_recaptcha is None:  # noqa: E501
            raise ValueError("Invalid value for `bypass_recaptcha`, must not be `None`")  # noqa: E501

        self._bypass_recaptcha = bypass_recaptcha

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
        if not isinstance(other, AccountFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountFullResponse):
            return True

        return self.to_dict() != other.to_dict()
