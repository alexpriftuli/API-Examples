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

from mindbody_api.models.client_index_value import ClientIndexValue  # noqa: F401,E501


class ClientIndex(object):
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
        'id': 'int',
        'name': 'str',
        'required_business_mode': 'bool',
        'required_consumer_mode': 'bool',
        'values': 'list[ClientIndexValue]',
        'action': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'required_business_mode': 'RequiredBusinessMode',
        'required_consumer_mode': 'RequiredConsumerMode',
        'values': 'Values',
        'action': 'Action'
    }

    def __init__(self, id=None, name=None, required_business_mode=None, required_consumer_mode=None, values=None, action=None):  # noqa: E501
        """ClientIndex - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._required_business_mode = None
        self._required_consumer_mode = None
        self._values = None
        self._action = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if required_business_mode is not None:
            self.required_business_mode = required_business_mode
        if required_consumer_mode is not None:
            self.required_consumer_mode = required_consumer_mode
        if values is not None:
            self.values = values
        if action is not None:
            self.action = action

    @property
    def id(self):
        """Gets the id of this ClientIndex.  # noqa: E501

        The unique ID of the client index.  # noqa: E501

        :return: The id of this ClientIndex.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientIndex.

        The unique ID of the client index.  # noqa: E501

        :param id: The id of this ClientIndex.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClientIndex.  # noqa: E501

        The name of the client index.  # noqa: E501

        :return: The name of this ClientIndex.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientIndex.

        The name of the client index.  # noqa: E501

        :param name: The name of this ClientIndex.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required_business_mode(self):
        """Gets the required_business_mode of this ClientIndex.  # noqa: E501

        When `true`, indicates that the index is required when creating profiles in business mode.  # noqa: E501

        :return: The required_business_mode of this ClientIndex.  # noqa: E501
        :rtype: bool
        """
        return self._required_business_mode

    @required_business_mode.setter
    def required_business_mode(self, required_business_mode):
        """Sets the required_business_mode of this ClientIndex.

        When `true`, indicates that the index is required when creating profiles in business mode.  # noqa: E501

        :param required_business_mode: The required_business_mode of this ClientIndex.  # noqa: E501
        :type: bool
        """

        self._required_business_mode = required_business_mode

    @property
    def required_consumer_mode(self):
        """Gets the required_consumer_mode of this ClientIndex.  # noqa: E501

        When `true`, indicates that the index is required when creating profiles in consumer mode.  # noqa: E501

        :return: The required_consumer_mode of this ClientIndex.  # noqa: E501
        :rtype: bool
        """
        return self._required_consumer_mode

    @required_consumer_mode.setter
    def required_consumer_mode(self, required_consumer_mode):
        """Sets the required_consumer_mode of this ClientIndex.

        When `true`, indicates that the index is required when creating profiles in consumer mode.  # noqa: E501

        :param required_consumer_mode: The required_consumer_mode of this ClientIndex.  # noqa: E501
        :type: bool
        """

        self._required_consumer_mode = required_consumer_mode

    @property
    def values(self):
        """Gets the values of this ClientIndex.  # noqa: E501

        Contains information about the index's possible values.  # noqa: E501

        :return: The values of this ClientIndex.  # noqa: E501
        :rtype: list[ClientIndexValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ClientIndex.

        Contains information about the index's possible values.  # noqa: E501

        :param values: The values of this ClientIndex.  # noqa: E501
        :type: list[ClientIndexValue]
        """

        self._values = values

    @property
    def action(self):
        """Gets the action of this ClientIndex.  # noqa: E501

        The action performed on this object.  # noqa: E501

        :return: The action of this ClientIndex.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ClientIndex.

        The action performed on this object.  # noqa: E501

        :param action: The action of this ClientIndex.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Added", "Updated", "Failed", "Removed"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

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
        if issubclass(ClientIndex, dict):
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
        if not isinstance(other, ClientIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
