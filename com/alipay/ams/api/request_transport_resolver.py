#!/usr/bin/env python
# -*- coding: utf-8 -*-


_SESSION_HTTP2_ROUTES = (
    ("POST", "/ams/api/v1/meter/uploadEvent"),
)


def requires_session_http2(http_method, path):
    method = http_method.upper() if http_method else ""
    return (method, path) in _SESSION_HTTP2_ROUTES
