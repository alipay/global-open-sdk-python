import json




class RateResult:
    def __init__(self):
        
        self.__buy_currency = None  # type: str
        self.__sell_currency = None  # type: str
        self.__exchange_rate = None  # type: str
        

    @property
    def buy_currency(self):
        """Gets the buy_currency of this RateResult.
        
        """
        return self.__buy_currency

    @buy_currency.setter
    def buy_currency(self, value):
        self.__buy_currency = value
    @property
    def sell_currency(self):
        """Gets the sell_currency of this RateResult.
        
        """
        return self.__sell_currency

    @sell_currency.setter
    def sell_currency(self, value):
        self.__sell_currency = value
    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this RateResult.
        
        """
        return self.__exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self.__exchange_rate = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "buy_currency") and self.buy_currency is not None:
            params['buyCurrency'] = self.buy_currency
        if hasattr(self, "sell_currency") and self.sell_currency is not None:
            params['sellCurrency'] = self.sell_currency
        if hasattr(self, "exchange_rate") and self.exchange_rate is not None:
            params['exchangeRate'] = self.exchange_rate
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'buyCurrency' in response_body:
            self.__buy_currency = response_body['buyCurrency']
        if 'sellCurrency' in response_body:
            self.__sell_currency = response_body['sellCurrency']
        if 'exchangeRate' in response_body:
            self.__exchange_rate = response_body['exchangeRate']
