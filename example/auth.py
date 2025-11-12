#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.model.grant_type import GrantType
from com.alipay.ams.api.model.scope_type import ScopeType
from com.alipay.ams.api.model.customer_belongs_to import CustomerBelongsTo
from com.alipay.ams.api.model.os_type import OsType
from com.alipay.ams.api.model.terminal_type import TerminalType
from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.request.auth.alipay_auth_apply_token_request import AlipayAuthApplyTokenRequest
from com.alipay.ams.api.request.auth.alipay_auth_consult_request import AlipayAuthConsultRequest
from com.alipay.ams.api.request.auth.alipay_auth_query_token_request import AlipayAuthQueryTokenRequest
from com.alipay.ams.api.response.auth.alipay_auth_apply_token_response import AlipayAuthApplyTokenResponse
from com.alipay.ams.api.response.auth.alipay_auth_query_token_response import AlipayAuthQueryTokenResponse
from com.alipay.ams.api.response.auth.alipay_auth_consult_response import AlipayAuthConsultResponse
from com.alipay.ams.api.request.auth.alipay_auth_revoke_token_request import AlipayAuthRevokeTokenRequest
from com.alipay.ams.api.response.auth.alipay_auth_revoke_token_response import AlipayAuthRevokeTokenResponse

GATEWAY_HOST = "https://open-sea.alipay.com"
CLIENT_ID = "SANDBOX_5YC31G2ZNMQK07357"
MERCHANT_PRIVATE_KEY = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDhnOLYh3Tte5ELNzD6kr6TSN+F4oXaNlnKgx2aGf/xSSHIh1k+wihv6HbwPAexdtjpDQAgwEv4YXpdH3erQLuy3oBIBVsdbXWg09TRttyBeM8FzbMru6qR1TceypEPhR9W4/hP9DZEmn9XZmR7xR9KStDKJdnqSNr578IVFvp3hXUt2HfwoHbUwwOPbu8a66th9b1PyNJ5DOdSoTj52tvFMOyfCmKOn9U/bwtcT/EGEJFlIj1QjBSwlEeCBDUVwwKlo2ttMP5Omy7i4Lxi5NKAMdw+Cru49FqGEf9B/JKfovd6EcwrnUeDfXVltNrPJjdr19WzatDh0k0wE/9QT6EnAgMBAAECggEAZsbQdDFo69KRpZlT36I/3NqisNwbe+esidum/Y+Aj8tv72jxF+zc/PXaUOAX5RkuASSh/Ul8kj7dvlRacJJBr1868xQ1iLdXkZdOaOazluuQ66TkTTTlpB+MR6Oh538OYsfhU5L9sczr28XSWqvW8EIa0SvjFJ5x2tAFCxR3r0AqXFrRteHSPYI01sle9ynCq3frBQwX481N/T0YvDQNFiRw+YlzJwJsZqPooFA2H/o+AL+LQED7eevnLYvevNS4GGVkWNO7gfKFHJA3RCMJgRqsXfxs2SG2cBx6YBYCQ7JurP8veMr3NBf/OOGCZln4zY4Vl5bTXe5vxeT5gzm18QKBgQD/jCH38x0AIjx0zwpZyvcp6C/2PohVjb6B/TbAiMmaIjpei06DCXHrDiObTLoxguZfmA+ypiPTZBOwFEDo7wDJ8khQwRMx9ydPMiaWoFCvl5iSke2vs/ONxdw02zRGj2uivgqjDf+94eTS8aSTJ+7kt1KLq4ZQf80Efywv+0xVnwKBgQDiAy5MMU8oDiSun8FoSBX3SomjdOX/tg4hMZ2PKYnXTJFUJ5bkjLhgdsPO5WGcFGsdReuweTzKteIRmS0zvdekVIpWFchflyeIM3+OuI1ZJJG6t28Xg3e8VOXCD917fjLnOOmH3f7PV/rj59wVM0yPvGStlAbPP0kwrcci8Wo3eQKBgQDE/ujctGwhw0KppUVMbRtWEeiPQitlEGzQ1jtT9t661DH82hT/DNPlqLOoL2DFdCxVeup3BH5PojFPJn3XUw9fnkdDAWPju6xw768xpIouooV6T8ZUETvqiaG0mVrWHg+SmD+o7My+OxpjxuXgjwMpC201wFc9TRflpIeSwX1Z7wKBgQCpUgy7VC2jKoVctZ6ly2t5akQXSxqMKg4H3C3X9RypSVmPHGG1M59l1VP4imxIDBv7QEjEWu+qRfzphkIRA2asXBGPUJ5eztT0+u/TMnvijr0GjyoRCZMIaun+KviY7gCgrUh3W17sY1M4rpl44Ie5H0ClscIwPY9NgsMvcIFMsQKBgG/XoSq4KjB+/SFdLTH4ITLb6Q8rvWOOyu6OvTBCgfxhq4R+rBP/40bvd1Ax5Eawfwq/GDfUL5jpzoaJGXGXDI90eXdeDOHZB7rq/+un9De1jPLGc1Ty7YT3SctYAvFw8jo0K65eckL7AaiGHk39eOXrWmJVVchOVlkX8TayiTgk"
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq7zEydi4Q2VvUIb1Mjpm/I2R3NVWcSMddlhvHYJADZ07YOGjvlQPbH3iixhLMnk1Y0tT7Sw7B1Ov1kXDGUhnui/YmGQBDbz9vg4iPDXA8OU7TaSsIk2BbP4+uZoortx2AZu/ABTGBDvyhLyJBkNplJ7196Np+IMaxi2RlT2NEAV4vFIurUcfFl5vvMliyV1SacvIyONkurzixSLirlKBl35t1mGm44xqh7M40tcMScgdF8pIdkzVz0nAnBcGb0aTeD3YLQmYFFmbQhWIe7MAa0BPEK7sxTJ1x1PbRUCHEXiZURnPjZTD7FBsTfLlcGOlOe0DXB7mrWm+AP+fVBjbAwIDAQAB"



def apply_token(authCode):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    # 申请token
    alipay_auth_apply_token_request = AlipayAuthApplyTokenRequest()

    alipay_auth_apply_token_request.grant_type = GrantType.AUTHORIZATION_CODE
    alipay_auth_apply_token_request.customer_belongs_to = "ALIPAY_CN"
    alipay_auth_apply_token_request.merchant_region = "SG"
    alipay_auth_apply_token_request.auth_code = authCode

    rsp_body = default_alipay_client.execute(alipay_auth_apply_token_request)

    alipay_auth_apply_token_response = AlipayAuthApplyTokenResponse(rsp_body)

    if alipay_auth_apply_token_response.result.result_code == "SUCCESS":
        print(alipay_auth_apply_token_response.access_token)
    else:
        print(alipay_auth_apply_token_response.result.result_message)


def query_token():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)

    # 查询token
    alipay_auth_query_token_request = AlipayAuthQueryTokenRequest()
    alipay_auth_query_token_request.access_token = "2020042910435415881282340824710273532915573saFBMrdXVH"

    rsp_body = default_alipay_client.execute(alipay_auth_query_token_request)

    alipay_auth_query_token_response = AlipayAuthQueryTokenResponse(rsp_body)

    if alipay_auth_query_token_response.result.result_code == "SUCCESS":
        print(alipay_auth_query_token_response.access_token)
    else:
        print(alipay_auth_query_token_response.result.result_message)


def auth_consult():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)

    alipay_auth_consult_request = AlipayAuthConsultRequest()
    alipay_auth_consult_request.auth_redirect_url = "https://www.yourRedirectUrl.com"
    alipay_auth_consult_request.auth_state = "663A8FA9-D836-56EE-8AA1-dd1F6F6811f989DC7"
    alipay_auth_consult_request.customer_belongs_to = CustomerBelongsTo.ALIPAY_CN
    alipay_auth_consult_request.auth_client_id = "SM_0001"
    alipay_auth_consult_request.os_type = OsType.ANDROID

    alipay_auth_consult_request.os_version = "6.6.6"

    scopes = [ScopeType.AGREEMENT_PAY]
    alipay_auth_consult_request.scopes = scopes

    alipay_auth_consult_request.terminal_type = TerminalType.APP

    rsp_body = default_alipay_client.execute(alipay_auth_consult_request)

    alipay_auth_consult_response = AlipayAuthConsultResponse(rsp_body)

    if alipay_auth_consult_response.result.result_code == "SUCCESS":
        print(alipay_auth_consult_response.auth_url)
        print(alipay_auth_consult_response.normal_url)
    else:
        print(alipay_auth_consult_response.result.result_message)


def revoke_token(accessToken):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLIC_KEY)
    alipay_revoke_token_request = AlipayAuthRevokeTokenRequest()
    alipay_revoke_token_request.access_token = accessToken

    rsp_body = default_alipay_client.execute(alipay_revoke_token_request)

    alipay_auth_revoke_token_response = AlipayAuthRevokeTokenResponse(rsp_body)

    if alipay_auth_revoke_token_response.result.result_code == "SUCCESS":
        print(alipay_auth_revoke_token_response.extend_info)
    else:
        print(alipay_auth_revoke_token_response.result.result_message)


auth_consult()
# apply_token("281001139396884133901370")
# revoke_token("28288803001156671722394041000cUJRjjdzzo171000759")
