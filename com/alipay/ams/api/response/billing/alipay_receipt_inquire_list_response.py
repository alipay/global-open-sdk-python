import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.receipt import Receipt



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayReceiptInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__receipts = None  # type: [Receipt]
        self.__total = None  # type: int
        self.__has_more = None  # type: bool
        self.__next_cursor = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayReceiptInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def receipts(self):
        """
        List of receipt summaries, limited to &#x60;limit&#x60; (max 100) per page. Returned only when result.resultCode is SUCCESS.
        """
        return self.__receipts

    @receipts.setter
    def receipts(self, value):
        self.__receipts = value
    @property
    def total(self):
        """
        Total number of matching records across all pages. Requires an extra &#x60;COUNT&#x60; query - use &#x60;includeTotal&#x3D;true&#x60; to request it. Absent from response when &#x60;includeTotal&#x60; is omitted or &#x60;false&#x60;. Can be null (not returned by default). Returned only when result.resultCode is SUCCESS.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
    @property
    def has_more(self):
        """
        Whether more results exist beyond the current page. Detected by fetching &#x60;limit + 1&#x60; rows internally - if the extra row exists, &#x60;hasMore&#x3D;true&#x60; (the extra row is not returned). &#x60;false&#x60; &#x3D; last page - hide the \&quot;Next\&quot; button. Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def next_cursor(self):
        """
        The &#x60;receiptId&#x60; of the last receipt in the current page. Use this value as &#x60;startingAfter&#x60; in the next request to fetch the next page. Absent when &#x60;hasMore&#x3D;false&#x60;. Can be null (no more pages). Returned only when result.resultCode is SUCCESS.
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self.__next_cursor = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "receipts") and self.receipts is not None:
            params['receipts'] = self.receipts
        if hasattr(self, "total") and self.total is not None:
            params['total'] = self.total
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "next_cursor") and self.next_cursor is not None:
            params['nextCursor'] = self.next_cursor
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayReceiptInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'receipts' in response_body:
            self.__receipts = []
            for item in response_body['receipts']:
                obj = Receipt()
                obj.parse_rsp_body(item)
                self.__receipts.append(obj)
        if 'total' in response_body:
            self.__total = response_body['total']
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'nextCursor' in response_body:
            self.__next_cursor = response_body['nextCursor']
