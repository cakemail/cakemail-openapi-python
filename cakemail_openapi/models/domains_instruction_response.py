# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class DomainsInstructionResponse(object):
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
        'bounce': 'list[DomainInstructionResponse]',
        'tracking': 'list[DomainInstructionResponse]'
    }

    attribute_map = {
        'bounce': 'bounce',
        'tracking': 'tracking'
    }

    def __init__(self, bounce=None, tracking=None, local_vars_configuration=None):  # noqa: E501
        """DomainsInstructionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bounce = None
        self._tracking = None
        self.discriminator = None

        self.bounce = bounce
        self.tracking = tracking

    @property
    def bounce(self):
        """Gets the bounce of this DomainsInstructionResponse.  # noqa: E501


        :return: The bounce of this DomainsInstructionResponse.  # noqa: E501
        :rtype: list[DomainInstructionResponse]
        """
        return self._bounce

    @bounce.setter
    def bounce(self, bounce):
        """Sets the bounce of this DomainsInstructionResponse.


        :param bounce: The bounce of this DomainsInstructionResponse.  # noqa: E501
        :type: list[DomainInstructionResponse]
        """
        if self.local_vars_configuration.client_side_validation and bounce is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce`, must not be `None`")  # noqa: E501

        self._bounce = bounce

    @property
    def tracking(self):
        """Gets the tracking of this DomainsInstructionResponse.  # noqa: E501


        :return: The tracking of this DomainsInstructionResponse.  # noqa: E501
        :rtype: list[DomainInstructionResponse]
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this DomainsInstructionResponse.


        :param tracking: The tracking of this DomainsInstructionResponse.  # noqa: E501
        :type: list[DomainInstructionResponse]
        """
        if self.local_vars_configuration.client_side_validation and tracking is None:  # noqa: E501
            raise ValueError("Invalid value for `tracking`, must not be `None`")  # noqa: E501

        self._tracking = tracking

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
        if not isinstance(other, DomainsInstructionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainsInstructionResponse):
            return True

        return self.to_dict() != other.to_dict()
