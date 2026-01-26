import json
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateExchangeResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__exchange_request_id = None  # type: str
        self.__exchange_trade_type = None  # type: str
        self.__exchange_mode = None  # type: str
        self.__quote = None  # type: Quote
        self.__buy_amount = None  # type: Amount
        self.__sell_amount = None  # type: Amount
        self.__exchange_start_time = None  # type: str
        self.__exchange_end_time = None  # type: str
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def exchange_request_id(self):
        """Gets the exchange_request_id of this AlipayCreateExchangeResponse.
        
        """
        return self.__exchange_request_id

    @exchange_request_id.setter
    def exchange_request_id(self, value):
        self.__exchange_request_id = value
    @property
    def exchange_trade_type(self):
        """Gets the exchange_trade_type of this AlipayCreateExchangeResponse.
        
        """
        return self.__exchange_trade_type

    @exchange_trade_type.setter
    def exchange_trade_type(self, value):
        self.__exchange_trade_type = value
    @property
    def exchange_mode(self):
        """Gets the exchange_mode of this AlipayCreateExchangeResponse.
        
        """
        return self.__exchange_mode

    @exchange_mode.setter
    def exchange_mode(self, value):
        self.__exchange_mode = value
    @property
    def quote(self):
        """Gets the quote of this AlipayCreateExchangeResponse.
        
        """
        return self.__quote

    @quote.setter
    def quote(self, value):
        self.__quote = value
    @property
    def buy_amount(self):
        """Gets the buy_amount of this AlipayCreateExchangeResponse.
        
        """
        return self.__buy_amount

    @buy_amount.setter
    def buy_amount(self, value):
        self.__buy_amount = value
    @property
    def sell_amount(self):
        """Gets the sell_amount of this AlipayCreateExchangeResponse.
        
        """
        return self.__sell_amount

    @sell_amount.setter
    def sell_amount(self, value):
        self.__sell_amount = value
    @property
    def exchange_start_time(self):
        """Gets the exchange_start_time of this AlipayCreateExchangeResponse.
        
        """
        return self.__exchange_start_time

    @exchange_start_time.setter
    def exchange_start_time(self, value):
        self.__exchange_start_time = value
    @property
    def exchange_end_time(self):
        """Gets the exchange_end_time of this AlipayCreateExchangeResponse.
        
        """
        return self.__exchange_end_time

    @exchange_end_time.setter
    def exchange_end_time(self, value):
        self.__exchange_end_time = value
    @property
    def result(self):
        """Gets the result of this AlipayCreateExchangeResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "exchange_request_id") and self.exchange_request_id is not None:
            params['exchangeRequestId'] = self.exchange_request_id
        if hasattr(self, "exchange_trade_type") and self.exchange_trade_type is not None:
            params['exchangeTradeType'] = self.exchange_trade_type
        if hasattr(self, "exchange_mode") and self.exchange_mode is not None:
            params['exchangeMode'] = self.exchange_mode
        if hasattr(self, "quote") and self.quote is not None:
            params['quote'] = self.quote
        if hasattr(self, "buy_amount") and self.buy_amount is not None:
            params['buyAmount'] = self.buy_amount
        if hasattr(self, "sell_amount") and self.sell_amount is not None:
            params['sellAmount'] = self.sell_amount
        if hasattr(self, "exchange_start_time") and self.exchange_start_time is not None:
            params['exchangeStartTime'] = self.exchange_start_time
        if hasattr(self, "exchange_end_time") and self.exchange_end_time is not None:
            params['exchangeEndTime'] = self.exchange_end_time
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateExchangeResponse, self).parse_rsp_body(response_body)
        if 'exchangeRequestId' in response_body:
            self.__exchange_request_id = response_body['exchangeRequestId']
        if 'exchangeTradeType' in response_body:
            self.__exchange_trade_type = response_body['exchangeTradeType']
        if 'exchangeMode' in response_body:
            self.__exchange_mode = response_body['exchangeMode']
        if 'quote' in response_body:
            self.__quote = Quote()
            self.__quote.parse_rsp_body(response_body['quote'])
        if 'buyAmount' in response_body:
            self.__buy_amount = Amount()
            self.__buy_amount.parse_rsp_body(response_body['buyAmount'])
        if 'sellAmount' in response_body:
            self.__sell_amount = Amount()
            self.__sell_amount.parse_rsp_body(response_body['sellAmount'])
        if 'exchangeStartTime' in response_body:
            self.__exchange_start_time = response_body['exchangeStartTime']
        if 'exchangeEndTime' in response_body:
            self.__exchange_end_time = response_body['exchangeEndTime']
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
