from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.customs_info import CustomsInfo
from com.alipay.ams.api.model.merchant_customs_info import MerchantCustomsInfo
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.request.declare.alipay_customs_declare_request import AlipayCustomsDeclareRequest
from com.alipay.ams.api.request.declare.alipay_customs_query_request import AlipayCustomsQueryRequest
from com.alipay.ams.api.response.declare.alipay_customs_declare_response import AlipayCustomsDeclareResponse
from com.alipay.ams.api.response.declare.alipay_customs_query_response import AlipayCustomsQueryResponse

GATEWAY_HOST = "https://open-sea.alipay.com"
CLIENT_ID = "SANDBOX_5YC31G2ZNMQK07357"
MERCHANT_PRIVATE_KEY = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDhnOLYh3Tte5ELNzD6kr6TSN+F4oXaNlnKgx2aGf/xSSHIh1k+wihv6HbwPAexdtjpDQAgwEv4YXpdH3erQLuy3oBIBVsdbXWg09TRttyBeM8FzbMru6qR1TceypEPhR9W4/hP9DZEmn9XZmR7xR9KStDKJdnqSNr578IVFvp3hXUt2HfwoHbUwwOPbu8a66th9b1PyNJ5DOdSoTj52tvFMOyfCmKOn9U/bwtcT/EGEJFlIj1QjBSwlEeCBDUVwwKlo2ttMP5Omy7i4Lxi5NKAMdw+Cru49FqGEf9B/JKfovd6EcwrnUeDfXVltNrPJjdr19WzatDh0k0wE/9QT6EnAgMBAAECggEAZsbQdDFo69KRpZlT36I/3NqisNwbe+esidum/Y+Aj8tv72jxF+zc/PXaUOAX5RkuASSh/Ul8kj7dvlRacJJBr1868xQ1iLdXkZdOaOazluuQ66TkTTTlpB+MR6Oh538OYsfhU5L9sczr28XSWqvW8EIa0SvjFJ5x2tAFCxR3r0AqXFrRteHSPYI01sle9ynCq3frBQwX481N/T0YvDQNFiRw+YlzJwJsZqPooFA2H/o+AL+LQED7eevnLYvevNS4GGVkWNO7gfKFHJA3RCMJgRqsXfxs2SG2cBx6YBYCQ7JurP8veMr3NBf/OOGCZln4zY4Vl5bTXe5vxeT5gzm18QKBgQD/jCH38x0AIjx0zwpZyvcp6C/2PohVjb6B/TbAiMmaIjpei06DCXHrDiObTLoxguZfmA+ypiPTZBOwFEDo7wDJ8khQwRMx9ydPMiaWoFCvl5iSke2vs/ONxdw02zRGj2uivgqjDf+94eTS8aSTJ+7kt1KLq4ZQf80Efywv+0xVnwKBgQDiAy5MMU8oDiSun8FoSBX3SomjdOX/tg4hMZ2PKYnXTJFUJ5bkjLhgdsPO5WGcFGsdReuweTzKteIRmS0zvdekVIpWFchflyeIM3+OuI1ZJJG6t28Xg3e8VOXCD917fjLnOOmH3f7PV/rj59wVM0yPvGStlAbPP0kwrcci8Wo3eQKBgQDE/ujctGwhw0KppUVMbRtWEeiPQitlEGzQ1jtT9t661DH82hT/DNPlqLOoL2DFdCxVeup3BH5PojFPJn3XUw9fnkdDAWPju6xw768xpIouooV6T8ZUETvqiaG0mVrWHg+SmD+o7My+OxpjxuXgjwMpC201wFc9TRflpIeSwX1Z7wKBgQCpUgy7VC2jKoVctZ6ly2t5akQXSxqMKg4H3C3X9RypSVmPHGG1M59l1VP4imxIDBv7QEjEWu+qRfzphkIRA2asXBGPUJ5eztT0+u/TMnvijr0GjyoRCZMIaun+KviY7gCgrUh3W17sY1M4rpl44Ie5H0ClscIwPY9NgsMvcIFMsQKBgG/XoSq4KjB+/SFdLTH4ITLb6Q8rvWOOyu6OvTBCgfxhq4R+rBP/40bvd1Ax5Eawfwq/GDfUL5jpzoaJGXGXDI90eXdeDOHZB7rq/+un9De1jPLGc1Ty7YT3SctYAvFw8jo0K65eckL7AaiGHk39eOXrWmJVVchOVlkX8TayiTgk"
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq7zEydi4Q2VvUIb1Mjpm/I2R3NVWcSMddlhvHYJADZ07YOGjvlQPbH3iixhLMnk1Y0tT7Sw7B1Ov1kXDGUhnui/YmGQBDbz9vg4iPDXA8OU7TaSsIk2BbP4+uZoortx2AZu/ABTGBDvyhLyJBkNplJ7196Np+IMaxi2RlT2NEAV4vFIurUcfFl5vvMliyV1SacvIyONkurzixSLirlKBl35t1mGm44xqh7M40tcMScgdF8pIdkzVz0nAnBcGb0aTeD3YLQmYFFmbQhWIe7MAa0BPEK7sxTJ1x1PbRUCHEXiZURnPjZTD7FBsTfLlcGOlOe0DXB7mrWm+AP+fVBjbAwIDAQAB"



def declare(paymentId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipayCustomsDeclareRequest = AlipayCustomsDeclareRequest()
    alipayCustomsDeclareRequest.declaration_request_id = "declaration_test_00001"
    alipayCustomsDeclareRequest.payment_id = paymentId
    alipayCustomsDeclareRequest.declaration_amount = Amount("CNY", 100)
    merchantCustomsInfo = MerchantCustomsInfo()
    merchantCustomsInfo.merchant_customs_code = "amsdemoskr"
    merchantCustomsInfo.merchant_customs_name = "amsdemo"
    alipayCustomsDeclareRequest.merchant_customs_info = merchantCustomsInfo
    alipayCustomsDeclareRequest.split_order = "false"
    customs = CustomsInfo()
    customs.region = "CN"
    customs.customs_code = "ZONGSHU"
    alipayCustomsDeclareRequest.customs = customs
    buyerCertificate = Certificate()
    holderName = UserName()
    holderName.first_name = "f"
    holderName.last_name = "l"
    holderName.full_name = "guodong.wzj"
    holderName.middle_name = "m"
    buyerCertificate.holder_name = holderName
    buyerCertificate.certificate_no = "123456789"
    buyerCertificate.certificate_type = "ID_CARD"
    alipayCustomsDeclareRequest.buyer_certificate = buyerCertificate

    rsp_body = default_alipay_client.execute(alipayCustomsDeclareRequest)

    alipayCustomsDeclareResponse = AlipayCustomsDeclareResponse(rsp_body)
    if alipayCustomsDeclareResponse.result.result_status.name == ResultStatusType.S.name:
        print(alipayCustomsDeclareResponse.customs_payment_id)
    else:
        print(alipayCustomsDeclareResponse.result.result_message)


def inquiryDeclaration(declarationRequestIds):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLIC_KEY)
    alipayCustomsQueryRequest = AlipayCustomsQueryRequest()
    alipayCustomsQueryRequest.declaration_request_ids = declarationRequestIds

    rsp_body = default_alipay_client.execute(alipayCustomsQueryRequest)

    alipayCustomsQueryResponse = AlipayCustomsQueryResponse(rsp_body)
    if alipayCustomsQueryResponse.result.result_status.name == ResultStatusType.S.name:
        print(alipayCustomsQueryResponse.result.result_status)
    else:
        print(alipayCustomsQueryResponse.result.result_message)


declare("202407311940108001001887A0209760494")
# inquiryDeclaration(["declaration_test_00001"])
