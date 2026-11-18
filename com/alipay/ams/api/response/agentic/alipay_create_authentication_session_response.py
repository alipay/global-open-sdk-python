import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateAuthenticationSessionResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__normal_url = None  # type: str
        self.__sd_hash = None  # type: str
        self.__authentication_session_expiry_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreateAuthenticationSessionResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def normal_url(self):
        """
        Authentication intermediate-page URL. Required when result.resultStatus&#x3D;S.
        """
        return self.__normal_url

    @normal_url.setter
    def normal_url(self, value):
        self.__normal_url = value
    @property
    def sd_hash(self):
        """
        Mastercard L2 mandate hash. Required when result.resultStatus&#x3D;S for Mastercard IMMEDIATE/AUTONOMOUS. No separate length limit is specified; the total AMS message-size limit applies.
        """
        return self.__sd_hash

    @sd_hash.setter
    def sd_hash(self, value):
        self.__sd_hash = value
    @property
    def authentication_session_expiry_time(self):
        """
        Authentication session expiration time, required when result.resultStatus&#x3D;S. If redirect is not completed by then, the session ends and authentication remains incomplete. Use a new authenticationRequestId to create a new session. Wire value is an RFC 3339 / ISO 8601 string with a timezone, up to 64 characters; it is not converted to a date object.
        """
        return self.__authentication_session_expiry_time

    @authentication_session_expiry_time.setter
    def authentication_session_expiry_time(self, value):
        self.__authentication_session_expiry_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "normal_url") and self.normal_url is not None:
            params['normalUrl'] = self.normal_url
        if hasattr(self, "sd_hash") and self.sd_hash is not None:
            params['sdHash'] = self.sd_hash
        if hasattr(self, "authentication_session_expiry_time") and self.authentication_session_expiry_time is not None:
            params['authenticationSessionExpiryTime'] = self.authentication_session_expiry_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateAuthenticationSessionResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'normalUrl' in response_body:
            self.__normal_url = response_body['normalUrl']
        if 'sdHash' in response_body:
            self.__sd_hash = response_body['sdHash']
        if 'authenticationSessionExpiryTime' in response_body:
            self.__authentication_session_expiry_time = response_body['authenticationSessionExpiryTime']
