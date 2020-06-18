#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.payment_method_category_type import PaymentMethodCategoryType
from com.alipay.ams.api.model.amount_limit_info import AmountLimitInfo


class PaymentOption(object):

    def __init__(self):
        self.__payment_method_type = None
        self.__payment_method_category = None
        self.__enabled = None
        self.__preferred = None
        self.__disable_reason = None
        self.__amount_limit_info_map = None
        self.__supported_currencies = None
        self.__payment_option_detail = None
        self.__extend_info = None

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @property
    def payment_method_category(self):
        return self.__payment_method_category

    @property
    def enabled(self):
        return self.__enabled

    @property
    def preferred(self):
        return self.__preferred

    @property
    def disable_reason(self):
        return self.__disable_reason

    @property
    def amount_limit_info_map(self):
        return self.__amount_limit_info_map

    @property
    def supported_currencies(self):
        return self.__supported_currencies

    @property
    def payment_option_detail(self):
        return self.__payment_option_detail

    @property
    def extend_info(self):
        return self.__extend_info

    def parse_rsp_body(self, payment_option_body):
        if type(payment_option_body) == str:
            payment_option_body = json.loads(payment_option_body)

        if 'paymentMethodType' in payment_option_body:
            self.__payment_method_type = payment_option_body['paymentMethodType']

        if 'paymentMethodCategory' in payment_option_body:
            payment_method_category = PaymentMethodCategoryType.value_of(payment_option_body['paymentMethodCategory'])
            self.__payment_method_category = payment_method_category

        if 'enabled' in payment_option_body:
            self.__enabled = payment_option_body['enabled']

        if 'preferred' in payment_option_body:
            self.__preferred = payment_option_body['preferred']

        if 'disableReason' in payment_option_body:
            self.__disable_reason = payment_option_body['disableReason']

        if 'amountLimitInfoMap' in payment_option_body:
            amount_limit_info_map = dict()
            for key, value in payment_option_body['amountLimitInfoMap']:
                amount_limit_info = AmountLimitInfo()
                amount_limit_info.parse_rsp_body(value)
                amount_limit_info_map[key] = amount_limit_info
            self.__amount_limit_info_map = amount_limit_info_map

        if 'supportedCurrencies' in payment_option_body:
            self.__supported_currencies = payment_option_body['supportedCurrencies']

        if 'paymentOptionDetail' in payment_option_body:
            self.__payment_option_detail = payment_option_body['paymentOptionDetail']

        if 'extendInfo' in payment_option_body:
            self.__extend_info = payment_option_body['extendInfo']

