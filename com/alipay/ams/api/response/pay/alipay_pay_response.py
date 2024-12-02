#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.challenge_action_form import ChallengeActionForm
from com.alipay.ams.api.model.order_code_form import OrderCodeForm
from com.alipay.ams.api.model.payment_result_info import PaymentResultInfo
from com.alipay.ams.api.model.promotion_result import PromotionResult
from com.alipay.ams.api.model.psp_customer_info import PspCustomerInfo
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.redirect_action_form import RedirectActionForm
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayPayResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayPayResponse, self).__init__()
        self.__payment_request_id = None
        self.__payment_id = None
        self.__payment_amount = None  # type: Amount
        self.__actual_payment_amount = None  # type: Amount
        self.__payment_quote = None  # type: Quote
        self.__payment_time = None
        self.__payment_create_time = None
        self.__auth_expiry_time = None
        self.__non_guarantee_coupon_value = None
        self.__payment_action_form = None
        self.__psp_customer_info = None
        self.__challenge_action_form = None  # type: ChallengeActionForm
        self.__redirect_action_form = None  # type: RedirectActionForm
        self.__order_code_form = None  # type: OrderCodeForm
        self.__extend_info = None
        self.__gross_settlement_amount = None  # type: Amount
        self.__settlement_quote = None  # type: Quote
        self.__payment_data = None
        self.__app_identifier = None
        self.__app_link_url = None
        self.__normal_url = None
        self.__scheme_url = None
        self.__payment_result_info = None  # type: PaymentResultInfo
        self.__promotion_result = None  # type: PromotionResult
        self.__payment_method_type = None
        self.__parse_rsp_body(rsp_body)

    @property
    def gross_settlement_amount(self):
        return self.__gross_settlement_amount

    @property
    def settlement_quote(self):
        return self.__settlement_quote

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def payment_amount(self):
        return self.__payment_amount

    @property
    def actual_payment_amount(self):
        return self.__actual_payment_amount

    @property
    def payment_quote(self):
        return self.__payment_quote

    @property
    def payment_time(self):
        return self.__payment_time

    @property
    def payment_create_time(self):
        return self.__payment_create_time

    @property
    def auth_expiry_time(self):
        return self.__auth_expiry_time

    @property
    def non_guarantee_coupon_value(self):
        return self.__non_guarantee_coupon_value

    @property
    def payment_action_form(self):
        return self.__payment_action_form

    @property
    def psp_customer_info(self):
        return self.__psp_customer_info

    @property
    def challenge_action_form(self):
        return self.__challenge_action_form

    @property
    def redirect_action_form(self):
        return self.__redirect_action_form

    @property
    def order_code_form(self):
        return self.__order_code_form

    @property
    def extend_info(self):
        return self.__extend_info

    @property
    def payment_data(self):
        return self.__payment_data

    @property
    def app_identifier(self):
        return self.__app_identifier

    @property
    def app_link_url(self):
        return self.__app_link_url

    @property
    def normal_url(self):
        return self.__normal_url

    @property
    def scheme_url(self):
        return self.__scheme_url

    @property
    def payment_result_info(self):
        return self.__payment_result_info

    @property
    def promotion_result(self):
        return self.__promotion_result

    @property
    def payment_method_type(self):
        return self.__payment_method_type

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayPayResponse, self).parse_rsp_body(rsp_body)
        if 'paymentRequestId' in response:
            self.__payment_request_id = response['paymentRequestId']
        if 'paymentId' in response:
            self.__payment_id = response['paymentId']
        if 'paymentAmount' in response:
            payment_amount = Amount()
            payment_amount.parse_rsp_body(response['paymentAmount'])
            self.__payment_amount = payment_amount
        if 'actualPaymentAmount' in response:
            actual_payment_amount = Amount()
            actual_payment_amount.parse_rsp_body(response['actualPaymentAmount'])
            self.__actual_payment_amount = actual_payment_amount
        if 'paymentQuote' in response:
            quote = Quote()
            quote.parse_rsp_body(response['paymentQuote'])
            self.__payment_quote = quote
        if 'paymentTime' in response:
            self.__payment_time = response['paymentTime']
        if 'paymentCreateTime' in response:
            self.__payment_create_time = response['paymentCreateTime']
        if 'authExpiryTime' in response:
            self.__auth_expiry_time = response['authExpiryTime']
        if 'nonGuaranteeCouponValue' in response:
            self.__non_guarantee_coupon_value = response['nonGuaranteeCouponValue']
        if 'paymentActionForm' in response:
            self.__payment_action_form = response['paymentActionForm']
        if 'pspCustomerInfo' in response:
            psp_customer_info = PspCustomerInfo()
            psp_customer_info.parse_rsp_body(response['pspCustomerInfo'])
            self.__psp_customer_info = psp_customer_info
        if 'challengeActionForm' in response:
            challenge_action_form = ChallengeActionForm()
            challenge_action_form.parse_rsp_body(response['challengeActionForm'])
            self.__challenge_action_form = challenge_action_form
        if 'redirectActionForm' in response:
            redirect_action_form = RedirectActionForm()
            redirect_action_form.parse_rsp_body(response['redirectActionForm'])
            self.__redirect_action_form = redirect_action_form
        if 'orderCodeForm' in response:
            order_code_form = OrderCodeForm()
            order_code_form.parse_rsp_body(response['orderCodeForm'])
            self.__order_code_form = order_code_form
        if 'extendInfo' in response:
            self.__extend_info = response['extendInfo']
        if 'grossSettlementAmount' in response:
            gross_settlement_amount = Amount()
            gross_settlement_amount.parse_rsp_body(response['grossSettlementAmount'])
            self.__gross_settlement_amount = gross_settlement_amount
        if 'settlementQuote' in response:
            settlement_quote = Quote()
            settlement_quote.parse_rsp_body(response['settlementQuote'])
            self.__settlement_quote = settlement_quote
        if 'paymentData' in response:
            self.__payment_data = response['paymentData']
        if 'appIdentifier' in response:
            self.__app_identifier = response['appIdentifier']
        if 'appLinkUrl' in response:
            self.__app_link_url = response['appLinkUrl']
        if 'normalUrl' in response:
            self.__normal_url = response['normalUrl']
        if 'schemeUrl' in response:
            self.__scheme_url = response['schemeUrl']
        if 'paymentResultInfo' in response:
            payment_result_info = PaymentResultInfo()
            payment_result_info.parse_rsp_body(response['paymentResultInfo'])
            self.__payment_result_info = payment_result_info
        if 'promotionResult' in response:
            promotion_result = PromotionResult()
            promotion_result.parse_rsp_body(response['promotionResult'])
            self.__promotion_result = promotion_result
        if 'paymentMethodType' in response:
            self.__payment_method_type = response['paymentMethodType']
