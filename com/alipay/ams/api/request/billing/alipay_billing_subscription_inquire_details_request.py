import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionInquireDetailsRequest, self).__init__("/ams/api/v1/billing/subscription/inquireDetails") 

        self.__subscription_id = None  # type: str
        

    @property
    def subscription_id(self):
        """
        The subscription ID. Maximum length: 64 characters.
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
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
