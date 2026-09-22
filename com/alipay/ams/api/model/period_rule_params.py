import json




class PeriodRuleParams:
    def __init__(self):
        
        self.__period_type = None  # type: str
        self.__period = None  # type: str
        self.__single_amount = None  # type: str
        

    @property
    def period_type(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. Maximum length: 10 characters. Allowed values: DAY, MONTH. The authorization period unit. For MONTH, the planned execution day must be from 1 through 28.
        """
        return self.__period_type

    @period_type.setter
    def period_type(self, value):
        self.__period_type = value
    @property
    def period(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. A quoted positive integer interval, not a JSON number; at most 32 digits.
        """
        return self.__period

    @period.setter
    def period(self, value):
        self.__period = value
    @property
    def single_amount(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. The positive single-payment authorization limit in CNY yuan, with exactly two decimal places, for example \&quot;88.88\&quot;. It is not an Amount object or a minor-unit value. Do not multiply, divide, round, or infer it from a payment amount. Zero, negative values, numbers and scientific notation are invalid.
        """
        return self.__single_amount

    @single_amount.setter
    def single_amount(self, value):
        self.__single_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "period_type") and self.period_type is not None:
            params['periodType'] = self.period_type
        if hasattr(self, "period") and self.period is not None:
            params['period'] = self.period
        if hasattr(self, "single_amount") and self.single_amount is not None:
            params['singleAmount'] = self.single_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'periodType' in response_body:
            self.__period_type = response_body['periodType']
        if 'period' in response_body:
            self.__period = response_body['period']
        if 'singleAmount' in response_body:
            self.__single_amount = response_body['singleAmount']
