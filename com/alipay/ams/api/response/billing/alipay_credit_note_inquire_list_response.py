import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.credit_note_summary import CreditNoteSummary



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreditNoteInquireListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__has_more = None  # type: bool
        self.__total_count = None  # type: int
        self.__list = None  # type: [CreditNoteSummary]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreditNoteInquireListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
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
    @property
    def list(self):
        """
        The list. Note: See documentation for details.
        """
        return self.__list

    @list.setter
    def list(self, value):
        self.__list = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "total_count") and self.total_count is not None:
            params['totalCount'] = self.total_count
        if hasattr(self, "list") and self.list is not None:
            params['list'] = self.list
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreditNoteInquireListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
        if 'list' in response_body:
            self.__list = []
            for item in response_body['list']:
                obj = CreditNoteSummary()
                obj.parse_rsp_body(item)
                self.__list.append(obj)
