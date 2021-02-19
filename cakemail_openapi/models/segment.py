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


class Segment(object):
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
        'query': 'str',
        'fiql': 'str',
        'json': 'object',
        'name': 'str'
    }

    attribute_map = {
        'query': 'query',
        'fiql': 'fiql',
        'json': 'json',
        'name': 'name'
    }

    def __init__(self, query=None, fiql=None, json=None, name=None, local_vars_configuration=None):  # noqa: E501
        """Segment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._fiql = None
        self._json = None
        self._name = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if fiql is not None:
            self.fiql = fiql
        if json is not None:
            self.json = json
        self.name = name

    @property
    def query(self):
        """Gets the query of this Segment.  # noqa: E501

        SQL-like expression (use one of query, fiql and json)  # noqa: E501

        :return: The query of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Segment.

        SQL-like expression (use one of query, fiql and json)  # noqa: E501

        :param query: The query of this Segment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                query is not None and len(query) < 1):
            raise ValueError("Invalid value for `query`, length must be greater than or equal to `1`")  # noqa: E501

        self._query = query

    @property
    def fiql(self):
        """Gets the fiql of this Segment.  # noqa: E501

        FIQL expression (use one of query, fiql and json)  # noqa: E501

        :return: The fiql of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._fiql

    @fiql.setter
    def fiql(self, fiql):
        """Sets the fiql of this Segment.

        FIQL expression (use one of query, fiql and json)  # noqa: E501

        :param fiql: The fiql of this Segment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fiql is not None and len(fiql) < 1):
            raise ValueError("Invalid value for `fiql`, length must be greater than or equal to `1`")  # noqa: E501

        self._fiql = fiql

    @property
    def json(self):
        """Gets the json of this Segment.  # noqa: E501

        JSON expression (use one of query, fiql and json)  # noqa: E501

        :return: The json of this Segment.  # noqa: E501
        :rtype: object
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this Segment.

        JSON expression (use one of query, fiql and json)  # noqa: E501

        :param json: The json of this Segment.  # noqa: E501
        :type: object
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this Segment.  # noqa: E501


        :return: The name of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Segment.


        :param name: The name of this Segment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, Segment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Segment):
            return True

        return self.to_dict() != other.to_dict()
