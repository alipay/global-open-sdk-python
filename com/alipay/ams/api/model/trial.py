import json


class Trial(object):
    def __init__(self):
        self.__trial_start_period = None
        self.__trial_amount = None
        self.__trial_end_period = None

    @property
    def trial_start_period(self):
        return self.__trial_start_period

    @trial_start_period.setter
    def trial_start_period(self, value):
        self.__trial_start_period = value

    @property
    def trial_amount(self):
        return self.__trial_amount

    @trial_amount.setter
    def trial_amount(self, value):
        self.__trial_amount = value

    @property
    def trial_end_period(self):
        return self.__trial_end_period

    @trial_end_period.setter
    def trial_end_period(self, value):
        self.__trial_end_period = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__trial_start_period is not None:
            params['trialStartPeriod'] = self.__trial_start_period
        if self.__trial_amount is not None:
            params['trialAmount'] = self.__trial_amount
        if self.__trial_end_period is not None:
            params['trialEndPeriod'] = self.__trial_end_period

        return params
