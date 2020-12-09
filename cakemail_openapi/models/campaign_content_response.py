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


class CampaignContentResponse(object):
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
        'subject': 'str',
        'html': 'str',
        'text': 'str',
        'json': 'object',
        'type': 'ContentTypeResponse',
        'hash': 'str',
        'last_updated_on': 'int',
        'encoding': 'EncodingResponse',
        'default_unsubscribe_link': 'bool',
        'social_bar': 'bool',
        'footer': 'str'
    }

    attribute_map = {
        'subject': 'subject',
        'html': 'html',
        'text': 'text',
        'json': 'json',
        'type': 'type',
        'hash': 'hash',
        'last_updated_on': 'last_updated_on',
        'encoding': 'encoding',
        'default_unsubscribe_link': 'default_unsubscribe_link',
        'social_bar': 'social_bar',
        'footer': 'footer'
    }

    def __init__(self, subject=None, html=None, text=None, json=None, type=None, hash=None, last_updated_on=None, encoding=None, default_unsubscribe_link=None, social_bar=None, footer=None, local_vars_configuration=None):  # noqa: E501
        """CampaignContentResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subject = None
        self._html = None
        self._text = None
        self._json = None
        self._type = None
        self._hash = None
        self._last_updated_on = None
        self._encoding = None
        self._default_unsubscribe_link = None
        self._social_bar = None
        self._footer = None
        self.discriminator = None

        if subject is not None:
            self.subject = subject
        if html is not None:
            self.html = html
        if text is not None:
            self.text = text
        if json is not None:
            self.json = json
        if type is not None:
            self.type = type
        if hash is not None:
            self.hash = hash
        if last_updated_on is not None:
            self.last_updated_on = last_updated_on
        if encoding is not None:
            self.encoding = encoding
        if default_unsubscribe_link is not None:
            self.default_unsubscribe_link = default_unsubscribe_link
        if social_bar is not None:
            self.social_bar = social_bar
        if footer is not None:
            self.footer = footer

    @property
    def subject(self):
        """Gets the subject of this CampaignContentResponse.  # noqa: E501


        :return: The subject of this CampaignContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CampaignContentResponse.


        :param subject: The subject of this CampaignContentResponse.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def html(self):
        """Gets the html of this CampaignContentResponse.  # noqa: E501


        :return: The html of this CampaignContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this CampaignContentResponse.


        :param html: The html of this CampaignContentResponse.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def text(self):
        """Gets the text of this CampaignContentResponse.  # noqa: E501


        :return: The text of this CampaignContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CampaignContentResponse.


        :param text: The text of this CampaignContentResponse.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def json(self):
        """Gets the json of this CampaignContentResponse.  # noqa: E501


        :return: The json of this CampaignContentResponse.  # noqa: E501
        :rtype: object
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CampaignContentResponse.


        :param json: The json of this CampaignContentResponse.  # noqa: E501
        :type: object
        """

        self._json = json

    @property
    def type(self):
        """Gets the type of this CampaignContentResponse.  # noqa: E501


        :return: The type of this CampaignContentResponse.  # noqa: E501
        :rtype: ContentTypeResponse
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CampaignContentResponse.


        :param type: The type of this CampaignContentResponse.  # noqa: E501
        :type: ContentTypeResponse
        """

        self._type = type

    @property
    def hash(self):
        """Gets the hash of this CampaignContentResponse.  # noqa: E501


        :return: The hash of this CampaignContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this CampaignContentResponse.


        :param hash: The hash of this CampaignContentResponse.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def last_updated_on(self):
        """Gets the last_updated_on of this CampaignContentResponse.  # noqa: E501


        :return: The last_updated_on of this CampaignContentResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_on

    @last_updated_on.setter
    def last_updated_on(self, last_updated_on):
        """Sets the last_updated_on of this CampaignContentResponse.


        :param last_updated_on: The last_updated_on of this CampaignContentResponse.  # noqa: E501
        :type: int
        """

        self._last_updated_on = last_updated_on

    @property
    def encoding(self):
        """Gets the encoding of this CampaignContentResponse.  # noqa: E501


        :return: The encoding of this CampaignContentResponse.  # noqa: E501
        :rtype: EncodingResponse
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this CampaignContentResponse.


        :param encoding: The encoding of this CampaignContentResponse.  # noqa: E501
        :type: EncodingResponse
        """

        self._encoding = encoding

    @property
    def default_unsubscribe_link(self):
        """Gets the default_unsubscribe_link of this CampaignContentResponse.  # noqa: E501


        :return: The default_unsubscribe_link of this CampaignContentResponse.  # noqa: E501
        :rtype: bool
        """
        return self._default_unsubscribe_link

    @default_unsubscribe_link.setter
    def default_unsubscribe_link(self, default_unsubscribe_link):
        """Sets the default_unsubscribe_link of this CampaignContentResponse.


        :param default_unsubscribe_link: The default_unsubscribe_link of this CampaignContentResponse.  # noqa: E501
        :type: bool
        """

        self._default_unsubscribe_link = default_unsubscribe_link

    @property
    def social_bar(self):
        """Gets the social_bar of this CampaignContentResponse.  # noqa: E501


        :return: The social_bar of this CampaignContentResponse.  # noqa: E501
        :rtype: bool
        """
        return self._social_bar

    @social_bar.setter
    def social_bar(self, social_bar):
        """Sets the social_bar of this CampaignContentResponse.


        :param social_bar: The social_bar of this CampaignContentResponse.  # noqa: E501
        :type: bool
        """

        self._social_bar = social_bar

    @property
    def footer(self):
        """Gets the footer of this CampaignContentResponse.  # noqa: E501


        :return: The footer of this CampaignContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """Sets the footer of this CampaignContentResponse.


        :param footer: The footer of this CampaignContentResponse.  # noqa: E501
        :type: str
        """

        self._footer = footer

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
        if not isinstance(other, CampaignContentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignContentResponse):
            return True

        return self.to_dict() != other.to_dict()
