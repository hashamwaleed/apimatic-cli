# -*- coding: utf-8 -*-

"""
    apimaticlib.controllers.transformer_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 09/21/2016
"""

from .base_controller import *



class TransformerController(BaseController):

    """A Controller to access Endpoints in the apimaticlib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def transform_from_file(self,
                            file,
                            format):
        """Does a POST request to /transform.

        Transform an API description from a file.

        Args:
            file (string): TODO: type description here. Example: 
            format (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/transform'

        # Process optional query parameters
        _query_parameters = {
            'format': format
        }

        _files = {
            'file': file
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0'
        }

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, files=_files, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def transform_from_url(self,
                           description_url,
                           format):
        """Does a GET request to /transform.

        Transform an API description from a URL.

        Args:
            description_url (string): TODO: type description here. Example: 
            format (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/transform'

        # Process optional query parameters
        _query_parameters = {
            'descriptionUrl': description_url,
            'format': format
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def transform_from_key(self,
                           api_key,
                           format):
        """Does a GET request to /transform.

        Transform an API description from an API key.

        Args:
            api_key (string): TODO: type description here. Example: 
            format (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/transform'

        # Process optional query parameters
        _query_parameters = {
            'apiKey': api_key,
            'format': format
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body


