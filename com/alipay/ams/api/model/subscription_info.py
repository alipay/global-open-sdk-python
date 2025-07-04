import json

from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.trial import Trial


class SubscriptionInfo(object):
    def __init__(self):
        self.__subscription_description = None  # type: str
        self.__subscription_start_time = None  # type: str
        self.__subscription_end_time = None  # type: str
        self.__period_rule = None  # type: PeriodRule
        self.__trials = None  # type: list: Trial
        self.__subscription_notify_url = None  # type: str
        self.__subscription_expiry_time = None  # type: str

    @property
    def subscription_description(self):
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value

    @property
    def subscription_start_time(self):
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value

    @property
    def subscription_end_time(self):
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value

    @property
    def period_rule(self):
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value

    @property
    def trials(self):
        return self.__trials

    @trials.setter
    def trials(self, value):
        self.__trials = value

    @property
    def subscription_notify_url(self):
        return self.__subscription_notify_url

    @subscription_notify_url.setter
    def subscription_notify_url(self, value):
        self.__subscription_notify_url = value

    @property
    def subscription_expiry_time(self):
        return self.__subscription_expiry_time

    @subscription_expiry_time.setter
    def subscription_expiry_time(self, value):
        self.__subscription_expiry_time = value
    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__subscription_description is not None:
            params['subscriptionDescription'] = self.__subscription_description
        if self.__subscription_start_time is not None:
            params['subscriptionStartTime'] = self.__subscription_start_time
        if self.__subscription_end_time is not None:
            params['subscriptionEndTime'] = self.__subscription_end_time
        if self.__period_rule is not None:
            params['periodRule'] = self.__period_rule
        if self.__trials is not None:
            params['trials'] = self.__trials
        if self.__subscription_notify_url is not None:
            params['subscriptionNotifyUrl'] = self.__subscription_notify_url
        if self.__subscription_expiry_time is not None:
            params['subscriptionExpiryTime'] = self.__subscription_expiry_time

        return params
