#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl

"""
python2中是httplib，python3中是http.client
"""
try:
    import http.client as http_client
except ImportError:
    import httplib as http_client

"""
python2中是urlparse，python3中是urllib.parse
"""
try:
    import urllib.parse as url_parse
except ImportError:
    import urlparse as url_parse

from com.alipay.ams.api.tools.constants import *
from com.alipay.ams.api.exception.exception import AlipayApiException


def __get_http_connection(url, timeout=DEFAULT_TIMEOUT):
    url_parse_result = url_parse.urlparse(url)
    host_name = url_parse_result.hostname
    port = 443
    context = ssl._create_unverified_context()
    connection = http_client.HTTPSConnection(
        host=host_name, port=port, timeout=timeout, context=context
    )
    return connection


def do_post(url, headers=None, req_body=None, charset=DEFAULT_CHARSET):
    connection = __get_http_connection(url)
    try:
        connection.connect()
    except Exception as e:
        raise AlipayApiException("connect failed. " + str(e))

    try:
        connection.request("POST", url, body=req_body.encode(charset), headers=headers)
    except Exception as e:
        raise AlipayApiException("request failed. " + str(e))

    response = connection.getresponse()
    if response.status != 200:
        raise AlipayApiException("invalid http status " + str(response.status))
    headers = response.getheaders()
    result = response.read()
    try:
        response.close()
        connection.close()
    except Exception as e:
        raise AlipayApiException("close failed. " + str(e))

    return headers, result


def do_post_api_key(url, headers, req_body, charset=DEFAULT_CHARSET):
    """Use runtime CA trust and hostname verification; never follow redirects."""
    parsed = url_parse.urlparse(url)
    if parsed.scheme != "https":
        raise AlipayApiException("API Key requires HTTPS")
    connection = http_client.HTTPSConnection(
        host=parsed.hostname, port=parsed.port or 443, timeout=DEFAULT_TIMEOUT,
        context=ssl.create_default_context(),
    )
    response = None
    try:
        connection.request("POST", parsed.path, body=req_body.encode(charset), headers=headers)
        response = connection.getresponse()
        result = response.read()
        if response.status != 200:
            key = headers["Authorization"][len("Bearer "):]
            body = result.decode(charset, errors="replace").replace(key, "[REDACTED]")
            raise AlipayApiException("API Key HTTP status %s: %s" % (response.status, body))
        return response.getheaders(), result
    except ssl.SSLError:
        raise AlipayApiException("API Key TLS connection failed; check gateway certificate and trusted CA configuration")
    except (OSError, IOError, http_client.HTTPException) as e:
        key = headers["Authorization"][len("Bearer "):]
        detail = str(e).replace(key, "[REDACTED]")
        raise AlipayApiException("API Key request failed. " + detail)
    finally:
        if response is not None:
            response.close()
        connection.close()
