#!/usr/bin/env python
# -*- coding: utf-8 -*-


_SESSION_HTTP2_ROUTES = (
    ("POST", "/ams/api/v1/meter/uploadEvent"),
)


def requires_session_http2(http_method, path):
    method = http_method.upper() if http_method else ""
    return (method, path) in _SESSION_HTTP2_ROUTES


def allows_unsigned_response(http_method, path):
    # Routes designed to return unsigned responses are currently the same set as the HTTP/2 session routes.
    return requires_session_http2(http_method, path)
