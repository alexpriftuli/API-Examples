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


class PayrollApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def payroll_get_class_payroll(self, site_id, version, **kwargs):  # noqa: E501
        """Get class payroll for staff members.  # noqa: E501

        A staff authorization token is not required for this endpoint, but if one is passed, its permissions are honored. Depending on the access permissions configured for the staff member whose token is passed, the endpoint returns either only the payroll information for that staff member or it returns the payroll information for all staff members.    Note that if a staff member is not paid for a class, earnings of zero are returned by this endpoint.    Note that this endpoint calculates both bonus and no-reg rates for assistants.These rates are not supported by the Payroll report in the web interface.    Note that this endpoint returns both the teacher’s adjusted rate and the assistant’s pay rate when the assistant is paid by the teacher.The Payroll report in the web interface only returns the teacher’s adjusted rate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payroll_get_class_payroll(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param datetime request_end_date_time: The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br />  Default: **Today’s date**  * If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.  * If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date.
        :param bool request_include_inactive_staff: When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false**
        :param int request_limit: Number of results to include, defaults to 100
        :param int request_offset: Page offset, defaults to 0.
        :param int request_staff_id: A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID.
        :param datetime request_start_date_time: The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.  * If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.  * If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date.
        :return: GetClassPayrollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payroll_get_class_payroll_with_http_info(site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.payroll_get_class_payroll_with_http_info(site_id, version, **kwargs)  # noqa: E501
            return data

    def payroll_get_class_payroll_with_http_info(self, site_id, version, **kwargs):  # noqa: E501
        """Get class payroll for staff members.  # noqa: E501

        A staff authorization token is not required for this endpoint, but if one is passed, its permissions are honored. Depending on the access permissions configured for the staff member whose token is passed, the endpoint returns either only the payroll information for that staff member or it returns the payroll information for all staff members.    Note that if a staff member is not paid for a class, earnings of zero are returned by this endpoint.    Note that this endpoint calculates both bonus and no-reg rates for assistants.These rates are not supported by the Payroll report in the web interface.    Note that this endpoint returns both the teacher’s adjusted rate and the assistant’s pay rate when the assistant is paid by the teacher.The Payroll report in the web interface only returns the teacher’s adjusted rate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payroll_get_class_payroll_with_http_info(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param datetime request_end_date_time: The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br />  Default: **Today’s date**  * If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.  * If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date.
        :param bool request_include_inactive_staff: When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false**
        :param int request_limit: Number of results to include, defaults to 100
        :param int request_offset: Page offset, defaults to 0.
        :param int request_staff_id: A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID.
        :param datetime request_start_date_time: The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.  * If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.  * If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date.
        :return: GetClassPayrollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'version', 'authorization', 'request_end_date_time', 'request_include_inactive_staff', 'request_limit', 'request_offset', 'request_staff_id', 'request_start_date_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payroll_get_class_payroll" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `payroll_get_class_payroll`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `payroll_get_class_payroll`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'request_end_date_time' in params:
            query_params.append(('request.endDateTime', params['request_end_date_time']))  # noqa: E501
        if 'request_include_inactive_staff' in params:
            query_params.append(('request.includeInactiveStaff', params['request_include_inactive_staff']))  # noqa: E501
        if 'request_limit' in params:
            query_params.append(('request.limit', params['request_limit']))  # noqa: E501
        if 'request_offset' in params:
            query_params.append(('request.offset', params['request_offset']))  # noqa: E501
        if 'request_staff_id' in params:
            query_params.append(('request.staffId', params['request_staff_id']))  # noqa: E501
        if 'request_start_date_time' in params:
            query_params.append(('request.startDateTime', params['request_start_date_time']))  # noqa: E501

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
            '/public/v{version}/payroll/classes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetClassPayrollResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def payroll_get_time_clock(self, site_id, version, **kwargs):  # noqa: E501
        """Get time card payroll for staff members.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payroll_get_time_clock(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param datetime request_end_date_time: The end of the date range for the time card information to be returned. If you do not supply an `EndDateTime`, data returns for the seven days prior to today’s date. Classes that begin before the `EndDateTime` are included in the response, regardless of the time that the class ends. The maximum allowed date range is 14 days.<br />  Default: **Today’s date**
        :param bool request_include_inactive_staff: When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false**
        :param int request_limit: Number of results to include, defaults to 100
        :param int request_offset: Page offset, defaults to 0.
        :param int request_staff_id: The staff ID for whom you want to retrieve time card information. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID.
        :param datetime request_start_date_time: The beginning of the date range for the time card information to be returned. If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply. The maximum allowed date range is 14 days.
        :return: GetTimeClockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payroll_get_time_clock_with_http_info(site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.payroll_get_time_clock_with_http_info(site_id, version, **kwargs)  # noqa: E501
            return data

    def payroll_get_time_clock_with_http_info(self, site_id, version, **kwargs):  # noqa: E501
        """Get time card payroll for staff members.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payroll_get_time_clock_with_http_info(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :param datetime request_end_date_time: The end of the date range for the time card information to be returned. If you do not supply an `EndDateTime`, data returns for the seven days prior to today’s date. Classes that begin before the `EndDateTime` are included in the response, regardless of the time that the class ends. The maximum allowed date range is 14 days.<br />  Default: **Today’s date**
        :param bool request_include_inactive_staff: When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false**
        :param int request_limit: Number of results to include, defaults to 100
        :param int request_offset: Page offset, defaults to 0.
        :param int request_staff_id: The staff ID for whom you want to retrieve time card information. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID.
        :param datetime request_start_date_time: The beginning of the date range for the time card information to be returned. If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply. The maximum allowed date range is 14 days.
        :return: GetTimeClockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'version', 'authorization', 'request_end_date_time', 'request_include_inactive_staff', 'request_limit', 'request_offset', 'request_staff_id', 'request_start_date_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payroll_get_time_clock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `payroll_get_time_clock`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `payroll_get_time_clock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []
        if 'request_end_date_time' in params:
            query_params.append(('request.endDateTime', params['request_end_date_time']))  # noqa: E501
        if 'request_include_inactive_staff' in params:
            query_params.append(('request.includeInactiveStaff', params['request_include_inactive_staff']))  # noqa: E501
        if 'request_limit' in params:
            query_params.append(('request.limit', params['request_limit']))  # noqa: E501
        if 'request_offset' in params:
            query_params.append(('request.offset', params['request_offset']))  # noqa: E501
        if 'request_staff_id' in params:
            query_params.append(('request.staffId', params['request_staff_id']))  # noqa: E501
        if 'request_start_date_time' in params:
            query_params.append(('request.startDateTime', params['request_start_date_time']))  # noqa: E501

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
            '/public/v{version}/payroll/timeclock', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTimeClockResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
