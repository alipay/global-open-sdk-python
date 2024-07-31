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

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLICK_KEY = ""
CLIENT_ID = ""
GATEWAY_HOST = ""



def declare(paymentId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLICK_KEY)
    alipayCustomsDeclareRequest =  AlipayCustomsDeclareRequest()
    alipayCustomsDeclareRequest.path = "/ams/sandbox/api/v1/customs/declare"
    alipayCustomsDeclareRequest.declaration_request_id = "declaration_test_00001"
    alipayCustomsDeclareRequest.payment_id = paymentId
    alipayCustomsDeclareRequest.declaration_amount = Amount("CNY",100)
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
                                                    ALIPAY_PUBLICK_KEY)
        alipayCustomsQueryRequest = AlipayCustomsQueryRequest()
        alipayCustomsQueryRequest.path = "/ams/sandbox/api/v1/customs/inquiryDeclarationRequests"
        alipayCustomsQueryRequest.declaration_request_ids = declarationRequestIds

        rsp_body = default_alipay_client.execute(alipayCustomsQueryRequest)

        alipayCustomsQueryResponse = AlipayCustomsQueryResponse(rsp_body)
        if alipayCustomsQueryResponse.result.result_status.name == ResultStatusType.S.name:
            print(alipayCustomsQueryResponse.result.result_status)
        else:
            print(alipayCustomsQueryResponse.result.result_message)

declare("202407311940108001001887A0209760494")
# inquiryDeclaration(["declaration_test_00001"])