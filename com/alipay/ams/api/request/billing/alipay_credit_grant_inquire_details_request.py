import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditGrantInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditGrantInquireDetailsRequest, self).__init__("/ams/api/v1/meter/creditGrant/inquireDetails") 

        self.__credit_grant_id = None  # type: str
        

    @property
    def credit_grant_id(self):
        """
        The credit grant ID. Maximum length: 64 characters.
        """
        return self.__credit_grant_id

    @credit_grant_id.setter
    def credit_grant_id(self, value):
        self.__credit_grant_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_grant_id") and self.credit_grant_id is not None:
            params['creditGrantId'] = self.credit_grant_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditGrantId' in response_body:
            self.__credit_grant_id = response_body['creditGrantId']
