import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayAuthRevokeTokenRequest(AlipayRequest):
    def __init__(self):
        super(AlipayAuthRevokeTokenRequest, self).__init__("/ams/api/v1/authorizations/revoke") 

        self.__access_token = None  # type: str
        self.__extend_info = None  # type: str
        self.__merchant_account_id = None  # type: str
        

    @property
    def access_token(self):
        """
        The access token that is used to access the corresponding scope of the user resource.   More information:  Maximum length: 128 characters
        """
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayAuthRevokeTokenRequest.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def merchant_account_id(self):
        """
        The merchant account ID for 2C2P Replatform scenario.
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "access_token") and self.access_token is not None:
            params['accessToken'] = self.access_token
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'accessToken' in response_body:
            self.__access_token = response_body['accessToken']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
