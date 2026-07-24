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
        The invoices.
        """
        return self.__invoices

    @invoices.setter
    def invoices(self, value):
        self.__invoices = value
    @property
    def total(self):
        """
        The total. Note: See documentation for details.
        """
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
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
