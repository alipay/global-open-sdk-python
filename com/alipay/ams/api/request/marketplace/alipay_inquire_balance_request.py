import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireBalanceRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireBalanceRequest, self).__init__("/ams/api/v1/accounts/inquireBalance") 

        self.__reference_merchant_id = None  # type: str
        

    @property
    def reference_merchant_id(self):
        """
        The unique ID that is assigned by the marketplace to identify the sub-merchant.  Specify this parameter if you inquire about the account balance of the sub-merchant. If you leave this parameter empty or do not specify this parameter, the default action is to inquire about the account balance of the marketplace.    More information:  Maximum length: 32 characters
        """
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id is not None:
            params['referenceMerchantId'] = self.reference_merchant_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceMerchantId' in response_body:
            self.__reference_merchant_id = response_body['referenceMerchantId']
