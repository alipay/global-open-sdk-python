import uuid

from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.card_brand import CardBrand
from com.alipay.ams.api.model.card_payment_method_detail import CardPaymentMethodDetail
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.payment_method_detail import PaymentMethodDetail
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.model.terminal_type import TerminalType
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.request.vaulting.alipay_vaulting_payment_method_request import \
    AlipayVaultingPaymentMethodRequest
from com.alipay.ams.api.request.vaulting.alipay_vaulting_query_request import AlipayVaultingQueryRequest
from com.alipay.ams.api.request.vaulting.alipay_vaulting_session_request import AlipayVaultingSessionRequest
from com.alipay.ams.api.response.vaulting.alipay_vaulting_payment_method_response import \
    AlipayVaultingPaymentMethodResponse
from com.alipay.ams.api.response.vaulting.alipay_vaulting_query_response import AlipayVaultingQueryResponse
from com.alipay.ams.api.response.vaulting.alipay_vaulting_session_response import AlipayVaultingSessionResponse

GATEWAY_HOST = "https://open-sea.alipay.com"
CLIENT_ID = "SANDBOX_5YC31G2ZNMQK07357"
MERCHANT_PRIVATE_KEY = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDhnOLYh3Tte5ELNzD6kr6TSN+F4oXaNlnKgx2aGf/xSSHIh1k+wihv6HbwPAexdtjpDQAgwEv4YXpdH3erQLuy3oBIBVsdbXWg09TRttyBeM8FzbMru6qR1TceypEPhR9W4/hP9DZEmn9XZmR7xR9KStDKJdnqSNr578IVFvp3hXUt2HfwoHbUwwOPbu8a66th9b1PyNJ5DOdSoTj52tvFMOyfCmKOn9U/bwtcT/EGEJFlIj1QjBSwlEeCBDUVwwKlo2ttMP5Omy7i4Lxi5NKAMdw+Cru49FqGEf9B/JKfovd6EcwrnUeDfXVltNrPJjdr19WzatDh0k0wE/9QT6EnAgMBAAECggEAZsbQdDFo69KRpZlT36I/3NqisNwbe+esidum/Y+Aj8tv72jxF+zc/PXaUOAX5RkuASSh/Ul8kj7dvlRacJJBr1868xQ1iLdXkZdOaOazluuQ66TkTTTlpB+MR6Oh538OYsfhU5L9sczr28XSWqvW8EIa0SvjFJ5x2tAFCxR3r0AqXFrRteHSPYI01sle9ynCq3frBQwX481N/T0YvDQNFiRw+YlzJwJsZqPooFA2H/o+AL+LQED7eevnLYvevNS4GGVkWNO7gfKFHJA3RCMJgRqsXfxs2SG2cBx6YBYCQ7JurP8veMr3NBf/OOGCZln4zY4Vl5bTXe5vxeT5gzm18QKBgQD/jCH38x0AIjx0zwpZyvcp6C/2PohVjb6B/TbAiMmaIjpei06DCXHrDiObTLoxguZfmA+ypiPTZBOwFEDo7wDJ8khQwRMx9ydPMiaWoFCvl5iSke2vs/ONxdw02zRGj2uivgqjDf+94eTS8aSTJ+7kt1KLq4ZQf80Efywv+0xVnwKBgQDiAy5MMU8oDiSun8FoSBX3SomjdOX/tg4hMZ2PKYnXTJFUJ5bkjLhgdsPO5WGcFGsdReuweTzKteIRmS0zvdekVIpWFchflyeIM3+OuI1ZJJG6t28Xg3e8VOXCD917fjLnOOmH3f7PV/rj59wVM0yPvGStlAbPP0kwrcci8Wo3eQKBgQDE/ujctGwhw0KppUVMbRtWEeiPQitlEGzQ1jtT9t661DH82hT/DNPlqLOoL2DFdCxVeup3BH5PojFPJn3XUw9fnkdDAWPju6xw768xpIouooV6T8ZUETvqiaG0mVrWHg+SmD+o7My+OxpjxuXgjwMpC201wFc9TRflpIeSwX1Z7wKBgQCpUgy7VC2jKoVctZ6ly2t5akQXSxqMKg4H3C3X9RypSVmPHGG1M59l1VP4imxIDBv7QEjEWu+qRfzphkIRA2asXBGPUJ5eztT0+u/TMnvijr0GjyoRCZMIaun+KviY7gCgrUh3W17sY1M4rpl44Ie5H0ClscIwPY9NgsMvcIFMsQKBgG/XoSq4KjB+/SFdLTH4ITLb6Q8rvWOOyu6OvTBCgfxhq4R+rBP/40bvd1Ax5Eawfwq/GDfUL5jpzoaJGXGXDI90eXdeDOHZB7rq/+un9De1jPLGc1Ty7YT3SctYAvFw8jo0K65eckL7AaiGHk39eOXrWmJVVchOVlkX8TayiTgk"
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq7zEydi4Q2VvUIb1Mjpm/I2R3NVWcSMddlhvHYJADZ07YOGjvlQPbH3iixhLMnk1Y0tT7Sw7B1Ov1kXDGUhnui/YmGQBDbz9vg4iPDXA8OU7TaSsIk2BbP4+uZoortx2AZu/ABTGBDvyhLyJBkNplJ7196Np+IMaxi2RlT2NEAV4vFIurUcfFl5vvMliyV1SacvIyONkurzixSLirlKBl35t1mGm44xqh7M40tcMScgdF8pIdkzVz0nAnBcGb0aTeD3YLQmYFFmbQhWIe7MAa0BPEK7sxTJ1x1PbRUCHEXiZURnPjZTD7FBsTfLlcGOlOe0DXB7mrWm+AP+fVBjbAwIDAQAB"


def createVaultingSession():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_vaulting_session_request = AlipayVaultingSessionRequest()
    alipay_vaulting_session_request.vaulting_request_id = str(uuid.uuid4())
    alipay_vaulting_session_request.payment_method_type = "CARD"
    alipay_vaulting_session_request.vaulting_notification_url = "https://www.yourNotifyUrl.com"
    alipay_vaulting_session_request.redirect_url = "https://www.yourRedirectUrl.com"

    rsp_body = default_alipay_client.execute(alipay_vaulting_session_request)
    response = AlipayVaultingSessionResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_vaulting_session_request.vaulting_request_id)
        print(response.vaulting_session_id)
        print(response.vaulting_session_data)
        print(response.result.result_message)
    else:
        print(response.result.result_message)

def vaultPaymentMethod():
    alipayV_vaulting_payment_method_request = AlipayVaultingPaymentMethodRequest()
    alipayV_vaulting_payment_method_request.vaulting_request_id = str(uuid.uuid4())
    alipayV_vaulting_payment_method_request.vaulting_notification_url = "https://www.yourNotifyUrl.com"
    alipayV_vaulting_payment_method_request.redirect_url = "https://www.yourRedirectUrl.com"
    alipayV_vaulting_payment_method_request.merchant_region = "BR"

    paymentMethodDetail = PaymentMethodDetail()
    paymentMethodDetail.payment_method_type = "CARD"
    cardPaymentMethodDetail = CardPaymentMethodDetail()
    cardPaymentMethodDetail.card_no = "4111111111111111"
    cardPaymentMethodDetail.brand = CardBrand.VISA
    address = Address()
    address.city = "Sao Paulo"
    address.address1 = "Av. Paulista"
    address.address2 = "2000"
    address.zip_code = "01310-000"
    cardPaymentMethodDetail.address = address
    username = UserName()
    username.first_name = "JOHN"
    username.last_name = "SMITH"
    cardPaymentMethodDetail.user_name = username
    cardPaymentMethodDetail.expiry_year = "2025"
    cardPaymentMethodDetail.expiry_month = "12"
    cardPaymentMethodDetail.cvv = "123"
    paymentMethodDetail.card = cardPaymentMethodDetail
    alipayV_vaulting_payment_method_request.payment_method_detail = paymentMethodDetail

    env = Env()
    env.terminal_type = TerminalType.WEB
    alipayV_vaulting_payment_method_request.env = env

    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    rsp_body = default_alipay_client.execute(alipayV_vaulting_payment_method_request)
    response = AlipayVaultingPaymentMethodResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.result.result_message)
    else:
        print(response.result.result_message)

def inquireVaulting(vaultingRequestId):
    alipay_vaulting_query_request = AlipayVaultingQueryRequest()
    alipay_vaulting_query_request.vaulting_request_id = vaultingRequestId

    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    rsp_body = default_alipay_client.execute(alipay_vaulting_query_request)
    response = AlipayVaultingQueryResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.result.result_message)
    else:
        print(response.result.result_message)

# createVaultingSession()
vaultPaymentMethod()
# inquireVaulting("414c7492-78c7-4f61-89a2-2dc872ae0e0c")