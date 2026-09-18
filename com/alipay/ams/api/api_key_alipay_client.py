#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api._version import USER_AGENT
from com.alipay.ams.api.api_key_auth import ApiKeyAuth, add_extra_headers
from com.alipay.ams.api.exception.exception import AlipayApiException
from com.alipay.ams.api.net.api_key_http_rpc import do_post
from com.alipay.ams.api.request_transport_resolver import requires_session_http2


class ApiKeyAlipayClient(object):
    """Independent API Key client; execute returns the response body, like RSA."""

    def __init__(self, gateway_url, api_key, timeout=30):
        self.__auth = ApiKeyAuth(gateway_url, api_key)
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            raise ValueError("timeout must be positive")
        self.__timeout = timeout

    def execute(self, request):
        return self.execute_with_headers(request)

    def execute_with_headers(self, request, extra_headers=None):
        if not hasattr(request, "path") or not request.path:
            raise AlipayApiException("invalid path")
        method = request.http_method.value
        if requires_session_http2(method, request.path):
            from com.alipay.ams.api.session_http2_executor import execute_session_http2

            return execute_session_http2(
                self.__auth.gateway_url, request, extra_headers
            )
        error = None
        try:
            if method.upper() != "POST":
                raise AlipayApiException(
                    "Only POST is supported for ordinary API requests"
                )
            path = self.__auth.path(request.path)
            headers = {
                "Authorization": self.__auth.authorization(),
                "Content-Type": "application/json; charset=UTF-8",
                "User-Agent": USER_AGENT,
            }
            add_extra_headers(headers, extra_headers)
            return do_post(
                self.__auth.gateway_url + path,
                headers,
                request.to_ams_json(),
                self.__timeout,
            )
        except Exception as exc:
            error = self.__auth.redact(exc)
        # Raise outside the handler to avoid retaining a sensitive exception context.
        raise AlipayApiException(error)
