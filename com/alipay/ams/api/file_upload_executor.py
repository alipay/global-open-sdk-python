#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import json
import mimetypes

try:
    import urllib.parse as url_parse
except ImportError:
    import urlparse as url_parse

from com.alipay.ams.api._version import USER_AGENT
from com.alipay.ams.api.exception.exception import AlipayApiException
from com.alipay.ams.api.net.multipart_http_rpc import do_multipart_post
from com.alipay.ams.api.request.alipay_file_request import AlipayFileRequest
from com.alipay.ams.api.request.billing.alipay_product_upload_image_request import (
    AlipayProductUploadImageRequest,
)
from com.alipay.ams.api.response.billing.alipay_product_upload_image_response import (
    AlipayProductUploadImageResponse,
)
from com.alipay.ams.api.tools.constants import DEFAULT_CHARSET, DEFAULT_KEY_VERSION
from com.alipay.ams.api.tools.date_tools import get_cur_iso8601_time
from com.alipay.ams.api.tools.signature_tool import sign, verify

try:
    string_types = (basestring,)
except NameError:
    string_types = (str,)


_GATEWAY_HOSTS = {
    "open-sea-global.alipay.com": "open-big-sea.alipay.com",
    "open-sea.alipay.com": "open-big-sea.alipay.com",
    "open-na-global.alipay.com": "open-big-na.alipay.com",
    "open-na.alipay.com": "open-big-na.alipay.com",
    "open-de-global.alipay.com": "open-big-de-global.alipay.com",
}

_PRODUCT_IMAGE_OPERATION = {
    "path": "/ams/api/v1/billing/product/uploadImage",
    "max_file_size": 2 * 1024 * 1024,
    "file_part_names": ("file", "imageFile"),
    "response_type": AlipayProductUploadImageResponse,
}

_OPERATIONS = {
    AlipayProductUploadImageRequest: _PRODUCT_IMAGE_OPERATION,
}


def normalize_explicit_upload_gateway(upload_gateway_url):
    return _normalize_gateway(upload_gateway_url, require_known_host=False)


def execute_file_upload(
    request,
    gateway_url,
    upload_gateway_url,
    client_id,
    merchant_private_key,
    alipay_public_key,
    agent_token=None,
):
    if not isinstance(request, AlipayFileRequest):
        raise AlipayApiException("request must be an AlipayFileRequest")
    operation = _OPERATIONS.get(type(request))
    if operation is None:
        raise AlipayApiException("Only SDK-provided file upload requests are supported")

    product_id = request.product_id
    if not isinstance(product_id, string_types) or not product_id.strip():
        raise AlipayApiException("product_id can't be empty")
    if len(product_id) > 64:
        raise AlipayApiException("product_id length cannot exceed 64 characters")

    file_content = _read_bounded_file(request.file, operation["max_file_size"])
    file_name = request.filename
    file_content_type = mimetypes.guess_type(file_name)[0] or "application/octet-stream"
    request_body = json.dumps(
        {
            "productId": product_id,
            "fileSha256": hashlib.sha256(file_content).hexdigest(),
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )

    path = operation["path"]
    if client_id.startswith("SANDBOX_"):
        path = path.replace("/ams/api", "/ams/sandbox/api", 1)
    gateway = _resolve_upload_gateway(gateway_url, upload_gateway_url)
    request_time = get_cur_iso8601_time()
    signature_value = sign(
        "POST",
        path,
        client_id,
        request_time,
        request_body,
        merchant_private_key,
    )
    key_version = request.key_version or DEFAULT_KEY_VERSION
    headers = {
        "Accept": "text/plain,text/xml,text/javascript,text/html",
        "Cache-Control": "no-cache",
        "Connection": "Keep-Alive",
        "User-Agent": USER_AGENT,
        "Request-Time": request_time,
        "client-id": client_id,
        "Signature": "algorithm=RSA256,keyVersion={0},signature={1}".format(
            key_version, signature_value
        ),
    }
    if agent_token:
        headers["Agent-Token"] = agent_token

    response_headers, response = do_multipart_post(
        gateway + path,
        headers,
        request_body,
        operation["file_part_names"],
        file_name,
        file_content_type,
        file_content,
    )
    response_body = response.decode(DEFAULT_CHARSET)
    response_data = _parse_response(response_body)
    _verify_response(
        response_headers,
        response_body,
        response_data,
        path,
        client_id,
        alipay_public_key,
    )
    return operation["response_type"](response_body)


def _read_bounded_file(file_object, max_file_size):
    if file_object is None or not hasattr(file_object, "read"):
        raise AlipayApiException("file must be a readable binary file object")

    position = None
    if hasattr(file_object, "tell"):
        try:
            position = file_object.tell()
        except (IOError, OSError):
            position = None

    read_error = None
    try:
        content = file_object.read(max_file_size + 1)
    except Exception as exc:
        read_error = exc
        content = None
    finally:
        if position is not None and hasattr(file_object, "seek"):
            try:
                file_object.seek(position)
            except (IOError, OSError) as exc:
                if read_error is None:
                    raise AlipayApiException("Unable to restore file position: " + str(exc))

    if read_error is not None:
        raise AlipayApiException("Unable to read file: " + str(read_error))
    if isinstance(content, bytearray):
        content = bytes(content)
    if not isinstance(content, bytes):
        raise AlipayApiException("file must be opened in binary mode")
    if not content:
        raise AlipayApiException("file can't be empty")
    if len(content) > max_file_size:
        raise AlipayApiException(
            "file size cannot exceed {0} bytes".format(max_file_size)
        )
    return content


def _parse_response(response_body):
    try:
        response_data = json.loads(response_body)
    except (TypeError, ValueError) as exc:
        raise AlipayApiException("Invalid file response JSON: " + str(exc))
    if not isinstance(response_data, dict) or not isinstance(
        response_data.get("result"), dict
    ):
        raise AlipayApiException("File response result field is missing")
    return response_data


def _verify_response(
    response_headers,
    response_body,
    response_data,
    path,
    client_id,
    alipay_public_key,
):
    headers = {}
    for name, value in response_headers:
        headers[name.lower()] = value
    response_time = headers.get("response-time")
    signature_value = _extract_signature(headers.get("signature"))

    if not signature_value and not response_time:
        if response_data["result"].get("resultStatus") != "F":
            raise AlipayApiException("Unsigned file response is not a failure response")
        return
    if not signature_value or not response_time:
        raise AlipayApiException(
            "File response must contain both Signature and Response-Time"
        )
    try:
        verified = verify(
            "POST",
            path,
            client_id,
            response_time,
            response_body,
            signature_value,
            alipay_public_key,
        )
    except Exception as exc:
        raise AlipayApiException("File response verification failed: " + str(exc))
    if not verified:
        raise AlipayApiException("File response signature verification failed")


def _extract_signature(signature_header):
    if not signature_header:
        return None
    for item in signature_header.split(","):
        key_value = item.strip().split("=", 1)
        if len(key_value) == 2 and key_value[0].lower() == "signature":
            return key_value[1]
    return None


def _resolve_upload_gateway(gateway_url, explicit_upload_gateway):
    if explicit_upload_gateway:
        return explicit_upload_gateway
    return _normalize_gateway(gateway_url, require_known_host=True)


def _normalize_gateway(gateway_url, require_known_host):
    if not isinstance(gateway_url, string_types) or not gateway_url.strip():
        raise AlipayApiException("upload gateway URL can't be empty")
    candidate = gateway_url.strip()
    if "://" not in candidate:
        candidate = "https://" + candidate
    parsed = url_parse.urlparse(candidate)
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise AlipayApiException("upload gateway URL must use HTTPS")
    if parsed.username or parsed.password or parsed.path not in ("", "/"):
        raise AlipayApiException("upload gateway URL must not contain credentials or a path")
    if parsed.params or parsed.query or parsed.fragment:
        raise AlipayApiException("upload gateway URL must not contain params, query, or fragment")
    try:
        port = parsed.port
    except ValueError as exc:
        raise AlipayApiException("invalid upload gateway port: " + str(exc))
    if require_known_host and port not in (None, 443):
        raise AlipayApiException("upload gateway URL only supports port 443")

    host = parsed.hostname.lower()
    if require_known_host:
        mapped_host = _GATEWAY_HOSTS.get(host)
        if mapped_host is None:
            raise AlipayApiException(
                "No upload gateway mapping for {0}; configure one explicitly".format(host)
            )
        host = mapped_host
    authority = host
    if not require_known_host and port is not None:
        authority += ":" + str(port)
    return "https://" + authority
