import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.dispute_evidence_result import DisputeEvidenceResult



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipaySupplyEvidenceResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__dispute_id = None  # type: str
        self.__evidence_results = None  # type: [DisputeEvidenceResult]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipaySupplyEvidenceResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def dispute_id(self):
        """
        The dispute ID, returned when resultStatus is S.
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value
    @property
    def evidence_results(self):
        """
        Per-tag results returned for partial success or tag-specific failures. Omitted for overall success and failures that do not identify individual tags.
        """
        return self.__evidence_results

    @evidence_results.setter
    def evidence_results(self, value):
        self.__evidence_results = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "dispute_id") and self.dispute_id is not None:
            params['disputeId'] = self.dispute_id
        if hasattr(self, "evidence_results") and self.evidence_results is not None:
            params['evidenceResults'] = self.evidence_results
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipaySupplyEvidenceResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'disputeId' in response_body:
            self.__dispute_id = response_body['disputeId']
        if 'evidenceResults' in response_body:
            self.__evidence_results = []
            for item in response_body['evidenceResults']:
                obj = DisputeEvidenceResult()
                obj.parse_rsp_body(item)
                self.__evidence_results.append(obj)
