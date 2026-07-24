import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditGrantUpdateExpiryRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditGrantUpdateExpiryRequest, self).__init__("/ams/api/v1/meter/creditGrant/updateExpiry") 

        self.__credit_grant_id = None  # type: str
        self.__expiry_mode = None  # type: str
        self.__expiry_date_time = None  # type: str
        

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
    def expiry_mode(self):
        """
        The expiry mode. Maximum length: 16 characters.
        """
        return self.__expiry_mode

    @expiry_mode.setter
    def expiry_mode(self, value):
        self.__expiry_mode = value
    @property
    def expiry_date_time(self):
        """
        The expiry date time. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__expiry_date_time

    @expiry_date_time.setter
    def expiry_date_time(self, value):
        self.__expiry_date_time = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_grant_id") and self.credit_grant_id is not None:
            params['creditGrantId'] = self.credit_grant_id
        if hasattr(self, "expiry_mode") and self.expiry_mode is not None:
            params['expiryMode'] = self.expiry_mode
        if hasattr(self, "expiry_date_time") and self.expiry_date_time is not None:
            params['expiryDateTime'] = self.expiry_date_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditGrantId' in response_body:
            self.__credit_grant_id = response_body['creditGrantId']
        if 'expiryMode' in response_body:
            self.__expiry_mode = response_body['expiryMode']
        if 'expiryDateTime' in response_body:
            self.__expiry_date_time = response_body['expiryDateTime']
