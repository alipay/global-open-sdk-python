import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquiryStatementDetailRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquiryStatementDetailRequest, self).__init__("/ams/api/v1/aba/accounts/inquiryStatementDetail") 

        self.__statement_id = None  # type: str
        

    @property
    def statement_id(self):
        """Gets the statement_id of this AlipayInquiryStatementDetailRequest.
        
        """
        return self.__statement_id

    @statement_id.setter
    def statement_id(self, value):
        self.__statement_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "statement_id") and self.statement_id is not None:
            params['statementId'] = self.statement_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'statementId' in response_body:
            self.__statement_id = response_body['statementId']
