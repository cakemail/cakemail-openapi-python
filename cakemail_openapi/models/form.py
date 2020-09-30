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


class Form(object):
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
        'name': 'str',
        'status': 'FormStatus',
        'content': 'FormContent',
        'redirections': 'FormRedirections',
        'list_id': 'int',
        'language': 'Languages'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'content': 'content',
        'redirections': 'redirections',
        'list_id': 'list_id',
        'language': 'language'
    }

    def __init__(self, name=None, status=None, content=None, redirections=None, list_id=None, language=None, local_vars_configuration=None):  # noqa: E501
        """Form - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._status = None
        self._content = None
        self._redirections = None
        self._list_id = None
        self._language = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if content is not None:
            self.content = content
        if redirections is not None:
            self.redirections = redirections
        if list_id is not None:
            self.list_id = list_id
        if language is not None:
            self.language = language

    @property
    def name(self):
        """Gets the name of this Form.  # noqa: E501


        :return: The name of this Form.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Form.


        :param name: The name of this Form.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Form.  # noqa: E501


        :return: The status of this Form.  # noqa: E501
        :rtype: FormStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Form.


        :param status: The status of this Form.  # noqa: E501
        :type: FormStatus
        """

        self._status = status

    @property
    def content(self):
        """Gets the content of this Form.  # noqa: E501


        :return: The content of this Form.  # noqa: E501
        :rtype: FormContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Form.


        :param content: The content of this Form.  # noqa: E501
        :type: FormContent
        """

        self._content = content

    @property
    def redirections(self):
        """Gets the redirections of this Form.  # noqa: E501


        :return: The redirections of this Form.  # noqa: E501
        :rtype: FormRedirections
        """
        return self._redirections

    @redirections.setter
    def redirections(self, redirections):
        """Sets the redirections of this Form.


        :param redirections: The redirections of this Form.  # noqa: E501
        :type: FormRedirections
        """

        self._redirections = redirections

    @property
    def list_id(self):
        """Gets the list_id of this Form.  # noqa: E501


        :return: The list_id of this Form.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this Form.


        :param list_id: The list_id of this Form.  # noqa: E501
        :type: int
        """

        self._list_id = list_id

    @property
    def language(self):
        """Gets the language of this Form.  # noqa: E501


        :return: The language of this Form.  # noqa: E501
        :rtype: Languages
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Form.


        :param language: The language of this Form.  # noqa: E501
        :type: Languages
        """

        self._language = language

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
        if not isinstance(other, Form):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Form):
            return True

        return self.to_dict() != other.to_dict()