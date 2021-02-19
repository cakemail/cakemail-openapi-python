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


class EncodingResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UTF_8 = "utf-8"
    ARMSCII_8 = "armscii-8"
    ASCII = "ascii"
    BIG_5 = "big-5"
    CP51932 = "cp51932"
    CP866 = "cp866"
    CP936 = "cp936"
    EUC_CN = "euc-cn"
    EUC_JP = "euc-jp"
    EUCJP_WIN = "eucjp-win"
    EUC_KR = "euc-kr"
    EUC_TW = "euc-tw"
    HZ = "hz"
    ISO_2022_JP = "iso-2022-jp"
    ISO_2022_JP_MS = "iso-2022-jp-ms"
    ISO_2022_KR = "iso-2022-kr"
    ISO_8859_1 = "iso-8859-1"
    ISO_8859_10 = "iso-8859-10"
    ISO_8859_13 = "iso-8859-13"
    ISO_8859_14 = "iso-8859-14"
    ISO_8859_15 = "iso-8859-15"
    ISO_8859_16 = "iso-8859-16"
    ISO_8859_2 = "iso-8859-2"
    ISO_8859_3 = "iso-8859-3"
    ISO_8859_4 = "iso-8859-4"
    ISO_8859_5 = "iso-8859-5"
    ISO_8859_6 = "iso-8859-6"
    ISO_8859_7 = "iso-8859-7"
    ISO_8859_8 = "iso-8859-8"
    ISO_8859_9 = "iso-8859-9"
    JIS = "jis"
    KOI8_R = "koi8-r"
    SJIS = "sjis"
    SJIS_WIN = "sjis-win"
    UHC = "uhc"
    WINDOWS_1251 = "windows-1251"
    WINDOWS_1252 = "windows-1252"
    OTHER = "other"

    allowable_values = [UTF_8, ARMSCII_8, ASCII, BIG_5, CP51932, CP866, CP936, EUC_CN, EUC_JP, EUCJP_WIN, EUC_KR, EUC_TW, HZ, ISO_2022_JP, ISO_2022_JP_MS, ISO_2022_KR, ISO_8859_1, ISO_8859_10, ISO_8859_13, ISO_8859_14, ISO_8859_15, ISO_8859_16, ISO_8859_2, ISO_8859_3, ISO_8859_4, ISO_8859_5, ISO_8859_6, ISO_8859_7, ISO_8859_8, ISO_8859_9, JIS, KOI8_R, SJIS, SJIS_WIN, UHC, WINDOWS_1251, WINDOWS_1252, OTHER]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """EncodingResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, EncodingResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncodingResponse):
            return True

        return self.to_dict() != other.to_dict()
