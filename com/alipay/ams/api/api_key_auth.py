#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Internal API Key authentication without decoding the identity fragment."""

import re

try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit

_RESERVED_HEADERS = frozenset(
    (
        "authorization",
        "signature",
        "client-id",
        "request-time",
        "key-version",
        "keyversion",
        "agent-token",
        "content-type",
        "user-agent",
        "x-sdkversion",
        "sdk-version",
        "host",
        "content-length",
        "transfer-encoding",
        "connection",
        "proxy-authorization",
    )
)


class ApiKeyAuth(object):
    def __init__(self, gateway_url, api_key):
        if not isinstance(api_key, str) or not re.match(
            r"\A(?:isak|irak)_(?:TEST|PROD)_[^_\s\x00-\x1f\x7f]+_[^\s\x00-\x1f\x7f]+\Z",
            api_key,
        ):
            raise ValueError("api_key must be a Standard or Restricted TEST/PROD key")
        try:
            uri = urlsplit(gateway_url)
            valid = (
                uri.scheme == "https"
                and uri.hostname
                and uri.username is None
                and uri.password is None
                and uri.path in ("", "/")
                and not uri.query
                and not uri.fragment
                and not re.search(r"\s", gateway_url)
            )
            uri.port  # Validate the configured port before any request.
        except (TypeError, ValueError):
            valid = False
        if not valid:
            raise ValueError("gateway_url must be an HTTPS base URL")
        self.gateway_url = gateway_url.rstrip("/")
        self.__api_key = api_key
        self.__sandbox = api_key.split("_", 2)[1] == "TEST"

    def authorization(self):
        return "Bearer " + self.__api_key

    def path(self, path):
        if (
            not isinstance(path, str)
            or not re.match(r"\A/ams/(?:sandbox/)?api/[A-Za-z0-9_/-]+\Z", path)
            or "//" in path
        ):
            raise ValueError("request path must be an ordinary /ams/api/ path")
        normal = path.replace("/ams/sandbox/api/", "/ams/api/", 1)
        return (
            normal.replace("/ams/api/", "/ams/sandbox/api/", 1)
            if self.__sandbox
            else normal
        )

    def redact(self, message):
        return str(message).replace(self.__api_key, "[REDACTED]")


def add_extra_headers(headers, extra_headers):
    for name, value in (extra_headers or {}).items():
        if (
            not isinstance(name, str)
            or not re.match(r"\A[!#$%&'*+.^_`|~0-9A-Za-z-]+\Z", name)
            or not isinstance(value, str)
            or "\r" in value
            or "\n" in value
        ):
            raise ValueError("Invalid custom header")
        if name.lower() not in _RESERVED_HEADERS:
            headers[name] = value
