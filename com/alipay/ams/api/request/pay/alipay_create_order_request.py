#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCreateOrderRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateOrderRequest, self).__init__(
            AntomPathConstants.CREATE_SESSION_PATH
        )
        self.__product_code = None
        self.__payment_request_id = None
        self.__order = None  # type: Order
        self.__payment_amount = None  # type: Amount
        self.__payment_redirect_url = None
        self.__payment_notify_url = None

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def payment_amount(self):
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value

    @property
    def payment_redirect_url(self):
        return self.__payment_redirect_url

    @payment_redirect_url.setter
    def payment_redirect_url(self, value):
        self.__payment_redirect_url = value

    @property
    def payment_notify_url(self):
        return self.__payment_notify_url

    @payment_notify_url.setter
    def payment_notify_url(self, value):
        self.__payment_notify_url = value

    def to_ams_json(self):
        json_str = json.dumps(
            obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3
        )
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_code") and self.product_code:
            params["productCode"] = self.product_code

        if hasattr(self, "payment_request_id") and self.payment_request_id:
            params["paymentRequestId"] = self.payment_request_id

        if hasattr(self, "order") and self.order:
            params["order"] = self.order

        if hasattr(self, "payment_amount") and self.payment_amount:
            params["paymentAmount"] = self.payment_amount

        if hasattr(self, "payment_redirect_url") and self.payment_redirect_url:
            params["paymentRedirectUrl"] = self.payment_redirect_url

        if hasattr(self, "payment_notify_url") and self.payment_notify_url:
            params["paymentNotifyUrl"] = self.payment_notify_url

        return params
