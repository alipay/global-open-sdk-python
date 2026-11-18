import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayMeterCreateSessionResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__session_id = None  # type: str
        self.__session_expiry_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayMeterCreateSessionResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def session_id(self):
        """
        The session id. Maximum length: 48 characters. Note: See documentation for details.
        """
        return self.__session_id

    @session_id.setter
    def session_id(self, value):
        self.__session_id = value
    @property
    def session_expiry_time(self):
        """
        The session expiry time. Maximum length: 13 characters. Note: See documentation for details.
        """
        return self.__session_expiry_time

    @session_expiry_time.setter
    def session_expiry_time(self, value):
        self.__session_expiry_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "session_id") and self.session_id is not None:
            params['sessionId'] = self.session_id
        if hasattr(self, "session_expiry_time") and self.session_expiry_time is not None:
            params['sessionExpiryTime'] = self.session_expiry_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayMeterCreateSessionResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'sessionId' in response_body:
            self.__session_id = response_body['sessionId']
        if 'sessionExpiryTime' in response_body:
            self.__session_expiry_time = response_body['sessionExpiryTime']
