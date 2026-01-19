import json




class PaymentQuote:
    def __init__(self):
        
        self.__buy_currency = None  # type: str
        self.__sell_currency = None  # type: str
        self.__quote_id = None  # type: str
        self.__exchange_rate = None  # type: float
        

    @property
    def buy_currency(self):
        """
        商户视角下买入的币种 - 商户订单定价币种
        """
        return self.__buy_currency

    @buy_currency.setter
    def buy_currency(self, value):
        self.__buy_currency = value
    @property
    def sell_currency(self):
        """
        商户视角下卖出的币种 - 用户支付币种
        """
        return self.__sell_currency

    @sell_currency.setter
    def sell_currency(self, value):
        self.__sell_currency = value
    @property
    def quote_id(self):
        """
        蚂蚁为此次报价颁发的唯一id
        """
        return self.__quote_id

    @quote_id.setter
    def quote_id(self, value):
        self.__quote_id = value
    @property
    def exchange_rate(self):
        """
        商户可直接用于乘法计算的最终汇率值，精度统一为15位decimal place
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
        if hasattr(self, "quote_id") and self.quote_id is not None:
            params['quoteId'] = self.quote_id
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
        if 'quoteId' in response_body:
            self.__quote_id = response_body['quoteId']
        if 'exchangeRate' in response_body:
            self.__exchange_rate = response_body['exchangeRate']
