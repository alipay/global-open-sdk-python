import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateBindingSessionResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__normal_url = None  # type: str
        self.__sd_hash = None  # type: str
        self.__binding_session_data = None  # type: str
        self.__binding_session_expiry_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreateBindingSessionResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def normal_url(self):
        """
        Binding intermediate-page URL. Required when result.resultStatus&#x3D;S.
        """
        return self.__normal_url

    @normal_url.setter
    def normal_url(self, value):
        self.__normal_url = value
    @property
    def sd_hash(self):
        """
        Mastercard L2 mandate hash. Required only when result.resultStatus&#x3D;S and the request is CARD + MASTERCARD + authorizeOnBind&#x3D;true + purchaseType&#x3D;IMMEDIATE. Treat as opaque and pass unchanged to inquirePaymentToken. Not returned for other channels or scenarios. No separate length limit; subject to the total AMS message-size limit.
        """
        return self.__sd_hash

    @sd_hash.setter
    def sd_hash(self, value):
        self.__sd_hash = value
    @property
    def binding_session_data(self):
        """
        Encrypted binding-session data to pass unchanged to the frontend SDK. Do not parse or modify it. Required and non-empty only for successful CARD responses; omitted for APM and F/U. Valid until bindingSessionExpiryTime. Does not indicate completed binding or authorization, and is not a subsequent business-context identifier.
        """
        return self.__binding_session_data

    @binding_session_data.setter
    def binding_session_data(self, value):
        self.__binding_session_data = value
    @property
    def binding_session_expiry_time(self):
        """
        Binding session expiration time, required when result.resultStatus&#x3D;S. If redirect is not completed by then, the session ends and binding remains incomplete. Use a new bindingRequestId to create a new session. Wire value is an RFC 3339 / ISO 8601 string with a timezone, up to 64 characters; it is not converted to a date object.
        """
        return self.__binding_session_expiry_time

    @binding_session_expiry_time.setter
    def binding_session_expiry_time(self, value):
        self.__binding_session_expiry_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "normal_url") and self.normal_url is not None:
            params['normalUrl'] = self.normal_url
        if hasattr(self, "sd_hash") and self.sd_hash is not None:
            params['sdHash'] = self.sd_hash
        if hasattr(self, "binding_session_data") and self.binding_session_data is not None:
            params['bindingSessionData'] = self.binding_session_data
        if hasattr(self, "binding_session_expiry_time") and self.binding_session_expiry_time is not None:
            params['bindingSessionExpiryTime'] = self.binding_session_expiry_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateBindingSessionResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'normalUrl' in response_body:
            self.__normal_url = response_body['normalUrl']
        if 'sdHash' in response_body:
            self.__sd_hash = response_body['sdHash']
        if 'bindingSessionData' in response_body:
            self.__binding_session_data = response_body['bindingSessionData']
        if 'bindingSessionExpiryTime' in response_body:
            self.__binding_session_expiry_time = response_body['bindingSessionExpiryTime']
