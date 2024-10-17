#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount


class CouponPaymentMethodDetail(object):

    def __init__(self):
        self.__coupon_id = None
        self.__available_amount = None  # type: Amount
        self.__coupon_name = None
        self.__coupon_description = None
        self.__coupon_expire_time = None
        self.__payment_method_detail_metadata = None

    @property
    def coupon_id(self):
        return self.__coupon_id


    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value

    @property
    def available_amount(self):
        return self.__available_amount

    @available_amount.setter
    def available_amount(self, value):
        self.__available_amount = value

    @property
    def coupon_name(self):
        return self.__coupon_name


    @coupon_name.setter
    def coupon_name(self, value):
        self.__coupon_name = value

    @property
    def coupon_description(self):
        return self.__coupon_description


    @coupon_description.setter
    def coupon_description(self, value):
        self.__coupon_description = value

    @property
    def coupon_expire_time(self):
        return self.__coupon_expire_time

    @coupon_expire_time.setter
    def coupon_expire_time(self, value):
        self.__coupon_expire_time = value

    @property
    def payment_method_detail_metadata(self):
        return self.__payment_method_detail_metadata
    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value

    def to_ams_dict(self):
        params = dict()
        if self.__coupon_id:
            params['couponId'] = self.__coupon_id
        if self.__available_amount:
            params['availableAmount'] = self.__available_amount.to_ams_dict()
        if self.__coupon_name:
            params['couponName'] = self.__coupon_name
        if self.__coupon_description:
            params['couponDescription'] = self.__coupon_description
        if self.__coupon_expire_time:
            params['couponExpireTime'] = self.__coupon_expire_time
        if self.__payment_method_detail_metadata:
            params['paymentMethodDetailMetadata'] = self.__payment_method_detail_metadata
        return params

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
