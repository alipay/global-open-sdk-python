#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCaptureRequest(AlipayRequest):

    def __init__(self):
        super(AlipayCaptureRequest, self).__init__(AntomPathConstants.CAPTURE_PATH)
        self.__capture_request_id = None
        self.__payment_id = None
        self.__capture_amount = None  # type: Amount
        self.__is_last_capture = None

    @property
    def capture_request_id(self):
        return self.__capture_request_id

    @capture_request_id.setter
    def capture_request_id(self, value):
        self.__capture_request_id = value

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def capture_amount(self):
        return self.__capture_amount

    @capture_amount.setter
    def capture_amount(self, value):
        self.__capture_amount = value

    @property
    def is_last_capture(self):
        return self.__is_last_capture

    @is_last_capture.setter
    def is_last_capture(self, value):
        self.__is_last_capture = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id:
            params['paymentId'] = self.payment_id

        if hasattr(self, "capture_request_id") and self.capture_request_id:
            params['captureRequestId'] = self.capture_request_id

        if hasattr(self, "capture_amount") and self.capture_amount:
            params['captureAmount'] = self.capture_amount

        if hasattr(self, "is_last_capture") and self.is_last_capture:
            params['isLastCapture'] = self.is_last_capture

        return params
