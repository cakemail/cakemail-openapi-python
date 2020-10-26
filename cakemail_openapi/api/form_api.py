# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
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


class FormApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_form(self, create_form, **kwargs):  # noqa: E501
        """Create a form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_form(create_form, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateForm create_form: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreateFormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_form_with_http_info(create_form, **kwargs)  # noqa: E501

    def create_form_with_http_info(self, create_form, **kwargs):  # noqa: E501
        """Create a form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_form_with_http_info(create_form, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateForm create_form: (required)
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
        :return: tuple(CreateFormResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'create_form',
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
                    " to method create_form" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_form' is set
        if self.api_client.client_side_validation and ('create_form' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_form'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_form` when calling `create_form`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_form' in local_var_params:
            body_params = local_var_params['create_form']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/forms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateFormResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_form(self, form_id, **kwargs):  # noqa: E501
        """Delete a form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_form(form_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str form_id: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeleteFormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_form_with_http_info(form_id, **kwargs)  # noqa: E501

    def delete_form_with_http_info(self, form_id, **kwargs):  # noqa: E501
        """Delete a form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_form_with_http_info(form_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str form_id: (required)
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
        :return: tuple(DeleteFormResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'form_id',
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
                    " to method delete_form" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'form_id' is set
        if self.api_client.client_side_validation and ('form_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['form_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `form_id` when calling `delete_form`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'form_id' in local_var_params:
            path_params['form_id'] = local_var_params['form_id']  # noqa: E501

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
            '/forms/{form_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteFormResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form(self, form_id, **kwargs):  # noqa: E501
        """Show a form details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form(form_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str form_id: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_form_with_http_info(form_id, **kwargs)  # noqa: E501

    def get_form_with_http_info(self, form_id, **kwargs):  # noqa: E501
        """Show a form details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form_with_http_info(form_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str form_id: (required)
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
        :return: tuple(FormResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'form_id',
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
                    " to method get_form" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'form_id' is set
        if self.api_client.client_side_validation and ('form_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['form_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `form_id` when calling `get_form`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'form_id' in local_var_params:
            path_params['form_id'] = local_var_params['form_id']  # noqa: E501

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
            '/forms/{form_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_forms(self, **kwargs):  # noqa: E501
        """Show all forms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_forms(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str sort: Sort term and direction, using syntax `[-|+]term`.  Valid terms:   - `name`   - `language`   - `created_on`   - `last_updated_on`   - `list_id`   - `status`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FormsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_forms_with_http_info(**kwargs)  # noqa: E501

    def list_forms_with_http_info(self, **kwargs):  # noqa: E501
        """Show all forms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_forms_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int account_id:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str sort: Sort term and direction, using syntax `[-|+]term`.  Valid terms:   - `name`   - `language`   - `created_on`   - `last_updated_on`   - `list_id`   - `status`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FormsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'page',
            'per_page',
            'with_count',
            'sort'
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
                    " to method list_forms" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_forms`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `list_forms`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'sort' in local_var_params and not re.search(r'[-|+]?[a-zA-Z_]+', local_var_params['sort']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sort` when calling `list_forms`, must conform to the pattern `/[-|+]?[a-zA-Z_]+/`")  # noqa: E501
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
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

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
            '/forms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_form(self, form_id, patch_form, **kwargs):  # noqa: E501
        """Update a form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_form(form_id, patch_form, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str form_id: (required)
        :param PatchForm patch_form: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PatchFormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.patch_form_with_http_info(form_id, patch_form, **kwargs)  # noqa: E501

    def patch_form_with_http_info(self, form_id, patch_form, **kwargs):  # noqa: E501
        """Update a form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_form_with_http_info(form_id, patch_form, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str form_id: (required)
        :param PatchForm patch_form: (required)
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
        :return: tuple(PatchFormResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'form_id',
            'patch_form',
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
                    " to method patch_form" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'form_id' is set
        if self.api_client.client_side_validation and ('form_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['form_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `form_id` when calling `patch_form`")  # noqa: E501
        # verify the required parameter 'patch_form' is set
        if self.api_client.client_side_validation and ('patch_form' not in local_var_params or  # noqa: E501
                                                        local_var_params['patch_form'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `patch_form` when calling `patch_form`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'form_id' in local_var_params:
            path_params['form_id'] = local_var_params['form_id']  # noqa: E501

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_form' in local_var_params:
            body_params = local_var_params['patch_form']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/forms/{form_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PatchFormResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
