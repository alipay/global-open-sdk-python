import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.price import Price



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPriceInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__prices = None  # type: [Price]
        self.__has_more = None  # type: bool
        self.__total_count = None  # type: int
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPriceInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def prices(self):
        """
        The prices.
        """
        return self.__prices

    @prices.setter
    def prices(self, value):
        self.__prices = value
    @property
    def has_more(self):
        """
        The has more.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def total_count(self):
        """
        The total number of records. Note: See documentation for details.
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "prices") and self.prices is not None:
            params['prices'] = self.prices
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "total_count") and self.total_count is not None:
            params['totalCount'] = self.total_count
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPriceInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'prices' in response_body:
            self.__prices = []
            for item in response_body['prices']:
                obj = Price()
                obj.parse_rsp_body(item)
                self.__prices.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
