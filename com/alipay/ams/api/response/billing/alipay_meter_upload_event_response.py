import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.error import Error



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayMeterUploadEventResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__retry_after = None  # type: int
        self.__errors = None  # type: [Error]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayMeterUploadEventResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def retry_after(self):
        """
        The retry after. Note: See documentation for details.
        """
        return self.__retry_after

    @retry_after.setter
    def retry_after(self, value):
        self.__retry_after = value
    @property
    def errors(self):
        """
        The errors. Note: See documentation for details.
        """
        return self.__errors

    @errors.setter
    def errors(self, value):
        self.__errors = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "retry_after") and self.retry_after is not None:
            params['retryAfter'] = self.retry_after
        if hasattr(self, "errors") and self.errors is not None:
            params['errors'] = self.errors
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayMeterUploadEventResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'retryAfter' in response_body:
            self.__retry_after = response_body['retryAfter']
        if 'errors' in response_body:
            self.__errors = []
            for item in response_body['errors']:
                obj = Error()
                obj.parse_rsp_body(item)
                self.__errors.append(obj)
