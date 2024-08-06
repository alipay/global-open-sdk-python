#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from com.alipay.ams.api.model.code_detail import CodeDetail


class OrderCodeForm(object):
    def __init__(self):
        self.__payment_method_type = None
        self.__expire_time = None
        self.__code_details = None  # type: list[CodeDetail]
        self.__extend_info = None

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value

    @property
    def expire_time(self):
        return self.__expire_time

    @expire_time.setter
    def expire_time(self, value):
        self.__expire_time = value

    @property
    def code_details(self):
        return self.__code_details

    @code_details.setter
    def code_details(self, value):
        self.__code_details = value

    @property
    def extend_info(self):
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value

    def parse_rsp_body(self, order_code_form_body):
        if type(order_code_form_body) == str:
            order_code_form_body = json.loads(order_code_form_body)

        if 'paymentMethodType' in order_code_form_body:
            self.__payment_method_type = order_code_form_body['paymentMethodType']

        if 'expireTime' in order_code_form_body:
            self.__expire_time = order_code_form_body['expireTime']

        if 'codeDetails' in order_code_form_body:
            self.__code_details = []
            for entry in order_code_form_body['codeDetails']:
                code_detail = CodeDetail()
                code_detail.parse_rsp_body(entry)
                self.__code_details.append(code_detail)

        if 'extendInfo' in order_code_form_body:
            self.__extend_info = order_code_form_body['extendInfo']
