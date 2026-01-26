import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class AccountBalance:
    def __init__(self):
        
        self.__currency = None  # type: str
        self.__available_balance = None  # type: Amount
        self.__frozen_balance = None  # type: Amount
        self.__total_balance = None  # type: Amount
        

    @property
    def currency(self):
        """Gets the currency of this AccountBalance.
        
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def available_balance(self):
        """Gets the available_balance of this AccountBalance.
        
        """
        return self.__available_balance

    @available_balance.setter
    def available_balance(self, value):
        self.__available_balance = value
    @property
    def frozen_balance(self):
        """Gets the frozen_balance of this AccountBalance.
        
        """
        return self.__frozen_balance

    @frozen_balance.setter
    def frozen_balance(self, value):
        self.__frozen_balance = value
    @property
    def total_balance(self):
        """Gets the total_balance of this AccountBalance.
        
        """
        return self.__total_balance

    @total_balance.setter
    def total_balance(self, value):
        self.__total_balance = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "available_balance") and self.available_balance is not None:
            params['availableBalance'] = self.available_balance
        if hasattr(self, "frozen_balance") and self.frozen_balance is not None:
            params['frozenBalance'] = self.frozen_balance
        if hasattr(self, "total_balance") and self.total_balance is not None:
            params['totalBalance'] = self.total_balance
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'availableBalance' in response_body:
            self.__available_balance = Amount()
            self.__available_balance.parse_rsp_body(response_body['availableBalance'])
        if 'frozenBalance' in response_body:
            self.__frozen_balance = Amount()
            self.__frozen_balance.parse_rsp_body(response_body['frozenBalance'])
        if 'totalBalance' in response_body:
            self.__total_balance = Amount()
            self.__total_balance.parse_rsp_body(response_body['totalBalance'])
