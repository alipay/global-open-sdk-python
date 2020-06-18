#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayInitAuthenticationResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayInitAuthenticationResponse, self).__init__()
        self.__authentication_request_id = None
        self.__parse_rsp_body(rsp_body)

    @property
    def authentication_request_id(self):
        return self.__authentication_request_id

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayInitAuthenticationResponse, self).parse_rsp_body(rsp_body)
        if 'authenticationRequestId' in response:
            self.__authentication_request_id = response['authenticationRequestId']
