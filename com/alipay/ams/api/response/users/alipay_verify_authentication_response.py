#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayVerifyAuthenticationResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayVerifyAuthenticationResponse, self).__init__()
        self.__is_passed = None
        self.__parse_rsp_body(rsp_body)

    @property
    def is_passed(self):
        return self.__is_passed

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayVerifyAuthenticationResponse, self).parse_rsp_body(
            rsp_body
        )
        if "isPassed" in response:
            self.__is_passed = response["isPassed"]
