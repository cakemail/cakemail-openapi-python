# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.3.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class CampaignLogResponse(object):
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
        'contact_id': 'int',
        'email': 'str',
        'type': 'EventTypeResponse',
        'timestamp': 'int',
        'occurrences': 'int',
        'user_agent': 'UserInfo',
        'ip': 'str',
        'hostname': 'str',
        'additional_info': 'AdditionalInfo'
    }

    attribute_map = {
        'id': 'id',
        'contact_id': 'contact_id',
        'email': 'email',
        'type': 'type',
        'timestamp': 'timestamp',
        'occurrences': 'occurrences',
        'user_agent': 'user_agent',
        'ip': 'ip',
        'hostname': 'hostname',
        'additional_info': 'additional_info'
    }

    def __init__(self, id=None, contact_id=None, email=None, type=None, timestamp=None, occurrences=None, user_agent=None, ip=None, hostname=None, additional_info=None, local_vars_configuration=None):  # noqa: E501
        """CampaignLogResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._contact_id = None
        self._email = None
        self._type = None
        self._timestamp = None
        self._occurrences = None
        self._user_agent = None
        self._ip = None
        self._hostname = None
        self._additional_info = None
        self.discriminator = None

        self.id = id
        self.contact_id = contact_id
        if email is not None:
            self.email = email
        if type is not None:
            self.type = type
        if timestamp is not None:
            self.timestamp = timestamp
        self.occurrences = occurrences
        if user_agent is not None:
            self.user_agent = user_agent
        if ip is not None:
            self.ip = ip
        if hostname is not None:
            self.hostname = hostname
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this CampaignLogResponse.  # noqa: E501


        :return: The id of this CampaignLogResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CampaignLogResponse.


        :param id: The id of this CampaignLogResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def contact_id(self):
        """Gets the contact_id of this CampaignLogResponse.  # noqa: E501


        :return: The contact_id of this CampaignLogResponse.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this CampaignLogResponse.


        :param contact_id: The contact_id of this CampaignLogResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and contact_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_id`, must not be `None`")  # noqa: E501

        self._contact_id = contact_id

    @property
    def email(self):
        """Gets the email of this CampaignLogResponse.  # noqa: E501


        :return: The email of this CampaignLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CampaignLogResponse.


        :param email: The email of this CampaignLogResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def type(self):
        """Gets the type of this CampaignLogResponse.  # noqa: E501


        :return: The type of this CampaignLogResponse.  # noqa: E501
        :rtype: EventTypeResponse
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CampaignLogResponse.


        :param type: The type of this CampaignLogResponse.  # noqa: E501
        :type: EventTypeResponse
        """

        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this CampaignLogResponse.  # noqa: E501


        :return: The timestamp of this CampaignLogResponse.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CampaignLogResponse.


        :param timestamp: The timestamp of this CampaignLogResponse.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def occurrences(self):
        """Gets the occurrences of this CampaignLogResponse.  # noqa: E501


        :return: The occurrences of this CampaignLogResponse.  # noqa: E501
        :rtype: int
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this CampaignLogResponse.


        :param occurrences: The occurrences of this CampaignLogResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and occurrences is None:  # noqa: E501
            raise ValueError("Invalid value for `occurrences`, must not be `None`")  # noqa: E501

        self._occurrences = occurrences

    @property
    def user_agent(self):
        """Gets the user_agent of this CampaignLogResponse.  # noqa: E501


        :return: The user_agent of this CampaignLogResponse.  # noqa: E501
        :rtype: UserInfo
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this CampaignLogResponse.


        :param user_agent: The user_agent of this CampaignLogResponse.  # noqa: E501
        :type: UserInfo
        """

        self._user_agent = user_agent

    @property
    def ip(self):
        """Gets the ip of this CampaignLogResponse.  # noqa: E501


        :return: The ip of this CampaignLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CampaignLogResponse.


        :param ip: The ip of this CampaignLogResponse.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def hostname(self):
        """Gets the hostname of this CampaignLogResponse.  # noqa: E501


        :return: The hostname of this CampaignLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CampaignLogResponse.


        :param hostname: The hostname of this CampaignLogResponse.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def additional_info(self):
        """Gets the additional_info of this CampaignLogResponse.  # noqa: E501


        :return: The additional_info of this CampaignLogResponse.  # noqa: E501
        :rtype: AdditionalInfo
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CampaignLogResponse.


        :param additional_info: The additional_info of this CampaignLogResponse.  # noqa: E501
        :type: AdditionalInfo
        """

        self._additional_info = additional_info

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
        if not isinstance(other, CampaignLogResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignLogResponse):
            return True

        return self.to_dict() != other.to_dict()
