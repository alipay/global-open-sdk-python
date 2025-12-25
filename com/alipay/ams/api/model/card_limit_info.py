import json




class CardLimitInfo:
    def __init__(self):
        
        self.__currency = None  # type: str
        self.__daily_limit_max = None  # type: str
        self.__monthly_limit_max = None  # type: str
        self.__per_transaction_limit_max = None  # type: str
        self.__per_card_limit_max = None  # type: str
        

    @property
    def currency(self):
        """Gets the currency of this CardLimitInfo.
        
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def daily_limit_max(self):
        """Gets the daily_limit_max of this CardLimitInfo.
        
        """
        return self.__daily_limit_max

    @daily_limit_max.setter
    def daily_limit_max(self, value):
        self.__daily_limit_max = value
    @property
    def monthly_limit_max(self):
        """Gets the monthly_limit_max of this CardLimitInfo.
        
        """
        return self.__monthly_limit_max

    @monthly_limit_max.setter
    def monthly_limit_max(self, value):
        self.__monthly_limit_max = value
    @property
    def per_transaction_limit_max(self):
        """Gets the per_transaction_limit_max of this CardLimitInfo.
        
        """
        return self.__per_transaction_limit_max

    @per_transaction_limit_max.setter
    def per_transaction_limit_max(self, value):
        self.__per_transaction_limit_max = value
    @property
    def per_card_limit_max(self):
        """Gets the per_card_limit_max of this CardLimitInfo.
        
        """
        return self.__per_card_limit_max

    @per_card_limit_max.setter
    def per_card_limit_max(self, value):
        self.__per_card_limit_max = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "daily_limit_max") and self.daily_limit_max is not None:
            params['dailyLimitMax'] = self.daily_limit_max
        if hasattr(self, "monthly_limit_max") and self.monthly_limit_max is not None:
            params['monthlyLimitMax'] = self.monthly_limit_max
        if hasattr(self, "per_transaction_limit_max") and self.per_transaction_limit_max is not None:
            params['perTransactionLimitMax'] = self.per_transaction_limit_max
        if hasattr(self, "per_card_limit_max") and self.per_card_limit_max is not None:
            params['perCardLimitMax'] = self.per_card_limit_max
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'dailyLimitMax' in response_body:
            self.__daily_limit_max = response_body['dailyLimitMax']
        if 'monthlyLimitMax' in response_body:
            self.__monthly_limit_max = response_body['monthlyLimitMax']
        if 'perTransactionLimitMax' in response_body:
            self.__per_transaction_limit_max = response_body['perTransactionLimitMax']
        if 'perCardLimitMax' in response_body:
            self.__per_card_limit_max = response_body['perCardLimitMax']
