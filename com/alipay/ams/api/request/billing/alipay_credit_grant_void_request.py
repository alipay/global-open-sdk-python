import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditGrantVoidRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditGrantVoidRequest, self).__init__("/ams/api/v1/meter/creditGrant/void") 

        self.__credit_grant_id = None  # type: str
        self.__void_reason = None  # type: str
        

    @property
    def credit_grant_id(self):
        """
        The credit grant ID. Maximum length: 64 characters.
        """
        return self.__credit_grant_id

    @credit_grant_id.setter
    def credit_grant_id(self, value):
        self.__credit_grant_id = value
    @property
    def void_reason(self):
        """
        The void reason. Maximum length: 1024 characters.
        """
        return self.__void_reason

    @void_reason.setter
    def void_reason(self, value):
        self.__void_reason = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_grant_id") and self.credit_grant_id is not None:
            params['creditGrantId'] = self.credit_grant_id
        if hasattr(self, "void_reason") and self.void_reason is not None:
            params['voidReason'] = self.void_reason
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditGrantId' in response_body:
            self.__credit_grant_id = response_body['creditGrantId']
        if 'voidReason' in response_body:
            self.__void_reason = response_body['voidReason']
