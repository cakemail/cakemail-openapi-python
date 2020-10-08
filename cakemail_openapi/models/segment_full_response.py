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


class SegmentFullResponse(object):
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
        'name': 'str',
        'query': 'str',
        'fiql': 'str',
        'json': 'object',
        'campaigns_count': 'int',
        'last_used': 'int',
        'created_on': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'query': 'query',
        'fiql': 'fiql',
        'json': 'json',
        'campaigns_count': 'campaigns_count',
        'last_used': 'last_used',
        'created_on': 'created_on'
    }

    def __init__(self, id=None, name=None, query=None, fiql=None, json=None, campaigns_count=None, last_used=None, created_on=None, local_vars_configuration=None):  # noqa: E501
        """SegmentFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._query = None
        self._fiql = None
        self._json = None
        self._campaigns_count = None
        self._last_used = None
        self._created_on = None
        self.discriminator = None

        self.id = id
        self.name = name
        if query is not None:
            self.query = query
        if fiql is not None:
            self.fiql = fiql
        if json is not None:
            self.json = json
        self.campaigns_count = campaigns_count
        self.last_used = last_used
        self.created_on = created_on

    @property
    def id(self):
        """Gets the id of this SegmentFullResponse.  # noqa: E501

        Segment id  # noqa: E501

        :return: The id of this SegmentFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SegmentFullResponse.

        Segment id  # noqa: E501

        :param id: The id of this SegmentFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SegmentFullResponse.  # noqa: E501

        Segment name  # noqa: E501

        :return: The name of this SegmentFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SegmentFullResponse.

        Segment name  # noqa: E501

        :param name: The name of this SegmentFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def query(self):
        """Gets the query of this SegmentFullResponse.  # noqa: E501

        SQL-like expression  # noqa: E501

        :return: The query of this SegmentFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SegmentFullResponse.

        SQL-like expression  # noqa: E501

        :param query: The query of this SegmentFullResponse.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def fiql(self):
        """Gets the fiql of this SegmentFullResponse.  # noqa: E501

        FIQL expression  # noqa: E501

        :return: The fiql of this SegmentFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._fiql

    @fiql.setter
    def fiql(self, fiql):
        """Sets the fiql of this SegmentFullResponse.

        FIQL expression  # noqa: E501

        :param fiql: The fiql of this SegmentFullResponse.  # noqa: E501
        :type: str
        """

        self._fiql = fiql

    @property
    def json(self):
        """Gets the json of this SegmentFullResponse.  # noqa: E501

        JSON expression  # noqa: E501

        :return: The json of this SegmentFullResponse.  # noqa: E501
        :rtype: object
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this SegmentFullResponse.

        JSON expression  # noqa: E501

        :param json: The json of this SegmentFullResponse.  # noqa: E501
        :type: object
        """

        self._json = json

    @property
    def campaigns_count(self):
        """Gets the campaigns_count of this SegmentFullResponse.  # noqa: E501

        Number of campaigns using this Segment  # noqa: E501

        :return: The campaigns_count of this SegmentFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._campaigns_count

    @campaigns_count.setter
    def campaigns_count(self, campaigns_count):
        """Sets the campaigns_count of this SegmentFullResponse.

        Number of campaigns using this Segment  # noqa: E501

        :param campaigns_count: The campaigns_count of this SegmentFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaigns_count is None:  # noqa: E501
            raise ValueError("Invalid value for `campaigns_count`, must not be `None`")  # noqa: E501

        self._campaigns_count = campaigns_count

    @property
    def last_used(self):
        """Gets the last_used of this SegmentFullResponse.  # noqa: E501

        Last used date (Unix time)  # noqa: E501

        :return: The last_used of this SegmentFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this SegmentFullResponse.

        Last used date (Unix time)  # noqa: E501

        :param last_used: The last_used of this SegmentFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and last_used is None:  # noqa: E501
            raise ValueError("Invalid value for `last_used`, must not be `None`")  # noqa: E501

        self._last_used = last_used

    @property
    def created_on(self):
        """Gets the created_on of this SegmentFullResponse.  # noqa: E501

        Creation date (Unix time)  # noqa: E501

        :return: The created_on of this SegmentFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SegmentFullResponse.

        Creation date (Unix time)  # noqa: E501

        :param created_on: The created_on of this SegmentFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

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
        if not isinstance(other, SegmentFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SegmentFullResponse):
            return True

        return self.to_dict() != other.to_dict()
