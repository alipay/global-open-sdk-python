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

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLIC_KEY = ""
CLIENT_ID = ""
GATEWAY_HOST = ""

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
    alipay_subscription_create_request.payment_notification_url = "http://www.yourNotifyUrl.com"

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
    alipay_subscription_create_request.subscription_notification_url = "http://www.yourNotifyUrl.com"

    order_info = OrderInfo()
    order_info.order_amount = Amount("HKD", "100")
    alipay_subscription_create_request.order_info = order_info
    payment_method = PaymentMethod()
    payment_method.payment_method_type = CustomerBelongsTo.ALIPAY_HK
    alipay_subscription_create_request.payment_method = payment_method

    alipay_subscription_create_request.subscription_redirect_url = "http://www.yourRedirectUrl.com"
    alipay_subscription_create_request.payment_notification_url = "http://www.yourNotifyUrl.com"
    alipay_subscription_create_request.subscription_notification_url = "http://www.yourNotifyUrl.com"

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

# subscriptionsCreate()
# subscriptionsChange("202410171900000000000001J0000010317")
subscriptionCancel("202410171900000000000001J0000010317")