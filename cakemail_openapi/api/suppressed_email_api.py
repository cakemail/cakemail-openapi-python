# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.3.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cakemail_openapi.api_client import ApiClient
from cakemail_openapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SuppressedEmailApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_suppressed_email(self, suppressed_email, **kwargs):  # noqa: E501
        """Add a suppressed email  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_suppressed_email(suppressed_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SuppressedEmail suppressed_email: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreateSuppressedEmailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_suppressed_email_with_http_info(suppressed_email, **kwargs)  # noqa: E501

    def create_suppressed_email_with_http_info(self, suppressed_email, **kwargs):  # noqa: E501
        """Add a suppressed email  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_suppressed_email_with_http_info(suppressed_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SuppressedEmail suppressed_email: (required)
        :param int account_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CreateSuppressedEmailResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'suppressed_email',
            'account_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_suppressed_email" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'suppressed_email' is set
        if self.api_client.client_side_validation and ('suppressed_email' not in local_var_params or  # noqa: E501
                                                        local_var_params['suppressed_email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `suppressed_email` when calling `create_suppressed_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'suppressed_email' in local_var_params:
            body_params = local_var_params['suppressed_email']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/suppressed-emails', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateSuppressedEmailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_suppressed_email(self, email, **kwargs):  # noqa: E501
        """Delete a suppressed email  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_suppressed_email(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str email: Full email, a local part wildcard or a domain wildcard. Examples: *@domain.com, john@*, john@domain.com (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeleteSuppressedEmailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_suppressed_email_with_http_info(email, **kwargs)  # noqa: E501

    def delete_suppressed_email_with_http_info(self, email, **kwargs):  # noqa: E501
        """Delete a suppressed email  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_suppressed_email_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str email: Full email, a local part wildcard or a domain wildcard. Examples: *@domain.com, john@*, john@domain.com (required)
        :param int account_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeleteSuppressedEmailResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'email',
            'account_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_suppressed_email" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if self.api_client.client_side_validation and ('email' not in local_var_params or  # noqa: E501
                                                        local_var_params['email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `email` when calling `delete_suppressed_email`")  # noqa: E501

        if self.api_client.client_side_validation and 'email' in local_var_params and not re.search(r'(^\*@[^@*]+\.[^@*]+$|^[^@*]+@\*$|^[^@*]+@[^@*]+\.[^@*]+$)', local_var_params['email']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `email` when calling `delete_suppressed_email`, must conform to the pattern `/(^\*@[^@*]+\.[^@*]+$|^[^@*]+@\*$|^[^@*]+@[^@*]+\.[^@*]+$)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'email' in local_var_params:
            path_params['email'] = local_var_params['email']  # noqa: E501

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/suppressed-emails/{email}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteSuppressedEmailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_suppressed_emails(self, **kwargs):  # noqa: E501
        """Show all suppressed emails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_suppressed_emails(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SuppressedEmailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_suppressed_emails_with_http_info(**kwargs)  # noqa: E501

    def list_suppressed_emails_with_http_info(self, **kwargs):  # noqa: E501
        """Show all suppressed emails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_suppressed_emails_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SuppressedEmailsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'page',
            'per_page',
            'with_count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_suppressed_emails" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'with_count' in local_var_params and local_var_params['with_count'] is not None:  # noqa: E501
            query_params.append(('with_count', local_var_params['with_count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/suppressed-emails', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuppressedEmailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
