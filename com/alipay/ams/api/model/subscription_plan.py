import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.period_rule import PeriodRule




class SubscriptionPlan:
    def __init__(self):
        
        self.__allow_accumulate = None  # type: bool
        self.__max_accumulate_amount = None  # type: Amount
        self.__period_rule = None  # type: PeriodRule
        self.__subscription_start_time = None  # type: str
        self.__subscription_notification_url = None  # type: str
        

    @property
    def allow_accumulate(self):
        """
        Whether to allow accumulation of unused amounts
        """
        return self.__allow_accumulate

    @allow_accumulate.setter
    def allow_accumulate(self, value):
        self.__allow_accumulate = value
    @property
    def max_accumulate_amount(self):
        """Gets the max_accumulate_amount of this SubscriptionPlan.
        
        """
        return self.__max_accumulate_amount

    @max_accumulate_amount.setter
    def max_accumulate_amount(self, value):
        self.__max_accumulate_amount = value
    @property
    def period_rule(self):
        """Gets the period_rule of this SubscriptionPlan.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value
    @property
    def subscription_start_time(self):
        """
        Start time of the subscription plan in ISO 8601 format
        """
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value
    @property
    def subscription_notification_url(self):
        """
        URL for subscription notifications
        """
        return self.__subscription_notification_url

    @subscription_notification_url.setter
    def subscription_notification_url(self, value):
        self.__subscription_notification_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "allow_accumulate") and self.allow_accumulate is not None:
            params['allowAccumulate'] = self.allow_accumulate
        if hasattr(self, "max_accumulate_amount") and self.max_accumulate_amount is not None:
            params['maxAccumulateAmount'] = self.max_accumulate_amount
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        if hasattr(self, "subscription_start_time") and self.subscription_start_time is not None:
            params['subscriptionStartTime'] = self.subscription_start_time
        if hasattr(self, "subscription_notification_url") and self.subscription_notification_url is not None:
            params['subscriptionNotificationUrl'] = self.subscription_notification_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'allowAccumulate' in response_body:
            self.__allow_accumulate = response_body['allowAccumulate']
        if 'maxAccumulateAmount' in response_body:
            self.__max_accumulate_amount = Amount()
            self.__max_accumulate_amount.parse_rsp_body(response_body['maxAccumulateAmount'])
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
        if 'subscriptionStartTime' in response_body:
            self.__subscription_start_time = response_body['subscriptionStartTime']
        if 'subscriptionNotificationUrl' in response_body:
            self.__subscription_notification_url = response_body['subscriptionNotificationUrl']
