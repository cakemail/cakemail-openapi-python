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


class AcceptListPolicyResponse(object):
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
        'object': 'str',
        'policy_accepted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'object': 'object',
        'policy_accepted': 'policy_accepted'
    }

    def __init__(self, id=None, object='list', policy_accepted=True, local_vars_configuration=None):  # noqa: E501
        """AcceptListPolicyResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._object = None
        self._policy_accepted = None
        self.discriminator = None

        self.id = id
        if object is not None:
            self.object = object
        if policy_accepted is not None:
            self.policy_accepted = policy_accepted

    @property
    def id(self):
        """Gets the id of this AcceptListPolicyResponse.  # noqa: E501


        :return: The id of this AcceptListPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AcceptListPolicyResponse.


        :param id: The id of this AcceptListPolicyResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object(self):
        """Gets the object of this AcceptListPolicyResponse.  # noqa: E501


        :return: The object of this AcceptListPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this AcceptListPolicyResponse.


        :param object: The object of this AcceptListPolicyResponse.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def policy_accepted(self):
        """Gets the policy_accepted of this AcceptListPolicyResponse.  # noqa: E501


        :return: The policy_accepted of this AcceptListPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._policy_accepted

    @policy_accepted.setter
    def policy_accepted(self, policy_accepted):
        """Sets the policy_accepted of this AcceptListPolicyResponse.


        :param policy_accepted: The policy_accepted of this AcceptListPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._policy_accepted = policy_accepted

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
        if not isinstance(other, AcceptListPolicyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AcceptListPolicyResponse):
            return True

        return self.to_dict() != other.to_dict()
