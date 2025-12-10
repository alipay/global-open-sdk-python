import json
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.trial import Trial




class SubscriptionInfo:
    def __init__(self):
        
        self.__subscription_description = None  # type: str
        self.__subscription_start_time = None  # type: str
        self.__subscription_end_time = None  # type: str
        self.__period_rule = None  # type: PeriodRule
        self.__trials = None  # type: [Trial]
        self.__subscription_notify_url = None  # type: str
        self.__subscription_expiry_time = None  # type: str
        

    @property
    def subscription_description(self):
        """
        Description of the subscription plan
        """
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value
    @property
    def subscription_start_time(self):
        """
        Start time of the subscription in ISO 8601 format
        """
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value
    @property
    def subscription_end_time(self):
        """
        End time of the subscription in ISO 8601 format
        """
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value
    @property
    def period_rule(self):
        """Gets the period_rule of this SubscriptionInfo.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value
    @property
    def trials(self):
        """
        List of trial periods for the subscription
        """
        return self.__trials

    @trials.setter
    def trials(self, value):
        self.__trials = value
    @property
    def subscription_notify_url(self):
        """
        URL for subscription notifications
        """
        return self.__subscription_notify_url

    @subscription_notify_url.setter
    def subscription_notify_url(self, value):
        self.__subscription_notify_url = value
    @property
    def subscription_expiry_time(self):
        """
        Expiry time of the subscription in ISO 8601 format
        """
        return self.__subscription_expiry_time

    @subscription_expiry_time.setter
    def subscription_expiry_time(self, value):
        self.__subscription_expiry_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_description") and self.subscription_description is not None:
            params['subscriptionDescription'] = self.subscription_description
        if hasattr(self, "subscription_start_time") and self.subscription_start_time is not None:
            params['subscriptionStartTime'] = self.subscription_start_time
        if hasattr(self, "subscription_end_time") and self.subscription_end_time is not None:
            params['subscriptionEndTime'] = self.subscription_end_time
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        if hasattr(self, "trials") and self.trials is not None:
            params['trials'] = self.trials
        if hasattr(self, "subscription_notify_url") and self.subscription_notify_url is not None:
            params['subscriptionNotifyUrl'] = self.subscription_notify_url
        if hasattr(self, "subscription_expiry_time") and self.subscription_expiry_time is not None:
            params['subscriptionExpiryTime'] = self.subscription_expiry_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscriptionDescription' in response_body:
            self.__subscription_description = response_body['subscriptionDescription']
        if 'subscriptionStartTime' in response_body:
            self.__subscription_start_time = response_body['subscriptionStartTime']
        if 'subscriptionEndTime' in response_body:
            self.__subscription_end_time = response_body['subscriptionEndTime']
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
        if 'trials' in response_body:
            self.__trials = []
            for item in response_body['trials']:
                self.__trials.append(item)
        if 'subscriptionNotifyUrl' in response_body:
            self.__subscription_notify_url = response_body['subscriptionNotifyUrl']
        if 'subscriptionExpiryTime' in response_body:
            self.__subscription_expiry_time = response_body['subscriptionExpiryTime']
