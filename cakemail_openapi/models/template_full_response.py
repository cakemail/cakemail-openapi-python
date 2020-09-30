# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class TemplateFullResponse(object):
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
        'id': 'int',
        'name': 'str',
        'updated_on': 'int',
        'content': 'TemplateContentResponse'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'updated_on': 'updated_on',
        'content': 'content'
    }

    def __init__(self, id=None, name=None, updated_on=None, content=None, local_vars_configuration=None):  # noqa: E501
        """TemplateFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._updated_on = None
        self._content = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.updated_on = updated_on
        self.content = content

    @property
    def id(self):
        """Gets the id of this TemplateFullResponse.  # noqa: E501


        :return: The id of this TemplateFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateFullResponse.


        :param id: The id of this TemplateFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TemplateFullResponse.  # noqa: E501


        :return: The name of this TemplateFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateFullResponse.


        :param name: The name of this TemplateFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def updated_on(self):
        """Gets the updated_on of this TemplateFullResponse.  # noqa: E501


        :return: The updated_on of this TemplateFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this TemplateFullResponse.


        :param updated_on: The updated_on of this TemplateFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and updated_on is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_on`, must not be `None`")  # noqa: E501

        self._updated_on = updated_on

    @property
    def content(self):
        """Gets the content of this TemplateFullResponse.  # noqa: E501


        :return: The content of this TemplateFullResponse.  # noqa: E501
        :rtype: TemplateContentResponse
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TemplateFullResponse.


        :param content: The content of this TemplateFullResponse.  # noqa: E501
        :type: TemplateContentResponse
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, TemplateFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateFullResponse):
            return True

        return self.to_dict() != other.to_dict()