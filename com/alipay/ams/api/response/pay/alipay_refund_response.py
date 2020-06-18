#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.response.alipay_response import AlipayResponse
from com.alipay.ams.api.model.amount import Amount


class AlipayRefundResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayRefundResponse, self).__init__()
        self.__refund_request_id = None
        self.__refund_id = None
        self.__payment_id = None
        self.__refund_amount = None
        self.__refund_time = None
        self.__refund_non_guarantee_coupon_amount = None
        self.__parse_rsp_body(rsp_body)

    @property
    def refund_request_id(self):
        return self.__refund_request_id

    @property
    def refund_id(self):
        return self.__refund_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def refund_amount(self):
        return self.__refund_amount

    @property
    def refund_time(self):
        return self.__refund_time

    @property
    def refund_non_guarantee_coupon_amount(self):
        return self.__refund_non_guarantee_coupon_amount

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayRefundResponse, self).parse_rsp_body(rsp_body)
        if 'refundRequestId' in response:
            self.__refund_request_id = response['refundRequestId']
        if 'paymentId' in response:
            self.__payment_id = response['paymentId']
        if 'refundId' in response:
            self.__refund_id = response['refundId']
        if 'refundAmount' in response:
            refund_amount = Amount()
            refund_amount.parse_rsp_body(response['refundAmount'])
            self.__refund_amount = refund_amount
        if 'refundTime' in response:
            self.__refund_time = response['refundTime']
        if 'refundNonGuaranteeCouponAmount' in response:
            refund_non_guarantee_coupon_amount = Amount()
            refund_non_guarantee_coupon_amount.parse_rsp_body(response['refundNonGuaranteeCouponAmount'])
            self.__refund_non_guarantee_coupon_amount = refund_non_guarantee_coupon_amount

