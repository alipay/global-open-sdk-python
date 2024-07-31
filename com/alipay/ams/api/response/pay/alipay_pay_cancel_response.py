#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayPayCancelResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayPayCancelResponse, self).__init__()
        self.__payment_id = None
        self.__payment_request_id = None
        self.__cancel_time = None
        self.__parse_rsp_body(rsp_body)

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def cancel_time(self):
        return self.__cancel_time

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayPayCancelResponse, self).parse_rsp_body(rsp_body)
        if 'paymentRequestId' in response:
            self.__payment_request_id = response['paymentRequestId']
        if 'paymentId' in response:
            self.__payment_id = response['paymentId']
        if 'cancelTime' in response:
            self.__cancel_time = response['cancelTime']
