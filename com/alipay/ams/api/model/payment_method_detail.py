#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.payment_method_detail_type import PaymentMethodDetailType
from com.alipay.ams.api.model.card_payment_method_detail import CardPaymentMethodDetail
from com.alipay.ams.api.model.external_payment_method_detail import ExternalPaymentMethodDetail
from com.alipay.ams.api.model.discount_payment_method_detail import DiscountPaymentMethodDetail
from com.alipay.ams.api.model.coupon_payment_method_detail import CouponPaymentMethodDetail


class PaymentMethodDetail(object):

    def __init__(self):
        self.__payment_method_detail_type = None
        self.__card = None
        self.__external_account = None
        self.__discount = None
        self.__coupon = None
        self.__extend_info = None

    @property
    def payment_method_detail_type(self):
        return self.__payment_method_detail_type

    @property
    def card(self):
        return self.__card

    @property
    def external_account(self):
        return self.__external_account

    @property
    def discount(self):
        return self.__discount

    @property
    def coupon(self):
        return self.__coupon

    @property
    def extend_info(self):
        return self.__extend_info

    def parse_rsp_body(self, external_payment_method_detail_body):
        if type(external_payment_method_detail_body) == str:
            external_payment_method_detail_body = json.loads(external_payment_method_detail_body)

        if 'paymentMethodDetailType' in external_payment_method_detail_body:
            payment_method_detail_type = PaymentMethodDetailType.value_of(external_payment_method_detail_body['paymentMethodDetailType'])
            self.__payment_method_detail_type = payment_method_detail_type

        if 'card' in external_payment_method_detail_body:
            card = CardPaymentMethodDetail()
            card.parse_rsp_body(external_payment_method_detail_body['card'])
            self.__card = card

        if 'externalAccount' in external_payment_method_detail_body:
            external_account = ExternalPaymentMethodDetail()
            external_account.parse_rsp_body(external_payment_method_detail_body['externalAccount'])
            self.__external_account = external_account

        if 'discount' in external_payment_method_detail_body:
            discount = DiscountPaymentMethodDetail()
            discount.parse_rsp_body(external_payment_method_detail_body['discount'])
            self.__discount = discount

        if 'coupon' in external_payment_method_detail_body:
            coupon = CouponPaymentMethodDetail()
            coupon.parse_rsp_body(external_payment_method_detail_body['coupon'])
            self.__coupon = coupon

        if 'extendInfo' in external_payment_method_detail_body:
            self.__extend_info = external_payment_method_detail_body['extendInfo']

