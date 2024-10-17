#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.tools.signature_tool import *
from com.alipay.ams.api.tools.date_tools import *
from com.alipay.ams.api.net.default_http_rpc import *


class DefaultAlipayClient(object):

    def __init__(self, gateway_url, client_id, merchant_private_key, alipay_public_key):
        self.__gateway_url = gateway_url
        self.__client_id = client_id
        self.__merchant_private_key = merchant_private_key
        self.__alipay_public_key = alipay_public_key
        self.__is_sandbox_mode = client_id.startswith("SANDBOX_")

    """
    内部方法，生成请求签名
    """

    def __gen_sign(self, http_method, path, client_id, req_time, req_body):
        try:
            sign_value = sign(http_method, path, client_id, req_time, req_body, self.__merchant_private_key)
        except Exception as e:
            raise AlipayApiException("request sign failed. " + str(e))
        return sign_value

    """
    内部方法，生成请求签名
    """

    def __verify_sign(self, http_method, path, client_id, rsp_time, rsp_body, rsp_signature):
        try:
            is_verify = verify(http_method, path, client_id, rsp_time, rsp_body, rsp_signature,
                               self.__alipay_public_key)
        except Exception as e:
            raise AlipayApiException("response verify failed. " + str(e))
        return is_verify

    def __parse_header(self, headers):
        for item in headers:
            header_key = item[0]
            if header_key == "signature":
                signature = item[1]
                if signature:
                    signature_item = signature.split("signature=")
                    rsp_signature = signature_item[1]
            if header_key == "response-time":
                response_time = item[1]
            if header_key == "client-id":
                client_id = item[1]

        if "rsp_signature" not in locals():
            raise AlipayApiException("response header exception，signature not exist.")
        if "response_time" not in locals():
            raise AlipayApiException("response header exception，response-time not exist.")
        if "client_id" not in locals():
            raise AlipayApiException("response header exception，client-id not exist.")

        return rsp_signature, response_time, client_id

    def execute(self, request):

        if not hasattr(request, "path") or not request.path:
            raise AlipayApiException('invalid path')

        client_id = self.__client_id
        self.__is_sandbox_mode = client_id.startswith("SANDBOX_")
        self.adjust_sandbox_url(request)
        http_method = request.http_method.value
        path = request.path
        req_time = get_cur_iso8601_time()
        req_body = request.to_ams_json()

        sign_value = self.__gen_sign(http_method, path, client_id, req_time, req_body)

        key_version = DEFAULT_KEY_VERSION
        if hasattr(request, "key_version") and request.key_version:
            key_version = request.key_version

        signature = "algorithm=RSA256,keyVersion=" + key_version + ",signature=" + sign_value
        headers = {
            "Content-type": "application/json; charset=UTF-8",
            "Accept": "text/plain,text/xml,text/javascript,text/html",
            "Cache-Control": "no-cache",
            "Connection": "Keep-Alive",
            "User-Agent": "global-alipay-sdk-python",
            "Request-Time": req_time,
            "client-id": client_id,
            "Signature": signature
        }

        url = self.__gateway_url + path
        headers, response = do_post(url, headers, req_body)

        rsp_body = response.decode(DEFAULT_CHARSET)

        rsp_signature, response_time, client_id = self.__parse_header(headers)
        if not rsp_signature or not response_time:
            return rsp_body

        is_verify = self.__verify_sign(http_method, path, client_id, response_time, rsp_body, rsp_signature)
        if not is_verify:
            raise AlipayApiException("response signature verify failed.")

        return rsp_body

    def adjust_sandbox_url(self, request):
        if self.__is_sandbox_mode:
            origin_path = request.path
            new_path = origin_path.replace('/ams/api', '/ams/sandbox/api', 1)
            request.path = new_path

