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


class PatchWorkflow(object):
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
        'goal': 'str',
        'description': 'str',
        'trigger': 'WorkflowTrigger',
        'audience': 'WorkflowAudience',
        'blueprint': 'WorkflowFromBlueprint'
    }

    attribute_map = {
        'name': 'name',
        'goal': 'goal',
        'description': 'description',
        'trigger': 'trigger',
        'audience': 'audience',
        'blueprint': 'blueprint'
    }

    def __init__(self, name=None, goal=None, description=None, trigger=None, audience=None, blueprint=None, local_vars_configuration=None):  # noqa: E501
        """PatchWorkflow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._goal = None
        self._description = None
        self._trigger = None
        self._audience = None
        self._blueprint = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if goal is not None:
            self.goal = goal
        if description is not None:
            self.description = description
        if trigger is not None:
            self.trigger = trigger
        if audience is not None:
            self.audience = audience
        if blueprint is not None:
            self.blueprint = blueprint

    @property
    def name(self):
        """Gets the name of this PatchWorkflow.  # noqa: E501


        :return: The name of this PatchWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchWorkflow.


        :param name: The name of this PatchWorkflow.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def goal(self):
        """Gets the goal of this PatchWorkflow.  # noqa: E501


        :return: The goal of this PatchWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._goal

    @goal.setter
    def goal(self, goal):
        """Sets the goal of this PatchWorkflow.


        :param goal: The goal of this PatchWorkflow.  # noqa: E501
        :type: str
        """

        self._goal = goal

    @property
    def description(self):
        """Gets the description of this PatchWorkflow.  # noqa: E501


        :return: The description of this PatchWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatchWorkflow.


        :param description: The description of this PatchWorkflow.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def trigger(self):
        """Gets the trigger of this PatchWorkflow.  # noqa: E501


        :return: The trigger of this PatchWorkflow.  # noqa: E501
        :rtype: WorkflowTrigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this PatchWorkflow.


        :param trigger: The trigger of this PatchWorkflow.  # noqa: E501
        :type: WorkflowTrigger
        """

        self._trigger = trigger

    @property
    def audience(self):
        """Gets the audience of this PatchWorkflow.  # noqa: E501


        :return: The audience of this PatchWorkflow.  # noqa: E501
        :rtype: WorkflowAudience
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this PatchWorkflow.


        :param audience: The audience of this PatchWorkflow.  # noqa: E501
        :type: WorkflowAudience
        """

        self._audience = audience

    @property
    def blueprint(self):
        """Gets the blueprint of this PatchWorkflow.  # noqa: E501


        :return: The blueprint of this PatchWorkflow.  # noqa: E501
        :rtype: WorkflowFromBlueprint
        """
        return self._blueprint

    @blueprint.setter
    def blueprint(self, blueprint):
        """Sets the blueprint of this PatchWorkflow.


        :param blueprint: The blueprint of this PatchWorkflow.  # noqa: E501
        :type: WorkflowFromBlueprint
        """

        self._blueprint = blueprint

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
        if not isinstance(other, PatchWorkflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchWorkflow):
            return True

        return self.to_dict() != other.to_dict()
