#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayUserQueryInfoResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayUserQueryInfoResponse, self).__init__()
        self.__user_id = None
        self.__user_login_id = None
        self.__hash_user_login_id = None
        self.__parse_rsp_body(rsp_body)

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_login_id(self):
        return self.__user_login_id

    @property
    def hash_user_login_id(self):
        return self.__hash_user_login_id

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayUserQueryInfoResponse, self).parse_rsp_body(rsp_body)
        if "userId" in response:
            self.__user_id = response["userId"]

        if "userLoginId" in response:
            self.__user_login_id = response["userLoginId"]

        if "hashUserLoginId" in response:
            self.__hash_user_login_id = response["hashUserLoginId"]
