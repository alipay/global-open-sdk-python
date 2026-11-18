import json
from com.alipay.ams.api.model.dispute_evidence_type import DisputeEvidenceType



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayDownloadDisputeEvidenceRequest(AlipayRequest):
    def __init__(self):
        super(AlipayDownloadDisputeEvidenceRequest, self).__init__("/ams/api/v1/payments/downloadDisputeEvidence") 

        self.__dispute_id = None  # type: str
        self.__dispute_evidence_type = None  # type: DisputeEvidenceType
        

    @property
    def dispute_id(self):
        """
        The unique ID that is assigned by Antom to identify a dispute.  More information:  Maximum length: 64 characters
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value
    @property
    def dispute_evidence_type(self):
        """Gets the dispute_evidence_type of this AlipayDownloadDisputeEvidenceRequest.
        
        """
        return self.__dispute_evidence_type

    @dispute_evidence_type.setter
    def dispute_evidence_type(self, value):
        self.__dispute_evidence_type = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "dispute_id") and self.dispute_id is not None:
            params['disputeId'] = self.dispute_id
        if hasattr(self, "dispute_evidence_type") and self.dispute_evidence_type is not None:
            params['disputeEvidenceType'] = self.dispute_evidence_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'disputeId' in response_body:
            self.__dispute_id = response_body['disputeId']
        if 'disputeEvidenceType' in response_body:
            dispute_evidence_type_temp = DisputeEvidenceType.value_of(response_body['disputeEvidenceType'])
            self.__dispute_evidence_type = dispute_evidence_type_temp
