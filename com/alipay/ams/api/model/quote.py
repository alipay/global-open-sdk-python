import json
from com.alipay.ams.api.model.amount import Amount




class Quote:
    def __init__(self):
        
        self.__quote_id = None  # type: str
        self.__quote_currency_pair = None  # type: str
        self.__quote_price = None  # type: float
        self.__quote_start_time = None  # type: str
        self.__quote_expiry_time = None  # type: str
        self.__guaranteed = None  # type: bool
        self.__exchange_amount = None  # type: Amount
        

    @property
    def quote_id(self):
        """
        The unique ID that is assigned by Antom to identify an exchange rate.   More information:  Maximum length: 64 characters
        """
        return self.__quote_id

    @quote_id.setter
    def quote_id(self, value):
        self.__quote_id = value
    @property
    def quote_currency_pair(self):
        """
        The exchange rate between settlement currency and transaction currency. Two currencies are separated with a slash and use the three-letter ISO-4217 currency code.    More information:  Maximum length: 16 characters
        """
        return self.__quote_currency_pair

    @quote_currency_pair.setter
    def quote_currency_pair(self, value):
        self.__quote_currency_pair = value
    @property
    def quote_price(self):
        """
        The exchange rate used when a currency conversion between settlement currency and transaction currency occurs.    More information:  Value range: 1 - unlimited
        """
        return self.__quote_price

    @quote_price.setter
    def quote_price(self, value):
        self.__quote_price = value
    @property
    def quote_start_time(self):
        """
        Effective time of the exchange rate.   More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__quote_start_time

    @quote_start_time.setter
    def quote_start_time(self, value):
        self.__quote_start_time = value
    @property
    def quote_expiry_time(self):
        """
        Expiration time of the exchange rate.    More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__quote_expiry_time

    @quote_expiry_time.setter
    def quote_expiry_time(self, value):
        self.__quote_expiry_time = value
    @property
    def guaranteed(self):
        """
        Guaranteed exchange rate available for payment.    
        """
        return self.__guaranteed

    @guaranteed.setter
    def guaranteed(self, value):
        self.__guaranteed = value
    @property
    def exchange_amount(self):
        """Gets the exchange_amount of this Quote.
        
        """
        return self.__exchange_amount

    @exchange_amount.setter
    def exchange_amount(self, value):
        self.__exchange_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "quote_id") and self.quote_id is not None:
            params['quoteId'] = self.quote_id
        if hasattr(self, "quote_currency_pair") and self.quote_currency_pair is not None:
            params['quoteCurrencyPair'] = self.quote_currency_pair
        if hasattr(self, "quote_price") and self.quote_price is not None:
            params['quotePrice'] = self.quote_price
        if hasattr(self, "quote_start_time") and self.quote_start_time is not None:
            params['quoteStartTime'] = self.quote_start_time
        if hasattr(self, "quote_expiry_time") and self.quote_expiry_time is not None:
            params['quoteExpiryTime'] = self.quote_expiry_time
        if hasattr(self, "guaranteed") and self.guaranteed is not None:
            params['guaranteed'] = self.guaranteed
        if hasattr(self, "exchange_amount") and self.exchange_amount is not None:
            params['exchangeAmount'] = self.exchange_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'quoteId' in response_body:
            self.__quote_id = response_body['quoteId']
        if 'quoteCurrencyPair' in response_body:
            self.__quote_currency_pair = response_body['quoteCurrencyPair']
        if 'quotePrice' in response_body:
            self.__quote_price = response_body['quotePrice']
        if 'quoteStartTime' in response_body:
            self.__quote_start_time = response_body['quoteStartTime']
        if 'quoteExpiryTime' in response_body:
            self.__quote_expiry_time = response_body['quoteExpiryTime']
        if 'guaranteed' in response_body:
            self.__guaranteed = response_body['guaranteed']
        if 'exchangeAmount' in response_body:
            self.__exchange_amount = Amount()
            self.__exchange_amount.parse_rsp_body(response_body['exchangeAmount'])
