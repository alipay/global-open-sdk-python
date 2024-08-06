from com.alipay.ams.api.model.dispute_evidence_format_type import DisputeEvidenceFormatType
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayDownloadDisputeEvidenceResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayDownloadDisputeEvidenceResponse, self).__init__()
        self.__dispute_evidence = None
        self.__dispute_evidence_format = None  # type:DisputeEvidenceFormatType
        self.parse_rsp_body(rsp_body)

    @property
    def dispute_evidence(self):
        return self.__dispute_evidence

    @property
    def dispute_evidence_format(self):
        return self.__dispute_evidence_format

    def parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipayDownloadDisputeEvidenceResponse, self).parse_rsp_body(rsp_body)
        if 'disputeEvidence' in rsp_dict:
            self.__dispute_evidence = rsp_dict['disputeEvidence']
        if 'disputeEvidenceFormat' in rsp_dict:
            self.__dispute_evidence_format = rsp_dict['disputeEvidenceFormat']
