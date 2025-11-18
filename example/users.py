#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.request.users.alipay_user_query_info_request import (
    AlipayUserQueryInfoRequest,
)
from com.alipay.ams.api.response.users.alipay_user_query_info_response import (
    AlipayUserQueryInfoResponse,
)
from com.alipay.ams.api.request.users.alipay_init_authentication_request import (
    AlipayInitAuthenticationRequest,
)
from com.alipay.ams.api.response.users.alipay_init_authentication_response import (
    AlipayInitAuthenticationResponse,
)
from com.alipay.ams.api.request.users.alipay_verify_authentication_request import (
    AlipayVerifyAuthenticationRequest,
)
from com.alipay.ams.api.response.users.alipay_verify_authentication_response import (
    AlipayVerifyAuthenticationResponse,
)
from com.alipay.ams.api.model.authentication_type import AuthenticationType
from com.alipay.ams.api.model.authentication_channel_type import (
    AuthenticationChannelType,
)
from com.alipay.ams.api.model.user_identity_type import UserIdentityType

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLIC_KEY = ""
CLIENT_ID = ""


def user_query_info():
    default_alipay_client = DefaultAlipayClient(
        "https://open-na.alipay.com", CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY
    )

    alipay_user_query_info_request = AlipayUserQueryInfoRequest()
    alipay_user_query_info_request.path = "/ams/sandbox/api/v1/users/inquiryUserInfo"
    alipay_user_query_info_request.access_token = (
        "2020060417341615912632560749423400649135650RJsliOKYQP"
    )

    rsp_body = default_alipay_client.execute(alipay_user_query_info_request)

    alipay_user_query_info_response = AlipayUserQueryInfoResponse(rsp_body)

    if (
        alipay_user_query_info_response.result.result_status.name
        != ResultStatusType.F.name
    ):
        print(alipay_user_query_info_response.user_login_id)
    else:
        print(alipay_user_query_info_response.result.result_message)


def init_authentication():
    default_alipay_client = DefaultAlipayClient(
        "https://open-na.alipay.com", CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY
    )
    alipay_init_authentication_request = AlipayInitAuthenticationRequest()
    alipay_init_authentication_request.path = (
        "/ams/sandbox/api/v1/users/initAuthentication"
    )
    alipay_init_authentication_request.authentication_channel_type = (
        AuthenticationChannelType.SMS
    )
    alipay_init_authentication_request.authentication_request_id = "test_1"
    alipay_init_authentication_request.authentication_type = AuthenticationType.OTP
    alipay_init_authentication_request.user_identity_type = (
        UserIdentityType.WALLET_TOKEN
    )
    alipay_init_authentication_request.user_identity_value = (
        "2020042910435415881282340824710273532915573saFBMrdXVH"
    )

    rsp_body = default_alipay_client.execute(alipay_init_authentication_request)

    alipay_init_authentication_response = AlipayInitAuthenticationResponse(rsp_body)

    if (
        alipay_init_authentication_response.result.result_status.name
        != ResultStatusType.F.name
    ):
        print(alipay_init_authentication_response.authentication_request_id)
    else:
        print(alipay_init_authentication_response.result.result_message)


def verify_authentication():
    default_alipay_client = DefaultAlipayClient(
        "https://open-na.alipay.com", CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY
    )
    alipay_verify_authentication_request = AlipayVerifyAuthenticationRequest()
    alipay_verify_authentication_request.path = (
        "/ams/sandbox/api/v1/users/verifyAuthentication"
    )
    alipay_verify_authentication_request.authentication_request_id = "test_1"
    alipay_verify_authentication_request.authentication_type = AuthenticationType.OTP
    alipay_verify_authentication_request.authentication_value = "666"

    rsp_body = default_alipay_client.execute(alipay_verify_authentication_request)

    alipay_verify_authentication_response = AlipayVerifyAuthenticationResponse(rsp_body)

    if (
        alipay_verify_authentication_response.result.result_status.name
        != ResultStatusType.F.name
    ):
        print(alipay_verify_authentication_response.is_passed)
    else:
        print(alipay_verify_authentication_response.result.result_message)
