```
Language：Python  
Python version：2.7+  
Releass ^1.4.23
Copyright：Ant financial services group  
```

#### 1 The sample for pay 
```
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", client_id, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)

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
