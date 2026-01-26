import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateExchangeRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateExchangeRequest, self).__init__("/ams/v1/aba/funds/createExchange") 

        self.__buy_amount = None  # type: Amount
        self.__sell_amount = None  # type: Amount
        self.__exchange_trade_type = None  # type: str
        self.__exchange_request_id = None  # type: str
        self.__exchange_mode = None  # type: str
        

    @property
    def buy_amount(self):
        """Gets the buy_amount of this AlipayCreateExchangeRequest.
        
        """
        return self.__buy_amount

    @buy_amount.setter
    def buy_amount(self, value):
        self.__buy_amount = value
    @property
    def sell_amount(self):
        """Gets the sell_amount of this AlipayCreateExchangeRequest.
        
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
    @property
    def exchange_request_id(self):
        """Gets the exchange_request_id of this AlipayCreateExchangeRequest.
        
        """
        return self.__exchange_request_id

    @exchange_request_id.setter
    def exchange_request_id(self, value):
        self.__exchange_request_id = value
    @property
    def exchange_mode(self):
        """
        Foreign exchange delivery model. Possible value range:   APPOINTED: indicates an exchange rate at the appointed time.
        """
        return self.__exchange_mode

    @exchange_mode.setter
    def exchange_mode(self, value):
        self.__exchange_mode = value


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
        if hasattr(self, "exchange_request_id") and self.exchange_request_id is not None:
            params['exchangeRequestId'] = self.exchange_request_id
        if hasattr(self, "exchange_mode") and self.exchange_mode is not None:
            params['exchangeMode'] = self.exchange_mode
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
        if 'exchangeRequestId' in response_body:
            self.__exchange_request_id = response_body['exchangeRequestId']
        if 'exchangeMode' in response_body:
            self.__exchange_mode = response_body['exchangeMode']
