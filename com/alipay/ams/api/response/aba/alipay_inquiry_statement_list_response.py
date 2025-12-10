import json
from com.alipay.ams.api.model.statement import Statement
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquiryStatementListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__statement_list = None  # type: [Statement]
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def statement_list(self):
        """Gets the statement_list of this AlipayInquiryStatementListResponse.
        
        """
        return self.__statement_list

    @statement_list.setter
    def statement_list(self, value):
        self.__statement_list = value
    @property
    def result(self):
        """Gets the result of this AlipayInquiryStatementListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "statement_list") and self.statement_list is not None:
            params['statementList'] = self.statement_list
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquiryStatementListResponse, self).parse_rsp_body(response_body)
        if 'statementList' in response_body:
            self.__statement_list = []
            for item in response_body['statementList']:
                obj = Statement()
                obj.parse_rsp_body(item)
                self.__statement_list.append(obj)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
