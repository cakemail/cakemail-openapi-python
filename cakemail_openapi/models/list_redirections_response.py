# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class ListRedirectionsResponse(object):
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
        'after_opt_in': 'str',
        'after_double_opt_in': 'str',
        'after_opt_out': 'str'
    }

    attribute_map = {
        'after_opt_in': 'after_opt_in',
        'after_double_opt_in': 'after_double_opt_in',
        'after_opt_out': 'after_opt_out'
    }

    def __init__(self, after_opt_in=None, after_double_opt_in=None, after_opt_out=None, local_vars_configuration=None):  # noqa: E501
        """ListRedirectionsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._after_opt_in = None
        self._after_double_opt_in = None
        self._after_opt_out = None
        self.discriminator = None

        if after_opt_in is not None:
            self.after_opt_in = after_opt_in
        if after_double_opt_in is not None:
            self.after_double_opt_in = after_double_opt_in
        if after_opt_out is not None:
            self.after_opt_out = after_opt_out

    @property
    def after_opt_in(self):
        """Gets the after_opt_in of this ListRedirectionsResponse.  # noqa: E501


        :return: The after_opt_in of this ListRedirectionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._after_opt_in

    @after_opt_in.setter
    def after_opt_in(self, after_opt_in):
        """Sets the after_opt_in of this ListRedirectionsResponse.


        :param after_opt_in: The after_opt_in of this ListRedirectionsResponse.  # noqa: E501
        :type: str
        """

        self._after_opt_in = after_opt_in

    @property
    def after_double_opt_in(self):
        """Gets the after_double_opt_in of this ListRedirectionsResponse.  # noqa: E501


        :return: The after_double_opt_in of this ListRedirectionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._after_double_opt_in

    @after_double_opt_in.setter
    def after_double_opt_in(self, after_double_opt_in):
        """Sets the after_double_opt_in of this ListRedirectionsResponse.


        :param after_double_opt_in: The after_double_opt_in of this ListRedirectionsResponse.  # noqa: E501
        :type: str
        """

        self._after_double_opt_in = after_double_opt_in

    @property
    def after_opt_out(self):
        """Gets the after_opt_out of this ListRedirectionsResponse.  # noqa: E501


        :return: The after_opt_out of this ListRedirectionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._after_opt_out

    @after_opt_out.setter
    def after_opt_out(self, after_opt_out):
        """Sets the after_opt_out of this ListRedirectionsResponse.


        :param after_opt_out: The after_opt_out of this ListRedirectionsResponse.  # noqa: E501
        :type: str
        """

        self._after_opt_out = after_opt_out

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
        if not isinstance(other, ListRedirectionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListRedirectionsResponse):
            return True

        return self.to_dict() != other.to_dict()
