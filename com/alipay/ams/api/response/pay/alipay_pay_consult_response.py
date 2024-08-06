#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.payment_method_info import PaymentMethodInfo
from com.alipay.ams.api.model.payment_option import PaymentOption
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayPayConsultResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayPayConsultResponse, self).__init__()
        self.__payment_options = None  # type:PaymentOption
        self.__payment_method_infos = None
        self.__extend_info = None
        self.__parse_rsp_body(rsp_body)

    @property
    def payment_options(self):
        return self.__payment_options

    @property
    def payment_method_infos(self):
        return self.__payment_method_infos

    @property
    def extend_info(self):
        return self.__extend_info

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayPayConsultResponse, self).parse_rsp_body(rsp_body)
        if 'paymentOptions' in response:
            payment_options = PaymentOption()
            payment_options.parse_rsp_body(response['paymentOptions'])
            self.__payment_options = payment_options
        if 'paymentMethodInfos' in response:
            payment_method_infos = PaymentMethodInfo()
            payment_method_infos.parse_rsp_body(response['paymentMethodInfos'])
            self.__payment_method_infos = payment_method_infos
        if 'extendInfo' in response:
            self.__extend_info = response['extendInfo']
