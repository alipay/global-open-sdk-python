# Read ANTOM_GATEWAY_URL, ANTOM_API_KEY, ANTOM_REDIRECT_URL and ANTOM_NOTIFY_URL from the environment.
# Use a TEST key with createPaymentSession permission for sandbox testing.
# This example creates a CARD session for USD 1.00; it does not complete a payment.
# Replace 127.0.0.1 with the buyer's IP. Notifications require a reachable endpoint.

import os
import uuid
from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.payment_factor import PaymentFactor
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.product_code_type import ProductCodeType
from com.alipay.ams.api.model.terminal_type import TerminalType
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.request.pay.alipay_payment_session_request import AlipayPaymentSessionRequest
from com.alipay.ams.api.response.pay.alipay_payment_session_response import AlipayPaymentSessionResponse

def main():
    client = DefaultAlipayClient(
        gateway_url=os.environ["ANTOM_GATEWAY_URL"],
        api_key=os.environ["ANTOM_API_KEY"],
    )
    amount = Amount(currency="USD", value="100")
    order = Order()
    order.reference_order_id = str(uuid.uuid4())
    order.order_description = "API Key example"
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
    request.payment_request_id = str(uuid.uuid4())
    request.order = order
    request.payment_amount = amount
    request.payment_method = method
    request.payment_factor = factor
    request.settlement_strategy = settlement
    request.env = env
    request.payment_redirect_url = os.environ["ANTOM_REDIRECT_URL"]
    request.payment_notify_url = os.environ["ANTOM_NOTIFY_URL"]

    # Transport errors propagate as exceptions; also check the business result.
    response = AlipayPaymentSessionResponse(client.execute(request))
    result = response.result
    if result is None or result.result_status != ResultStatusType.S or result.result_code != "SUCCESS":
        raise RuntimeError("Session creation was not successful: " +
                           (result.result_code if result else "missing result"))
    if not response.payment_session_id:
        raise RuntimeError("Missing paymentSessionId")
    # Use response.payment_session_data or the returned URL with your checkout.
    print("Payment session created")


if __name__ == "__main__":
    main()
