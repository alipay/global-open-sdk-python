#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayUserQueryInfoRequest(AlipayRequest):

    def __init__(self):
        super(AlipayUserQueryInfoRequest, self).__init__()
        self.__access_token = None

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "access_token") and self.access_token:
            params["accessToken"] = self.access_token

        return params
