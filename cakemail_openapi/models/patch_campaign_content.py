# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class PatchCampaignContent(object):
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
        'template_id': 'int',
        'type': 'ContentType',
        'encoding': 'Encoding',
        'default_unsubscribe_link': 'bool'
    }

    attribute_map = {
        'subject': 'subject',
        'html': 'html',
        'text': 'text',
        'json': 'json',
        'template_id': 'template_id',
        'type': 'type',
        'encoding': 'encoding',
        'default_unsubscribe_link': 'default_unsubscribe_link'
    }

    def __init__(self, subject=None, html=None, text=None, json=None, template_id=None, type=None, encoding=None, default_unsubscribe_link=None, local_vars_configuration=None):  # noqa: E501
        """PatchCampaignContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subject = None
        self._html = None
        self._text = None
        self._json = None
        self._template_id = None
        self._type = None
        self._encoding = None
        self._default_unsubscribe_link = None
        self.discriminator = None

        if subject is not None:
            self.subject = subject
        if html is not None:
            self.html = html
        if text is not None:
            self.text = text
        if json is not None:
            self.json = json
        if template_id is not None:
            self.template_id = template_id
        if type is not None:
            self.type = type
        if encoding is not None:
            self.encoding = encoding
        if default_unsubscribe_link is not None:
            self.default_unsubscribe_link = default_unsubscribe_link

    @property
    def subject(self):
        """Gets the subject of this PatchCampaignContent.  # noqa: E501


        :return: The subject of this PatchCampaignContent.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PatchCampaignContent.


        :param subject: The subject of this PatchCampaignContent.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) < 1):
            raise ValueError("Invalid value for `subject`, length must be greater than or equal to `1`")  # noqa: E501

        self._subject = subject

    @property
    def html(self):
        """Gets the html of this PatchCampaignContent.  # noqa: E501


        :return: The html of this PatchCampaignContent.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this PatchCampaignContent.


        :param html: The html of this PatchCampaignContent.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                html is not None and len(html) < 1):
            raise ValueError("Invalid value for `html`, length must be greater than or equal to `1`")  # noqa: E501

        self._html = html

    @property
    def text(self):
        """Gets the text of this PatchCampaignContent.  # noqa: E501


        :return: The text of this PatchCampaignContent.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PatchCampaignContent.


        :param text: The text of this PatchCampaignContent.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                text is not None and len(text) < 1):
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def json(self):
        """Gets the json of this PatchCampaignContent.  # noqa: E501


        :return: The json of this PatchCampaignContent.  # noqa: E501
        :rtype: object
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this PatchCampaignContent.


        :param json: The json of this PatchCampaignContent.  # noqa: E501
        :type: object
        """

        self._json = json

    @property
    def template_id(self):
        """Gets the template_id of this PatchCampaignContent.  # noqa: E501


        :return: The template_id of this PatchCampaignContent.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this PatchCampaignContent.


        :param template_id: The template_id of this PatchCampaignContent.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                template_id is not None and template_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `template_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._template_id = template_id

    @property
    def type(self):
        """Gets the type of this PatchCampaignContent.  # noqa: E501


        :return: The type of this PatchCampaignContent.  # noqa: E501
        :rtype: ContentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PatchCampaignContent.


        :param type: The type of this PatchCampaignContent.  # noqa: E501
        :type: ContentType
        """

        self._type = type

    @property
    def encoding(self):
        """Gets the encoding of this PatchCampaignContent.  # noqa: E501


        :return: The encoding of this PatchCampaignContent.  # noqa: E501
        :rtype: Encoding
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this PatchCampaignContent.


        :param encoding: The encoding of this PatchCampaignContent.  # noqa: E501
        :type: Encoding
        """

        self._encoding = encoding

    @property
    def default_unsubscribe_link(self):
        """Gets the default_unsubscribe_link of this PatchCampaignContent.  # noqa: E501


        :return: The default_unsubscribe_link of this PatchCampaignContent.  # noqa: E501
        :rtype: bool
        """
        return self._default_unsubscribe_link

    @default_unsubscribe_link.setter
    def default_unsubscribe_link(self, default_unsubscribe_link):
        """Sets the default_unsubscribe_link of this PatchCampaignContent.


        :param default_unsubscribe_link: The default_unsubscribe_link of this PatchCampaignContent.  # noqa: E501
        :type: bool
        """

        self._default_unsubscribe_link = default_unsubscribe_link

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
        if not isinstance(other, PatchCampaignContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchCampaignContent):
            return True

        return self.to_dict() != other.to_dict()
