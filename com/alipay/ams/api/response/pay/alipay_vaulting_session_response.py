import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayVaultingSessionResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__vaulting_session_data = None  # type: str
        self.__vaulting_session_id = None  # type: str
        self.__vaulting_session_expiry_time = None  # type: str
        self.__normal_url = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayVaultingSessionResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def vaulting_session_data(self):
        """
        The encrypted vaulting session data. Pass the data to your front end to initiate the client-side SDK.     More information:  Maximum length: 4096 characters 
        """
        return self.__vaulting_session_data

    @vaulting_session_data.setter
    def vaulting_session_data(self, value):
        self.__vaulting_session_data = value
    @property
    def vaulting_session_id(self):
        """
        The encrypted ID is assigned by Antom to identify a vaulting session.     More information:  Maximum length: 64 characters 
        """
        return self.__vaulting_session_id

    @vaulting_session_id.setter
    def vaulting_session_id(self, value):
        self.__vaulting_session_id = value
    @property
    def vaulting_session_expiry_time(self):
        """
        The specific date and time after which the vaulting session will expire.   More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__vaulting_session_expiry_time

    @vaulting_session_expiry_time.setter
    def vaulting_session_expiry_time(self, value):
        self.__vaulting_session_expiry_time = value
    @property
    def normal_url(self):
        """
        The normal URL for vaulting session
        """
        return self.__normal_url

    @normal_url.setter
    def normal_url(self, value):
        self.__normal_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "vaulting_session_data") and self.vaulting_session_data is not None:
            params['vaultingSessionData'] = self.vaulting_session_data
        if hasattr(self, "vaulting_session_id") and self.vaulting_session_id is not None:
            params['vaultingSessionId'] = self.vaulting_session_id
        if hasattr(self, "vaulting_session_expiry_time") and self.vaulting_session_expiry_time is not None:
            params['vaultingSessionExpiryTime'] = self.vaulting_session_expiry_time
        if hasattr(self, "normal_url") and self.normal_url is not None:
            params['normalUrl'] = self.normal_url
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayVaultingSessionResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'vaultingSessionData' in response_body:
            self.__vaulting_session_data = response_body['vaultingSessionData']
        if 'vaultingSessionId' in response_body:
            self.__vaulting_session_id = response_body['vaultingSessionId']
        if 'vaultingSessionExpiryTime' in response_body:
            self.__vaulting_session_expiry_time = response_body['vaultingSessionExpiryTime']
        if 'normalUrl' in response_body:
            self.__normal_url = response_body['normalUrl']
