import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireSubscriptionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireSubscriptionRequest, self).__init__("/ams/api/v1/subscriptions/inquireSubscription") 

        self.__merchant_account_id = None  # type: str
        self.__subscription_id = None  # type: str
        

    @property
    def merchant_account_id(self):
        """
        A unique ID to identify a specific merchant account.
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def subscription_id(self):
        """
        The unique ID assigned by Antom to identify a subscription.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
