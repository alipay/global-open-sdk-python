import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipaySubscriptionsInquiryResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__allow_retry = None  # type: str
        self.__max_amount_floor = None  # type: Amount
        self.__payment_amount = None  # type: Amount
        self.__period_rule = None  # type: PeriodRule
        self.__subscription_end_time = None  # type: str
        self.__subscription_request_id = None  # type: str
        self.__subscription_start_time = None  # type: str
        self.__subscription_status = None  # type: str
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def allow_retry(self):
        """Gets the allow_retry of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__allow_retry

    @allow_retry.setter
    def allow_retry(self, value):
        self.__allow_retry = value
    @property
    def max_amount_floor(self):
        """Gets the max_amount_floor of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__max_amount_floor

    @max_amount_floor.setter
    def max_amount_floor(self, value):
        self.__max_amount_floor = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def period_rule(self):
        """Gets the period_rule of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value
    @property
    def subscription_end_time(self):
        """Gets the subscription_end_time of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value
    @property
    def subscription_request_id(self):
        """Gets the subscription_request_id of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value
    @property
    def subscription_start_time(self):
        """Gets the subscription_start_time of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value
    @property
    def subscription_status(self):
        """Gets the subscription_status of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__subscription_status

    @subscription_status.setter
    def subscription_status(self, value):
        self.__subscription_status = value
    @property
    def result(self):
        """Gets the result of this AlipaySubscriptionsInquiryResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "allow_retry") and self.allow_retry is not None:
            params['allowRetry'] = self.allow_retry
        if hasattr(self, "max_amount_floor") and self.max_amount_floor is not None:
            params['maxAmountFloor'] = self.max_amount_floor
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        if hasattr(self, "subscription_end_time") and self.subscription_end_time is not None:
            params['subscriptionEndTime'] = self.subscription_end_time
        if hasattr(self, "subscription_request_id") and self.subscription_request_id is not None:
            params['subscriptionRequestId'] = self.subscription_request_id
        if hasattr(self, "subscription_start_time") and self.subscription_start_time is not None:
            params['subscriptionStartTime'] = self.subscription_start_time
        if hasattr(self, "subscription_status") and self.subscription_status is not None:
            params['subscriptionStatus'] = self.subscription_status
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipaySubscriptionsInquiryResponse, self).parse_rsp_body(response_body)
        if 'allowRetry' in response_body:
            self.__allow_retry = response_body['allowRetry']
        if 'maxAmountFloor' in response_body:
            self.__max_amount_floor = Amount()
            self.__max_amount_floor.parse_rsp_body(response_body['maxAmountFloor'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
        if 'subscriptionEndTime' in response_body:
            self.__subscription_end_time = response_body['subscriptionEndTime']
        if 'subscriptionRequestId' in response_body:
            self.__subscription_request_id = response_body['subscriptionRequestId']
        if 'subscriptionStartTime' in response_body:
            self.__subscription_start_time = response_body['subscriptionStartTime']
        if 'subscriptionStatus' in response_body:
            self.__subscription_status = response_body['subscriptionStatus']
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
