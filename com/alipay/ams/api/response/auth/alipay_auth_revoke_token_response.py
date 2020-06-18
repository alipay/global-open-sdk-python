#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayAuthRevokeTokenResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayAuthRevokeTokenResponse, self).__init__()
        self.__extend_info = None
        self.__parse_rsp_body(rsp_body)

    @property
    def extend_info(self):
        return self.__extend_info

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayAuthRevokeTokenResponse, self).parse_rsp_body(rsp_body)
        if 'extendInfo' in response:
            self.__extend_info = response['extendInfo']
