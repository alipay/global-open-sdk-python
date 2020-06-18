#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PaymentVerificationData(object):
    def __init__(self):
        self.__verify_request_id = None
        self.__authentication_code = None

    @property
    def verify_request_id(self):
        return self.__verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self.__verify_request_id = value

    @property
    def authentication_code(self):
        return self.__authentication_code

    @authentication_code.setter
    def authentication_code(self, value):
        self.__authentication_code = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "verify_request_id") and self.verify_request_id:
            params['verifyRequestId'] = self.verify_request_id

        if hasattr(self, "authentication_code") and self.authentication_code:
            params['authenticationCode'] = self.authentication_code

        return params
