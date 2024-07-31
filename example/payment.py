#!/usr/bin/env python
# -*- coding: utf-8 -*-
from com.alipay.ams.api.model.buyer import Buyer
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.goods import Goods
from com.alipay.ams.api.model.terminal_type import TerminalType
from com.alipay.ams.api.model.os_type import OsType
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.request.pay.alipay_create_session_request import AlipayCreateSessionRequest
from com.alipay.ams.api.request.pay.alipay_pay_request import AlipayPayRequest
from com.alipay.ams.api.request.pay.alipay_refund_query_request import AlipayRefundQueryRequest
from com.alipay.ams.api.response.pay.alipay_create_session_response import AlipayCreateSessionResponse
from com.alipay.ams.api.response.pay.alipay_pay_response import AlipayPayResponse
from com.alipay.ams.api.request.pay.alipay_pay_consult_request import AlipayPayConsultRequest
from com.alipay.ams.api.response.pay.alipay_pay_consult_response import AlipayPayConsultResponse
from com.alipay.ams.api.request.pay.alipay_pay_query_request import AlipayPayQueryRequest
from com.alipay.ams.api.response.pay.alipay_pay_query_response import AlipayPayQueryResponse
from com.alipay.ams.api.request.pay.alipay_pay_cancel_request import AlipayPayCancelRequest
from com.alipay.ams.api.response.pay.alipay_pay_cancel_response import AlipayPayCancelResponse
from com.alipay.ams.api.request.pay.alipay_capture_request import AlipayCaptureRequest
from com.alipay.ams.api.response.pay.alipay_capture_response import AlipayCaptureResponse
from com.alipay.ams.api.request.pay.alipay_refund_request import AlipayRefundRequest
from com.alipay.ams.api.response.pay.alipay_refund_query_response import AlipayRefundQueryResponse
from com.alipay.ams.api.response.pay.alipay_refund_response import AlipayRefundResponse


MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLICK_KEY = ""
CLIENT_ID = ""
GATEWAY_HOST = ""

def pay():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST,
                                                CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)

    alipay_pay_request = AlipayPayRequest()
    alipay_pay_request.path = "/ams/sandbox/api/v1/payments/pay"


    alipay_pay_request.product_code = ProductCodeType.CASHIER_PAYMENT
    alipay_pay_request.payment_notify_url = "https://www.taobao.com"
    alipay_pay_request.payment_redirect_url = "https://www.taobao.com?param1=sl"
    alipay_pay_request.payment_request_id = "pay_python_test_13"

    payment_method = PaymentMethod()
    payment_method.payment_method_type = "ALIPAY_CN"
    payment_method.payment_method_id = "20200404095501585965350751669161222"
    alipay_pay_request.payment_method = payment_method

    amount = Amount("CNY", "10000")
    alipay_pay_request.payment_amount = amount

    order = Order()
    order.reference_order_id = "102775765656121"
    order.order_description = "Mi Band 3 Wrist Strap Metal Screwless Stainless Steel For Xiaomi Mi Band 3"
    order.order_amount = amount

    buyer = Buyer()
    buyer.buyer_email = "test@alipay.com"
    buyer.reference_buyer_id = "12345679"
    order.buyer = buyer

    goods_arr = []
    good = Goods()
    good.goods_brand = "goods_brand"
    good.goods_name = "goods_name"
    goods_arr.append(good)
    order.goods = goods_arr

    merchant = Merchant()
    merchant.merchant_mcc = "merchantMcc"
    merchant.reference_merchant_id = "12346789022221121"

    order.merchant = merchant
    alipay_pay_request.order = order

    settlement_strategy = SettlementStrategy()
    settlement_strategy.settlement_currency = "USD"
    alipay_pay_request.settlement_strategy = settlement_strategy

    env = Env()
    env.terminal_type = TerminalType.WEB
    alipay_pay_request.env = env


    # paymentFactor = PaymentFactor()
    # paymentFactor.is_authorization = True
    # alipay_pay_request.payment_factor = paymentFactor

    print(alipay_pay_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_pay_request)

    alipay_pay_response = AlipayPayResponse(rsp_body)

    if alipay_pay_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_pay_response.payment_id)
        print(alipay_pay_response.payment_create_time)
        print(alipay_pay_response.normal_url)
    else:
        print(alipay_pay_response.result.result_message)


def pay_consult():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)
    pay_consult_request = AlipayPayConsultRequest()
    pay_consult_request.path = "/ams/sandbox/api/v1/payments/consult"
    pay_consult_request.product_code = ProductCodeType.CASHIER_PAYMENT
    # pay_consult_request.customer_id = "123441"
    pay_consult_request.user_region = "SG"


    payment_amount = Amount("USD", "1000")
    pay_consult_request.payment_amount = payment_amount

    env = Env()
    env.terminal_type = TerminalType.APP
    env.os_type = OsType.IOS
    # env.device_token_id = "60e62513a925bf5575111cad5976835b"
    # env.client_ip = "127.0.0.1"
    pay_consult_request.env = env

    settlementStrategy = SettlementStrategy()
    settlementStrategy.settlement_currency = "USD"
    pay_consult_request.settlement_strategy = settlementStrategy

    pay_consult_request.allowed_payment_method_regions = ["HK", "US","CN"]

    paymentFactor = PaymentFactor()
    paymentFactor.presentment_mode="BUNDLE"
    pay_consult_request.payment_factor = paymentFactor



    rsp_body = default_alipay_client.execute(pay_consult_request)

    pay_consult_response = AlipayPayConsultResponse(rsp_body)
    if pay_consult_response.result.result_status.name != ResultStatusType.F.name:
        print(pay_consult_response.payment_options)
    else:
        print(pay_consult_response.result.result_message)


def pay_cancel(paymentId):

    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)

    alipay_pay_cancel_request = AlipayPayCancelRequest()
    alipay_pay_cancel_request.path = "/ams/sandbox/api/v1/payments/cancel"
    alipay_pay_cancel_request.payment_id = paymentId

    rsp_body = default_alipay_client.execute(alipay_pay_cancel_request)

    alipay_pay_cancel_response = AlipayPayCancelResponse(rsp_body)

    if alipay_pay_cancel_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_pay_cancel_response.cancel_time)
    else:
        print(alipay_pay_cancel_response.result.result_message)


def pay_query(paymenId):

    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)

    alipay_pay_query_request = AlipayPayQueryRequest()
    alipay_pay_query_request.path = "/ams/sandbox/api/v1/payments/inquiryPayment"
    alipay_pay_query_request.payment_id = paymenId


    rsp_body = default_alipay_client.execute(alipay_pay_query_request)

    alipay_pay_query_response = AlipayPayQueryResponse(rsp_body)

    if alipay_pay_query_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_pay_query_response.payment_id)
        print(alipay_pay_query_response.payment_status)
    else:
        print(alipay_pay_query_response.result.result_message)


def capture(paymentId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLICK_KEY)

    alipay_capture_request = AlipayCaptureRequest()
    alipay_capture_request.path = "/ams/sandbox/api/v1/payments/capture"
    alipay_capture_request.payment_id = paymentId
    alipay_capture_request.capture_request_id = "python_capture_test_01"
    alipay_capture_request.is_last_capture = "true"

    capture_amount = Amount("USD", "100")
    alipay_capture_request.capture_amount = capture_amount

    print(alipay_capture_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_capture_request)

    alipay_capture_response = AlipayCaptureResponse(rsp_body)

    if alipay_capture_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_capture_response.capture_id)
    else:
        print(alipay_capture_response.result.result_message)


def refund(paymentId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLICK_KEY)

    alipay_refund_request = AlipayRefundRequest()
    alipay_refund_request.path = "/ams/sandbox/api/v1/payments/refund"
    alipay_refund_request.refund_request_id = "python_test_refund_1212"
    alipay_refund_request.payment_id = paymentId

    refund_amount = Amount("CNY", "100")
    alipay_refund_request.refund_amount = refund_amount

    print(alipay_refund_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_refund_request)

    alipay_refund_response = AlipayRefundResponse(rsp_body)

    if alipay_refund_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_refund_response.refund_request_id)
    else:
        print(alipay_refund_response.result.result_message)

def inqueryRefund(paymentRefundRequestId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLICK_KEY)

    alipay_inquery_refund_request = AlipayRefundQueryRequest()
    alipay_inquery_refund_request.path = "/ams/sandbox/api/v1/payments/inquiryRefund"
    alipay_inquery_refund_request.refund_request_id = paymentRefundRequestId


    rsp_body = default_alipay_client.execute(alipay_inquery_refund_request)

    alipay_inquery_refund_response = AlipayRefundQueryResponse(rsp_body)

    if alipay_inquery_refund_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_inquery_refund_response.refund_amount)
    else:
        print(alipay_inquery_refund_response.result.result_message)

def createPaymentSession():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLICK_KEY)

    alipay_create_session_request = AlipayCreateSessionRequest()
    alipay_create_session_request.path = "/ams/sandbox/api/v1/payments/createPaymentSession"
    alipay_create_session_request.payment_request_id = "python_test_payment_request_id_1212"
    alipay_create_session_request.payment_amount = Amount("SGD", "4200")
    alipay_create_session_request.product_code = ProductCodeType.CASHIER_PAYMENT
    paymentMethod = PaymentMethod()
    paymentMethod.payment_method_type = "SHOPEEPAY_SG"
    alipay_create_session_request.payment_method = paymentMethod

    buyer = Buyer()
    buyer.reference_buyer_id = "123456"

    order = Order()
    order.reference_order_id = "123456"
    order.order_description = "test"
    order.buyer = buyer
    alipay_create_session_request.order = order

    alipay_create_session_request.payment_redirect_url = "https://www.alipay.com"
    alipay_create_session_request.payment_notify_url = "https://www.alipay.com"

    rsp_body = default_alipay_client.execute(alipay_create_session_request)

    alipay_create_session_response = AlipayCreateSessionResponse(rsp_body)

    if alipay_create_session_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_create_session_response.payment_session_id)
    else:
        print(alipay_create_session_response.result.result_message)


# refund("202407311940108001001882A0209648393")
# pay()
createPaymentSession()
