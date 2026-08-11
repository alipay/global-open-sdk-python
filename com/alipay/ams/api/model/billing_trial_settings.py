import json




class BillingTrialSettings:
    def __init__(self):
        
        self.__trial_period_days = None  # type: int
        self.__trial_end = None  # type: str
        self.__trial_end_behavior = None  # type: str
        

    @property
    def trial_period_days(self):
        """
        Relative trial duration in days. Value range: 1-365. Exactly one of &#x60;trialPeriodDays&#x60; and &#x60;trialEnd&#x60; must be provided when trial settings are used.
        """
        return self.__trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, value):
        self.__trial_period_days = value
    @property
    def trial_end(self):
        """
        Absolute trial end time in ISO 8601 format with a timezone offset. Exactly one of &#x60;trialPeriodDays&#x60; and &#x60;trialEnd&#x60; must be provided when trial settings are used.
        """
        return self.__trial_end

    @trial_end.setter
    def trial_end(self, value):
        self.__trial_end = value
    @property
    def trial_end_behavior(self):
        """
        Behavior when the trial ends without an available payment method. Valid values are CANCEL and PAUSE.
        """
        return self.__trial_end_behavior

    @trial_end_behavior.setter
    def trial_end_behavior(self, value):
        self.__trial_end_behavior = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "trial_period_days") and self.trial_period_days is not None:
            params['trialPeriodDays'] = self.trial_period_days
        if hasattr(self, "trial_end") and self.trial_end is not None:
            params['trialEnd'] = self.trial_end
        if hasattr(self, "trial_end_behavior") and self.trial_end_behavior is not None:
            params['trialEndBehavior'] = self.trial_end_behavior
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'trialPeriodDays' in response_body:
            self.__trial_period_days = response_body['trialPeriodDays']
        if 'trialEnd' in response_body:
            self.__trial_end = response_body['trialEnd']
        if 'trialEndBehavior' in response_body:
            self.__trial_end_behavior = response_body['trialEndBehavior']
