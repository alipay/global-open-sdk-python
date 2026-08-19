import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCustomerCreatePortalLinkResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__token = None  # type: str
        self.__portal_url = None  # type: str
        self.__expires_at = None  # type: str
        self.__send_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCustomerCreatePortalLinkResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def token(self):
        """
        Opaque URL-safe bearer token. Treat it as a credential: do not log, parse, or store its internal structure because the format may change without notice. Maximum length: 4096 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value
    @property
    def portal_url(self):
        """
        Fully-qualified portal URL. Null when the portal base URL is not configured for the merchant; in that case, build the URL from &#x60;token&#x60;. Maximum length: 2048 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__portal_url

    @portal_url.setter
    def portal_url(self, value):
        self.__portal_url = value
    @property
    def expires_at(self):
        """
        Expiration time of the portal link, returned as a string. Maximum length: 32 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value
    @property
    def send_status(self):
        """
        Email send status. Valid values are &#x60;SENT&#x60; and &#x60;FAILED&#x60;. Populated only when request &#x60;autoSend&#x3D;true&#x60;; a send failure never blocks link creation. Null when &#x60;autoSend&#x3D;false&#x60;. Maximum length: 16 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__send_status

    @send_status.setter
    def send_status(self, value):
        self.__send_status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "token") and self.token is not None:
            params['token'] = self.token
        if hasattr(self, "portal_url") and self.portal_url is not None:
            params['portalUrl'] = self.portal_url
        if hasattr(self, "expires_at") and self.expires_at is not None:
            params['expiresAt'] = self.expires_at
        if hasattr(self, "send_status") and self.send_status is not None:
            params['sendStatus'] = self.send_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCustomerCreatePortalLinkResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'token' in response_body:
            self.__token = response_body['token']
        if 'portalUrl' in response_body:
            self.__portal_url = response_body['portalUrl']
        if 'expiresAt' in response_body:
            self.__expires_at = response_body['expiresAt']
        if 'sendStatus' in response_body:
            self.__send_status = response_body['sendStatus']
