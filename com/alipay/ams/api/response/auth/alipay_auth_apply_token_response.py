#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayAuthApplyTokenResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayAuthApplyTokenResponse, self).__init__()
        self.__access_token = None
        self.__access_token_expiry_time = None
        self.__refresh_token = None
        self.__refresh_token_expiry_time = None
        self.__user_login_id = None
        self.__extend_info = None
        self.__parse_rsp_body(rsp_body)

    @property
    def access_token(self):
        return self.__access_token

    @property
    def access_token_expiry_time(self):
        return self.__access_token_expiry_time

    @property
    def refresh_token(self):
        return self.__refresh_token

    @property
    def refresh_token_expiry_time(self):
        return self.__refresh_token_expiry_time

    @property
    def extend_info(self):
        return self.__extend_info

    @property
    def user_login_id(self):
        return self.__user_login_id

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayAuthApplyTokenResponse, self).parse_rsp_body(rsp_body)
        if 'accessToken' in response:
            self.__access_token = response['accessToken']
        if 'accessTokenExpiryTime' in response:
            self.__access_token_expiry_time = response['accessTokenExpiryTime']
        if 'refreshToken' in response:
            self.__refresh_token = response['refreshToken']
        if 'refreshTokenExpiryTime' in response:
            self.__refresh_token_expiry_time = response['refreshTokenExpiryTime']
        if 'extendInfo' in response:
            self.__extend_info = response['extendInfo']

        if 'userLoginId' in response:
            self.__user_login_id = response['userLoginId']
