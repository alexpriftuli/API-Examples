# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mindbody_api.models.client import Client  # noqa: F401,E501


class UpdateClientResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client': 'Client'
    }

    attribute_map = {
        'client': 'Client'
    }

    def __init__(self, client=None):  # noqa: E501
        """UpdateClientResponse - a model defined in Swagger"""  # noqa: E501

        self._client = None
        self.discriminator = None

        if client is not None:
            self.client = client

    @property
    def client(self):
        """Gets the client of this UpdateClientResponse.  # noqa: E501

        Contains information about the updated client.  # noqa: E501

        :return: The client of this UpdateClientResponse.  # noqa: E501
        :rtype: Client
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this UpdateClientResponse.

        Contains information about the updated client.  # noqa: E501

        :param client: The client of this UpdateClientResponse.  # noqa: E501
        :type: Client
        """

        self._client = client

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UpdateClientResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateClientResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
