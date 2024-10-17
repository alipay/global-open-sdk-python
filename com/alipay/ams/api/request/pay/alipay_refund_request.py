#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayRefundRequest(AlipayRequest):

    def __init__(self):
        super(AlipayRefundRequest, self).__init__(AntomPathConstants.REFUND_PATH)
        self.__refund_request_id = None
        self.__reference_refund_id = None
        self.__payment_id = None
        self.__refund_amount = None  # type: Amount
        self.__refund_reason = None
        self.__is_async_refund = None
        self.__refund_notify_url = None
        self.__extend_info = None

    @property
    def refund_request_id(self):
        return self.__refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self.__refund_request_id = value

    @property
    def reference_refund_id(self):
        return self.__reference_refund_id

    @reference_refund_id.setter
    def reference_refund_id(self, value):
        self.__reference_refund_id = value

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def refund_amount(self):
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value

    @property
    def refund_reason(self):
        return self.__refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self.__refund_reason = value

    @property
    def is_async_refund(self):
        return self.__is_async_refund

    @is_async_refund.setter
    def is_async_refund(self, value):
        self.__is_async_refund = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    @property
    def refund_notify_url(self):
        return self.__refund_notify_url

    @refund_notify_url.setter
    def refund_notify_url(self, value):
        self.__refund_notify_url = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id:
            params['paymentId'] = self.payment_id

        if hasattr(self, "refund_request_id") and self.refund_request_id:
            params['refundRequestId'] = self.refund_request_id

        if hasattr(self, "reference_refund_id") and self.reference_refund_id:
            params['referenceRefundId'] = self.reference_refund_id

        if hasattr(self, "refund_amount") and self.refund_amount:
            params['refundAmount'] = self.refund_amount

        if hasattr(self, "refund_reason") and self.refund_reason:
            params['refundReason'] = self.refund_reason

        if hasattr(self, "is_async_refund") and self.is_async_refund:
            params['isAsyncRefund'] = self.is_async_refund

        if hasattr(self, "extend_info") and self.extend_info:
            params['extendInfo'] = self.extend_info

        if hasattr(self, "refund_notify_url") and self.refund_notify_url:
            params['refundNotifyUrl'] = self.refund_notify_url

        return params
