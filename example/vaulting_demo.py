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

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLIC_KEY = ""
CLIENT_ID = ""
GATEWAY_HOST = ""

def createVaultingSession():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_vaulting_session_request = AlipayVaultingSessionRequest()
    alipay_vaulting_session_request.vaulting_request_id = str(uuid.uuid4())
    alipay_vaulting_session_request.payment_method_type = "CARD"
    alipay_vaulting_session_request.vaulting_notification_url = "http://www.yourNotifyUrl.com"
    alipay_vaulting_session_request.redirect_url = "http://www.yourRedirectUrl.com"

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
    alipayV_vaulting_payment_method_request.vaulting_notification_url = "http://www.yourNotifyUrl.com"
    alipayV_vaulting_payment_method_request.redirect_url = "http://www.yourRedirectUrl.com"
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
# vaultPaymentMethod()
inquireVaulting("414c7492-78c7-4f61-89a2-2dc872ae0e0c")