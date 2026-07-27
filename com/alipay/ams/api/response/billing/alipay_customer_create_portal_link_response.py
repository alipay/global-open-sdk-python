import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.error_stack import ErrorStack



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCustomerCreatePortalLinkResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__token = None  # type: str
        self.__portal_url = None  # type: str
        self.__expires_at = None  # type: str
        self.__send_status = None  # type: str
        self.__success = None  # type: bool
        self.__error_context = None  # type: ErrorStack
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
        The encrypted token. Maximum length: 512 characters.
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value
    @property
    def portal_url(self):
        """
        The portal access URL. Maximum length: 1024 characters. Note: See documentation for details.
        """
        return self.__portal_url

    @portal_url.setter
    def portal_url(self, value):
        self.__portal_url = value
    @property
    def expires_at(self):
        """
        The expiration time.
        """
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value
    @property
    def send_status(self):
        """
        The email sending status. Maximum length: 6 characters. Note: See documentation for details.
        """
        return self.__send_status

    @send_status.setter
    def send_status(self, value):
        self.__send_status = value
    @property
    def success(self):
        """
        Indicates whether the operation is successful.
        """
        return self.__success

    @success.setter
    def success(self, value):
        self.__success = value
    @property
    def error_context(self):
        """Gets the error_context of this AlipayCustomerCreatePortalLinkResponse.
        
        """
        return self.__error_context

    @error_context.setter
    def error_context(self, value):
        self.__error_context = value


    

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
        if hasattr(self, "success") and self.success is not None:
            params['success'] = self.success
        if hasattr(self, "error_context") and self.error_context is not None:
            params['errorContext'] = self.error_context
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
        if 'success' in response_body:
            self.__success = response_body['success']
        if 'errorContext' in response_body:
            self.__error_context = ErrorStack()
            self.__error_context.parse_rsp_body(response_body['errorContext'])
