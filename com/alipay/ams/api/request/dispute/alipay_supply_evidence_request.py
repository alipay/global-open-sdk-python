import json
from com.alipay.ams.api.model. supply_evidence_content import SupplyEvidenceContent



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySupplyEvidenceRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySupplyEvidenceRequest, self).__init__("/ams/api/v1/payments/supplyEvidence") 

        self.__dispute_id = None  # type: str
        self.__evidence_content = None  # type: {str: (SupplyEvidenceContent,)}
        

    @property
    def dispute_id(self):
        """
        The Antom dispute ID. Cannot be empty. DISPUTE_NOT_FOUND_OR_NO_ACCESS is returned if it does not exist or belongs to another merchant.
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value
    @property
    def evidence_content(self):
        """
        Evidence keyed by evidenceTag, with the tag&#39;s field object as its value. Submit between 1 and 32 keys. Supported tags and their fields are described in SupplyEvidenceContent. Unsupported tags return EVIDENCE_TAG_NOT_SUPPORTED. Exceeding a collection or map limit rejects the entire request with CAPACITY_EXCEEDED; values are never silently truncated. Resubmitting the same disputeId and evidenceTag replaces the previously submitted tag content.
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
            self.__evidence_content = {}
            for key, value in response_body['evidenceContent'].items():
                obj = SupplyEvidenceContent()
                obj.parse_rsp_body(value)
                self.__evidence_content[key] = obj
