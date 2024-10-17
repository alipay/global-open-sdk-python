#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.amount import Amount


class DiscountPaymentMethodDetail(object):

    def __init__(self):
        self.__discount_id = None
        self.__available_amount = None  # type: Amount
        self.__discount_name = None
        self.__discount_description = None
        self.__payment_method_detail_metadata = None

    @property
    def discount_id(self):
        return self.__discount_id

    @discount_id.setter
    def discount_id(self, value):
        self.__discount_id = value

    @property
    def discount_name(self):
        return self.__discount_name


    @discount_name.setter
    def discount_name(self, value):
        self.__discount_name = value

    @property
    def available_amount(self):
        return self.__available_amount

    @available_amount.setter
    def available_amount(self, value):
        self.__available_amount = value

    @property
    def discount_description(self):
        return self.__discount_description


    @discount_description.setter
    def discount_description(self, value):
        self.__discount_description = value

    @property
    def payment_method_detail_metadata(self):
        return self.__payment_method_detail_metadata


    @payment_method_detail_metadata.setter
    def payment_method_detail_metadata(self, value):
        self.__payment_method_detail_metadata = value

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

    def to_ams_dict(self):
        params = dict()
        if self.discount_id:
            params['discountId'] = self.discount_id
        if self.available_amount:
            params['availableAmount'] = self.available_amount.to_ams_dict()
        if self.discount_name:
            params['discountName'] = self.discount_name
        if self.discount_description:
            params['discountDescription'] = self.discount_description
        if self.payment_method_detail_metadata:
            params['paymentMethodDetailMetadata'] = self.payment_method_detail_metadata
        return params
