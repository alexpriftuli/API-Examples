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

from mindbody_api.models.model_class import ModelClass  # noqa: F401,E501
from mindbody_api.models.pagination_response import PaginationResponse  # noqa: F401,E501


class GetClassesResponse(object):
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
        'pagination_response': 'PaginationResponse',
        'classes': 'list[ModelClass]'
    }

    attribute_map = {
        'pagination_response': 'PaginationResponse',
        'classes': 'Classes'
    }

    def __init__(self, pagination_response=None, classes=None):  # noqa: E501
        """GetClassesResponse - a model defined in Swagger"""  # noqa: E501

        self._pagination_response = None
        self._classes = None
        self.discriminator = None

        if pagination_response is not None:
            self.pagination_response = pagination_response
        if classes is not None:
            self.classes = classes

    @property
    def pagination_response(self):
        """Gets the pagination_response of this GetClassesResponse.  # noqa: E501

        Contains information about the pagination used.  # noqa: E501

        :return: The pagination_response of this GetClassesResponse.  # noqa: E501
        :rtype: PaginationResponse
        """
        return self._pagination_response

    @pagination_response.setter
    def pagination_response(self, pagination_response):
        """Sets the pagination_response of this GetClassesResponse.

        Contains information about the pagination used.  # noqa: E501

        :param pagination_response: The pagination_response of this GetClassesResponse.  # noqa: E501
        :type: PaginationResponse
        """

        self._pagination_response = pagination_response

    @property
    def classes(self):
        """Gets the classes of this GetClassesResponse.  # noqa: E501

        A list of the requested classes.  # noqa: E501

        :return: The classes of this GetClassesResponse.  # noqa: E501
        :rtype: list[ModelClass]
        """
        return self._classes

    @classes.setter
    def classes(self, classes):
        """Sets the classes of this GetClassesResponse.

        A list of the requested classes.  # noqa: E501

        :param classes: The classes of this GetClassesResponse.  # noqa: E501
        :type: list[ModelClass]
        """

        self._classes = classes

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
        if issubclass(GetClassesResponse, dict):
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
        if not isinstance(other, GetClassesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
