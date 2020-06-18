#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount


class CouponPaymentMethodDetail(object):

    def __init__(self):
        self.__coupon_id = None
        self.__available_amount = None
        self.__coupon_name = None
        self.__coupon_description = None
        self.__coupon_expire_time = None
        self.__payment_method_detail_metadata = None

    @property
    def coupon_id(self):
        return self.__coupon_id

    @property
    def available_amount(self):
        return self.__available_amount

    @property
    def coupon_name(self):
        return self.__coupon_name

    @property
    def coupon_description(self):
        return self.__coupon_description

    @property
    def coupon_expire_time(self):
        return self.__coupon_expire_time

    @property
    def payment_method_detail_metadata(self):
        return self.__payment_method_detail_metadata

    def parse_rsp_body(self, coupon_payment_method_detail_body):
        if type(coupon_payment_method_detail_body) == str:
            coupon_payment_method_detail_body = json.loads(coupon_payment_method_detail_body)

        if 'couponId' in coupon_payment_method_detail_body:
            self.__coupon_id = coupon_payment_method_detail_body['couponId']

        if 'availableAmount' in coupon_payment_method_detail_body:
            available_amount = Amount()
            available_amount.parse_rsp_body(coupon_payment_method_detail_body['availableAmount'])
            self.__available_amount = available_amount

        if 'couponName' in coupon_payment_method_detail_body:
            self.__coupon_name = coupon_payment_method_detail_body['couponName']

        if 'couponDescription' in coupon_payment_method_detail_body:
            self.__coupon_description = coupon_payment_method_detail_body['couponDescription']

        if 'couponExpireTime' in coupon_payment_method_detail_body:
            self.__coupon_expire_time = coupon_payment_method_detail_body['couponExpireTime']

        if 'paymentMethodDetailMetadata' in coupon_payment_method_detail_body:
            self.__payment_method_detail_metadata = coupon_payment_method_detail_body['paymentMethodDetailMetadata']
