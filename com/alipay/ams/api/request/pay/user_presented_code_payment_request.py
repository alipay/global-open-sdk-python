#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.request.pay.alipay_pay_request import AlipayPayRequest


class UserPresentedCodePaymentRequest(AlipayPayRequest):

    def __init__(
        self,
        payment_request_id,
        order,
        currency,
        amount_in_cents,
        payment_code,
        payment_notify_url=None,
        payment_expiry_time=None,
    ):
        super(AlipayPayRequest, self).__init__(AntomPathConstants.PAYMENT_PATH)
        self.product_code = ProductCodeType.IN_STORE_PAYMENT
        self.payment_amount = Amount(currency, amount_in_cents)

        self.payment_method = PaymentMethod()
        self.payment_method.payment_method_type = "CONNECT_WALLET"
        self.payment_method.payment_method_id = payment_code

        self.payment_factor = PaymentFactor()
        self.payment_factor.in_store_payment_scenario = "PaymentCode"

        self.payment_request_id = payment_request_id
        self.order = order
        self.payment_notify_url = payment_notify_url
        self.payment_expiry_time = payment_expiry_time

    def to_ams_json(self):
        self._validate_()
        return super(UserPresentedCodePaymentRequest, self).to_ams_json()

    def _validate_(self):
        assert self.order, "order required."
        assert self.order.merchant, "order.merchant required."
        assert self.order.order_amount, "order.order_amount required."
        assert self.order.order_description, "order.order_description required."
        assert (
            self.order.merchant.reference_merchant_id
        ), "order.merchant.reference_merchant_id required."
        assert self.order.merchant.merchant_mcc, "order.merchant.merchant_mcc required."
        assert (
            self.order.merchant.merchant_name
        ), "order.merchant.merchant_name required."
        assert self.order.merchant.store, "order.merchant.store required."
        assert (
            self.order.merchant.store.reference_store_id
        ), "order.merchant.store.reference_store_id required."
        assert (
            self.order.merchant.store.store_name
        ), "order.merchant.store.store_name required."
        assert (
            self.order.merchant.store.store_mcc
        ), "order.merchant.store.store_mcc required."
        assert self.order.env, "order.env required."
        assert self.order.env.store_terminal_id, "order.env.store_terminal_id required."
        assert (
            self.order.env.store_terminal_request_time
        ), "order.env.store_terminal_request_time required."
