#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.refund_detail import RefundDetail
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayRefundResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayRefundResponse, self).__init__()
        self.__refund_request_id = None
        self.__refund_id = None
        self.__payment_id = None
        self.__refund_amount = None  # type: Amount
        self.__refund_time = None
        self.__refund_non_guarantee_coupon_amount = None
        self.__acquirer_reference_no = None
        self.__gross_settlement_amount = None  # type: Amount
        self.__settlement_quote = None  # type: Quote
        self.__refund_details = None  # type:list:RefundDetail
        self.__refund_source_account_no = None
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

    @property
    def acquirer_reference_no(self):
        return self.__acquirer_reference_no

    @property
    def gross_settlement_amount(self):
        return self.__gross_settlement_amount

    @property
    def settlement_quote(self):
        return self.__settlement_quote

    @property
    def refund_details(self):
        return self.__refund_details

    @property
    def refund_source_account_no(self):
        return self.__refund_source_account_no

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

        if 'acquirerReferenceNo' in response:
            self.__acquirer_reference_no = response['acquirerReferenceNo']

        if 'grossSettlementAmount' in response:
            gross_settlement_amount = Amount()
            gross_settlement_amount.parse_rsp_body(response['grossSettlementAmount'])
            self.__gross_settlement_amount = gross_settlement_amount

        if 'settlementQuote' in response:
            settlement_quote = Quote()
            settlement_quote.parse_rsp_body(response['settlementQuote'])
            self.__settlement_quote = settlement_quote

        if 'refundDetails' in response:
            refund_details = []
            for refund_detail in response['refundDetails']:
                refund_detail_obj = RefundDetail()
                refund_detail_obj.parse_rsp_body(refund_detail)
                refund_details.append(refund_detail_obj)
            self.__refund_details = refund_details

        if 'refundSourceAccountNo' in response:
            self.__refund_source_account_no = response['refundSourceAccountNo']
