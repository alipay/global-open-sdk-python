import json
from com.alipay.ams.api.model.result_info import ResultInfo
from com.alipay.ams.api.model.coupon import Coupon



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCouponInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__coupons = None  # type: [Coupon]
        self.__has_more = None  # type: bool
        self.__next_cursor = None  # type: str
        self.__total = None  # type: int
        self.__previous_cursor = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCouponInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def coupons(self):
        """
        List of coupon summary items. Empty array if no results. Returned when resultCode is &#x60;SUCCESS&#x60;. Maximum size: 100 elements per page.
        """
        return self.__coupons

    @coupons.setter
    def coupons(self, value):
        self.__coupons = value
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
        The &#x60;couponId&#x60; of the last element of the current page. Pass as &#x60;startingAfter&#x60; in the next request to page toward older items (&#x60;gmt_create DESC&#x60; keyset). Returned when &#x60;hasMore&#x60; is &#x60;true&#x60;. Absent when &#x60;hasMore&#x60; is &#x60;false&#x60;. Returned only when result.resultCode is SUCCESS.
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self.__next_cursor = value
    @property
    def total(self):
        """
        Total count of matching coupons. Only returned when request has &#x60;includeTotal&#x3D;true&#x60;. Returned only when result.resultCode is SUCCESS.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
    @property
    def previous_cursor(self):
        """
        The &#x60;couponId&#x60; of the first element of the current page. Pass as &#x60;endingBefore&#x60; to page toward newer items. Only returned when the request used &#x60;endingBefore&#x60;. Returned only when result.resultCode is SUCCESS.
        """
        return self.__previous_cursor

    @previous_cursor.setter
    def previous_cursor(self, value):
        self.__previous_cursor = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "coupons") and self.coupons is not None:
            params['coupons'] = self.coupons
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
        response_body = super(AlipayCouponInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'coupons' in response_body:
            self.__coupons = []
            for item in response_body['coupons']:
                obj = Coupon()
                obj.parse_rsp_body(item)
                self.__coupons.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'nextCursor' in response_body:
            self.__next_cursor = response_body['nextCursor']
        if 'total' in response_body:
            self.__total = response_body['total']
        if 'previousCursor' in response_body:
            self.__previous_cursor = response_body['previousCursor']
