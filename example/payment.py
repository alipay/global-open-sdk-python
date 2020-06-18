#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.amount import Amount
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
from com.alipay.ams.api.request.pay.alipay_pay_request import AlipayPayRequest
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
from com.alipay.ams.api.response.pay.alipay_refund_response import AlipayRefundResponse


MERCHANT_PRIVATE_KEY = ""

ALIPAY_PUBLICK_KEY = ""


def pay():
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", "T_111222333", MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)

    alipay_pay_request = AlipayPayRequest()
    alipay_pay_request.path = "/ams/sandbox/api/v1/payments/pay"

    alipay_pay_request.product_code = ProductCodeType.AGREEMENT_PAYMENT
    alipay_pay_request.payment_notify_url = "https://www.taobao.com"
    alipay_pay_request.payment_redirect_url = "https://www.taobao.com?param1=sl"
    alipay_pay_request.payment_request_id = "pay_python_test_06"

    payment_method = PaymentMethod()
    payment_method.payment_method_type = "GCASH"
    payment_method.payment_method_id = "20200404095550158596535057754730166962669640ZMvNAaATop"
    alipay_pay_request.payment_method = payment_method

    amount = Amount("PHP", "10000")
    alipay_pay_request.payment_amount = amount

    order = Order()
    order.reference_order_id = "102775765675669"
    order.order_description = "Mi Band 3 Wrist Strap Metal Screwless Stainless Steel For Xiaomi Mi Band 3"
    order.order_amount = amount

    goods_arr = []
    good = Goods()
    good.goods_brand = "goods_brand"
    good.goods_name = "goods_name"
    goods_arr.append(good)
    order.goods = goods_arr

    merchant = Merchant()
    merchant.merchant_mcc = "merchantMcc"
    merchant.reference_merchant_id = "referenceMerchantId"

    order.merchant = merchant
    alipay_pay_request.order = order

    settlement_strategy = SettlementStrategy()
    settlement_strategy.settlement_currency = "USD"
    alipay_pay_request.settlement_strategy = settlement_strategy

    env = Env()
    env.terminal_type = TerminalType.APP
    env.os_type = OsType.IOS
    alipay_pay_request.env = env

    # alipay_pay_request.is_authorization = "true"

    print(alipay_pay_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_pay_request)

    alipay_pay_response = AlipayPayResponse(rsp_body)

    if alipay_pay_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_pay_response.payment_id)
        print(alipay_pay_response.payment_create_time)
    else:
        print(alipay_pay_response.result.result_message)


def pay_consult():
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", "T_111222333", MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)
    pay_consult_request = AlipayPayConsultRequest()
    pay_consult_request.path = "/ams/sandbox/api/v1/payments/consult"
    pay_consult_request.product_code = ProductCodeType.CASHIER_PAYMENT
    pay_consult_request.customer_id = "aac_123445566"

    payment_amount = Amount("PHP", "30000")
    pay_consult_request.payment_amount = payment_amount

    env = Env()
    env.terminal_type = TerminalType.APP
    env.os_types = OsType.IOS
    env.device_token_id = "60e62513a925bf5575111cad5976835b"
    env.client_ip = "127.0.0.1"
    pay_consult_request.env = env

    rsp_body = default_alipay_client.execute(pay_consult_request)

    pay_consult_response = AlipayPayConsultResponse(rsp_body)
    if pay_consult_response.result.result_status.name != ResultStatusType.F.name:
        print(pay_consult_response.payment_method_infos)
    else:
        print(pay_consult_response.result.result_message)


def pay_cancel():

    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", "T_111222333", MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)

    alipay_pay_cancel_request = AlipayPayCancelRequest()
    alipay_pay_cancel_request.path = "/ams/sandbox/api/v1/payments/cancel"
    alipay_pay_cancel_request.payment_id = "080314159117139490377916696018735674lFdfeTMZmW202006010001926017"

    rsp_body = default_alipay_client.execute(alipay_pay_cancel_request)

    alipay_pay_cancel_response = AlipayPayCancelResponse(rsp_body)

    if alipay_pay_cancel_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_pay_cancel_response.cancel_time)
    else:
        print(alipay_pay_cancel_response.result.result_message)


def pay_query():

    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", "T_111222333", MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)

    alipay_pay_query_request = AlipayPayQueryRequest()
    alipay_pay_query_request.path = "/ams/sandbox/api/v1/payments/inquiryPayment"
    alipay_pay_query_request.payment_id = "908151415881481145864730154037503460TDoUNGArzf202004290001696669"

    rsp_body = default_alipay_client.execute(alipay_pay_query_request)

    alipay_pay_query_response = AlipayPayQueryResponse(rsp_body)

    if alipay_pay_query_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_pay_query_response.payment_id)
    else:
        print(alipay_pay_query_response.result.result_message)


def capture():
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", "T_111222333", MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLICK_KEY)

    alipay_capture_request = AlipayCaptureRequest()
    alipay_capture_request.path = "/ams/sandbox/api/v1/payments/capture"
    alipay_capture_request.payment_id = "035622159167498257460439798959626996HSfvJALvrw202006080001969186"
    alipay_capture_request.capture_request_id = "python_test_03"

    capture_amount = Amount("PHP", "10000")
    alipay_capture_request.capture_amount = capture_amount

    print(alipay_capture_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_capture_request)

    alipay_capture_response = AlipayCaptureResponse(rsp_body)

    if alipay_capture_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_capture_response.capture_id)
    else:
        print(alipay_capture_response.result.result_message)


def refund():
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", "T_111222333", MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLICK_KEY)

    alipay_refund_request = AlipayRefundRequest()
    alipay_refund_request.path = "/ams/sandbox/api/v1/payments/refund"
    alipay_refund_request.refund_request_id = "python_test_refund_01"
    alipay_refund_request.payment_id = "060511159168271108778369768472747804ykDUtomosY202006080001966591"

    refund_amount = Amount("PHP", "9000")
    alipay_refund_request.refund_amount = refund_amount

    print(alipay_refund_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_refund_request)

    alipay_refund_response = AlipayRefundResponse(rsp_body)

    if alipay_refund_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_refund_response.refund_request_id)
    else:
        print(alipay_refund_response.result.result_message)


refund()

