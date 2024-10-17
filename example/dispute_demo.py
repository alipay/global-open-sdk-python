from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.dispute_evidence_type import DisputeEvidenceType
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.request.dispute.alipay_accept_dispute_request import AlipayAcceptDisputeRequest
from com.alipay.ams.api.request.dispute.alipay_download_dispute_evidence_request import \
    AlipayDownloadDisputeEvidenceRequest
from com.alipay.ams.api.request.dispute.alipay_supply_defense_document_request import AlipaySupplyDefenseDocumentRequest
from com.alipay.ams.api.response.dispute.alipay_accept_dispute_response import AlipayAcceptDisputeResponse
from com.alipay.ams.api.response.dispute.alipay_download_dispute_evidence_response import \
    AlipayDownloadDisputeEvidenceResponse
from com.alipay.ams.api.response.dispute.alipay_supply_defense_document_response import \
    AlipaySupplyDefenseDocumentResponse

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLIC_KEY = ""
CLIENT_ID = ""
GATEWAY_HOST = ""

def acceptDispute(disputeId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_accept_dispute_request = AlipayAcceptDisputeRequest()
    alipay_accept_dispute_request.dispute_id = disputeId

    rsp_body = default_alipay_client.execute(alipay_accept_dispute_request)

    response = AlipayAcceptDisputeResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.result.result_status.name)
        print(response.result.result_message)
        print(response.dispute_resolution_time)
    else:
        print(response.result.result_message)


def supplyDefenseDocument(disputeId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_supply_defense_document_request = AlipaySupplyDefenseDocumentRequest()
    alipay_supply_defense_document_request.dispute_id = disputeId
    alipay_supply_defense_document_request.dispute_evidence = "test"

    rsp_body = default_alipay_client.execute(alipay_supply_defense_document_request)

    response = AlipaySupplyDefenseDocumentResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.result.result_status.name)
        print(response.result.result_message)
        print(response.dispute_resolution_time)
    else:
        print(response.result.result_message)

def downloadDisputeEvidence(disputeId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_download_dispute_evidence_request = AlipayDownloadDisputeEvidenceRequest()
    alipay_download_dispute_evidence_request.dispute_id = disputeId
    alipay_download_dispute_evidence_request.dispute_evidence_type = DisputeEvidenceType.DISPUTE_EVIDENCE_TEMPLATE

    rsp_body = default_alipay_client.execute(alipay_download_dispute_evidence_request)

    response = AlipayDownloadDisputeEvidenceResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.result.result_status.name)
        print(response.result.result_message)
        print(response.dispute_evidence_format)
    else:
        print(response.result.result_message)
