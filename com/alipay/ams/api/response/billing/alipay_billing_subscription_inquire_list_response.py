import json
from com.alipay.ams.api.model.result_info import ResultInfo
from com.alipay.ams.api.model.subscription import Subscription



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__subscriptions = None  # type: [Subscription]
        self.__has_more = None  # type: bool
        self.__next_cursor = None  # type: str
        self.__prev_cursor = None  # type: str
        self.__total = None  # type: int
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayBillingSubscriptionInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def subscriptions(self):
        """
        The subscriptions.
        """
        return self.__subscriptions

    @subscriptions.setter
    def subscriptions(self, value):
        self.__subscriptions = value
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
        if hasattr(self, "subscriptions") and self.subscriptions is not None:
            params['subscriptions'] = self.subscriptions
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
        response_body = super(AlipayBillingSubscriptionInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscriptions' in response_body:
            self.__subscriptions = []
            for item in response_body['subscriptions']:
                obj = Subscription()
                obj.parse_rsp_body(item)
                self.__subscriptions.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'nextCursor' in response_body:
            self.__next_cursor = response_body['nextCursor']
        if 'prevCursor' in response_body:
            self.__prev_cursor = response_body['prevCursor']
        if 'total' in response_body:
            self.__total = response_body['total']
