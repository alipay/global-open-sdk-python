#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.redirect_action_form import RedirectActionForm
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayCreateOrderResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayCreateOrderResponse, self).__init__()
        self.__payment_request_id = None
        self.__payment_id = None
        self.__client_payment_token = None
        self.__payment_amount = None  # type: Amount
        self.__redirect_action_form = None
        self.__parse_rsp_body(rsp_body)

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def client_payment_token(self):
        return self.__client_payment_token

    @property
    def payment_amount(self):
        return self.__payment_amount

    @property
    def redirect_action_form(self):
        return self.__redirect_action_form

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayCreateOrderResponse, self).parse_rsp_body(rsp_body)
        if 'paymentRequestId' in response:
            self.__payment_request_id = response['paymentRequestId']
        if 'paymentId' in response:
            self.__payment_id = response['paymentId']
        if 'paymentAmount' in response:
            payment_amount = Amount()
            payment_amount.parse_rsp_body(response['paymentAmount'])
            self.__payment_amount = payment_amount
        if 'clientPaymentToken' in response:
            self.__client_payment_token = response['clientPaymentToken']
        if 'redirectActionForm' in response:
            redirect_action_form = RedirectActionForm()
            redirect_action_form.parse_rsp_body(response['redirectActionForm'])
            self.__redirect_action_form = redirect_action_form
