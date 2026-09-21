# Antom SDK for Python

Latest release: **1.6.1**

## Installation

```sh
python -m pip install --upgrade global-open-sdk-python
```

Use Python 3 for the examples below.

## Quick start

- **API Key:** follow the [setup guide](docs/api-key-client.md) and run the [sandbox example](example/api_key_payment_session.py).
- **RSA:** follow the [configuration](#rsa-configuration) and [inline example](#payment) below.
- Browse [more examples](example) and the [API documentation](https://global.alipay.com/docs/).

API Key and RSA clients share request/response models. File uploads and notification
verification still require RSA credentials.

### API Key client

Set `ANTOM_GATEWAY_URL` and `ANTOM_API_KEY` in your server environment.
This initializes the client; see the [setup guide](docs/api-key-client.md) for a
complete sandbox request and its additional configuration.

```python
import os
from com.alipay.ams.api.api_key_alipay_client import ApiKeyAlipayClient

client = ApiKeyAlipayClient(
    os.environ["ANTOM_GATEWAY_URL"], os.environ["ANTOM_API_KEY"])
```

### RSA configuration

Before using the RSA client, prepare these values from your Antom integration:

```properties
gatewayUrl=your_regional_https_gateway
clientId=your_client_id
merchantPrivateKey=your_merchant_private_key
alipayPublicKey=your_antom_public_key
```

The examples read them from `ANTOM_GATEWAY_URL`, `ANTOM_CLIENT_ID`,
`ANTOM_MERCHANT_PRIVATE_KEY`, and `ANTOM_PUBLIC_KEY`, respectively.
Keep keys in server-side configuration. Replace sample order data and callback
URLs with your own values before sending a request.

### Payment

Save as `payment_example.py` and configure the four environment variables above.

```python
import os
import uuid
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

MERCHANT_PRIVATE_KEY = os.environ["ANTOM_MERCHANT_PRIVATE_KEY"]
ALIPAY_PUBLIC_KEY = os.environ["ANTOM_PUBLIC_KEY"]
CLIENT_ID = os.environ["ANTOM_CLIENT_ID"]
GATEWAY_HOST = os.environ["ANTOM_GATEWAY_URL"]



default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                            ALIPAY_PUBLIC_KEY)

alipay_pay_request = AlipayPayRequest()

alipay_pay_request.product_code = ProductCodeType.CASHIER_PAYMENT
alipay_pay_request.payment_notify_url = "https://www.yourNotifyUrl.com"
alipay_pay_request.payment_redirect_url = "https://www.yourRedirectUrl.com"
alipay_pay_request.payment_request_id = str(uuid.uuid4())

payment_method = PaymentMethod()
payment_method.payment_method_type = "GCASH"
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

## Upgrade notes

Gateway responses with `resultStatus S` must be signed; responses with only one
of the signature and response-time headers are rejected.

Billing integrations: `availableAmount` now uses `Amount`; the `AvailableAmount`
model has been removed.

## Meter event upload

Install the optional HTTP/2 dependencies. This API requires Python 3.9 or later;
other SDK APIs retain the package's existing Python compatibility.

```bash
pip install "global-open-sdk-python[http2]"
```

`meter/createSession` uses the regular signed AMS transport. Use its session ID
to call `meter/uploadEvent` through `execute_with_headers`:

The fragment below assumes an initialized RSA client, a valid session ID from
`meter/createSession`, and a populated collection of meter event batches.

```python
# Requires Python 3.9+ and: pip install "global-open-sdk-python[http2]"
from com.alipay.ams.api.request.billing.alipay_meter_upload_event_request import AlipayMeterUploadEventRequest

request = AlipayMeterUploadEventRequest()
request.meters = meters
response_body = default_alipay_client.execute_with_headers(
    request, {"X-Session-Id": session_id}
)
```

The SDK sends `meter/uploadEvent` to the gateway URL configured on the client,
without sandbox path rewriting, request signing, response signature verification,
or automatic retries. This API requires HTTP/2.

## Advanced usage

### Sign and verify without the HTTP client

Use the exact transmitted path, timestamp, body, and configured keys. The variables
below come from your request/response. Verify notifications before parsing their
original body.

```python
from com.alipay.ams.api.tools.signature_tool import sign, verify

signature = sign(http_method, path, client_id, request_time, request_body, merchant_private_key)
verified = verify(
    http_method, path, client_id, response_time, response_body, response_signature, alipay_public_key
)
```

## Support

For integration questions, contact overseas_support@service.alibaba.com.
