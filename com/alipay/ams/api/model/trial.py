import json
from com.alipay.ams.api.model.amount import Amount




class Trial:
    def __init__(self):
        
        self.__trial_period = None  # type: int
        self.__trial_amount = None  # type: Amount
        self.__trial_start_period = None  # type: int
        self.__trial_end_period = None  # type: int
        

    @property
    def trial_period(self):
        """Gets the trial_period of this Trial.
        
        """
        return self.__trial_period

    @trial_period.setter
    def trial_period(self, value):
        self.__trial_period = value
    @property
    def trial_amount(self):
        """Gets the trial_amount of this Trial.
        
        """
        return self.__trial_amount

    @trial_amount.setter
    def trial_amount(self, value):
        self.__trial_amount = value
    @property
    def trial_start_period(self):
        """
        The start subscription period of the trial. For example, if the trial starts from the first subscription period, specify this parameter as 1.    More information:  Value range: 1 - unlimited
        """
        return self.__trial_start_period

    @trial_start_period.setter
    def trial_start_period(self, value):
        self.__trial_start_period = value
    @property
    def trial_end_period(self):
        """
        The end subscription period of the trial. For example, if the trial ends at the third subscription period, specify this parameter as 3.  Note: Specify this parameter if the end subscription period is different from the start subscription period. If you leave this parameter empty, the default value of this parameter is the same as the value of trialStartPeriod.  More information:  Value range: 1 - unlimited 
        """
        return self.__trial_end_period

    @trial_end_period.setter
    def trial_end_period(self, value):
        self.__trial_end_period = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "trial_period") and self.trial_period is not None:
            params['trialPeriod'] = self.trial_period
        if hasattr(self, "trial_amount") and self.trial_amount is not None:
            params['trialAmount'] = self.trial_amount
        if hasattr(self, "trial_start_period") and self.trial_start_period is not None:
            params['trialStartPeriod'] = self.trial_start_period
        if hasattr(self, "trial_end_period") and self.trial_end_period is not None:
            params['trialEndPeriod'] = self.trial_end_period
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'trialPeriod' in response_body:
            self.__trial_period = response_body['trialPeriod']
        if 'trialAmount' in response_body:
            self.__trial_amount = Amount()
            self.__trial_amount.parse_rsp_body(response_body['trialAmount'])
        if 'trialStartPeriod' in response_body:
            self.__trial_start_period = response_body['trialStartPeriod']
        if 'trialEndPeriod' in response_body:
            self.__trial_end_period = response_body['trialEndPeriod']
