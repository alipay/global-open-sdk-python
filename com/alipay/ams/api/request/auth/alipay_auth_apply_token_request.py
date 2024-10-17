#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.customer_belongs_to import CustomerBelongsTo
from com.alipay.ams.api.model.grant_type import GrantType
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayAuthApplyTokenRequest(AlipayRequest):

    def __init__(self):
        super(AlipayAuthApplyTokenRequest, self).__init__(AntomPathConstants.AUTH_APPLY_TOKEN_PATH)
        self.__grant_type = None  # type:GrantType
        self.__customer_belongs_to = None  # type:CustomerBelongsTo
        self.__auth_code = None
        self.__refresh_token = None
        self.__extend_info = None
        self.__merchant_region = None

    @property
    def merchant_region(self):
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value

    @property
    def grant_type(self):
        return self.__grant_type

    @grant_type.setter
    def grant_type(self, value):
        self.__grant_type = value

    @property
    def customer_belongs_to(self):
        return self.__customer_belongs_to

    @customer_belongs_to.setter
    def customer_belongs_to(self, value):
        self.__customer_belongs_to = value

    @property
    def auth_code(self):
        return self.__auth_code

    @auth_code.setter
    def auth_code(self, value):
        self.__auth_code = value

    @property
    def refresh_token(self):
        return self.__refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self.__refresh_token = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "grant_type") and self.grant_type:
            params['grantType'] = self.grant_type
        if hasattr(self, "customer_belongs_to") and self.customer_belongs_to:
            params['customerBelongsTo'] = self.customer_belongs_to
        if hasattr(self, "auth_code") and self.auth_code:
            params['authCode'] = self.auth_code
        if hasattr(self, "refresh_token") and self.refresh_token:
            params['refreshToken'] = self.refresh_token
        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "merchant_region") and self.merchant_region:
            params['merchantRegion'] = self.merchant_region
        return params
