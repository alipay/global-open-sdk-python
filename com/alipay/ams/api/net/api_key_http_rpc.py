#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""HTTPS transport with certificate validation, no redirects and no retries."""

import ssl

try:
    import http.client as http_client
    from urllib.parse import urlsplit
except ImportError:
    import httplib as http_client
    from urlparse import urlsplit
from com.alipay.ams.api.exception.exception import AlipayApiException


def do_post(url, headers, req_body, timeout):
    uri = urlsplit(url)
    connection = http_client.HTTPSConnection(
        uri.hostname,
        port=uri.port or 443,
        timeout=timeout,
        context=ssl.create_default_context(),
    )
    try:
        connection.request(
            "POST", uri.path, body=req_body.encode("utf-8"), headers=headers
        )
        response = connection.getresponse()
        try:
            if response.status != 200:
                raise AlipayApiException("invalid http status " + str(response.status))
            return response.read().decode("utf-8")
        finally:
            response.close()
    finally:
        connection.close()
