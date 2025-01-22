#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_result_info import PaymentResultInfo
from com.alipay.ams.api.model.promotion_result import PromotionResult
from com.alipay.ams.api.model.psp_customer_info import PspCustomerInfo
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.redirect_action_form import RedirectActionForm
from com.alipay.ams.api.model.transaction import Transaction
from com.alipay.ams.api.model.transaction_status_type import TransactionStatusType
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayPayQueryResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayPayQueryResponse, self).__init__()
        self.__payment_status = None  # type: TransactionStatusType
        self.__payment_result_code = None
        self.__payment_result_message = None
        self.__payment_request_id = None
        self.__payment_id = None
        self.__auth_payment_id = None
        self.__payment_amount = None  # type: Amount
        self.__actual_payment_amount = None
        self.__payment_quote = None  # type: Quote
        self.__auth_expiry_time = None
        self.__payment_create_time = None
        self.__payment_time = None
        self.__non_guarantee_coupon_amount = None
        self.__psp_customer_info = None  # type: PspCustomerInfo
        self.__redirect_action_form = None  # type: RedirectActionForm
        self.__extend_info = None
        self.__transactions = None  # type: list[Transaction]
        self.__customs_declaration_amount = None  # type: Amount
        self.__gross_settlement_amount = None  # type: Amount
        self.__settlement_quote = None  # type: Quote
        self.__acquirer_reference_no = None
        self.__payment_result_info = None  # type: PaymentResultInfo
        self.__promotion_results = None  # type: PromotionResult
        self.__earliest_settlement_time = None
        self.__parse_rsp_body(rsp_body)

    @property
    def customs_declaration_amount(self):
        return self.__customs_declaration_amount

    @property
    def gross_settlement_amount(self):
        return self.__gross_settlement_amount

    @property
    def settlement_quote(self):
        return self.__settlement_quote

    @property
    def payment_status(self):
        return self.__payment_status

    @property
    def payment_result_code(self):
        return self.__payment_result_code

    @property
    def payment_result_message(self):
        return self.__payment_result_message

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def auth_payment_id(self):
        return self.__auth_payment_id

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
    def auth_expiry_time(self):
        return self.__auth_expiry_time

    @property
    def payment_create_time(self):
        return self.__payment_create_time

    @property
    def payment_time(self):
        return self.__payment_time

    @property
    def non_guarantee_coupon_amount(self):
        return self.__non_guarantee_coupon_amount

    @property
    def psp_customer_info(self):
        return self.__psp_customer_info

    @property
    def redirect_action_form(self):
        return self.__redirect_action_form

    @property
    def extend_info(self):
        return self.__extend_info

    @property
    def transactions(self):
        return self.__transactions

    @property
    def acquirer_reference_no(self):
        return self.__acquirer_reference_no

    @property
    def payment_result_info(self):
        return self.__payment_result_info

    @property
    def promotion_results(self):
        return self.__promotion_results

    @property
    def earliest_settlement_time(self):
        return self.__earliest_settlement_time

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayPayQueryResponse, self).parse_rsp_body(rsp_body)

        if 'paymentStatus' in response:
            payment_status = TransactionStatusType.value_of(response['paymentStatus'])
            self.__payment_status = payment_status

        if 'paymentRequestId' in response:
            self.__payment_request_id = response['paymentRequestId']

        if 'paymentResultCode' in response:
            self.__payment_result_code = response['paymentResultCode']

        if 'paymentResultMessage' in response:
            self.__payment_result_message = response['paymentResultMessage']

        if 'paymentId' in response:
            self.__payment_id = response['paymentId']

        if 'paymentRequestId' in response:
            self.__payment_request_id = response['paymentRequestId']

        if 'authPaymentId' in response:
            self.__auth_payment_id = response['authPaymentId']

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

        if 'redirectActionForm' in response:
            redirect_action_form = RedirectActionForm()
            redirect_action_form.parse_rsp_body(response['redirectActionForm'])
            self.__redirect_action_form = redirect_action_form

        if 'extendInfo' in response:
            self.__extend_info = response['extendInfo']

        if 'transactions' in response:
            transactions = []
            for transaction_body in response['transactions']:
                transaction = Transaction()
                transaction.parse_rsp_body(transaction_body)
                transactions.append(transaction)
            self.__transactions = transactions

        if 'customsDeclarationAmount' in response:
            customs_declaration_amount = Amount()
            customs_declaration_amount.parse_rsp_body(response['customsDeclarationAmount'])
            self.__customs_declaration_amount = customs_declaration_amount

        if 'grossSettlementAmount' in response:
            gross_settlement_amount = Amount()
            gross_settlement_amount.parse_rsp_body(response['grossSettlementAmount'])
            self.__gross_settlement_amount = gross_settlement_amount

        if 'settlementQuote' in response:
            settlement_quote = Quote()
            settlement_quote.parse_rsp_body(response['settlementQuote'])
            self.__settlement_quote = settlement_quote

        if 'acquirerReferenceNo' in response:
            self.__acquirer_reference_no = response['acquirerReferenceNo']

        if 'paymentResultInfo' in response:
            payment_result_info = PaymentResultInfo()
            payment_result_info.parse_rsp_body(response['paymentResultInfo'])
            self.__payment_result_info = payment_result_info

        if 'promotionResults' in response:
            promotion_results = PromotionResult()
            promotion_results.parse_rsp_body(response['promotionResults'])
            self.__promotion_results = promotion_results

        if 'earliestSettlementTime' in response:
            self.__earliest_settlement_time = response['earliestSettlementTime']
