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


class UserTokenApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_token_issue(self, request, site_id, version, **kwargs):  # noqa: E501
        """Get a staff user token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_token_issue(request, site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IssueRequest request: (required)
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :return: IssueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_token_issue_with_http_info(request, site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.user_token_issue_with_http_info(request, site_id, version, **kwargs)  # noqa: E501
            return data

    def user_token_issue_with_http_info(self, request, site_id, version, **kwargs):  # noqa: E501
        """Get a staff user token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_token_issue_with_http_info(request, site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IssueRequest request: (required)
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :return: IssueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'site_id', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_token_issue" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `user_token_issue`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `user_token_issue`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `user_token_issue`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}
        if 'site_id' in params:
            header_params['siteId'] = params['site_id']  # noqa: E501

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
            '/public/v{version}/usertoken/issue', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IssueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_token_revoke(self, site_id, version, **kwargs):  # noqa: E501
        """Revoke a user token.  # noqa: E501

        Revokes the user token in the Authorization header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_token_revoke(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_token_revoke_with_http_info(site_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.user_token_revoke_with_http_info(site_id, version, **kwargs)  # noqa: E501
            return data

    def user_token_revoke_with_http_info(self, site_id, version, **kwargs):  # noqa: E501
        """Revoke a user token.  # noqa: E501

        Revokes the user token in the Authorization header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_token_revoke_with_http_info(site_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str site_id: ID of the site from which to pull data. (required)
        :param str version: (required)
        :param str authorization: A staff user authorization token.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'version', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_token_revoke" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `user_token_revoke`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `user_token_revoke`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/public/v{version}/usertoken/revoke', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
