#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayPayCancelRequest(AlipayRequest):

    def __init__(self):
        super(AlipayPayCancelRequest, self).__init__()
        self.__payment_id = None
        self.__payment_request_id = None

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id:
            params['paymentId'] = self.payment_id

        if hasattr(self, "payment_request_id") and self.payment_request_id:
            params['paymentRequestId'] = self.payment_request_id

        return params
