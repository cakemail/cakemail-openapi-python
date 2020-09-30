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


class CreateAttributeResponse(object):
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
        'object': 'str',
        'created': 'bool',
        'data': 'CustomAttributeFullResponse'
    }

    attribute_map = {
        'name': 'name',
        'object': 'object',
        'created': 'created',
        'data': 'data'
    }

    def __init__(self, name=None, object='attribute', created=True, data=None, local_vars_configuration=None):  # noqa: E501
        """CreateAttributeResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._object = None
        self._created = None
        self._data = None
        self.discriminator = None

        self.name = name
        if object is not None:
            self.object = object
        if created is not None:
            self.created = created
        self.data = data

    @property
    def name(self):
        """Gets the name of this CreateAttributeResponse.  # noqa: E501


        :return: The name of this CreateAttributeResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAttributeResponse.


        :param name: The name of this CreateAttributeResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def object(self):
        """Gets the object of this CreateAttributeResponse.  # noqa: E501


        :return: The object of this CreateAttributeResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this CreateAttributeResponse.


        :param object: The object of this CreateAttributeResponse.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def created(self):
        """Gets the created of this CreateAttributeResponse.  # noqa: E501


        :return: The created of this CreateAttributeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreateAttributeResponse.


        :param created: The created of this CreateAttributeResponse.  # noqa: E501
        :type: bool
        """

        self._created = created

    @property
    def data(self):
        """Gets the data of this CreateAttributeResponse.  # noqa: E501


        :return: The data of this CreateAttributeResponse.  # noqa: E501
        :rtype: CustomAttributeFullResponse
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateAttributeResponse.


        :param data: The data of this CreateAttributeResponse.  # noqa: E501
        :type: CustomAttributeFullResponse
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, CreateAttributeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAttributeResponse):
            return True

        return self.to_dict() != other.to_dict()