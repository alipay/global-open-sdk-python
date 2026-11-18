import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.invoice import Invoice



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__invoices = None  # type: [Invoice]
        self.__total = None  # type: str
        self.__has_more = None  # type: bool
        self.__next_cursor = None  # type: str
        self.__degrade = None  # type: bool
        self.__previous_cursor = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def invoices(self):
        """
        Array of invoice summary objects. May be empty if no invoices match. Maximum 100 elements per page (controlled by &#x60;limit&#x60; parameter). Cannot be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__invoices

    @invoices.setter
    def invoices(self, value):
        self.__invoices = value
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
        The &#x60;invoiceId&#x60; of the last invoice in the current page. Use this value as &#x60;startingAfter&#x60; in the next request to fetch the next page. Absent when &#x60;hasMore&#x3D;false&#x60;. Can be null (no more pages). Returned only when result.resultCode is SUCCESS.
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self.__next_cursor = value
    @property
    def degrade(self):
        """
        Whether the degrade DB served the query (ZSearch fallback path). &#x60;null&#x60; when ZSearch served the query normally (backward-compatible with existing callers). &#x60;true&#x60; when degrade DB served the query. Can be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__degrade

    @degrade.setter
    def degrade(self, value):
        self.__degrade = value
    @property
    def previous_cursor(self):
        """
        The &#x60;invoiceId&#x60; of the first invoice in the current page. Use this value as &#x60;endingBefore&#x60; to navigate further backward. Only populated when the current request used &#x60;endingBefore&#x60;. Not populated in forward navigation. Can be null. Returned only when result.resultCode is SUCCESS.
        """
        return self.__previous_cursor

    @previous_cursor.setter
    def previous_cursor(self, value):
        self.__previous_cursor = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "invoices") and self.invoices is not None:
            params['invoices'] = self.invoices
        if hasattr(self, "total") and self.total is not None:
            params['total'] = self.total
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "next_cursor") and self.next_cursor is not None:
            params['nextCursor'] = self.next_cursor
        if hasattr(self, "degrade") and self.degrade is not None:
            params['degrade'] = self.degrade
        if hasattr(self, "previous_cursor") and self.previous_cursor is not None:
            params['previousCursor'] = self.previous_cursor
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'invoices' in response_body:
            self.__invoices = []
            for item in response_body['invoices']:
                obj = Invoice()
                obj.parse_rsp_body(item)
                self.__invoices.append(obj)
        if 'total' in response_body:
            self.__total = response_body['total']
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'nextCursor' in response_body:
            self.__next_cursor = response_body['nextCursor']
        if 'degrade' in response_body:
            self.__degrade = response_body['degrade']
        if 'previousCursor' in response_body:
            self.__previous_cursor = response_body['previousCursor']
