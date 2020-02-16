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

from mindbody_api.models.amenity import Amenity  # noqa: F401,E501


class Location(object):
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
        'additional_image_ur_ls': 'list[str]',
        'address': 'str',
        'address2': 'str',
        'amenities': 'list[Amenity]',
        'business_description': 'str',
        'city': 'str',
        'description': 'str',
        'has_classes': 'bool',
        'id': 'int',
        'latitude': 'float',
        'longitude': 'float',
        'name': 'str',
        'phone': 'str',
        'phone_extension': 'str',
        'postal_code': 'str',
        'site_id': 'int',
        'state_prov_code': 'str',
        'tax1': 'float',
        'tax2': 'float',
        'tax3': 'float',
        'tax4': 'float',
        'tax5': 'float',
        'total_number_of_ratings': 'int',
        'average_rating': 'float',
        'total_number_of_deals': 'int'
    }

    attribute_map = {
        'additional_image_ur_ls': 'AdditionalImageURLs',
        'address': 'Address',
        'address2': 'Address2',
        'amenities': 'Amenities',
        'business_description': 'BusinessDescription',
        'city': 'City',
        'description': 'Description',
        'has_classes': 'HasClasses',
        'id': 'Id',
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'name': 'Name',
        'phone': 'Phone',
        'phone_extension': 'PhoneExtension',
        'postal_code': 'PostalCode',
        'site_id': 'SiteID',
        'state_prov_code': 'StateProvCode',
        'tax1': 'Tax1',
        'tax2': 'Tax2',
        'tax3': 'Tax3',
        'tax4': 'Tax4',
        'tax5': 'Tax5',
        'total_number_of_ratings': 'TotalNumberOfRatings',
        'average_rating': 'AverageRating',
        'total_number_of_deals': 'TotalNumberOfDeals'
    }

    def __init__(self, additional_image_ur_ls=None, address=None, address2=None, amenities=None, business_description=None, city=None, description=None, has_classes=None, id=None, latitude=None, longitude=None, name=None, phone=None, phone_extension=None, postal_code=None, site_id=None, state_prov_code=None, tax1=None, tax2=None, tax3=None, tax4=None, tax5=None, total_number_of_ratings=None, average_rating=None, total_number_of_deals=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501

        self._additional_image_ur_ls = None
        self._address = None
        self._address2 = None
        self._amenities = None
        self._business_description = None
        self._city = None
        self._description = None
        self._has_classes = None
        self._id = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._phone = None
        self._phone_extension = None
        self._postal_code = None
        self._site_id = None
        self._state_prov_code = None
        self._tax1 = None
        self._tax2 = None
        self._tax3 = None
        self._tax4 = None
        self._tax5 = None
        self._total_number_of_ratings = None
        self._average_rating = None
        self._total_number_of_deals = None
        self.discriminator = None

        if additional_image_ur_ls is not None:
            self.additional_image_ur_ls = additional_image_ur_ls
        if address is not None:
            self.address = address
        if address2 is not None:
            self.address2 = address2
        if amenities is not None:
            self.amenities = amenities
        if business_description is not None:
            self.business_description = business_description
        if city is not None:
            self.city = city
        if description is not None:
            self.description = description
        if has_classes is not None:
            self.has_classes = has_classes
        if id is not None:
            self.id = id
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if phone_extension is not None:
            self.phone_extension = phone_extension
        if postal_code is not None:
            self.postal_code = postal_code
        if site_id is not None:
            self.site_id = site_id
        if state_prov_code is not None:
            self.state_prov_code = state_prov_code
        if tax1 is not None:
            self.tax1 = tax1
        if tax2 is not None:
            self.tax2 = tax2
        if tax3 is not None:
            self.tax3 = tax3
        if tax4 is not None:
            self.tax4 = tax4
        if tax5 is not None:
            self.tax5 = tax5
        if total_number_of_ratings is not None:
            self.total_number_of_ratings = total_number_of_ratings
        if average_rating is not None:
            self.average_rating = average_rating
        if total_number_of_deals is not None:
            self.total_number_of_deals = total_number_of_deals

    @property
    def additional_image_ur_ls(self):
        """Gets the additional_image_ur_ls of this Location.  # noqa: E501

        A list of URLs of any images associated with this location.  # noqa: E501

        :return: The additional_image_ur_ls of this Location.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_image_ur_ls

    @additional_image_ur_ls.setter
    def additional_image_ur_ls(self, additional_image_ur_ls):
        """Sets the additional_image_ur_ls of this Location.

        A list of URLs of any images associated with this location.  # noqa: E501

        :param additional_image_ur_ls: The additional_image_ur_ls of this Location.  # noqa: E501
        :type: list[str]
        """

        self._additional_image_ur_ls = additional_image_ur_ls

    @property
    def address(self):
        """Gets the address of this Location.  # noqa: E501

        The first line of the location’s street address.  # noqa: E501

        :return: The address of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Location.

        The first line of the location’s street address.  # noqa: E501

        :param address: The address of this Location.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Location.  # noqa: E501

        A second address line for the location’s street address, if needed.  # noqa: E501

        :return: The address2 of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Location.

        A second address line for the location’s street address, if needed.  # noqa: E501

        :param address2: The address2 of this Location.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def amenities(self):
        """Gets the amenities of this Location.  # noqa: E501

        A list of strings representing amenities available at the location.  # noqa: E501

        :return: The amenities of this Location.  # noqa: E501
        :rtype: list[Amenity]
        """
        return self._amenities

    @amenities.setter
    def amenities(self, amenities):
        """Sets the amenities of this Location.

        A list of strings representing amenities available at the location.  # noqa: E501

        :param amenities: The amenities of this Location.  # noqa: E501
        :type: list[Amenity]
        """

        self._amenities = amenities

    @property
    def business_description(self):
        """Gets the business_description of this Location.  # noqa: E501

        The business description for the location, as configured by the business owner.  # noqa: E501

        :return: The business_description of this Location.  # noqa: E501
        :rtype: str
        """
        return self._business_description

    @business_description.setter
    def business_description(self, business_description):
        """Sets the business_description of this Location.

        The business description for the location, as configured by the business owner.  # noqa: E501

        :param business_description: The business_description of this Location.  # noqa: E501
        :type: str
        """

        self._business_description = business_description

    @property
    def city(self):
        """Gets the city of this Location.  # noqa: E501

        The location’s city.  # noqa: E501

        :return: The city of this Location.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Location.

        The location’s city.  # noqa: E501

        :param city: The city of this Location.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def description(self):
        """Gets the description of this Location.  # noqa: E501

        A description of the location.  # noqa: E501

        :return: The description of this Location.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Location.

        A description of the location.  # noqa: E501

        :param description: The description of this Location.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def has_classes(self):
        """Gets the has_classes of this Location.  # noqa: E501

        When `true`, indicates that classes are held at this location.<br />  When `false`, Indicates that classes are not held at this location.  # noqa: E501

        :return: The has_classes of this Location.  # noqa: E501
        :rtype: bool
        """
        return self._has_classes

    @has_classes.setter
    def has_classes(self, has_classes):
        """Sets the has_classes of this Location.

        When `true`, indicates that classes are held at this location.<br />  When `false`, Indicates that classes are not held at this location.  # noqa: E501

        :param has_classes: The has_classes of this Location.  # noqa: E501
        :type: bool
        """

        self._has_classes = has_classes

    @property
    def id(self):
        """Gets the id of this Location.  # noqa: E501

        The ID assigned to this location.  # noqa: E501

        :return: The id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Location.

        The ID assigned to this location.  # noqa: E501

        :param id: The id of this Location.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def latitude(self):
        """Gets the latitude of this Location.  # noqa: E501

        The location’s latitude.  # noqa: E501

        :return: The latitude of this Location.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Location.

        The location’s latitude.  # noqa: E501

        :param latitude: The latitude of this Location.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Location.  # noqa: E501

        The location’s longitude.  # noqa: E501

        :return: The longitude of this Location.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Location.

        The location’s longitude.  # noqa: E501

        :param longitude: The longitude of this Location.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def name(self):
        """Gets the name of this Location.  # noqa: E501

        The name of this location.  # noqa: E501

        :return: The name of this Location.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Location.

        The name of this location.  # noqa: E501

        :param name: The name of this Location.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this Location.  # noqa: E501

        The location’s phone number.  # noqa: E501

        :return: The phone of this Location.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Location.

        The location’s phone number.  # noqa: E501

        :param phone: The phone of this Location.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def phone_extension(self):
        """Gets the phone_extension of this Location.  # noqa: E501

        The location’s phone extension.  # noqa: E501

        :return: The phone_extension of this Location.  # noqa: E501
        :rtype: str
        """
        return self._phone_extension

    @phone_extension.setter
    def phone_extension(self, phone_extension):
        """Sets the phone_extension of this Location.

        The location’s phone extension.  # noqa: E501

        :param phone_extension: The phone_extension of this Location.  # noqa: E501
        :type: str
        """

        self._phone_extension = phone_extension

    @property
    def postal_code(self):
        """Gets the postal_code of this Location.  # noqa: E501

        The location’s postal code.  # noqa: E501

        :return: The postal_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Location.

        The location’s postal code.  # noqa: E501

        :param postal_code: The postal_code of this Location.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def site_id(self):
        """Gets the site_id of this Location.  # noqa: E501

        The ID number assigned to this location.  # noqa: E501

        :return: The site_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Location.

        The ID number assigned to this location.  # noqa: E501

        :param site_id: The site_id of this Location.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def state_prov_code(self):
        """Gets the state_prov_code of this Location.  # noqa: E501

        The location’s state or province code.  # noqa: E501

        :return: The state_prov_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._state_prov_code

    @state_prov_code.setter
    def state_prov_code(self, state_prov_code):
        """Sets the state_prov_code of this Location.

        The location’s state or province code.  # noqa: E501

        :param state_prov_code: The state_prov_code of this Location.  # noqa: E501
        :type: str
        """

        self._state_prov_code = state_prov_code

    @property
    def tax1(self):
        """Gets the tax1 of this Location.  # noqa: E501

        A decimal representation of the location’s first tax rate. Tax properties are provided to apply all taxes to the purchase price that the purchase is subject to. Use as many tax properties as needed to represent all the taxes that apply in the location. Enter a decimal number that represents the appropriate tax rate. For example, for an 8% sales tax, enter 0.08.  # noqa: E501

        :return: The tax1 of this Location.  # noqa: E501
        :rtype: float
        """
        return self._tax1

    @tax1.setter
    def tax1(self, tax1):
        """Sets the tax1 of this Location.

        A decimal representation of the location’s first tax rate. Tax properties are provided to apply all taxes to the purchase price that the purchase is subject to. Use as many tax properties as needed to represent all the taxes that apply in the location. Enter a decimal number that represents the appropriate tax rate. For example, for an 8% sales tax, enter 0.08.  # noqa: E501

        :param tax1: The tax1 of this Location.  # noqa: E501
        :type: float
        """

        self._tax1 = tax1

    @property
    def tax2(self):
        """Gets the tax2 of this Location.  # noqa: E501

        A decimal representation of the location’s second tax rate. See the example in the description of Tax1.  # noqa: E501

        :return: The tax2 of this Location.  # noqa: E501
        :rtype: float
        """
        return self._tax2

    @tax2.setter
    def tax2(self, tax2):
        """Sets the tax2 of this Location.

        A decimal representation of the location’s second tax rate. See the example in the description of Tax1.  # noqa: E501

        :param tax2: The tax2 of this Location.  # noqa: E501
        :type: float
        """

        self._tax2 = tax2

    @property
    def tax3(self):
        """Gets the tax3 of this Location.  # noqa: E501

        A decimal representation of the location’s third tax rate. See the example in the description of Tax1.  # noqa: E501

        :return: The tax3 of this Location.  # noqa: E501
        :rtype: float
        """
        return self._tax3

    @tax3.setter
    def tax3(self, tax3):
        """Sets the tax3 of this Location.

        A decimal representation of the location’s third tax rate. See the example in the description of Tax1.  # noqa: E501

        :param tax3: The tax3 of this Location.  # noqa: E501
        :type: float
        """

        self._tax3 = tax3

    @property
    def tax4(self):
        """Gets the tax4 of this Location.  # noqa: E501

        A decimal representation of the location’s fourth tax rate. See the example in the description of Tax1.  # noqa: E501

        :return: The tax4 of this Location.  # noqa: E501
        :rtype: float
        """
        return self._tax4

    @tax4.setter
    def tax4(self, tax4):
        """Sets the tax4 of this Location.

        A decimal representation of the location’s fourth tax rate. See the example in the description of Tax1.  # noqa: E501

        :param tax4: The tax4 of this Location.  # noqa: E501
        :type: float
        """

        self._tax4 = tax4

    @property
    def tax5(self):
        """Gets the tax5 of this Location.  # noqa: E501

        A decimal representation of the location’s fifth tax rate. See the example in the description of Tax1.  # noqa: E501

        :return: The tax5 of this Location.  # noqa: E501
        :rtype: float
        """
        return self._tax5

    @tax5.setter
    def tax5(self, tax5):
        """Sets the tax5 of this Location.

        A decimal representation of the location’s fifth tax rate. See the example in the description of Tax1.  # noqa: E501

        :param tax5: The tax5 of this Location.  # noqa: E501
        :type: float
        """

        self._tax5 = tax5

    @property
    def total_number_of_ratings(self):
        """Gets the total_number_of_ratings of this Location.  # noqa: E501

        The number of reviews that clients have left for this location.  # noqa: E501

        :return: The total_number_of_ratings of this Location.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_ratings

    @total_number_of_ratings.setter
    def total_number_of_ratings(self, total_number_of_ratings):
        """Sets the total_number_of_ratings of this Location.

        The number of reviews that clients have left for this location.  # noqa: E501

        :param total_number_of_ratings: The total_number_of_ratings of this Location.  # noqa: E501
        :type: int
        """

        self._total_number_of_ratings = total_number_of_ratings

    @property
    def average_rating(self):
        """Gets the average_rating of this Location.  # noqa: E501

        The average rating for the location, out of five stars.  # noqa: E501

        :return: The average_rating of this Location.  # noqa: E501
        :rtype: float
        """
        return self._average_rating

    @average_rating.setter
    def average_rating(self, average_rating):
        """Sets the average_rating of this Location.

        The average rating for the location, out of five stars.  # noqa: E501

        :param average_rating: The average_rating of this Location.  # noqa: E501
        :type: float
        """

        self._average_rating = average_rating

    @property
    def total_number_of_deals(self):
        """Gets the total_number_of_deals of this Location.  # noqa: E501

        The number of distinct introductory pricing options available for purchase at this location.  # noqa: E501

        :return: The total_number_of_deals of this Location.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_deals

    @total_number_of_deals.setter
    def total_number_of_deals(self, total_number_of_deals):
        """Sets the total_number_of_deals of this Location.

        The number of distinct introductory pricing options available for purchase at this location.  # noqa: E501

        :param total_number_of_deals: The total_number_of_deals of this Location.  # noqa: E501
        :type: int
        """

        self._total_number_of_deals = total_number_of_deals

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
        if issubclass(Location, dict):
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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other