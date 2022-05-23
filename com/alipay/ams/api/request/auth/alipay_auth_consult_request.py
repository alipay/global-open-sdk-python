#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayAuthConsultRequest(AlipayRequest):

    def __init__(self):
        super(AlipayAuthConsultRequest, self).__init__()
        self.__customer_belongs_to = None
        self.__auth_client_id = None
        self.__auth_redirect_url = None
        self.__scopes = None
        self.__auth_state = None
        self.__terminal_type = None
        self.__os_type = None
        self.__os_version = None
        self.__extend_info = None
        self.__merchant_region = None

    @property
    def merchant_region(self):
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value

    @property
    def customer_belongs_to(self):
        return self.__customer_belongs_to

    @customer_belongs_to.setter
    def customer_belongs_to(self, value):
        self.__customer_belongs_to = value

    @property
    def auth_client_id(self):
        return self.__auth_client_id

    @auth_client_id.setter
    def auth_client_id(self, value):
        self.__auth_client_id = value

    @property
    def auth_redirect_url(self):
        return self.__auth_redirect_url

    @auth_redirect_url.setter
    def auth_redirect_url(self, value):
        self.__auth_redirect_url = value

    @property
    def scopes(self):
        return self.__scopes

    @scopes.setter
    def scopes(self, value):
        self.__scopes = value

    @property
    def auth_state(self):
        return self.__auth_state

    @auth_state.setter
    def auth_state(self, value):
        self.__auth_state = value

    @property
    def terminal_type(self):
        return self.__terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self.__terminal_type = value

    @property
    def os_type(self):
        return self.__os_type

    @os_type.setter
    def os_type(self, value):
        self.__os_type = value

    @property
    def os_version(self):
        return self.__os_version

    @os_version.setter
    def os_version(self, value):
        self.__os_version = value

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

        if hasattr(self, "customer_belongs_to") and self.customer_belongs_to:
            params['customerBelongsTo'] = self.customer_belongs_to
        if hasattr(self, "auth_client_id") and self.auth_client_id:
            params['authClientId'] = self.auth_client_id
        if hasattr(self, "auth_redirect_url") and self.auth_redirect_url:
            params['authRedirectUrl'] = self.auth_redirect_url
        if hasattr(self, "scopes") and self.scopes:
            params['scopes'] = self.scopes
        if hasattr(self, "auth_state") and self.auth_state:
            params['authState'] = self.auth_state
        if hasattr(self, "terminal_type") and self.terminal_type:
            params['terminalType'] = self.terminal_type
        if hasattr(self, "os_type") and self.os_type:
            params['osType'] = self.os_type
        if hasattr(self, "os_version") and self.os_version:
            params['osVersion'] = self.os_version
        if hasattr(self, "extendInfo") and self.extend_info:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "merchant_region") and self.merchant_region:
            params['merchantRegion'] = self.merchant_region
        return params
