#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayCaptureResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayCaptureResponse, self).__init__()
        self.__capture_request_id = None
        self.__capture_id = None
        self.__payment_id = None
        self.__capture_amount = None  # type: Amount
        self.__capture_time = None
        self.__acquirer_reference_no = None
        self.__parse_rsp_body(rsp_body)

    @property
    def capture_request_id(self):
        return self.__capture_request_id

    @property
    def capture_id(self):
        return self.__capture_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def capture_amount(self):
        return self.__capture_amount

    @property
    def capture_time(self):
        return self.__capture_time

    @property
    def acquirer__reference__no(self):
        return self.__acquirer_reference_no

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayCaptureResponse, self).parse_rsp_body(rsp_body)
        if 'captureRequestId' in response:
            self.__capture_request_id = response['captureRequestId']
        if 'paymentId' in response:
            self.__payment_id = response['paymentId']
        if 'captureId' in response:
            self.__capture_id = response['captureId']
        if 'captureAmount' in response:
            capture_amount = Amount()
            capture_amount.parse_rsp_body(response['captureAmount'])
            self.__capture_amount = capture_amount
        if 'captureTime' in response:
            self.__capture_time = response['captureTime']
        if 'acquirerReferenceNo' in response:
            self.__acquirer_reference_no = response['acquirerReferenceNo']
