import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayVaultingQueryRequest(AlipayRequest):
    def __init__(self):
        super(AlipayVaultingQueryRequest, self).__init__("/ams/api/v1/vaults/inquireVaulting") 

        self.__vaulting_request_id = None  # type: str
        self.__merchant_account_id = None  # type: str
        

    @property
    def vaulting_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a card vaulting request.  More information about this field  This field is an API idempotency field. For vaulting requests that are initiated with the same value of vaultingRequestId and reach a final status of S or F, the same result is to be returned for the request. More information:  Maximum length: 64 characters
        """
        return self.__vaulting_request_id

    @vaulting_request_id.setter
    def vaulting_request_id(self, value):
        self.__vaulting_request_id = value
    @property
    def merchant_account_id(self):
        """
        Merchant account ID for 2C2P integration scenario
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
        if hasattr(self, "vaulting_request_id") and self.vaulting_request_id is not None:
            params['vaultingRequestId'] = self.vaulting_request_id
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'vaultingRequestId' in response_body:
            self.__vaulting_request_id = response_body['vaultingRequestId']
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
