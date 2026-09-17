"""Create one sandbox payment session using an authorized Restricted TEST key."""

import json
import os
import uuid

from com.alipay.ams.api.api_key_alipay_client import ApiKeyAlipayClient
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.terminal_type import TerminalType
from com.alipay.ams.api.request.pay.alipay_payment_session_request import (
    AlipayPaymentSessionRequest,
)
from com.alipay.ams.api.response.pay.alipay_payment_session_response import (
    AlipayPaymentSessionResponse,
)


def required_env(name):
    value = os.environ.get(name)
    if not value or not value.strip():
        raise ValueError("Missing environment variable: " + name)
    return value


def main():
    key = required_env("ANTOM_API_KEY")
    if not key.startswith("irak_TEST_"):
        raise ValueError("This example requires a Restricted TEST key")
    client = ApiKeyAlipayClient(required_env("ANTOM_GATEWAY_URL"), key)
    notify_url = required_env("ANTOM_NOTIFY_URL")
    amount = Amount(currency="USD", value="100")
    order = Order()
    order.reference_order_id = "example-order-" + uuid.uuid4().hex
    order.order_description = "API Key sandbox example"
    order.order_amount = amount
    method = PaymentMethod()
    method.payment_method_type = "CARD"
    factor = PaymentFactor()
    factor.is_authorization = False
    settlement = SettlementStrategy()
    settlement.settlement_currency = "USD"
    env = Env()
    env.terminal_type = TerminalType.WEB
    env.client_ip = "127.0.0.1"
    request = AlipayPaymentSessionRequest()
    request.product_code = ProductCodeType.CASHIER_PAYMENT
    request.product_scene = "CHECKOUT_PAYMENT"
    request.payment_request_id = "example-session-" + uuid.uuid4().hex
    request.order = order
    request.payment_amount = amount
    request.payment_method = method
    request.payment_factor = factor
    request.settlement_strategy = settlement
    request.env = env
    # Use a separate redirect page in a real integration.
    request.payment_redirect_url = notify_url
    request.payment_notify_url = notify_url

    response_body = client.execute(request)
    response = AlipayPaymentSessionResponse(response_body)
    # Local debugging only: the response contains payment-session credentials.
    print(json.dumps(json.loads(response_body), indent=2, ensure_ascii=False))
    if (
        response.result is None
        or response.result.result_status != ResultStatusType.S
        or response.result.result_code != "SUCCESS"
    ):
        raise RuntimeError("createPaymentSession failed; see the response result")


if __name__ == "__main__":
    main()
