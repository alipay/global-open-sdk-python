#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
import uuid

try:
    import http.client as http_client
except ImportError:
    import httplib as http_client

try:
    import urllib.parse as url_parse
except ImportError:
    import urlparse as url_parse

from com.alipay.ams.api.exception.exception import AlipayApiException
from com.alipay.ams.api.tools.constants import DEFAULT_CHARSET, DEFAULT_TIMEOUT

try:
    string_types = (basestring,)
except NameError:
    string_types = (str,)


def do_multipart_post(
    url,
    headers,
    request_body,
    file_part_names,
    file_name,
    file_content_type,
    file_content,
):
    parsed = url_parse.urlparse(url)
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise AlipayApiException("Only HTTPS upload URLs are supported.")

    boundary = "----AntomBoundary" + uuid.uuid4().hex
    payload = _build_multipart(
        boundary,
        request_body,
        file_part_names,
        file_name,
        file_content_type,
        file_content,
    )
    request_headers = dict(headers or {})
    request_headers["Content-Type"] = "multipart/form-data; boundary=" + boundary
    request_headers["Content-Length"] = str(len(payload))

    port = parsed.port or 443
    context = ssl.create_default_context()
    connection = http_client.HTTPSConnection(
        parsed.hostname, port=port, timeout=DEFAULT_TIMEOUT, context=context
    )
    request_path = parsed.path or "/"
    if parsed.query:
        request_path += "?" + parsed.query

    try:
        connection.request("POST", request_path, body=payload, headers=request_headers)
        response = connection.getresponse()
        response_headers = response.getheaders()
        response_body = response.read()
        if response.status != 200:
            raise AlipayApiException(
                "invalid http status {0}, response body: {1}".format(
                    response.status, response_body.decode(DEFAULT_CHARSET, "replace")
                )
            )
        return response_headers, response_body
    except AlipayApiException:
        raise
    except Exception as exc:
        raise AlipayApiException("upload request failed. " + str(exc))
    finally:
        connection.close()


def _build_multipart(
    boundary,
    request_body,
    file_part_names,
    file_name,
    file_content_type,
    file_content,
):
    boundary_bytes = boundary.encode("ascii")
    safe_file_name = _sanitize_file_name(file_name).encode(DEFAULT_CHARSET)
    content_type = file_content_type.encode("ascii")
    payload = bytearray()

    payload.extend(b"--" + boundary_bytes + b"\r\n")
    payload.extend(b'Content-Disposition: form-data; name="body"\r\n')
    payload.extend(b"Content-Type: application/json; charset=UTF-8\r\n\r\n")
    payload.extend(request_body.encode(DEFAULT_CHARSET))
    payload.extend(b"\r\n")

    for field_name in file_part_names:
        field_name = _sanitize_field_name(field_name).encode("ascii")
        payload.extend(b"--" + boundary_bytes + b"\r\n")
        payload.extend(b'Content-Disposition: form-data; name="')
        payload.extend(field_name)
        payload.extend(b'"; filename="' + safe_file_name + b'"\r\n')
        payload.extend(b"Content-Type: " + content_type + b"\r\n")
        payload.extend(b"Content-Transfer-Encoding: binary\r\n\r\n")
        payload.extend(file_content)
        payload.extend(b"\r\n")

    payload.extend(b"--" + boundary_bytes + b"--\r\n")
    return bytes(payload)


def _sanitize_file_name(file_name):
    if not isinstance(file_name, string_types):
        file_name = str(file_name)
    file_name = file_name.replace("\\", "/").rsplit("/", 1)[-1]
    return "".join(
        "_" if character == '"' or ord(character) < 0x20 or ord(character) == 0x7F
        else character
        for character in file_name
    )


def _sanitize_field_name(field_name):
    if not isinstance(field_name, str) or not field_name:
        raise AlipayApiException("multipart field name cannot be empty")
    if not all(character.isalnum() or character in "_-" for character in field_name):
        raise AlipayApiException("invalid multipart field name")
    return field_name
