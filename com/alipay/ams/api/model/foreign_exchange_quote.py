import json




class ForeignExchangeQuote:
    def __init__(self):
        
        self.__exchange_rate = None  # type: str
        self.__source_currency = None  # type: str
        self.__target_currency = None  # type: str
        self.__quote_time = None  # type: str
        self.__quote_price = None  # type: str
        

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this ForeignExchangeQuote.
        
        """
        return self.__exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self.__exchange_rate = value
    @property
    def source_currency(self):
        """Gets the source_currency of this ForeignExchangeQuote.
        
        """
        return self.__source_currency

    @source_currency.setter
    def source_currency(self, value):
        self.__source_currency = value
    @property
    def target_currency(self):
        """Gets the target_currency of this ForeignExchangeQuote.
        
        """
        return self.__target_currency

    @target_currency.setter
    def target_currency(self, value):
        self.__target_currency = value
    @property
    def quote_time(self):
        """Gets the quote_time of this ForeignExchangeQuote.
        
        """
        return self.__quote_time

    @quote_time.setter
    def quote_time(self, value):
        self.__quote_time = value
    @property
    def quote_price(self):
        """Gets the quote_price of this ForeignExchangeQuote.
        
        """
        return self.__quote_price

    @quote_price.setter
    def quote_price(self, value):
        self.__quote_price = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "exchange_rate") and self.exchange_rate is not None:
            params['exchangeRate'] = self.exchange_rate
        if hasattr(self, "source_currency") and self.source_currency is not None:
            params['sourceCurrency'] = self.source_currency
        if hasattr(self, "target_currency") and self.target_currency is not None:
            params['targetCurrency'] = self.target_currency
        if hasattr(self, "quote_time") and self.quote_time is not None:
            params['quoteTime'] = self.quote_time
        if hasattr(self, "quote_price") and self.quote_price is not None:
            params['quotePrice'] = self.quote_price
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'exchangeRate' in response_body:
            self.__exchange_rate = response_body['exchangeRate']
        if 'sourceCurrency' in response_body:
            self.__source_currency = response_body['sourceCurrency']
        if 'targetCurrency' in response_body:
            self.__target_currency = response_body['targetCurrency']
        if 'quoteTime' in response_body:
            self.__quote_time = response_body['quoteTime']
        if 'quotePrice' in response_body:
            self.__quote_price = response_body['quotePrice']
