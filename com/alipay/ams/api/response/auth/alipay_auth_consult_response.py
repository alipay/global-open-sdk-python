#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.auth_code_form import AuthCodeForm
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayAuthConsultResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayAuthConsultResponse, self).__init__()
        self.__auth_url = None
        self.__extend_info = None
        self.__scheme_url = None
        self.__applink_url = None
        self.__appIdentifier = None
        self.__normal_url = None
        self.__auth_code_form = None  # type: AuthCodeForm
        self.__parse_rsp_body(rsp_body)

    @property
    def auth_url(self):
        return self.__auth_url

    @property
    def extend_info(self):
        return self.__extend_info

    @property
    def scheme_url(self):
        return self.__scheme_url

    @property
    def applink_url(self):
        return self.__applink_url

    @property
    def appIdentifier(self):
        return self.__appIdentifier

    @property
    def normal_url(self):
        return self.__normal_url

    @property
    def auth_code_form(self):
        return self.__auth_code_form

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayAuthConsultResponse, self).parse_rsp_body(rsp_body)
        if 'authUrl' in response:
            self.__auth_url = response['authUrl']
        if 'extendInfo' in response:
            self.__extend_info = response['extendInfo']

        if 'schemeUrl' in response:
            self.__scheme_url = response['schemeUrl']

        if 'applinkUrl' in response:
            self.__applink_url = response['applinkUrl']

        if 'appIdentifier' in response:
            self.__appIdentifier = response['appIdentifier']

        if 'normalUrl' in response:
            self.__normal_url = response['normalUrl']

        if 'authCodeForm' in response:
            self.__auth_code_form = response['authCodeForm']
