import json
from com.alipay.ams.api.model.statement import Statement
from com.alipay.ams.api.model.result_result import ResultResult



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquiryStatementResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__statement_list = None  # type: [Statement]
        self.__result = None  # type: ResultResult
        self.__total_count = None  # type: int
        self.__total_page_number = None  # type: int
        self.__current_page_number = None  # type: int
        self.parse_rsp_body(rsp_body) 


    @property
    def statement_list(self):
        """Gets the statement_list of this AlipayInquiryStatementResponse.
        
        """
        return self.__statement_list

    @statement_list.setter
    def statement_list(self, value):
        self.__statement_list = value
    @property
    def result(self):
        """Gets the result of this AlipayInquiryStatementResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def total_count(self):
        """Gets the total_count of this AlipayInquiryStatementResponse.
        
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value
    @property
    def total_page_number(self):
        """Gets the total_page_number of this AlipayInquiryStatementResponse.
        
        """
        return self.__total_page_number

    @total_page_number.setter
    def total_page_number(self, value):
        self.__total_page_number = value
    @property
    def current_page_number(self):
        """Gets the current_page_number of this AlipayInquiryStatementResponse.
        
        """
        return self.__current_page_number

    @current_page_number.setter
    def current_page_number(self, value):
        self.__current_page_number = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "statement_list") and self.statement_list is not None:
            params['statementList'] = self.statement_list
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "total_count") and self.total_count is not None:
            params['totalCount'] = self.total_count
        if hasattr(self, "total_page_number") and self.total_page_number is not None:
            params['totalPageNumber'] = self.total_page_number
        if hasattr(self, "current_page_number") and self.current_page_number is not None:
            params['currentPageNumber'] = self.current_page_number
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquiryStatementResponse, self).parse_rsp_body(response_body)
        if 'statementList' in response_body:
            self.__statement_list = []
            for item in response_body['statementList']:
                obj = Statement()
                obj.parse_rsp_body(item)
                self.__statement_list.append(obj)
        if 'result' in response_body:
            self.__result = ResultResult()
            self.__result.parse_rsp_body(response_body['result'])
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
        if 'totalPageNumber' in response_body:
            self.__total_page_number = response_body['totalPageNumber']
        if 'currentPageNumber' in response_body:
            self.__current_page_number = response_body['currentPageNumber']
