import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.limit import Limit
from com.alipay.ams.api.model.limit import Limit
from com.alipay.ams.api.model.limit import Limit




class CardLimitDetail:
    def __init__(self):
        
        self.__per_transaction_limit = None  # type: Amount
        self.__daily_limit = None  # type: Limit
        self.__monthly_limit = None  # type: Limit
        self.__per_card_limit = None  # type: Limit
        self.__daily_limit_max = None  # type: str
        self.__monthly_limit_max = None  # type: str
        self.__per_transaction_limit_max = None  # type: str
        self.__per_card_limit_max = None  # type: str
        

    @property
    def per_transaction_limit(self):
        """Gets the per_transaction_limit of this CardLimitDetail.
        
        """
        return self.__per_transaction_limit

    @per_transaction_limit.setter
    def per_transaction_limit(self, value):
        self.__per_transaction_limit = value
    @property
    def daily_limit(self):
        """Gets the daily_limit of this CardLimitDetail.
        
        """
        return self.__daily_limit

    @daily_limit.setter
    def daily_limit(self, value):
        self.__daily_limit = value
    @property
    def monthly_limit(self):
        """Gets the monthly_limit of this CardLimitDetail.
        
        """
        return self.__monthly_limit

    @monthly_limit.setter
    def monthly_limit(self, value):
        self.__monthly_limit = value
    @property
    def per_card_limit(self):
        """Gets the per_card_limit of this CardLimitDetail.
        
        """
        return self.__per_card_limit

    @per_card_limit.setter
    def per_card_limit(self, value):
        self.__per_card_limit = value
    @property
    def daily_limit_max(self):
        """Gets the daily_limit_max of this CardLimitDetail.
        
        """
        return self.__daily_limit_max

    @daily_limit_max.setter
    def daily_limit_max(self, value):
        self.__daily_limit_max = value
    @property
    def monthly_limit_max(self):
        """Gets the monthly_limit_max of this CardLimitDetail.
        
        """
        return self.__monthly_limit_max

    @monthly_limit_max.setter
    def monthly_limit_max(self, value):
        self.__monthly_limit_max = value
    @property
    def per_transaction_limit_max(self):
        """Gets the per_transaction_limit_max of this CardLimitDetail.
        
        """
        return self.__per_transaction_limit_max

    @per_transaction_limit_max.setter
    def per_transaction_limit_max(self, value):
        self.__per_transaction_limit_max = value
    @property
    def per_card_limit_max(self):
        """Gets the per_card_limit_max of this CardLimitDetail.
        
        """
        return self.__per_card_limit_max

    @per_card_limit_max.setter
    def per_card_limit_max(self, value):
        self.__per_card_limit_max = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "per_transaction_limit") and self.per_transaction_limit is not None:
            params['perTransactionLimit'] = self.per_transaction_limit
        if hasattr(self, "daily_limit") and self.daily_limit is not None:
            params['dailyLimit'] = self.daily_limit
        if hasattr(self, "monthly_limit") and self.monthly_limit is not None:
            params['monthlyLimit'] = self.monthly_limit
        if hasattr(self, "per_card_limit") and self.per_card_limit is not None:
            params['perCardLimit'] = self.per_card_limit
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
        if 'perTransactionLimit' in response_body:
            self.__per_transaction_limit = Amount()
            self.__per_transaction_limit.parse_rsp_body(response_body['perTransactionLimit'])
        if 'dailyLimit' in response_body:
            self.__daily_limit = Limit()
            self.__daily_limit.parse_rsp_body(response_body['dailyLimit'])
        if 'monthlyLimit' in response_body:
            self.__monthly_limit = Limit()
            self.__monthly_limit.parse_rsp_body(response_body['monthlyLimit'])
        if 'perCardLimit' in response_body:
            self.__per_card_limit = Limit()
            self.__per_card_limit.parse_rsp_body(response_body['perCardLimit'])
        if 'dailyLimitMax' in response_body:
            self.__daily_limit_max = response_body['dailyLimitMax']
        if 'monthlyLimitMax' in response_body:
            self.__monthly_limit_max = response_body['monthlyLimitMax']
        if 'perTransactionLimitMax' in response_body:
            self.__per_transaction_limit_max = response_body['perTransactionLimitMax']
        if 'perCardLimitMax' in response_body:
            self.__per_card_limit_max = response_body['perCardLimitMax']
