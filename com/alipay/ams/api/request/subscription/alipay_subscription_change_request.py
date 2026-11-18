import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.order_info import OrderInfo
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySubscriptionChangeRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubscriptionChangeRequest, self).__init__("/ams/api/v1/subscriptions/change") 

        self.__allow_accumulate = None  # type: bool
        self.__max_accumulate_amount = None  # type: Amount
        self.__subscription_change_request_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__subscription_description = None  # type: str
        self.__subscription_start_time = None  # type: str
        self.__subscription_end_time = None  # type: str
        self.__period_rule = None  # type: PeriodRule
        self.__subscription_expiry_time = None  # type: str
        self.__order_info = None  # type: OrderInfo
        self.__payment_amount = None  # type: Amount
        self.__payment_amount_difference = None  # type: Amount
        

    @property
    def allow_accumulate(self):
        """
        Whether to allow accumulate payment amount
        """
        return self.__allow_accumulate

    @allow_accumulate.setter
    def allow_accumulate(self, value):
        self.__allow_accumulate = value
    @property
    def max_accumulate_amount(self):
        """Gets the max_accumulate_amount of this AlipaySubscriptionChangeRequest.
        
        """
        return self.__max_accumulate_amount

    @max_accumulate_amount.setter
    def max_accumulate_amount(self, value):
        self.__max_accumulate_amount = value
    @property
    def subscription_change_request_id(self):
        """
        The unique ID assigned by a merchant to identify a subscription change request. Antom uses this field for idempotency control.   Note: For subscription change requests that are initiated with the same value of subscriptionChangeRequestId and reach a final status of ​S​ or​F​, the same result is to be returned for the request.  More information:  This field is an API idempotency field. Maximum length: 64 characters
        """
        return self.__subscription_change_request_id

    @subscription_change_request_id.setter
    def subscription_change_request_id(self, value):
        self.__subscription_change_request_id = value
    @property
    def subscription_id(self):
        """
        The unique ID assigned by Antom to identify a subscription. The value of this parameter is the value of the same parameter that is returned by notifyPayment and notifySubscription for the original subscription.    More information:  Maximum length: 64 characters
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def subscription_description(self):
        """
        The description of the subscription, used for displaying user consumption records and other actions.  Note: Specify this parameter if you want to change this information.  More information:  Maximum length: 256 characters
        """
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value
    @property
    def subscription_start_time(self):
        """
        The date and time when the subscription becomes active.   Note: Specify this parameter when you want to designate the start time of the changed subscription. If you leave this parameter empty, the default value of this parameter is the time when Antom receives this request.    More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value
    @property
    def subscription_end_time(self):
        """
        The date and time when the subscription ends. The default value of this parameter is 2099-12-31T23:59:59+08:00.   Note: Specify this parameter when you want to change this information.    More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value
    @property
    def period_rule(self):
        """Gets the period_rule of this AlipaySubscriptionChangeRequest.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value
    @property
    def subscription_expiry_time(self):
        """
        A specific date and time after which the created subscription expires. When the subscription expires, the order must be terminated. The default value of this parameter is 30 minutes after the subscription creation request is sent.  Note: Specify this parameter if you want to change the subscription creation expiration time. The specified payment expiration time must be less than 48 hours after the subscription request is sent.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__subscription_expiry_time

    @subscription_expiry_time.setter
    def subscription_expiry_time(self, value):
        self.__subscription_expiry_time = value
    @property
    def order_info(self):
        """Gets the order_info of this AlipaySubscriptionChangeRequest.
        
        """
        return self.__order_info

    @order_info.setter
    def order_info(self, value):
        self.__order_info = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipaySubscriptionChangeRequest.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_amount_difference(self):
        """Gets the payment_amount_difference of this AlipaySubscriptionChangeRequest.
        
        """
        return self.__payment_amount_difference

    @payment_amount_difference.setter
    def payment_amount_difference(self, value):
        self.__payment_amount_difference = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "allow_accumulate") and self.allow_accumulate is not None:
            params['allowAccumulate'] = self.allow_accumulate
        if hasattr(self, "max_accumulate_amount") and self.max_accumulate_amount is not None:
            params['maxAccumulateAmount'] = self.max_accumulate_amount
        if hasattr(self, "subscription_change_request_id") and self.subscription_change_request_id is not None:
            params['subscriptionChangeRequestId'] = self.subscription_change_request_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "subscription_description") and self.subscription_description is not None:
            params['subscriptionDescription'] = self.subscription_description
        if hasattr(self, "subscription_start_time") and self.subscription_start_time is not None:
            params['subscriptionStartTime'] = self.subscription_start_time
        if hasattr(self, "subscription_end_time") and self.subscription_end_time is not None:
            params['subscriptionEndTime'] = self.subscription_end_time
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        if hasattr(self, "subscription_expiry_time") and self.subscription_expiry_time is not None:
            params['subscriptionExpiryTime'] = self.subscription_expiry_time
        if hasattr(self, "order_info") and self.order_info is not None:
            params['orderInfo'] = self.order_info
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_amount_difference") and self.payment_amount_difference is not None:
            params['paymentAmountDifference'] = self.payment_amount_difference
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'allowAccumulate' in response_body:
            self.__allow_accumulate = response_body['allowAccumulate']
        if 'maxAccumulateAmount' in response_body:
            self.__max_accumulate_amount = Amount()
            self.__max_accumulate_amount.parse_rsp_body(response_body['maxAccumulateAmount'])
        if 'subscriptionChangeRequestId' in response_body:
            self.__subscription_change_request_id = response_body['subscriptionChangeRequestId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'subscriptionDescription' in response_body:
            self.__subscription_description = response_body['subscriptionDescription']
        if 'subscriptionStartTime' in response_body:
            self.__subscription_start_time = response_body['subscriptionStartTime']
        if 'subscriptionEndTime' in response_body:
            self.__subscription_end_time = response_body['subscriptionEndTime']
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
        if 'subscriptionExpiryTime' in response_body:
            self.__subscription_expiry_time = response_body['subscriptionExpiryTime']
        if 'orderInfo' in response_body:
            self.__order_info = OrderInfo()
            self.__order_info.parse_rsp_body(response_body['orderInfo'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentAmountDifference' in response_body:
            self.__payment_amount_difference = Amount()
            self.__payment_amount_difference.parse_rsp_body(response_body['paymentAmountDifference'])
