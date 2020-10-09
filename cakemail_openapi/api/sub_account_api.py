# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.7
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


class SubAccountApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_account(self, create_account, **kwargs):  # noqa: E501
        """Create a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_account(create_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateAccount create_account: (required)
        :param int partner_account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreateAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_account_with_http_info(create_account, **kwargs)  # noqa: E501

    def create_account_with_http_info(self, create_account, **kwargs):  # noqa: E501
        """Create a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_account_with_http_info(create_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateAccount create_account: (required)
        :param int partner_account_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CreateAccountResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'create_account',
            'partner_account_id'
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
                    " to method create_account" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_account' is set
        if self.api_client.client_side_validation and ('create_account' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_account'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_account` when calling `create_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'partner_account_id' in local_var_params and local_var_params['partner_account_id'] is not None:  # noqa: E501
            query_params.append(('partner_account_id', local_var_params['partner_account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_account' in local_var_params:
            body_params = local_var_params['create_account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/accounts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_account(self, account_id, **kwargs):  # noqa: E501
        """Delete a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_account(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeleteAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_account_with_http_info(account_id, **kwargs)  # noqa: E501

    def delete_account_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Delete a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_account_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeleteAccountResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method delete_account" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `delete_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501

        query_params = []

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
            '/accounts/{account_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account(self, account_id, **kwargs):  # noqa: E501
        """Show a sub-account details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_account_with_http_info(account_id, **kwargs)  # noqa: E501

    def get_account_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Show a sub-account details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccountResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method get_account" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `get_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501

        query_params = []

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
            '/accounts/{account_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_accounts(self, **kwargs):  # noqa: E501
        """Show all sub-accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int partner_account_id:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param bool recursive:
        :param str sort: Sort term and direction, using syntax `[-|+]term`.  Valid terms:   - `name`   - `created_on`
        :param str filter: Valid Terms:   - `name`   - `status`  Valid Operators:   - `==`  Query separator:   - `;`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_accounts_with_http_info(**kwargs)  # noqa: E501

    def list_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """Show all sub-accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int partner_account_id:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param bool recursive:
        :param str sort: Sort term and direction, using syntax `[-|+]term`.  Valid terms:   - `name`   - `created_on`
        :param str filter: Valid Terms:   - `name`   - `status`  Valid Operators:   - `==`  Query separator:   - `;`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccountsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'partner_account_id',
            'page',
            'per_page',
            'with_count',
            'recursive',
            'sort',
            'filter'
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
                    " to method list_accounts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_accounts`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `list_accounts`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'partner_account_id' in local_var_params and local_var_params['partner_account_id'] is not None:  # noqa: E501
            query_params.append(('partner_account_id', local_var_params['partner_account_id']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'with_count' in local_var_params and local_var_params['with_count'] is not None:  # noqa: E501
            query_params.append(('with_count', local_var_params['with_count']))  # noqa: E501
        if 'recursive' in local_var_params and local_var_params['recursive'] is not None:  # noqa: E501
            query_params.append(('recursive', local_var_params['recursive']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

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
            '/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_account(self, account_id, patch_account, **kwargs):  # noqa: E501
        """Update a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_account(account_id, patch_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param PatchAccount patch_account: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.patch_account_with_http_info(account_id, patch_account, **kwargs)  # noqa: E501

    def patch_account_with_http_info(self, account_id, patch_account, **kwargs):  # noqa: E501
        """Update a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_account_with_http_info(account_id, patch_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param PatchAccount patch_account: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccountResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'patch_account'
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
                    " to method patch_account" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `patch_account`")  # noqa: E501
        # verify the required parameter 'patch_account' is set
        if self.api_client.client_side_validation and ('patch_account' not in local_var_params or  # noqa: E501
                                                        local_var_params['patch_account'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `patch_account` when calling `patch_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_account' in local_var_params:
            body_params = local_var_params['patch_account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{account_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def suspend_account(self, account_id, **kwargs):  # noqa: E501
        """Suspend a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.suspend_account(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SuspendAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.suspend_account_with_http_info(account_id, **kwargs)  # noqa: E501

    def suspend_account_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Suspend a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.suspend_account_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SuspendAccountResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method suspend_account" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `suspend_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501

        query_params = []

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
            '/accounts/{account_id}/suspend', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuspendAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unsuspend_account(self, account_id, **kwargs):  # noqa: E501
        """Unsuspend a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsuspend_account(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UnsuspendAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.unsuspend_account_with_http_info(account_id, **kwargs)  # noqa: E501

    def unsuspend_account_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Unsuspend a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsuspend_account_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UnsuspendAccountResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method unsuspend_account" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `unsuspend_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501

        query_params = []

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
            '/accounts/{account_id}/unsuspend', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UnsuspendAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
