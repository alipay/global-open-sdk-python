import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayAuthRevokeTokenResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__extend_info = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayAuthRevokeTokenResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayAuthRevokeTokenResponse.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayAuthRevokeTokenResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
