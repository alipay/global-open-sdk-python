#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class PaymentMethodInfo(object):

    def __init__(self):
        self.__payment_method_type = None
        self.__payment_method_detail = None
        self.__enabled = None
        self.__preferred = None
        self.__extend_info = None

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @property
    def payment_method_detail(self):
        return self.__payment_method_detail

    @property
    def enabled(self):
        return self.__enabled

    @property
    def preferred(self):
        return self.__preferred

    @property
    def extend_info(self):
        return self.__extend_info

    def parse_rsp_body(self, payment_method_info_body):
        if type(payment_method_info_body) == str:
            payment_method_info_body = json.loads(payment_method_info_body)

        if 'paymentMethodType' in payment_method_info_body:
            self.__payment_method_type = payment_method_info_body['paymentMethodType']

        if 'paymentMethodDetail' in payment_method_info_body:
            self.__payment_method_detail = payment_method_info_body['paymentMethodDetail']

        if 'enabled' in payment_method_info_body:
            self.__enabled = payment_method_info_body['enabled']

        if 'preferred' in payment_method_info_body:
            self.__preferred = payment_method_info_body['preferred']

        if 'extendInfo' in payment_method_info_body:
            self.__extend_info = payment_method_info_body['extendInfo']
