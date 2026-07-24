import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionResumeRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionResumeRequest, self).__init__("/ams/api/v1/billing/subscription/resume") 

        self.__subscription_id = None  # type: str
        self.__billing_cycle_anchor = None  # type: str
        self.__proration_behavior = None  # type: str
        self.__proration_date = None  # type: str
        self.__reason_code = None  # type: str
        

    @property
    def subscription_id(self):
        """
        The subscription ID. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def billing_cycle_anchor(self):
        """
        The billing cycle anchor. Maximum length: 9 characters.
        """
        return self.__billing_cycle_anchor

    @billing_cycle_anchor.setter
    def billing_cycle_anchor(self, value):
        self.__billing_cycle_anchor = value
    @property
    def proration_behavior(self):
        """
        The proration behavior. Maximum length: 18 characters.
        """
        return self.__proration_behavior

    @proration_behavior.setter
    def proration_behavior(self, value):
        self.__proration_behavior = value
    @property
    def proration_date(self):
        """
        The proration date.
        """
        return self.__proration_date

    @proration_date.setter
    def proration_date(self, value):
        self.__proration_date = value
    @property
    def reason_code(self):
        """
        The reason code. Maximum length: 64 characters.
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
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "proration_behavior") and self.proration_behavior is not None:
            params['prorationBehavior'] = self.proration_behavior
        if hasattr(self, "proration_date") and self.proration_date is not None:
            params['prorationDate'] = self.proration_date
        if hasattr(self, "reason_code") and self.reason_code is not None:
            params['reasonCode'] = self.reason_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'prorationBehavior' in response_body:
            self.__proration_behavior = response_body['prorationBehavior']
        if 'prorationDate' in response_body:
            self.__proration_date = response_body['prorationDate']
        if 'reasonCode' in response_body:
            self.__reason_code = response_body['reasonCode']
