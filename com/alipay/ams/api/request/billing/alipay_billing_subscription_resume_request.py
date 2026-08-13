import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionResumeRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionResumeRequest, self).__init__("/ams/api/v1/billing/subscription/resume") 

        self.__subscription_id = None  # type: str
        self.__reason_code = None  # type: str
        

    @property
    def subscription_id(self):
        """
        The ID of the paused subscription to resume. If payment is already in progress, a repeated request returns PAYMENT_IN_PROCESSING without creating another charge. If the subscription is already active, the operation returns SUCCESS without changing it. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def reason_code(self):
        """
        The reason for resuming the subscription, recorded for audit purposes. HTML tags are not allowed. Maximum length: 64 characters.
        """
        return self.__reason_code

    @reason_code.setter
    def reason_code(self, value):
        self.__reason_code = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "reason_code") and self.reason_code is not None:
            params['reasonCode'] = self.reason_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'reasonCode' in response_body:
            self.__reason_code = response_body['reasonCode']
