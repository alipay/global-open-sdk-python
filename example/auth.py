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

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLIC_KEY = ""
CLIENT_ID = ""
GATEWAY_HOST = ""


def apply_token(authCode):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    # 申请token
    alipay_auth_apply_token_request = AlipayAuthApplyTokenRequest()

    alipay_auth_apply_token_request.path = '/ams/sandbox/api/v1/authorizations/applyToken'
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
    alipay_auth_query_token_request.path = '/ams/sandbox/api/v1/authorizations/query'
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
    alipay_auth_consult_request.path = "/ams/sandbox/api/v1/authorizations/consult"
    alipay_auth_consult_request.auth_redirect_url = "https://www.yourRedirectUrl.com/?param1=567&param2=123"
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
    alipay_revoke_token_request.path = "/ams/sandbox/api/v1/authorizations/revoke"
    alipay_revoke_token_request.access_token = accessToken

    rsp_body = default_alipay_client.execute(alipay_revoke_token_request)

    alipay_auth_revoke_token_response = AlipayAuthRevokeTokenResponse(rsp_body)

    if alipay_auth_revoke_token_response.result.result_code == "SUCCESS":
        print(alipay_auth_revoke_token_response.extend_info)
    else:
        print(alipay_auth_revoke_token_response.result.result_message)


# auth_consult()
# apply_token("281001139396884133901370")
revoke_token("28288803001156671722394041000cUJRjjdzzo171000759")
