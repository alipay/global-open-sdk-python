#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.card_payment_method_detail import CardPaymentMethodDetail
from com.alipay.ams.api.model.coupon_payment_method_detail import CouponPaymentMethodDetail
from com.alipay.ams.api.model.discount_payment_method_detail import DiscountPaymentMethodDetail
from com.alipay.ams.api.model.external_payment_method_detail import ExternalPaymentMethodDetail
from com.alipay.ams.api.model.payment_method_detail_type import PaymentMethodDetailType


class PaymentMethodDetail(object):

    def __init__(self):
        self.__payment_method_detail_type = None  # type: PaymentMethodDetailType
        self.__card = None  # type: CardPaymentMethodDetail
        self.__external_account = None  # type: ExternalPaymentMethodDetail
        self.__discount = None  # type: DiscountPaymentMethodDetail
        self.__coupon = None  # type: CouponPaymentMethodDetail
        self.__extend_info = None
        self.__payment_method_type = None


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

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @card.setter
    def card(self, value):
        self.__card = value
    @external_account.setter
    def external_account(self, value):
        self.__external_account = value
    @discount.setter
    def discount(self, value):
        self.__discount = value
    @coupon.setter
    def coupon(self, value):
        self.__coupon = value
    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value



    def parse_rsp_body(self, external_payment_method_detail_body):
        if type(external_payment_method_detail_body) == str:
            external_payment_method_detail_body = json.loads(external_payment_method_detail_body)

        if 'paymentMethodDetailType' in external_payment_method_detail_body:
            payment_method_detail_type = PaymentMethodDetailType.value_of(
                external_payment_method_detail_body['paymentMethodDetailType'])
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

        if 'paymentMethodType' in external_payment_method_detail_body:
            self.__payment_method_type = external_payment_method_detail_body['paymentMethodType']


    def to_ams_dict(self):
        params = dict()
        if self.payment_method_detail_type:
            params['paymentMethodDetailType'] = self.payment_method_detail_type.name
        if self.card:
            params['card'] = self.card.to_ams_dict()
        if self.external_account:
            params['externalAccount'] = self.external_account.to_ams_dict()

        if self.discount:
            params['discount'] = self.discount.to_ams_dict()
        if self.coupon:
            params['coupon'] = self.coupon.to_ams_dict()
        if self.extend_info:
            params['extendInfo'] = self.extend_info
        if self.payment_method_type:
            params['paymentMethodType'] = self.payment_method_type


        return params