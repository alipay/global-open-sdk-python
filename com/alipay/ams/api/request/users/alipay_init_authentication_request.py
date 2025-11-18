#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayInitAuthenticationRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInitAuthenticationRequest, self).__init__()
        self.__authentication_type = None
        self.__authentication_request_id = None
        self.__authentication_channel_type = None
        self.__user_identity_type = None
        self.__user_identity_value = None

    @property
    def authentication_type(self):
        return self.__authentication_type

    @authentication_type.setter
    def authentication_type(self, value):
        self.__authentication_type = value

    @property
    def authentication_request_id(self):
        return self.__authentication_request_id

    @authentication_request_id.setter
    def authentication_request_id(self, value):
        self.__authentication_request_id = value

    @property
    def authentication_channel_type(self):
        return self.__authentication_channel_type

    @authentication_channel_type.setter
    def authentication_channel_type(self, value):
        self.__authentication_channel_type = value

    @property
    def user_identity_type(self):
        return self.__user_identity_type

    @user_identity_type.setter
    def user_identity_type(self, value):
        self.__user_identity_type = value

    @property
    def user_identity_value(self):
        return self.__user_identity_value

    @user_identity_value.setter
    def user_identity_value(self, value):
        self.__user_identity_value = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "authentication_type") and self.authentication_type:
            params["authenticationType"] = self.authentication_type

        if (
            hasattr(self, "authentication_request_id")
            and self.authentication_request_id
        ):
            params["authenticationRequestId"] = self.authentication_request_id

        if (
            hasattr(self, "authentication_channel_type")
            and self.authentication_channel_type
        ):
            params["authenticationChannelType"] = self.authentication_channel_type

        if hasattr(self, "user_identity_type") and self.user_identity_type:
            params["userIdentityType"] = self.user_identity_type

        if hasattr(self, "user_identity_value") and self.user_identity_value:
            params["userIdentityValue"] = self.user_identity_value

        return params
