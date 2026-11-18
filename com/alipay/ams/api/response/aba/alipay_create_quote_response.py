import json
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateQuoteResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__exchange_trade_type = None  # type: str
        self.__quote = None  # type: Quote
        self.__sell_amount = None  # type: Amount
        self.__buy_amount = None  # type: Amount
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


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
    def quote(self):
        """Gets the quote of this AlipayCreateQuoteResponse.
        
        """
        return self.__quote

    @quote.setter
    def quote(self, value):
        self.__quote = value
    @property
    def sell_amount(self):
        """Gets the sell_amount of this AlipayCreateQuoteResponse.
        
        """
        return self.__sell_amount

    @sell_amount.setter
    def sell_amount(self, value):
        self.__sell_amount = value
    @property
    def buy_amount(self):
        """Gets the buy_amount of this AlipayCreateQuoteResponse.
        
        """
        return self.__buy_amount

    @buy_amount.setter
    def buy_amount(self, value):
        self.__buy_amount = value
    @property
    def result(self):
        """Gets the result of this AlipayCreateQuoteResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "exchange_trade_type") and self.exchange_trade_type is not None:
            params['exchangeTradeType'] = self.exchange_trade_type
        if hasattr(self, "quote") and self.quote is not None:
            params['quote'] = self.quote
        if hasattr(self, "sell_amount") and self.sell_amount is not None:
            params['sellAmount'] = self.sell_amount
        if hasattr(self, "buy_amount") and self.buy_amount is not None:
            params['buyAmount'] = self.buy_amount
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateQuoteResponse, self).parse_rsp_body(response_body)
        if 'exchangeTradeType' in response_body:
            self.__exchange_trade_type = response_body['exchangeTradeType']
        if 'quote' in response_body:
            self.__quote = Quote()
            self.__quote.parse_rsp_body(response_body['quote'])
        if 'sellAmount' in response_body:
            self.__sell_amount = Amount()
            self.__sell_amount.parse_rsp_body(response_body['sellAmount'])
        if 'buyAmount' in response_body:
            self.__buy_amount = Amount()
            self.__buy_amount.parse_rsp_body(response_body['buyAmount'])
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
