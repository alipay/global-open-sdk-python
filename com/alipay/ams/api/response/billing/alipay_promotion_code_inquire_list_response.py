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
        self.__total = None  # type: int
        self.__previous_cursor = None  # type: str
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
        List of promotion code summary items. Maximum size: 100 elements per page (governed by request &#x60;limit&#x60; max value 100). Empty array if no results. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__promotion_codes

    @promotion_codes.setter
    def promotion_codes(self, value):
        self.__promotion_codes = value
    @property
    def has_more(self):
        """
        Whether more results exist beyond the current page. &#x60;false&#x60; &#x3D; last page. Returned when resultCode is &#x60;SUCCESS&#x60;.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def next_cursor(self):
        """
        Entity ID of the last element. Pass as &#x60;startingAfter&#x60; in the next request. Returned when &#x60;hasMore&#x60; is &#x60;true&#x60;. Absent when &#x60;hasMore&#x60; is &#x60;false&#x60;. Returned only when result.resultCode is SUCCESS.
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self.__next_cursor = value
    @property
    def total(self):
        """
        Total count of matching promotion codes. Only returned when request has &#x60;includeTotal&#x3D;true&#x60;. Returned only when result.resultCode is SUCCESS.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
    @property
    def previous_cursor(self):
        """
        Entity ID of the first element. Pass as &#x60;endingBefore&#x60; to navigate backward. Only returned when request used &#x60;endingBefore&#x60;. Returned only when result.resultCode is SUCCESS.
        """
        return self.__previous_cursor

    @previous_cursor.setter
    def previous_cursor(self, value):
        self.__previous_cursor = value


    

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
        if hasattr(self, "total") and self.total is not None:
            params['total'] = self.total
        if hasattr(self, "previous_cursor") and self.previous_cursor is not None:
            params['previousCursor'] = self.previous_cursor
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
        if 'total' in response_body:
            self.__total = response_body['total']
        if 'previousCursor' in response_body:
            self.__previous_cursor = response_body['previousCursor']
