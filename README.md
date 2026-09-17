```
Language：Python  
Python version：2.7+  
Release ^1.6.0
Copyright：Ant financial services group  
```

#### Meter event upload

Install the optional HTTP/2 dependencies. This API requires Python 3.9 or later;
other SDK APIs retain the package's existing Python compatibility.

```bash
pip install "global-open-sdk-python[http2]"
```

`meter/createSession` uses the regular signed AMS transport. Use its session ID
to call `meter/uploadEvent` through `execute_with_headers`:

```python
# Requires Python 3.9+ and: pip install "global-open-sdk-python[http2]"
request = AlipayMeterUploadEventRequest()
request.meters = meters
response_body = default_alipay_client.execute_with_headers(
    request, {"X-Session-Id": session_id}
)
```

The SDK sends `meter/uploadEvent` to the gateway URL configured on the client,
without sandbox path rewriting, request signing, response signature verification,
or automatic retries. This API requires HTTP/2.

#### 1 The sample for pay 
```
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

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLIC_KEY = ""
CLIENT_ID = ""
GATEWAY_HOST = ""



default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                            ALIPAY_PUBLIC_KEY)

alipay_pay_request = AlipayPayRequest()

alipay_pay_request.product_code = ProductCodeType.AGREEMENT_PAYMENT
alipay_pay_request.payment_notify_url = "https://www.yourNotifyUrl.com"
alipay_pay_request.payment_redirect_url = "https://www.yourRedirectUrl.com"
alipay_pay_request.payment_request_id = "pay_python_test"

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
```

#### 2 If you don't care about HTTP calls,the sample for sign and verify  
```
from com.alipay.ams.api.tools.signature_tool import *

sign(http_method, path, client_id, req_time, req_body, merchant_private_key)
verify(http_method, path, client_id, rsp_time, rsp_body, rsp_signature, alipay_public_key)

```

## API Key authentication

See the [complete API Key example](example/api_key_example.py). From the repository root, run `python -m example.api_key_example`.

Initialize the client with your gateway URL and API Key; existing RSA usage remains supported.
This feature is available in the current source branch and has not been published yet.

Set `ANTOM_GATEWAY_URL` to your regional HTTPS gateway (for example,
`https://open-sea-global.alipay.com` for Asia), `ANTOM_API_KEY` to your key,
`ANTOM_REDIRECT_URL` to your checkout return URL, and `ANTOM_NOTIFY_URL` to your
notification endpoint. The application reads these variables; the SDK does not load them automatically.

The example creates a CARD payment session for USD 1.00 (`100` minor units),
with USD settlement. Use a merchant configured for this combination and a key
with createPaymentSession permission. Replace the example client IP with the
buyer's IP in your application. Exceptions propagate to the caller; a normal
response must still be checked for business success.

```python
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
```

- Standard and Restricted keys use the same client. TEST/PROD in the key selects
  the request environment; do not add a sandbox path to the gateway URL.
- Creating a session does not mean payment is complete. Notifications still use
  the existing signature verification mechanism.
- File upload is not supported with API Key authentication.
