# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mindbody_api.api_client import ApiClient


class EnrollmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def enrollment_add_client_to_enrollment(self, request, site_id, version, **kwargs):  # noqa: E501
        """Book a client into an enrollment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrollment_add_client_to_enrollment(request, site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddClientToEnrollmentRequest request: (required)
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :return: ClassSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enrollment_add_client_to_enrollment_with_http_info(request, site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.enrollment_add_client_to_enrollment_with_http_info(request, site_id, version, **kwargs)  # noqa: E501
            return data

    def enrollment_add_client_to_enrollment_with_http_info(self, request, site_id, version, **kwargs):  # noqa: E501
        """Book a client into an enrollment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrollment_add_client_to_enrollment_with_http_info(request, site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddClientToEnrollmentRequest request: (required)
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :return: ClassSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'site_id', 'version', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enrollment_add_client_to_enrollment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `enrollment_add_client_to_enrollment`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `enrollment_add_client_to_enrollment`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `enrollment_add_client_to_enrollment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}
        if 'site_id' in params:
            header_params['siteId'] = params['site_id']  # noqa: E501
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/public/v{version}/enrollment/addclienttoenrollment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClassSchedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enrollment_get_enrollments(self, site_id, version, **kwargs):  # noqa: E501
        """Get enrollments scheduled at a site.  # noqa: E501

        Returns a list of enrollments. An enrollment is a service, such as a workshop or an event, that a staff member offers to multiple students, who commit to coming to all or most of the scheduled sessions. Enrollments typically run for a limited time only.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrollment_get_enrollments(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param list[int] request_class_schedule_ids: A list of the requested class schedule IDs. If omitted, all class schedule IDs return.
        :param datetime request_end_date: The end of the date range. The response returns any active enrollments that occur on or before this day.<br />  Default: **StartDate**
        :param int request_limit: Number of results to include, defaults to 100
        :param list[int] request_location_ids: List of the IDs for the requested locations. If omitted, all location IDs return.
        :param int request_offset: Page offset, defaults to 0.
        :param list[int] request_program_ids: List of the IDs for the requested programs. If omitted, all program IDs return.
        :param list[int] request_session_type_ids: List of the IDs for the requested session types. If omitted, all session types IDs return.
        :param list[int] request_staff_ids: List of the IDs for the requested staff IDs. If omitted, all staff IDs return.
        :param datetime request_start_date: The start of the date range. The response returns any active enrollments that occur on or after this day.<br />  Default: **today’s date**
        :return: GetEnrollmentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enrollment_get_enrollments_with_http_info(site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.enrollment_get_enrollments_with_http_info(site_id, version, **kwargs)  # noqa: E501
            return data

    def enrollment_get_enrollments_with_http_info(self, site_id, version, **kwargs):  # noqa: E501
        """Get enrollments scheduled at a site.  # noqa: E501

        Returns a list of enrollments. An enrollment is a service, such as a workshop or an event, that a staff member offers to multiple students, who commit to coming to all or most of the scheduled sessions. Enrollments typically run for a limited time only.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrollment_get_enrollments_with_http_info(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param list[int] request_class_schedule_ids: A list of the requested class schedule IDs. If omitted, all class schedule IDs return.
        :param datetime request_end_date: The end of the date range. The response returns any active enrollments that occur on or before this day.<br />  Default: **StartDate**
        :param int request_limit: Number of results to include, defaults to 100
        :param list[int] request_location_ids: List of the IDs for the requested locations. If omitted, all location IDs return.
        :param int request_offset: Page offset, defaults to 0.
        :param list[int] request_program_ids: List of the IDs for the requested programs. If omitted, all program IDs return.
        :param list[int] request_session_type_ids: List of the IDs for the requested session types. If omitted, all session types IDs return.
        :param list[int] request_staff_ids: List of the IDs for the requested staff IDs. If omitted, all staff IDs return.
        :param datetime request_start_date: The start of the date range. The response returns any active enrollments that occur on or after this day.<br />  Default: **today’s date**
        :return: GetEnrollmentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'version', 'authorization', 'request_class_schedule_ids', 'request_end_date', 'request_limit', 'request_location_ids', 'request_offset', 'request_program_ids', 'request_session_type_ids', 'request_staff_ids', 'request_start_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enrollment_get_enrollments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `enrollment_get_enrollments`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `enrollment_get_enrollments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'request_class_schedule_ids' in params:
            query_params.append(('request.classScheduleIds', params['request_class_schedule_ids']))  # noqa: E501
            collection_formats['request.classScheduleIds'] = 'multi'  # noqa: E501
        if 'request_end_date' in params:
            query_params.append(('request.endDate', params['request_end_date']))  # noqa: E501
        if 'request_limit' in params:
            query_params.append(('request.limit', params['request_limit']))  # noqa: E501
        if 'request_location_ids' in params:
            query_params.append(('request.locationIds', params['request_location_ids']))  # noqa: E501
            collection_formats['request.locationIds'] = 'multi'  # noqa: E501
        if 'request_offset' in params:
            query_params.append(('request.offset', params['request_offset']))  # noqa: E501
        if 'request_program_ids' in params:
            query_params.append(('request.programIds', params['request_program_ids']))  # noqa: E501
            collection_formats['request.programIds'] = 'multi'  # noqa: E501
        if 'request_session_type_ids' in params:
            query_params.append(('request.sessionTypeIds', params['request_session_type_ids']))  # noqa: E501
            collection_formats['request.sessionTypeIds'] = 'multi'  # noqa: E501
        if 'request_staff_ids' in params:
            query_params.append(('request.staffIds', params['request_staff_ids']))  # noqa: E501
            collection_formats['request.staffIds'] = 'multi'  # noqa: E501
        if 'request_start_date' in params:
            query_params.append(('request.startDate', params['request_start_date']))  # noqa: E501

        header_params = {}
        if 'site_id' in params:
            header_params['siteId'] = params['site_id']  # noqa: E501
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/public/v{version}/enrollment/enrollments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetEnrollmentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)