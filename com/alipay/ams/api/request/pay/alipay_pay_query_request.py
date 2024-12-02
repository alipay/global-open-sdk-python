#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayPayQueryRequest(AlipayRequest):

    def __init__(self):
        super(AlipayPayQueryRequest, self).__init__(AntomPathConstants.INQUIRY_PAYMENT_PATH)
        self.__payment_id = None
        self.__payment_request_id = None
        self.__merchant_account_id = None


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

    @property
    def merchant_account_id(self):
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value


    # 将对象转换为json字符串
    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id:
            params['paymentId'] = self.payment_id

        if hasattr(self, "payment_request_id") and self.payment_request_id:
            params['paymentRequestId'] = self.payment_request_id

        if hasattr(self, "merchant_account_id") and self.merchant_account_id:
            params['merchantAccountId'] = self.merchant_account_id

        return params
