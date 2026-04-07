import json
from com.alipay.ams.api.model.amount import Amount




class TrialPhase:
    def __init__(self):
        
        self.__phase_no = None  # type: int
        self.__trial_amount = None  # type: Amount
        

    @property
    def phase_no(self):
        """
        The subscription period that applies trial.
        """
        return self.__phase_no

    @phase_no.setter
    def phase_no(self, value):
        self.__phase_no = value
    @property
    def trial_amount(self):
        """Gets the trial_amount of this TrialPhase.
        
        """
        return self.__trial_amount

    @trial_amount.setter
    def trial_amount(self, value):
        self.__trial_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "phase_no") and self.phase_no is not None:
            params['phaseNo'] = self.phase_no
        if hasattr(self, "trial_amount") and self.trial_amount is not None:
            params['trialAmount'] = self.trial_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'phaseNo' in response_body:
            self.__phase_no = response_body['phaseNo']
        if 'trialAmount' in response_body:
            self.__trial_amount = Amount()
            self.__trial_amount.parse_rsp_body(response_body['trialAmount'])
