import json
from com.alipay.ams.api.model.billing_subscription_cancel_cancellation_details import BillingSubscriptionCancelCancellationDetails



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionCancelRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionCancelRequest, self).__init__("/ams/api/v1/billing/subscription/cancel") 

        self.__subscription_id = None  # type: str
        self.__cancellation_type = None  # type: str
        self.__cancellation_reason = None  # type: str
        self.__cancellation_details = None  # type: BillingSubscriptionCancelCancellationDetails
        self.__proration_behavior = None  # type: str
        

    @property
    def subscription_id(self):
        """
        The target subscription ID. Repeated cancellation requests for the same subscription return the existing cancellation result. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def cancellation_type(self):
        """
        The cancellation type. Maximum length: 32 characters.
        """
        return self.__cancellation_type

    @cancellation_type.setter
    def cancellation_type(self, value):
        self.__cancellation_type = value
    @property
    def cancellation_reason(self):
        """
        A free-text cancellation reason. Do not include personally identifiable information. At least one of &#x60;cancellationReason&#x60; and &#x60;cancellationDetails.feedback&#x60; must be provided. Maximum length: 64 characters.
        """
        return self.__cancellation_reason

    @cancellation_reason.setter
    def cancellation_reason(self, value):
        self.__cancellation_reason = value
    @property
    def cancellation_details(self):
        """Gets the cancellation_details of this AlipayBillingSubscriptionCancelRequest.
        
        """
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = value
    @property
    def proration_behavior(self):
        """
        The proration behavior for immediate termination. Valid values are CREATE_PRORATIONS, NONE, and ALWAYS_INVOICE. Maximum length: 18 characters.
        """
        return self.__proration_behavior

    @proration_behavior.setter
    def proration_behavior(self, value):
        self.__proration_behavior = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "cancellation_type") and self.cancellation_type is not None:
            params['cancellationType'] = self.cancellation_type
        if hasattr(self, "cancellation_reason") and self.cancellation_reason is not None:
            params['cancellationReason'] = self.cancellation_reason
        if hasattr(self, "cancellation_details") and self.cancellation_details is not None:
            params['cancellationDetails'] = self.cancellation_details
        if hasattr(self, "proration_behavior") and self.proration_behavior is not None:
            params['prorationBehavior'] = self.proration_behavior
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'cancellationType' in response_body:
            self.__cancellation_type = response_body['cancellationType']
        if 'cancellationReason' in response_body:
            self.__cancellation_reason = response_body['cancellationReason']
        if 'cancellationDetails' in response_body:
            self.__cancellation_details = BillingSubscriptionCancelCancellationDetails()
            self.__cancellation_details.parse_rsp_body(response_body['cancellationDetails'])
        if 'prorationBehavior' in response_body:
            self.__proration_behavior = response_body['prorationBehavior']
