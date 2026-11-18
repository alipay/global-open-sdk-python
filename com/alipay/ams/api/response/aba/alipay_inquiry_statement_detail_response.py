import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.statement import Statement



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquiryStatementDetailResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__statement = None  # type: Statement
        self.__metadata = None  # type: {str: (str,)}
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquiryStatementDetailResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def statement(self):
        """Gets the statement of this AlipayInquiryStatementDetailResponse.
        
        """
        return self.__statement

    @statement.setter
    def statement(self, value):
        self.__statement = value
    @property
    def metadata(self):
        """
        Customer metadata in key-value format. - Key max length: 32 - Value max length: 128 - Max number of keys: 30 - Total JSON string max length: 3096
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "statement") and self.statement is not None:
            params['statement'] = self.statement
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquiryStatementDetailResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'statement' in response_body:
            self.__statement = Statement()
            self.__statement.parse_rsp_body(response_body['statement'])
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
