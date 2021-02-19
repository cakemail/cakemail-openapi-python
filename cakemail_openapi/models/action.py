# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.4.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class Action(object):
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
        'parent_id': 'str',
        'condition': 'ActionCondition',
        'delay': 'int',
        'type': 'ActionType',
        'email_settings': 'ActionEmailSettings'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'condition': 'condition',
        'delay': 'delay',
        'type': 'type',
        'email_settings': 'email_settings'
    }

    def __init__(self, name=None, parent_id=None, condition=None, delay=None, type=None, email_settings=None, local_vars_configuration=None):  # noqa: E501
        """Action - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._parent_id = None
        self._condition = None
        self._delay = None
        self._type = None
        self._email_settings = None
        self.discriminator = None

        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        self.condition = condition
        self.delay = delay
        self.type = type
        if email_settings is not None:
            self.email_settings = email_settings

    @property
    def name(self):
        """Gets the name of this Action.  # noqa: E501


        :return: The name of this Action.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Action.


        :param name: The name of this Action.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this Action.  # noqa: E501


        :return: The parent_id of this Action.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Action.


        :param parent_id: The parent_id of this Action.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def condition(self):
        """Gets the condition of this Action.  # noqa: E501


        :return: The condition of this Action.  # noqa: E501
        :rtype: ActionCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Action.


        :param condition: The condition of this Action.  # noqa: E501
        :type: ActionCondition
        """
        if self.local_vars_configuration.client_side_validation and condition is None:  # noqa: E501
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501

        self._condition = condition

    @property
    def delay(self):
        """Gets the delay of this Action.  # noqa: E501


        :return: The delay of this Action.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this Action.


        :param delay: The delay of this Action.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and delay is None:  # noqa: E501
            raise ValueError("Invalid value for `delay`, must not be `None`")  # noqa: E501

        self._delay = delay

    @property
    def type(self):
        """Gets the type of this Action.  # noqa: E501


        :return: The type of this Action.  # noqa: E501
        :rtype: ActionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Action.


        :param type: The type of this Action.  # noqa: E501
        :type: ActionType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def email_settings(self):
        """Gets the email_settings of this Action.  # noqa: E501


        :return: The email_settings of this Action.  # noqa: E501
        :rtype: ActionEmailSettings
        """
        return self._email_settings

    @email_settings.setter
    def email_settings(self, email_settings):
        """Sets the email_settings of this Action.


        :param email_settings: The email_settings of this Action.  # noqa: E501
        :type: ActionEmailSettings
        """

        self._email_settings = email_settings

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
        if not isinstance(other, Action):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Action):
            return True

        return self.to_dict() != other.to_dict()
