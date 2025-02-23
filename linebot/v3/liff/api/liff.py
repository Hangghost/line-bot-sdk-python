# coding: utf-8

"""
    LIFF server API

    LIFF Server API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from linebot.v3.liff.models.add_liff_app_request import AddLiffAppRequest
from linebot.v3.liff.models.add_liff_app_response import AddLiffAppResponse
from linebot.v3.liff.models.get_all_liff_apps_response import GetAllLiffAppsResponse
from linebot.v3.liff.models.update_liff_app_request import UpdateLiffAppRequest

from linebot.v3.liff.api_client import ApiClient
from linebot.v3.liff.api_response import ApiResponse
from linebot.v3.liff.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class Liff(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_liff_app(self, add_liff_app_request : AddLiffAppRequest, **kwargs) -> AddLiffAppResponse:  # noqa: E501
        """add_liff_app  # noqa: E501

        Adding the LIFF app to a channel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_liff_app(add_liff_app_request, async_req=True)
        >>> result = thread.get()

        :param add_liff_app_request: (required)
        :type add_liff_app_request: AddLiffAppRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddLiffAppResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_liff_app_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_liff_app_with_http_info(add_liff_app_request, **kwargs)  # noqa: E501

    @validate_arguments
    def add_liff_app_with_http_info(self, add_liff_app_request : AddLiffAppRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """add_liff_app  # noqa: E501

        Adding the LIFF app to a channel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_liff_app_with_http_info(add_liff_app_request, async_req=True)
        >>> result = thread.get()

        :param add_liff_app_request: (required)
        :type add_liff_app_request: AddLiffAppRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AddLiffAppResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'add_liff_app_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_liff_app" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['add_liff_app_request'] is not None:
            _body_params = _params['add_liff_app_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "AddLiffAppResponse",
            '400': None,
            '401': None,
        }

        return self.api_client.call_api(
            '/liff/v1/apps', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_liff_app(self, liff_id : Annotated[StrictStr, Field(..., description="ID of the LIFF app to be updated")], **kwargs) -> None:  # noqa: E501
        """Delete LIFF app from a channel  # noqa: E501

        Deletes a LIFF app from a channel.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_liff_app(liff_id, async_req=True)
        >>> result = thread.get()

        :param liff_id: ID of the LIFF app to be updated (required)
        :type liff_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_liff_app_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_liff_app_with_http_info(liff_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_liff_app_with_http_info(self, liff_id : Annotated[StrictStr, Field(..., description="ID of the LIFF app to be updated")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete LIFF app from a channel  # noqa: E501

        Deletes a LIFF app from a channel.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_liff_app_with_http_info(liff_id, async_req=True)
        >>> result = thread.get()

        :param liff_id: ID of the LIFF app to be updated (required)
        :type liff_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'liff_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_liff_app" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['liff_id']:
            _path_params['liffId'] = _params['liff_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/liff/v1/apps/{liffId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_all_liff_apps(self, **kwargs) -> GetAllLiffAppsResponse:  # noqa: E501
        """Get all LIFF apps  # noqa: E501

        Gets information on all the LIFF apps added to the channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_liff_apps(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAllLiffAppsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_all_liff_apps_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_all_liff_apps_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_all_liff_apps_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Get all LIFF apps  # noqa: E501

        Gets information on all the LIFF apps added to the channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_liff_apps_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetAllLiffAppsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_liff_apps" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "GetAllLiffAppsResponse",
            '401': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/liff/v1/apps', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_liff_app(self, liff_id : Annotated[StrictStr, Field(..., description="ID of the LIFF app to be updated")], update_liff_app_request : UpdateLiffAppRequest, **kwargs) -> None:  # noqa: E501
        """update_liff_app  # noqa: E501

        Update LIFF app settings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_liff_app(liff_id, update_liff_app_request, async_req=True)
        >>> result = thread.get()

        :param liff_id: ID of the LIFF app to be updated (required)
        :type liff_id: str
        :param update_liff_app_request: (required)
        :type update_liff_app_request: UpdateLiffAppRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_liff_app_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_liff_app_with_http_info(liff_id, update_liff_app_request, **kwargs)  # noqa: E501

    @validate_arguments
    def update_liff_app_with_http_info(self, liff_id : Annotated[StrictStr, Field(..., description="ID of the LIFF app to be updated")], update_liff_app_request : UpdateLiffAppRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """update_liff_app  # noqa: E501

        Update LIFF app settings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_liff_app_with_http_info(liff_id, update_liff_app_request, async_req=True)
        >>> result = thread.get()

        :param liff_id: ID of the LIFF app to be updated (required)
        :type liff_id: str
        :param update_liff_app_request: (required)
        :type update_liff_app_request: UpdateLiffAppRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'liff_id',
            'update_liff_app_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_liff_app" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['liff_id']:
            _path_params['liffId'] = _params['liff_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_liff_app_request'] is not None:
            _body_params = _params['update_liff_app_request']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/liff/v1/apps/{liffId}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))



    def liff_v1_apps_get(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_get was deprecated. use get_all_liff_apps instead.', DeprecationWarning)
        return self.get_all_liff_apps(*args, **kwargs)

    def liff_v1_apps_get_with_http_info(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_get_with_http_info was deprecated. use get_all_liff_apps_with_http_info instead.', DeprecationWarning)
        return self.get_all_liff_apps_with_http_info(*args, **kwargs)

    def liff_v1_apps_post(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_post was deprecated. use add_liff_app instead.', DeprecationWarning)
        return self.add_liff_app(*args, **kwargs)

    def liff_v1_apps_post_with_http_info(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_post_with_http_info was deprecated. use add_liff_app_with_http_info instead.', DeprecationWarning)
        return self.add_liff_app_with_http_info(*args, **kwargs)

    def liff_v1_apps_liff_id_put(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_liff_id_put was deprecated. use update_liff_app instead.', DeprecationWarning)
        return self.update_liff_app(*args, **kwargs)

    def liff_v1_apps_liff_id_put_with_http_info(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_liff_id_put_with_http_info was deprecated. use update_liff_app_with_http_info instead.', DeprecationWarning)
        return self.update_liff_app_with_http_info(*args, **kwargs)

    def liff_v1_apps_liff_id_delete(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_liff_id_delete was deprecated. use delete_liff_app instead.', DeprecationWarning)
        return self.delete_liff_app(*args, **kwargs)

    def liff_v1_apps_liff_id_delete_with_http_info(self, *args, **kwargs):
        import warnings
        warnings.warn('liff_v1_apps_liff_id_delete_with_http_info was deprecated. use delete_liff_app_with_http_info instead.', DeprecationWarning)
        return self.delete_liff_app_with_http_info(*args, **kwargs)
