import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySupplyDefenseDocumentRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySupplyDefenseDocumentRequest, self).__init__("/ams/api/v1/payments/supplyDefenseDocument") 

        self.__dispute_id = None  # type: str
        self.__dispute_evidence = None  # type: str
        

    @property
    def dispute_id(self):
        """
        The unique ID assigned by Antom to identify a dispute.  More information:  Maximum length: 64 characters
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value
    @property
    def dispute_evidence(self):
        """
        The dispute defense document that you prepare for defending the dispute, which is encoded in the Base64 format.  More information:  Maximum length: 1000000 characters
        """
        return self.__dispute_evidence

    @dispute_evidence.setter
    def dispute_evidence(self, value):
        self.__dispute_evidence = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "dispute_id") and self.dispute_id is not None:
            params['disputeId'] = self.dispute_id
        if hasattr(self, "dispute_evidence") and self.dispute_evidence is not None:
            params['disputeEvidence'] = self.dispute_evidence
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'disputeId' in response_body:
            self.__dispute_id = response_body['disputeId']
        if 'disputeEvidence' in response_body:
            self.__dispute_evidence = response_body['disputeEvidence']
