#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.exception.exception import AlipayApiException
from com.alipay.ams.api.net.http2_json_transport import post_http2_json


_SESSION_HEADER = "X-Session-Id"


def execute_session_http2(gateway_url, request, extra_headers):
    session_id = _validate_and_get_session_id(extra_headers)
    request_body = request.to_ams_json()
    response_body = post_http2_json(
        gateway_url, request.path, session_id, request_body
    )
    try:
        response_data = json.loads(response_body)
    except (TypeError, ValueError) as exc:
        raise AlipayApiException("Invalid HTTP/2 response JSON: " + str(exc))
    if not isinstance(response_data, dict) or not isinstance(
        response_data.get("result"), dict
    ):
        raise AlipayApiException("Response data error: result field is null")
    return response_body


def _validate_and_get_session_id(extra_headers):
    if extra_headers is None:
        extra_headers = {}
    if not hasattr(extra_headers, "items"):
        raise AlipayApiException("extra_headers must be a mapping")

    session_id = None
    for name, value in extra_headers.items():
        if not isinstance(name, str) or name.lower() != _SESSION_HEADER.lower():
            raise AlipayApiException(
                "Only X-Session-Id is supported for this API. Unsupported header: "
                + str(name)
            )
        if session_id is not None:
            raise AlipayApiException("X-Session-Id must be provided only once")
        session_id = value
    if not isinstance(session_id, str) or not session_id.strip():
        raise AlipayApiException("X-Session-Id cannot be null or blank")
    if "\r" in session_id or "\n" in session_id:
        raise AlipayApiException(
            "X-Session-Id cannot contain CR or LF characters"
        )
    return session_id
