import uuid

from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.cancellation_type import CancellationType
from com.alipay.ams.api.model.customer_belongs_to import CustomerBelongsTo
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.order_info import OrderInfo
from com.alipay.ams.api.model.os_type import OsType
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.period_type import PeriodType
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.terminal_type import TerminalType
from com.alipay.ams.api.request.subscription.alipay_subscription_cancel_request import AlipaySubscriptionCancelRequest
from com.alipay.ams.api.request.subscription.alipay_subscription_change_request import AlipaySubscriptionChangeRequest
from com.alipay.ams.api.request.subscription.alipay_subscription_create_request import AlipaySubscriptionCreateRequest
from com.alipay.ams.api.response.subscription.alipay_subscription_cancel_response import \
    AlipaySubscriptionCancelResponse
from com.alipay.ams.api.response.subscription.alipay_subscription_change_response import \
    AlipaySubscriptionChangeResponse
from com.alipay.ams.api.response.subscription.alipay_subscription_create_response import \
    AlipaySubscriptionCreateResponse

GATEWAY_HOST = "https://open-sea.alipay.com"
CLIENT_ID = "SANDBOX_5YC31G2ZNMQK07357"
MERCHANT_PRIVATE_KEY = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDhnOLYh3Tte5ELNzD6kr6TSN+F4oXaNlnKgx2aGf/xSSHIh1k+wihv6HbwPAexdtjpDQAgwEv4YXpdH3erQLuy3oBIBVsdbXWg09TRttyBeM8FzbMru6qR1TceypEPhR9W4/hP9DZEmn9XZmR7xR9KStDKJdnqSNr578IVFvp3hXUt2HfwoHbUwwOPbu8a66th9b1PyNJ5DOdSoTj52tvFMOyfCmKOn9U/bwtcT/EGEJFlIj1QjBSwlEeCBDUVwwKlo2ttMP5Omy7i4Lxi5NKAMdw+Cru49FqGEf9B/JKfovd6EcwrnUeDfXVltNrPJjdr19WzatDh0k0wE/9QT6EnAgMBAAECggEAZsbQdDFo69KRpZlT36I/3NqisNwbe+esidum/Y+Aj8tv72jxF+zc/PXaUOAX5RkuASSh/Ul8kj7dvlRacJJBr1868xQ1iLdXkZdOaOazluuQ66TkTTTlpB+MR6Oh538OYsfhU5L9sczr28XSWqvW8EIa0SvjFJ5x2tAFCxR3r0AqXFrRteHSPYI01sle9ynCq3frBQwX481N/T0YvDQNFiRw+YlzJwJsZqPooFA2H/o+AL+LQED7eevnLYvevNS4GGVkWNO7gfKFHJA3RCMJgRqsXfxs2SG2cBx6YBYCQ7JurP8veMr3NBf/OOGCZln4zY4Vl5bTXe5vxeT5gzm18QKBgQD/jCH38x0AIjx0zwpZyvcp6C/2PohVjb6B/TbAiMmaIjpei06DCXHrDiObTLoxguZfmA+ypiPTZBOwFEDo7wDJ8khQwRMx9ydPMiaWoFCvl5iSke2vs/ONxdw02zRGj2uivgqjDf+94eTS8aSTJ+7kt1KLq4ZQf80Efywv+0xVnwKBgQDiAy5MMU8oDiSun8FoSBX3SomjdOX/tg4hMZ2PKYnXTJFUJ5bkjLhgdsPO5WGcFGsdReuweTzKteIRmS0zvdekVIpWFchflyeIM3+OuI1ZJJG6t28Xg3e8VOXCD917fjLnOOmH3f7PV/rj59wVM0yPvGStlAbPP0kwrcci8Wo3eQKBgQDE/ujctGwhw0KppUVMbRtWEeiPQitlEGzQ1jtT9t661DH82hT/DNPlqLOoL2DFdCxVeup3BH5PojFPJn3XUw9fnkdDAWPju6xw768xpIouooV6T8ZUETvqiaG0mVrWHg+SmD+o7My+OxpjxuXgjwMpC201wFc9TRflpIeSwX1Z7wKBgQCpUgy7VC2jKoVctZ6ly2t5akQXSxqMKg4H3C3X9RypSVmPHGG1M59l1VP4imxIDBv7QEjEWu+qRfzphkIRA2asXBGPUJ5eztT0+u/TMnvijr0GjyoRCZMIaun+KviY7gCgrUh3W17sY1M4rpl44Ie5H0ClscIwPY9NgsMvcIFMsQKBgG/XoSq4KjB+/SFdLTH4ITLb6Q8rvWOOyu6OvTBCgfxhq4R+rBP/40bvd1Ax5Eawfwq/GDfUL5jpzoaJGXGXDI90eXdeDOHZB7rq/+un9De1jPLGc1Ty7YT3SctYAvFw8jo0K65eckL7AaiGHk39eOXrWmJVVchOVlkX8TayiTgk"
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq7zEydi4Q2VvUIb1Mjpm/I2R3NVWcSMddlhvHYJADZ07YOGjvlQPbH3iixhLMnk1Y0tT7Sw7B1Ov1kXDGUhnui/YmGQBDbz9vg4iPDXA8OU7TaSsIk2BbP4+uZoortx2AZu/ABTGBDvyhLyJBkNplJ7196Np+IMaxi2RlT2NEAV4vFIurUcfFl5vvMliyV1SacvIyONkurzixSLirlKBl35t1mGm44xqh7M40tcMScgdF8pIdkzVz0nAnBcGb0aTeD3YLQmYFFmbQhWIe7MAa0BPEK7sxTJ1x1PbRUCHEXiZURnPjZTD7FBsTfLlcGOlOe0DXB7mrWm+AP+fVBjbAwIDAQAB"



def subscriptionsCreate():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_subscription_create_request = AlipaySubscriptionCreateRequest()
    alipay_subscription_create_request.subscription_request_id = str(uuid.uuid4())
    env = Env()
    env.client_ip = "1.1.1.1"
    env.os_type = OsType.IOS
    env.terminal_type = TerminalType.WEB
    alipay_subscription_create_request.env = env
    alipay_subscription_create_request.payment_amount = Amount("HKD", "100")
    #replace with your notify url
    #or configur your notify url https://dashboard.alipay.com/global-payments/developers/iNotifyNotification
    alipay_subscription_create_request.payment_notification_url = "https://www.yourNotifyUrl.com"

    period_rule = PeriodRule()
    period_rule.period_type = PeriodType.MONTH
    period_rule.period_count = 1
    alipay_subscription_create_request.period_rule = period_rule

    settlement_strategy = SettlementStrategy()
    settlement_strategy.settlement_currency = "USD"
    alipay_subscription_create_request.settlement_strategy = settlement_strategy

    alipay_subscription_create_request.subscription_description = "test subscription"
    alipay_subscription_create_request.subscription_start_time = "2024-10-16T00:00:00+08:00"
    alipay_subscription_create_request.subscription_end_time = "2024-10-17T17:00:00+08:00"
    alipay_subscription_create_request.subscription_expiry_time = "2024-10-18T00:00:00+08:00"
    alipay_subscription_create_request.subscription_notification_url = "https://www.yourNotifyUrl.com"

    order_info = OrderInfo()
    order_info.order_amount = Amount("HKD", "100")
    alipay_subscription_create_request.order_info = order_info
    payment_method = PaymentMethod()
    payment_method.payment_method_type = CustomerBelongsTo.ALIPAY_HK
    alipay_subscription_create_request.payment_method = payment_method

    alipay_subscription_create_request.subscription_redirect_url = "https://www.yourRedirectUrl.com"
    alipay_subscription_create_request.payment_notification_url = "https://www.yourNotifyUrl.com"
    alipay_subscription_create_request.subscription_notification_url = "https://www.yourNotifyUrl.com"

    rsp_body = default_alipay_client.execute(alipay_subscription_create_request)
    response = AlipaySubscriptionCreateResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_subscription_create_request.subscription_request_id)
        print(response.normal_url)
        print(response.result.result_status)
        print(response.result.result_message)
    else:
        print(response.result.result_message)

def subscriptionsChange(subscriptionId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_subscription_change_request = AlipaySubscriptionChangeRequest()
    alipay_subscription_change_request.subscription_id = subscriptionId
    alipay_subscription_change_request.subscription_change_request_id = str(uuid.uuid4())
    alipay_subscription_change_request.payment_amount_difference = Amount("HKD", "100")
    alipay_subscription_change_request.payment_amount = Amount("HKD", "100")
    period_rule = PeriodRule()
    period_rule.period_type = PeriodType.MONTH
    period_rule.period_count = 1
    alipay_subscription_change_request.period_rule = period_rule
    alipay_subscription_change_request.subscription_start_time = "2024-10-16T00:00:00+08:00"
    alipay_subscription_change_request.subscription_end_time = "2024-10-17T17:00:00+08:00"
    order_info = OrderInfo()
    order_info.order_amount = Amount("HKD", "100")
    alipay_subscription_change_request.order_info = order_info


    rsp_body = default_alipay_client.execute(alipay_subscription_change_request)
    response = AlipaySubscriptionChangeResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.result.result_message)
    else:
        print(response.result.result_message)

def subscriptionCancel(subscriptionId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_subscription_cancel_request = AlipaySubscriptionCancelRequest()
    alipay_subscription_cancel_request.subscription_id = subscriptionId
    alipay_subscription_cancel_request.cancellation_type = CancellationType.CANCEL

    rsp_body = default_alipay_client.execute(alipay_subscription_cancel_request)
    response = AlipaySubscriptionCancelResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.result.result_message)
    else:
        print(response.result.result_message)

subscriptionsCreate()
# subscriptionsChange("202410171900000000000001J0000010317")
# subscriptionCancel("202410171900000000000001J0000010317")