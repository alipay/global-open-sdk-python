import json




class BillingTrialSettings:
    def __init__(self):
        
        self.__trial_period_days = None  # type: int
        self.__trial_end = None  # type: str
        

    @property
    def trial_period_days(self):
        """
        Number of trial period days.
        """
        return self.__trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, value):
        self.__trial_period_days = value
    @property
    def trial_end(self):
        """
        Trial end time.
        """
        return self.__trial_end

    @trial_end.setter
    def trial_end(self, value):
        self.__trial_end = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "trial_period_days") and self.trial_period_days is not None:
            params['trialPeriodDays'] = self.trial_period_days
        if hasattr(self, "trial_end") and self.trial_end is not None:
            params['trialEnd'] = self.trial_end
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'trialPeriodDays' in response_body:
            self.__trial_period_days = response_body['trialPeriodDays']
        if 'trialEnd' in response_body:
            self.__trial_end = response_body['trialEnd']
