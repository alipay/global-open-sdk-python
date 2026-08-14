#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    import urllib.parse as url_parse
except ImportError:
    import urlparse as url_parse

from com.alipay.ams.api._version import USER_AGENT
from com.alipay.ams.api.exception.exception import AlipayApiException


def post_http2_json(gateway_url, path, session_id, request_body):
    if sys.version_info < (3, 9):
        raise AlipayApiException(
            "This API requires Python 3.9 or later and the SDK http2 extra"
        )
    try:
        import h2  # noqa: F401
        import httpx
    except ImportError:
        raise AlipayApiException(
            "This API requires the optional HTTP/2 dependency. "
            "Install global-open-sdk-python[http2]."
        )

    request_url = _build_request_url(gateway_url, path)
    transport = httpx.HTTPTransport(http1=False, http2=True, retries=0)
    try:
        with httpx.Client(
            transport=transport,
            follow_redirects=False,
            timeout=httpx.Timeout(30.0, connect=15.0),
        ) as client:
            client.headers.clear()
            response = client.post(
                request_url,
                content=request_body.encode("utf-8"),
                headers={
                    "X-Session-Id": session_id,
                    "Content-Type": "application/json; charset=UTF-8",
                    "Accept": "application/json",
                    "User-Agent": USER_AGENT,
                },
            )
    except httpx.HTTPError as exc:
        raise AlipayApiException("HTTP/2 request failed: " + str(exc))

    if response.http_version != "HTTP/2":
        raise AlipayApiException(
            "This API requires HTTP/2, but negotiated protocol was "
            + response.http_version
        )
    if response.status_code != 200:
        raise AlipayApiException(
            "Response data error, HTTP status={0}, rspBody:{1}".format(
                response.status_code, response.text
            )
        )
    return response.text


def _build_request_url(gateway_url, path):
    parsed = url_parse.urlparse(gateway_url.strip())
    if (
        parsed.scheme.lower() != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in ("", "/")
    ):
        raise AlipayApiException(
            "gateway_url must be an HTTPS origin without path, query, "
            "fragment, or user info"
        )
    if not path or not path.startswith("/"):
        raise AlipayApiException("path must start with /")
    port = ":{0}".format(parsed.port) if parsed.port else ""
    return "https://{0}{1}{2}".format(parsed.hostname, port, path)
