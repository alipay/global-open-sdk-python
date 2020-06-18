#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayAuthConsultResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayAuthConsultResponse, self).__init__()
        self.__auth_url = None
        self.__extend_info = None
        self.__parse_rsp_body(rsp_body)

    @property
    def auth_url(self):
        return self.__auth_url

    @property
    def extend_info(self):
        return self.__extend_info

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayAuthConsultResponse, self).parse_rsp_body(rsp_body)
        if 'authUrl' in response:
            self.__auth_url = response['authUrl']
        if 'extendInfo' in response:
            self.__extend_info = response['extendInfo']
