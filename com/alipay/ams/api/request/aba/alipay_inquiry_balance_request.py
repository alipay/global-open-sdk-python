import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquiryBalanceRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquiryBalanceRequest, self).__init__("/ams/v1/aba/accounts/inquiryBalance") 

        self.__currency_list = None  # type: [str]
        self.__accesstoken = None  # type: str
        self.__customer_id = None  # type: str
        

    @property
    def currency_list(self):
        """
        A list containing 3-character ISO-4217 currency codes representing the currency that the merchant queries.
        """
        return self.__currency_list

    @currency_list.setter
    def currency_list(self, value):
        self.__currency_list = value
    @property
    def accesstoken(self):
        """Gets the accesstoken of this AlipayInquiryBalanceRequest.
        
        """
        return self.__accesstoken

    @accesstoken.setter
    def accesstoken(self, value):
        self.__accesstoken = value
    @property
    def customer_id(self):
        """Gets the customer_id of this AlipayInquiryBalanceRequest.
        
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "currency_list") and self.currency_list is not None:
            params['currencyList'] = self.currency_list
        if hasattr(self, "accesstoken") and self.accesstoken is not None:
            params['accesstoken'] = self.accesstoken
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currencyList' in response_body:
            self.__currency_list = response_body['currencyList']
        if 'accesstoken' in response_body:
            self.__accesstoken = response_body['accesstoken']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
