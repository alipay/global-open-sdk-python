import json
from com.alipay.ams.api.model.quote import Quote
from com.alipay.ams.api.model.result import Result


from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayInquireExchangeRateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__()

        self.__quotes = None  # type: [Quote]
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body)

    @property
    def quotes(self):
        """Gets the quotes of this AlipayInquireExchangeRateResponse."""
        return self.__quotes

    @quotes.setter
    def quotes(self, value):
        self.__quotes = value

    @property
    def result(self):
        """Gets the result of this AlipayInquireExchangeRateResponse."""
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "quotes") and self.quotes is not None:
            params["quotes"] = self.quotes
        if hasattr(self, "result") and self.result is not None:
            params["result"] = self.result
        return params

    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireExchangeRateResponse, self).parse_rsp_body(
            response_body
        )
        if "quotes" in response_body:
            self.__quotes = []
            for item in response_body["quotes"]:
                obj = Quote()
                obj.parse_rsp_body(item)
                self.__quotes.append(obj)
        if "result" in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body["result"])
