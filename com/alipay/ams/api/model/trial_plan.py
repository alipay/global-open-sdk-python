import json
from com.alipay.ams.api.model.trial_phase import TrialPhase




class TrialPlan:
    def __init__(self):
        
        self.__trial_end_time = None  # type: str
        self.__free_trial_days = None  # type: int
        self.__phases = None  # type: [TrialPhase]
        

    @property
    def trial_end_time(self):
        """
        Indicates the last date of trial phases.
        """
        return self.__trial_end_time

    @trial_end_time.setter
    def trial_end_time(self, value):
        self.__trial_end_time = value
    @property
    def free_trial_days(self):
        """
        Total free trial days.
        """
        return self.__free_trial_days

    @free_trial_days.setter
    def free_trial_days(self, value):
        self.__free_trial_days = value
    @property
    def phases(self):
        """
        Subscription periods that apply trial plan.
        """
        return self.__phases

    @phases.setter
    def phases(self, value):
        self.__phases = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "trial_end_time") and self.trial_end_time is not None:
            params['trialEndTime'] = self.trial_end_time
        if hasattr(self, "free_trial_days") and self.free_trial_days is not None:
            params['freeTrialDays'] = self.free_trial_days
        if hasattr(self, "phases") and self.phases is not None:
            params['phases'] = self.phases
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'trialEndTime' in response_body:
            self.__trial_end_time = response_body['trialEndTime']
        if 'freeTrialDays' in response_body:
            self.__free_trial_days = response_body['freeTrialDays']
        if 'phases' in response_body:
            self.__phases = []
            for item in response_body['phases']:
                obj = TrialPhase()
                obj.parse_rsp_body(item)
                self.__phases.append(obj)
