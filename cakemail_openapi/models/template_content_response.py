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


class TemplateContentResponse(object):
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
        'type': 'TemplateTypeEnum',
        'html': 'str',
        'text': 'str',
        'json': 'object'
    }

    attribute_map = {
        'type': 'type',
        'html': 'html',
        'text': 'text',
        'json': 'json'
    }

    def __init__(self, type=None, html=None, text=None, json=None, local_vars_configuration=None):  # noqa: E501
        """TemplateContentResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._html = None
        self._text = None
        self._json = None
        self.discriminator = None

        self.type = type
        if html is not None:
            self.html = html
        if text is not None:
            self.text = text
        if json is not None:
            self.json = json

    @property
    def type(self):
        """Gets the type of this TemplateContentResponse.  # noqa: E501


        :return: The type of this TemplateContentResponse.  # noqa: E501
        :rtype: TemplateTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateContentResponse.


        :param type: The type of this TemplateContentResponse.  # noqa: E501
        :type: TemplateTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def html(self):
        """Gets the html of this TemplateContentResponse.  # noqa: E501


        :return: The html of this TemplateContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this TemplateContentResponse.


        :param html: The html of this TemplateContentResponse.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def text(self):
        """Gets the text of this TemplateContentResponse.  # noqa: E501


        :return: The text of this TemplateContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TemplateContentResponse.


        :param text: The text of this TemplateContentResponse.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def json(self):
        """Gets the json of this TemplateContentResponse.  # noqa: E501


        :return: The json of this TemplateContentResponse.  # noqa: E501
        :rtype: object
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this TemplateContentResponse.


        :param json: The json of this TemplateContentResponse.  # noqa: E501
        :type: object
        """

        self._json = json

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
        if not isinstance(other, TemplateContentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateContentResponse):
            return True

        return self.to_dict() != other.to_dict()
