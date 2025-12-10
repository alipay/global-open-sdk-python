import json




class CurrencyPair:
    def __init__(self):
        
        self.__sell_currency = None  # type: str
        self.__buy_currency = None  # type: str
        

    @property
    def sell_currency(self):
        """Gets the sell_currency of this CurrencyPair.
        
        """
        return self.__sell_currency

    @sell_currency.setter
    def sell_currency(self, value):
        self.__sell_currency = value
    @property
    def buy_currency(self):
        """Gets the buy_currency of this CurrencyPair.
        
        """
        return self.__buy_currency

    @buy_currency.setter
    def buy_currency(self, value):
        self.__buy_currency = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "sell_currency") and self.sell_currency is not None:
            params['sellCurrency'] = self.sell_currency
        if hasattr(self, "buy_currency") and self.buy_currency is not None:
            params['buyCurrency'] = self.buy_currency
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'sellCurrency' in response_body:
            self.__sell_currency = response_body['sellCurrency']
        if 'buyCurrency' in response_body:
            self.__buy_currency = response_body['buyCurrency']
