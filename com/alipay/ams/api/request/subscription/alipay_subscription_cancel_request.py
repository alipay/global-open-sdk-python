import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySubscriptionCancelRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubscriptionCancelRequest, self).__init__("/ams/api/v1/subscriptions/cancel") 

        self.__subscription_id = None  # type: str
        self.__subscription_request_id = None  # type: str
        self.__cancellation_type = None  # type: str
        

    @property
    def subscription_id(self):
        """
        The unique ID assigned by Antom to identify a subscription. The value of this parameter is the value of the same parameter that is returned by notifyPayment and notifySubscription for the original subscription.  Note: Specify at least one of subscriptionId and subscriptionRequestId. A one-to-one correspondence between paymentId and paymentRequestId exists.  More information:  Maximum length: 64 characters
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def subscription_request_id(self):
        """
        The unique ID assigned by a merchant to identify a subscription request. Note: Specify at least one of subscriptionId and subscriptionRequestId. A one-to-one correspondence between paymentId and paymentRequestId exists.  More information:  Maximum length: 64 characters 
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
    @property
    def cancellation_type(self):
        """
        The cancellation type for the subscription. Valid values are:  CANCEL: indicates canceling the subscription. The subscription service is not provided to the user after the current subscription period ends. TERMINATE: indicates terminating the subscription. The subscription service is ceased immediately.   More information:  Maximum length: 32 characters
        """
        return self.__cancellation_type

    @cancellation_type.setter
    def cancellation_type(self, value):
        self.__cancellation_type = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "subscription_request_id") and self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "cancellation_type") and self.cancellation_type is not None:
            params['cancellationType'] = self.cancellation_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'subscriptionRequestId' in response_body:
            self.__subscription_request_id = response_body['subscriptionRequestId']
        if 'cancellationType' in response_body:
            self.__cancellation_type = response_body['cancellationType']
