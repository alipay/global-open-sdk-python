import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySupplyEvidenceRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySupplyEvidenceRequest, self).__init__("/ams/api/v1/payments/supplyEvidence") 

        self.__dispute_id = None  # type: str
        self.__evidence_content = None  # type: {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
        

    @property
    def dispute_id(self):
        """
        The unique ID assigned by Antom to identify a dispute.
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value
    @property
    def evidence_content(self):
        """
        Evidence objects keyed by evidence tag. Submitting the same tag replaces its previously submitted content. Omit optional fields that have no value.
        """
        return self.__evidence_content

    @evidence_content.setter
    def evidence_content(self, value):
        self.__evidence_content = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "dispute_id") and self.dispute_id is not None:
            params['disputeId'] = self.dispute_id
        if hasattr(self, "evidence_content") and self.evidence_content is not None:
            params['evidenceContent'] = self.evidence_content
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'disputeId' in response_body:
            self.__dispute_id = response_body['disputeId']
        if 'evidenceContent' in response_body:
            self.__evidence_content = response_body['evidenceContent']
