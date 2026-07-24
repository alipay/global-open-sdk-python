import json
from com.alipay.ams.api.model.period_rule import PeriodRule




class RecurringSettings:
    def __init__(self):
        
        self.__period_rule = None  # type: PeriodRule
        

    @property
    def period_rule(self):
        """Gets the period_rule of this RecurringSettings.
        
        """
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "period_rule") and self.period_rule is not None:
            params['periodRule'] = self.period_rule
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'periodRule' in response_body:
            self.__period_rule = PeriodRule()
            self.__period_rule.parse_rsp_body(response_body['periodRule'])
