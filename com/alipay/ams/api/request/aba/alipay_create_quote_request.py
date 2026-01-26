import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateQuoteRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateQuoteRequest, self).__init__("/ams/v1/aba/funds/createQuote") 

        self.__buy_amount = None  # type: Amount
        self.__sell_amount = None  # type: Amount
        self.__exchange_trade_type = None  # type: str
        

    @property
    def buy_amount(self):
        """Gets the buy_amount of this AlipayCreateQuoteRequest.
        
        """
        return self.__buy_amount

    @buy_amount.setter
    def buy_amount(self, value):
        self.__buy_amount = value
    @property
    def sell_amount(self):
        """Gets the sell_amount of this AlipayCreateQuoteRequest.
        
        """
        return self.__sell_amount

    @sell_amount.setter
    def sell_amount(self, value):
        self.__sell_amount = value
    @property
    def exchange_trade_type(self):
        """
        Foreign exchange delivery type. Possible value range:   SPOT: Real-time exchange rate.
        """
        return self.__exchange_trade_type

    @exchange_trade_type.setter
    def exchange_trade_type(self, value):
        self.__exchange_trade_type = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "buy_amount") and self.buy_amount is not None:
            params['buyAmount'] = self.buy_amount
        if hasattr(self, "sell_amount") and self.sell_amount is not None:
            params['sellAmount'] = self.sell_amount
        if hasattr(self, "exchange_trade_type") and self.exchange_trade_type is not None:
            params['exchangeTradeType'] = self.exchange_trade_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'buyAmount' in response_body:
            self.__buy_amount = Amount()
            self.__buy_amount.parse_rsp_body(response_body['buyAmount'])
        if 'sellAmount' in response_body:
            self.__sell_amount = Amount()
            self.__sell_amount.parse_rsp_body(response_body['sellAmount'])
        if 'exchangeTradeType' in response_body:
            self.__exchange_trade_type = response_body['exchangeTradeType']
