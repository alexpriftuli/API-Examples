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


class GetClientsRequest(object):
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
        'client_i_ds': 'list[str]',
        'search_text': 'str',
        'is_prospect': 'bool',
        'last_modified_date': 'datetime',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'client_i_ds': 'ClientIDs',
        'search_text': 'SearchText',
        'is_prospect': 'IsProspect',
        'last_modified_date': 'LastModifiedDate',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, client_i_ds=None, search_text=None, is_prospect=None, last_modified_date=None, limit=None, offset=None):  # noqa: E501
        """GetClientsRequest - a model defined in Swagger"""  # noqa: E501

        self._client_i_ds = None
        self._search_text = None
        self._is_prospect = None
        self._last_modified_date = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if client_i_ds is not None:
            self.client_i_ds = client_i_ds
        if search_text is not None:
            self.search_text = search_text
        if is_prospect is not None:
            self.is_prospect = is_prospect
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def client_i_ds(self):
        """Gets the client_i_ds of this GetClientsRequest.  # noqa: E501

        The requested client IDs.  Default: **all IDs** that the authenticated user’s access level allows.  # noqa: E501

        :return: The client_i_ds of this GetClientsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_i_ds

    @client_i_ds.setter
    def client_i_ds(self, client_i_ds):
        """Sets the client_i_ds of this GetClientsRequest.

        The requested client IDs.  Default: **all IDs** that the authenticated user’s access level allows.  # noqa: E501

        :param client_i_ds: The client_i_ds of this GetClientsRequest.  # noqa: E501
        :type: list[str]
        """

        self._client_i_ds = client_i_ds

    @property
    def search_text(self):
        """Gets the search_text of this GetClientsRequest.  # noqa: E501

        Text to use in the search. Can include FirstName, LastName, and Email. Note that user credentials must be provided.  # noqa: E501

        :return: The search_text of this GetClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this GetClientsRequest.

        Text to use in the search. Can include FirstName, LastName, and Email. Note that user credentials must be provided.  # noqa: E501

        :param search_text: The search_text of this GetClientsRequest.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def is_prospect(self):
        """Gets the is_prospect of this GetClientsRequest.  # noqa: E501

        When `true`, filters the results to include only those clients marked as prospects for the business.<br />  When `false`, indicates that only those clients who are not marked prospects should be returned.  # noqa: E501

        :return: The is_prospect of this GetClientsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_prospect

    @is_prospect.setter
    def is_prospect(self, is_prospect):
        """Sets the is_prospect of this GetClientsRequest.

        When `true`, filters the results to include only those clients marked as prospects for the business.<br />  When `false`, indicates that only those clients who are not marked prospects should be returned.  # noqa: E501

        :param is_prospect: The is_prospect of this GetClientsRequest.  # noqa: E501
        :type: bool
        """

        self._is_prospect = is_prospect

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this GetClientsRequest.  # noqa: E501

        Filters the results to include only the clients that have been modified on or after this date.  # noqa: E501

        :return: The last_modified_date of this GetClientsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this GetClientsRequest.

        Filters the results to include only the clients that have been modified on or after this date.  # noqa: E501

        :param last_modified_date: The last_modified_date of this GetClientsRequest.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def limit(self):
        """Gets the limit of this GetClientsRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetClientsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetClientsRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetClientsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetClientsRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetClientsRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetClientsRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetClientsRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

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
        if issubclass(GetClientsRequest, dict):
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
        if not isinstance(other, GetClientsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other