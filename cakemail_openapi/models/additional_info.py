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


class AdditionalInfo(object):
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
        'campaign_id': 'int',
        'clickthru_url': 'str',
        'raw': 'str'
    }

    attribute_map = {
        'campaign_id': 'campaign_id',
        'clickthru_url': 'clickthru_url',
        'raw': 'raw'
    }

    def __init__(self, campaign_id=None, clickthru_url=None, raw=None, local_vars_configuration=None):  # noqa: E501
        """AdditionalInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._campaign_id = None
        self._clickthru_url = None
        self._raw = None
        self.discriminator = None

        if campaign_id is not None:
            self.campaign_id = campaign_id
        if clickthru_url is not None:
            self.clickthru_url = clickthru_url
        if raw is not None:
            self.raw = raw

    @property
    def campaign_id(self):
        """Gets the campaign_id of this AdditionalInfo.  # noqa: E501


        :return: The campaign_id of this AdditionalInfo.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this AdditionalInfo.


        :param campaign_id: The campaign_id of this AdditionalInfo.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def clickthru_url(self):
        """Gets the clickthru_url of this AdditionalInfo.  # noqa: E501


        :return: The clickthru_url of this AdditionalInfo.  # noqa: E501
        :rtype: str
        """
        return self._clickthru_url

    @clickthru_url.setter
    def clickthru_url(self, clickthru_url):
        """Sets the clickthru_url of this AdditionalInfo.


        :param clickthru_url: The clickthru_url of this AdditionalInfo.  # noqa: E501
        :type: str
        """

        self._clickthru_url = clickthru_url

    @property
    def raw(self):
        """Gets the raw of this AdditionalInfo.  # noqa: E501


        :return: The raw of this AdditionalInfo.  # noqa: E501
        :rtype: str
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this AdditionalInfo.


        :param raw: The raw of this AdditionalInfo.  # noqa: E501
        :type: str
        """

        self._raw = raw

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
        if not isinstance(other, AdditionalInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalInfo):
            return True

        return self.to_dict() != other.to_dict()
