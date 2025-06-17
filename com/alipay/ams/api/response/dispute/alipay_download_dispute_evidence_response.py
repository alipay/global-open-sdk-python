import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.dispute_evidence_format_type import DisputeEvidenceFormatType



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayDownloadDisputeEvidenceResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__dispute_evidence = None  # type: str
        self.__dispute_evidence_format = None  # type: DisputeEvidenceFormatType
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayDownloadDisputeEvidenceResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def dispute_evidence(self):
        """
        The dispute evidence that is encoded in the Based64 format. Decode the Base64 document to get the Word or PDF file.  Note: This prameter is returned when the value of resultCode is SUCCESS.  More information:  Maximum length: 1000000 characters 
        """
        return self.__dispute_evidence

    @dispute_evidence.setter
    def dispute_evidence(self, value):
        self.__dispute_evidence = value
    @property
    def dispute_evidence_format(self):
        """Gets the dispute_evidence_format of this AlipayDownloadDisputeEvidenceResponse.
        
        """
        return self.__dispute_evidence_format

    @dispute_evidence_format.setter
    def dispute_evidence_format(self, value):
        self.__dispute_evidence_format = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "dispute_evidence") and self.dispute_evidence is not None:
            params['disputeEvidence'] = self.dispute_evidence
        if hasattr(self, "dispute_evidence_format") and self.dispute_evidence_format is not None:
            params['disputeEvidenceFormat'] = self.dispute_evidence_format
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayDownloadDisputeEvidenceResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'disputeEvidence' in response_body:
            self.__dispute_evidence = response_body['disputeEvidence']
        if 'disputeEvidenceFormat' in response_body:
            dispute_evidence_format_temp = DisputeEvidenceFormatType.value_of(response_body['disputeEvidenceFormat'])
            self.__dispute_evidence_format = dispute_evidence_format_temp
