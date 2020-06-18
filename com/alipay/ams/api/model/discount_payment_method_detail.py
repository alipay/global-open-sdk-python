#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount


class DiscountPaymentMethodDetail(object):

    def __init__(self):
        self.__discount_id = None
        self.__available_amount = None
        self.__discount_name = None
        self.__discount_description = None
        self.__payment_method_detail_metadata = None

    @property
    def discount_id(self):
        return self.__discount_id

    @property
    def discount_name(self):
        return self.__discount_name

    @property
    def available_amount(self):
        return self.__available_amount

    @property
    def discount_description(self):
        return self.__discount_description

    @property
    def payment_method_detail_metadata(self):
        return self.__payment_method_detail_metadata

    def parse_rsp_body(self, external_payment_method_detail_body):
        if type(external_payment_method_detail_body) == str:
            external_payment_method_detail_body = json.loads(external_payment_method_detail_body)

        if 'discountId' in external_payment_method_detail_body:
            self.__discount_id = external_payment_method_detail_body['discountId']

        if 'availableAmount' in external_payment_method_detail_body:
            available_amount = Amount()
            available_amount.parse_rsp_body(external_payment_method_detail_body['availableAmount'])
            self.__available_amount = available_amount

        if 'discountName' in external_payment_method_detail_body:
            self.__discount_name = external_payment_method_detail_body['discountName']

        if 'discountDescription' in external_payment_method_detail_body:
            self.__discount_description = external_payment_method_detail_body['discountDescription']

        if 'paymentMethodDetailMetadata' in external_payment_method_detail_body:
            self.__payment_method_detail_metadata = external_payment_method_detail_body['paymentMethodDetailMetadata']
