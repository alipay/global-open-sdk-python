import json
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.order_info import OrderInfo



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySubscriptionUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubscriptionUpdateRequest, self).__init__("/ams/api/v1/subscriptions/update") 

        self.__subscription_update_request_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__subscription_description = None  # type: str
        self.__period_rule = None  # type: PeriodRule
        self.__payment_amount = None  # type: Amount
        self.__subscription_end_time = None  # type: str
        self.__order_info = None  # type: OrderInfo
        

    @property
    def subscription_update_request_id(self):
        """
        The unique ID assigned by a merchant to identify a subscription update request.  More information:  Maximum length: 64 characters
        """
        return self.__subscription_update_request_id

    @subscription_update_request_id.setter
    def subscription_update_request_id(self, value):
        self.__subscription_update_request_id = value
    @property
    def subscription_id(self):
        """
        The unique ID assigned by Antom to identify a subscription.   More information:  Maximum length: 64 characters
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def subscription_description(self):
        """
        The description of the subscription, used for displaying user consumption records and other actions.  More information:  Maximum length: 256 characters
        """
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value
    @property
    def period_rule(self):
        """Gets the period_rule of this AlipaySubscriptionUpdateRequest.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipaySubscriptionUpdateRequest.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def subscription_end_time(self):
        """
        The date and time when the subscription ends.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value
    @property
    def order_info(self):
        """Gets the order_info of this AlipaySubscriptionUpdateRequest.
        
        """
        return self.__order_info

    @order_info.setter
    def order_info(self, value):
        self.__order_info = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_update_request_id") and self.subscription_update_request_id is not None:
            params['subscriptionUpdateRequestId'] = self.subscription_update_request_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "subscription_description") and self.subscription_description is not None:
            params['subscriptionDescription'] = self.subscription_description
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "subscription_end_time") and self.subscription_end_time is not None:
            params['subscriptionEndTime'] = self.subscription_end_time
        if hasattr(self, "order_info") and self.order_info is not None:
            params['orderInfo'] = self.order_info
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionUpdateRequestId' in response_body:
            self.__subscription_update_request_id = response_body['subscriptionUpdateRequestId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'subscriptionDescription' in response_body:
            self.__subscription_description = response_body['subscriptionDescription']
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'subscriptionEndTime' in response_body:
            self.__subscription_end_time = response_body['subscriptionEndTime']
        if 'orderInfo' in response_body:
            self.__order_info = OrderInfo()
            self.__order_info.parse_rsp_body(response_body['orderInfo'])
