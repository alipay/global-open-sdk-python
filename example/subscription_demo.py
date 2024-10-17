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

GATEWAY_HOST = "https://open-sea-global.alipay.com"
CLIENT_ID = "SANDBOX_5YBZ1G2ZHUPS06086"
MERCHANT_PRIVATE_KEY = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/PqnrI3zdRMIAqIFzOlNkop2o/jMVva22j05W7/Sv78PU7SMmwQGObmw9COcm2nX0N1ix0dlqH2lmXRmoE69hElXcWnDEzcSHpNe1HtM0eWgOLozrwpa0PXue0O0cxvEhZxuWqKUMrwf3cV9dziTzbmmK70wP5PcIstjqy8SK/LyMZ/W5q1xRrBlRmXQvAOnx79A9ok0m8H99ziwOye9aDr8Tb0LEVBxeUVB+XwniiHYDbxRjY1awsYOaK66W+gZcx4ORXx8xDjDPX6q45RNIuJRgSXdqsQQxEk5tKSHpSj8LSqz67Dr/Jyq8MVJn30VXL+uX+yHyeCNKe5tf+2IHAgMBAAECggEATw+DxU5tbzfej9EZet5Q3ViQnu0/hyxb5Q3HUA9w807GgX7rOjkuAIjLvEuy65AClUxQIWrkW4fS1duFIMPKi/G9hxPobKO4LG9MMXclzxqllr9NyKUwEiEcuuIaM/xWcP2kHRto6B5vx66ZwzjWc8BgZ2xX4HZCXdk57Y8BmIb9IejKgIYtyUWrYuGkvQsh+SHWX5CZVEgGlCy3uYOMDj0BkSJOrLc3yW6octGuVQLEgFx3EEB0ZJMThUB+gxInj/pl06iwCuWbZXxkRkXHrllz1gOvfGwhtccwPHrKGJDHDY+OIIgsd4eEDJjySdMjx2hydmCbxbRBxEIK5iW/kQKBgQD10ReS5F6T+QDgc2VdscZo/64PLldXtH71sTJoIat8XK0oPNSbkzJzPpuWwj6hpSKO1/8Hsq52gM2IjJBSx2q7nD9azVrBevl/aLhAmM4OX7ahSDaQZx3yHwL40onXAZIVDECyi1zRLtBDgKaGgLJdIZ2lzgo7Jhcw8J3S/Np52QKBgQDHKtTAl43dKuTV5QZ7PwItrgcjOvm6LzhuI+xbM5YnAOLcp7g9UP6LLI5kB00UkB9fDnoePVbwEgl0ShIKHCWBU++F4mjPoayoTQCKBzNuvK5wKklVPoVDsnwhGXIS8fkBmU5VtjArB0kCAoIpR5HEzIaCiaZZGWMiZ0kfBdBu3wKBgQC+ZRJ2Qw4CXMZSEu87b/u2zfq6ZXFfTD1d/b6GKzYQ4BN6bAtc6NkVrDOExLUQLMCklSZChyJcRQ1tKzqJ8013POFRamdWHvLqvWihF/nZ5kalizJADK6EH4MEyMXc06mbRd9Cq3Db0P+cmSPiYAJG4keh6gHAqJMj4+rKRfDOmQKBgCbdp9jRemCffzpyT/p7CDzLyh7I4nS/xD5SCkyd235PAPZYUG6+wH1+O2cvuY36tfSBybje9Xkxu+CSl8SbS4JaU9KHpTZncV8Cb8l/sDy62zuONPNKmQzl5q063vTtfU8fkJbPT8UFzexzetz9V2fVFaahn/GhL6RGDZHdO5h3AoGALV6PDVsB6VjJtE8RA8Bpsmwl6ytLDiEljFImkzXQzq4/gTz2NJXjKGnUC70pae1Z1OWMHoZWqFgg1YAxVHeFZBqLQ88HwmCwwRjLkUyFxPRlJ7y4V8olBsDY57E1j03MNENaal88bRpvKUoZRTh8HCbk6BV8e6o+2vMf3HUe2Ss="
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkJIL3C7NSzSQxP1DNK0Grktr5G5bMEj4ndEIBnSyFv8+e6ytS+G1+ch7EdZ4Lt7KYUGoFW1wJKyTS8V5UBMJTWxAkdc2uX3GrQiWbPvReMl3sNa3SC9Kmi8ofVKQdpAt8aZZaTLxmti0YyCh8zUTddE9AOeMZi8xvzC8chcGbfx4FA5meFGkPEBeYfxZgQzCjXnMJ/A2JFeh5g2443pfAq/caoIamcnTcA9qhJCMaqDyXb2pxXmg/VOClhqhaOjj4dnxzYKln1YNJw02SaVT9zjkNJkbY2QzCjEV0NdG/QLCQ/xBkFlDvlJ+nyCiTySqVOuJXGCos1cljMoYJGZLXQIDAQAB"


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