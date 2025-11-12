#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from random import random

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


GATEWAY_HOST = "https://open-sea.alipay.com"
CLIENT_ID = "SANDBOX_5YC31G2ZNMQK07357"
MERCHANT_PRIVATE_KEY = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDhnOLYh3Tte5ELNzD6kr6TSN+F4oXaNlnKgx2aGf/xSSHIh1k+wihv6HbwPAexdtjpDQAgwEv4YXpdH3erQLuy3oBIBVsdbXWg09TRttyBeM8FzbMru6qR1TceypEPhR9W4/hP9DZEmn9XZmR7xR9KStDKJdnqSNr578IVFvp3hXUt2HfwoHbUwwOPbu8a66th9b1PyNJ5DOdSoTj52tvFMOyfCmKOn9U/bwtcT/EGEJFlIj1QjBSwlEeCBDUVwwKlo2ttMP5Omy7i4Lxi5NKAMdw+Cru49FqGEf9B/JKfovd6EcwrnUeDfXVltNrPJjdr19WzatDh0k0wE/9QT6EnAgMBAAECggEAZsbQdDFo69KRpZlT36I/3NqisNwbe+esidum/Y+Aj8tv72jxF+zc/PXaUOAX5RkuASSh/Ul8kj7dvlRacJJBr1868xQ1iLdXkZdOaOazluuQ66TkTTTlpB+MR6Oh538OYsfhU5L9sczr28XSWqvW8EIa0SvjFJ5x2tAFCxR3r0AqXFrRteHSPYI01sle9ynCq3frBQwX481N/T0YvDQNFiRw+YlzJwJsZqPooFA2H/o+AL+LQED7eevnLYvevNS4GGVkWNO7gfKFHJA3RCMJgRqsXfxs2SG2cBx6YBYCQ7JurP8veMr3NBf/OOGCZln4zY4Vl5bTXe5vxeT5gzm18QKBgQD/jCH38x0AIjx0zwpZyvcp6C/2PohVjb6B/TbAiMmaIjpei06DCXHrDiObTLoxguZfmA+ypiPTZBOwFEDo7wDJ8khQwRMx9ydPMiaWoFCvl5iSke2vs/ONxdw02zRGj2uivgqjDf+94eTS8aSTJ+7kt1KLq4ZQf80Efywv+0xVnwKBgQDiAy5MMU8oDiSun8FoSBX3SomjdOX/tg4hMZ2PKYnXTJFUJ5bkjLhgdsPO5WGcFGsdReuweTzKteIRmS0zvdekVIpWFchflyeIM3+OuI1ZJJG6t28Xg3e8VOXCD917fjLnOOmH3f7PV/rj59wVM0yPvGStlAbPP0kwrcci8Wo3eQKBgQDE/ujctGwhw0KppUVMbRtWEeiPQitlEGzQ1jtT9t661DH82hT/DNPlqLOoL2DFdCxVeup3BH5PojFPJn3XUw9fnkdDAWPju6xw768xpIouooV6T8ZUETvqiaG0mVrWHg+SmD+o7My+OxpjxuXgjwMpC201wFc9TRflpIeSwX1Z7wKBgQCpUgy7VC2jKoVctZ6ly2t5akQXSxqMKg4H3C3X9RypSVmPHGG1M59l1VP4imxIDBv7QEjEWu+qRfzphkIRA2asXBGPUJ5eztT0+u/TMnvijr0GjyoRCZMIaun+KviY7gCgrUh3W17sY1M4rpl44Ie5H0ClscIwPY9NgsMvcIFMsQKBgG/XoSq4KjB+/SFdLTH4ITLb6Q8rvWOOyu6OvTBCgfxhq4R+rBP/40bvd1Ax5Eawfwq/GDfUL5jpzoaJGXGXDI90eXdeDOHZB7rq/+un9De1jPLGc1Ty7YT3SctYAvFw8jo0K65eckL7AaiGHk39eOXrWmJVVchOVlkX8TayiTgk"
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq7zEydi4Q2VvUIb1Mjpm/I2R3NVWcSMddlhvHYJADZ07YOGjvlQPbH3iixhLMnk1Y0tT7Sw7B1Ov1kXDGUhnui/YmGQBDbz9vg4iPDXA8OU7TaSsIk2BbP4+uZoortx2AZu/ABTGBDvyhLyJBkNplJ7196Np+IMaxi2RlT2NEAV4vFIurUcfFl5vvMliyV1SacvIyONkurzixSLirlKBl35t1mGm44xqh7M40tcMScgdF8pIdkzVz0nAnBcGb0aTeD3YLQmYFFmbQhWIe7MAa0BPEK7sxTJ1x1PbRUCHEXiZURnPjZTD7FBsTfLlcGOlOe0DXB7mrWm+AP+fVBjbAwIDAQAB"



def pay():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)

    alipay_pay_request = AlipayPayRequest()

    alipay_pay_request.product_code = ProductCodeType.CASHIER_PAYMENT
    alipay_pay_request.payment_notify_url = "https://www.yourNotifyUrl.com"
    alipay_pay_request.payment_redirect_url = "https://www.yourRedirectUrl.com"
    alipay_pay_request.payment_request_id = "pay_python_test" + str(uuid.uuid4())
    payment_method = PaymentMethod()
    payment_method.payment_method_type = "ALIPAY_CN"
    payment_method.payment_method_id = str(uuid.uuid4())
    alipay_pay_request.payment_method = payment_method

    amount = Amount("CNY", "10000")
    alipay_pay_request.payment_amount = amount

    order = Order()
    order.reference_order_id = str(uuid.uuid4())
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
    merchant.reference_merchant_id = str(uuid.uuid4())

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
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    pay_consult_request = AlipayPayConsultRequest()
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

    pay_consult_request.allowed_payment_method_regions = ["HK", "US", "CN"]

    paymentFactor = PaymentFactor()
    paymentFactor.presentment_mode = "BUNDLE"
    pay_consult_request.payment_factor = paymentFactor

    rsp_body = default_alipay_client.execute(pay_consult_request)

    pay_consult_response = AlipayPayConsultResponse(rsp_body)
    if pay_consult_response.result.result_status.name != ResultStatusType.F.name:
        print(pay_consult_response.payment_options)
    else:
        print(pay_consult_response.result.result_message)


def pay_cancel(paymentId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)

    alipay_pay_cancel_request = AlipayPayCancelRequest()
    alipay_pay_cancel_request.payment_id = paymentId

    rsp_body = default_alipay_client.execute(alipay_pay_cancel_request)

    alipay_pay_cancel_response = AlipayPayCancelResponse(rsp_body)

    if alipay_pay_cancel_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_pay_cancel_response.cancel_time)
    else:
        print(alipay_pay_cancel_response.result.result_message)


def pay_query(paymenId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)

    alipay_pay_query_request = AlipayPayQueryRequest()
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
                                                ALIPAY_PUBLIC_KEY)

    alipay_capture_request = AlipayCaptureRequest()
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
                                                ALIPAY_PUBLIC_KEY)

    alipay_refund_request = AlipayRefundRequest()
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
                                                ALIPAY_PUBLIC_KEY)

    alipay_inquery_refund_request = AlipayRefundQueryRequest()
    alipay_inquery_refund_request.refund_request_id = paymentRefundRequestId

    rsp_body = default_alipay_client.execute(alipay_inquery_refund_request)

    alipay_inquery_refund_response = AlipayRefundQueryResponse(rsp_body)

    if alipay_inquery_refund_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_inquery_refund_response.refund_amount)
    else:
        print(alipay_inquery_refund_response.result.result_message)


def createPaymentSession():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLIC_KEY)

    alipay_create_session_request = AlipayCreateSessionRequest()
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

    alipay_create_session_request.payment_redirect_url = "https://www.yourRedirectUrl.com"
    alipay_create_session_request.payment_notify_url = "https://www.yourNotifyUrl.com"

    rsp_body = default_alipay_client.execute(alipay_create_session_request)

    alipay_create_session_response = AlipayCreateSessionResponse(rsp_body)

    if alipay_create_session_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_create_session_response.payment_session_id)
    else:
        print(alipay_create_session_response.result.result_message)


# refund("202407311940108001001882A0209648393")
pay()
# createPaymentSession()
