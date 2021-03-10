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


class Pagination(object):
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
        'count': 'int',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'count': 'count',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, count=None, page=1, per_page=None, local_vars_configuration=None):  # noqa: E501
        """Pagination - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def count(self):
        """Gets the count of this Pagination.  # noqa: E501


        :return: The count of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Pagination.


        :param count: The count of this Pagination.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def page(self):
        """Gets the page of this Pagination.  # noqa: E501


        :return: The page of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this Pagination.


        :param page: The page of this Pagination.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this Pagination.  # noqa: E501


        :return: The per_page of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this Pagination.


        :param per_page: The per_page of this Pagination.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

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
        if not isinstance(other, Pagination):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Pagination):
            return True

        return self.to_dict() != other.to_dict()
