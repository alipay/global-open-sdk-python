import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayUpdateCardStatusResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__status = None  # type: str
        self.__request_id = None  # type: str
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def status(self):
        """Gets the status of this AlipayUpdateCardStatusResponse.
        
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def request_id(self):
        """Gets the request_id of this AlipayUpdateCardStatusResponse.
        
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
    @property
    def result(self):
        """Gets the result of this AlipayUpdateCardStatusResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "request_id") and self.request_id is not None:
            params['requestId'] = self.request_id
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayUpdateCardStatusResponse, self).parse_rsp_body(response_body)
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'requestId' in response_body:
            self.__request_id = response_body['requestId']
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
