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


class FormFullResponse(object):
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
        'name': 'str',
        'status': 'FormStatus',
        'content': 'FormContentResponse',
        'language': 'Languages',
        'created_on': 'int',
        'last_updated_on': 'int',
        'url': 'FormUrlsResponse',
        'thumbnail': 'str',
        'redirections': 'FormRedirectionsResponse',
        'list_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'content': 'content',
        'language': 'language',
        'created_on': 'created_on',
        'last_updated_on': 'last_updated_on',
        'url': 'url',
        'thumbnail': 'thumbnail',
        'redirections': 'redirections',
        'list_id': 'list_id'
    }

    def __init__(self, id=None, name=None, status=None, content=None, language=None, created_on=None, last_updated_on=None, url=None, thumbnail=None, redirections=None, list_id=None, local_vars_configuration=None):  # noqa: E501
        """FormFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._status = None
        self._content = None
        self._language = None
        self._created_on = None
        self._last_updated_on = None
        self._url = None
        self._thumbnail = None
        self._redirections = None
        self._list_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.content = content
        self.language = language
        if created_on is not None:
            self.created_on = created_on
        if last_updated_on is not None:
            self.last_updated_on = last_updated_on
        self.url = url
        if thumbnail is not None:
            self.thumbnail = thumbnail
        self.redirections = redirections
        if list_id is not None:
            self.list_id = list_id

    @property
    def id(self):
        """Gets the id of this FormFullResponse.  # noqa: E501


        :return: The id of this FormFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FormFullResponse.


        :param id: The id of this FormFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this FormFullResponse.  # noqa: E501


        :return: The name of this FormFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormFullResponse.


        :param name: The name of this FormFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this FormFullResponse.  # noqa: E501


        :return: The status of this FormFullResponse.  # noqa: E501
        :rtype: FormStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FormFullResponse.


        :param status: The status of this FormFullResponse.  # noqa: E501
        :type: FormStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def content(self):
        """Gets the content of this FormFullResponse.  # noqa: E501


        :return: The content of this FormFullResponse.  # noqa: E501
        :rtype: FormContentResponse
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this FormFullResponse.


        :param content: The content of this FormFullResponse.  # noqa: E501
        :type: FormContentResponse
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def language(self):
        """Gets the language of this FormFullResponse.  # noqa: E501


        :return: The language of this FormFullResponse.  # noqa: E501
        :rtype: Languages
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this FormFullResponse.


        :param language: The language of this FormFullResponse.  # noqa: E501
        :type: Languages
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def created_on(self):
        """Gets the created_on of this FormFullResponse.  # noqa: E501


        :return: The created_on of this FormFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this FormFullResponse.


        :param created_on: The created_on of this FormFullResponse.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_updated_on(self):
        """Gets the last_updated_on of this FormFullResponse.  # noqa: E501


        :return: The last_updated_on of this FormFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_on

    @last_updated_on.setter
    def last_updated_on(self, last_updated_on):
        """Sets the last_updated_on of this FormFullResponse.


        :param last_updated_on: The last_updated_on of this FormFullResponse.  # noqa: E501
        :type: int
        """

        self._last_updated_on = last_updated_on

    @property
    def url(self):
        """Gets the url of this FormFullResponse.  # noqa: E501


        :return: The url of this FormFullResponse.  # noqa: E501
        :rtype: FormUrlsResponse
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FormFullResponse.


        :param url: The url of this FormFullResponse.  # noqa: E501
        :type: FormUrlsResponse
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def thumbnail(self):
        """Gets the thumbnail of this FormFullResponse.  # noqa: E501


        :return: The thumbnail of this FormFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this FormFullResponse.


        :param thumbnail: The thumbnail of this FormFullResponse.  # noqa: E501
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def redirections(self):
        """Gets the redirections of this FormFullResponse.  # noqa: E501


        :return: The redirections of this FormFullResponse.  # noqa: E501
        :rtype: FormRedirectionsResponse
        """
        return self._redirections

    @redirections.setter
    def redirections(self, redirections):
        """Sets the redirections of this FormFullResponse.


        :param redirections: The redirections of this FormFullResponse.  # noqa: E501
        :type: FormRedirectionsResponse
        """
        if self.local_vars_configuration.client_side_validation and redirections is None:  # noqa: E501
            raise ValueError("Invalid value for `redirections`, must not be `None`")  # noqa: E501

        self._redirections = redirections

    @property
    def list_id(self):
        """Gets the list_id of this FormFullResponse.  # noqa: E501


        :return: The list_id of this FormFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this FormFullResponse.


        :param list_id: The list_id of this FormFullResponse.  # noqa: E501
        :type: int
        """

        self._list_id = list_id

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
        if not isinstance(other, FormFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormFullResponse):
            return True

        return self.to_dict() != other.to_dict()
