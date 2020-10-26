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


class SegmentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_segment(self, list_id, segment, **kwargs):  # noqa: E501
        """Create a segment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_segment(list_id, segment, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param Segment segment: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreateSegmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_segment_with_http_info(list_id, segment, **kwargs)  # noqa: E501

    def create_segment_with_http_info(self, list_id, segment, **kwargs):  # noqa: E501
        """Create a segment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_segment_with_http_info(list_id, segment, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param Segment segment: (required)
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
        :return: tuple(CreateSegmentResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'list_id',
            'segment',
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
                    " to method create_segment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `create_segment`")  # noqa: E501
        # verify the required parameter 'segment' is set
        if self.api_client.client_side_validation and ('segment' not in local_var_params or  # noqa: E501
                                                        local_var_params['segment'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `segment` when calling `create_segment`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `create_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'segment' in local_var_params:
            body_params = local_var_params['segment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/segments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateSegmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_segment(self, list_id, segment_id, **kwargs):  # noqa: E501
        """Delete a segment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_segment(list_id, segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int segment_id: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeleteSegmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_segment_with_http_info(list_id, segment_id, **kwargs)  # noqa: E501

    def delete_segment_with_http_info(self, list_id, segment_id, **kwargs):  # noqa: E501
        """Delete a segment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_segment_with_http_info(list_id, segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int segment_id: (required)
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
        :return: tuple(DeleteSegmentResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'list_id',
            'segment_id',
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
                    " to method delete_segment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `delete_segment`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if self.api_client.client_side_validation and ('segment_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['segment_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `segment_id` when calling `delete_segment`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `delete_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'segment_id' in local_var_params and local_var_params['segment_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `segment_id` when calling `delete_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501
        if 'segment_id' in local_var_params:
            path_params['segment_id'] = local_var_params['segment_id']  # noqa: E501

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
            '/lists/{list_id}/segments/{segment_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteSegmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_segment(self, list_id, segment_id, **kwargs):  # noqa: E501
        """Show a segment details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segment(list_id, segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int segment_id: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SegmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_segment_with_http_info(list_id, segment_id, **kwargs)  # noqa: E501

    def get_segment_with_http_info(self, list_id, segment_id, **kwargs):  # noqa: E501
        """Show a segment details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segment_with_http_info(list_id, segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int segment_id: (required)
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
        :return: tuple(SegmentResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'list_id',
            'segment_id',
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
                    " to method get_segment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `get_segment`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if self.api_client.client_side_validation and ('segment_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['segment_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `segment_id` when calling `get_segment`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `get_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'segment_id' in local_var_params and local_var_params['segment_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `segment_id` when calling `get_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501
        if 'segment_id' in local_var_params:
            path_params['segment_id'] = local_var_params['segment_id']  # noqa: E501

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
            '/lists/{list_id}/segments/{segment_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SegmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_segments(self, list_id, **kwargs):  # noqa: E501
        """Show all segments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_segments(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
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
        :return: SegmentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_segments_with_http_info(list_id, **kwargs)  # noqa: E501

    def list_segments_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Show all segments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_segments_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
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
        :return: tuple(SegmentsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'list_id',
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
                    " to method list_segments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `list_segments`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `list_segments`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_segments`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `list_segments`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501

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
            '/lists/{list_id}/segments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SegmentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_segment(self, list_id, segment_id, update_segment, **kwargs):  # noqa: E501
        """Update a segment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_segment(list_id, segment_id, update_segment, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int segment_id: (required)
        :param UpdateSegment update_segment: (required)
        :param int account_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PatchSegmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.patch_segment_with_http_info(list_id, segment_id, update_segment, **kwargs)  # noqa: E501

    def patch_segment_with_http_info(self, list_id, segment_id, update_segment, **kwargs):  # noqa: E501
        """Update a segment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_segment_with_http_info(list_id, segment_id, update_segment, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int segment_id: (required)
        :param UpdateSegment update_segment: (required)
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
        :return: tuple(PatchSegmentResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'list_id',
            'segment_id',
            'update_segment',
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
                    " to method patch_segment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `patch_segment`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if self.api_client.client_side_validation and ('segment_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['segment_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `segment_id` when calling `patch_segment`")  # noqa: E501
        # verify the required parameter 'update_segment' is set
        if self.api_client.client_side_validation and ('update_segment' not in local_var_params or  # noqa: E501
                                                        local_var_params['update_segment'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `update_segment` when calling `patch_segment`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `patch_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'segment_id' in local_var_params and local_var_params['segment_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `segment_id` when calling `patch_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501
        if 'segment_id' in local_var_params:
            path_params['segment_id'] = local_var_params['segment_id']  # noqa: E501

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_segment' in local_var_params:
            body_params = local_var_params['update_segment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/segments/{segment_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PatchSegmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
