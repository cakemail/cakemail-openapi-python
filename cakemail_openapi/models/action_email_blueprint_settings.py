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


class ActionEmailBlueprintSettings(object):
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
        'tracking': 'ActionTracking',
        'content': 'ActionContent'
    }

    attribute_map = {
        'tracking': 'tracking',
        'content': 'content'
    }

    def __init__(self, tracking=None, content=None, local_vars_configuration=None):  # noqa: E501
        """ActionEmailBlueprintSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tracking = None
        self._content = None
        self.discriminator = None

        if tracking is not None:
            self.tracking = tracking
        self.content = content

    @property
    def tracking(self):
        """Gets the tracking of this ActionEmailBlueprintSettings.  # noqa: E501


        :return: The tracking of this ActionEmailBlueprintSettings.  # noqa: E501
        :rtype: ActionTracking
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this ActionEmailBlueprintSettings.


        :param tracking: The tracking of this ActionEmailBlueprintSettings.  # noqa: E501
        :type: ActionTracking
        """

        self._tracking = tracking

    @property
    def content(self):
        """Gets the content of this ActionEmailBlueprintSettings.  # noqa: E501


        :return: The content of this ActionEmailBlueprintSettings.  # noqa: E501
        :rtype: ActionContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ActionEmailBlueprintSettings.


        :param content: The content of this ActionEmailBlueprintSettings.  # noqa: E501
        :type: ActionContent
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
        if not isinstance(other, ActionEmailBlueprintSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionEmailBlueprintSettings):
            return True

        return self.to_dict() != other.to_dict()
