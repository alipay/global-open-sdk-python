#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayAuthRevokeTokenRequest(AlipayRequest):

    def __init__(self):
        super(AlipayAuthRevokeTokenRequest, self).__init__(AntomPathConstants.AUTH_REVOKE_PATH)
        self.__access_token = None
        self.__extend_info = None

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "access_token") and self.access_token:
            params['accessToken'] = self.access_token
        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info
        return params
