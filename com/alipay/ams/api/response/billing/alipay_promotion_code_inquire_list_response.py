import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.promotion_code_info import PromotionCodeInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPromotionCodeInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__promotion_codes = None  # type: [PromotionCodeInfo]
        self.__has_more = None  # type: bool
        self.__next_cursor = None  # type: str
        self.__prev_cursor = None  # type: str
        self.__total = None  # type: int
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPromotionCodeInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def promotion_codes(self):
        """
        The promotion codes. Note: See documentation for details.
        """
        return self.__promotion_codes

    @promotion_codes.setter
    def promotion_codes(self, value):
        self.__promotion_codes = value
    @property
    def has_more(self):
        """
        The has more. Note: See documentation for details.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def next_cursor(self):
        """
        The next cursor. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self.__next_cursor = value
    @property
    def prev_cursor(self):
        """
        The prev cursor. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__prev_cursor

    @prev_cursor.setter
    def prev_cursor(self, value):
        self.__prev_cursor = value
    @property
    def total(self):
        """
        The total. Note: See documentation for details.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "promotion_codes") and self.promotion_codes is not None:
            params['promotionCodes'] = self.promotion_codes
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "next_cursor") and self.next_cursor is not None:
            params['nextCursor'] = self.next_cursor
        if hasattr(self, "prev_cursor") and self.prev_cursor is not None:
            params['prevCursor'] = self.prev_cursor
        if hasattr(self, "total") and self.total is not None:
            params['total'] = self.total
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPromotionCodeInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'promotionCodes' in response_body:
            self.__promotion_codes = []
            for item in response_body['promotionCodes']:
                obj = PromotionCodeInfo()
                obj.parse_rsp_body(item)
                self.__promotion_codes.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'nextCursor' in response_body:
            self.__next_cursor = response_body['nextCursor']
        if 'prevCursor' in response_body:
            self.__prev_cursor = response_body['prevCursor']
        if 'total' in response_body:
            self.__total = response_body['total']
