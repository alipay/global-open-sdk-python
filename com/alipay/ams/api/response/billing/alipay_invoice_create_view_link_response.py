import json
from com.alipay.ams.api.model.invoice_create_view_link_result import InvoiceCreateViewLinkResult



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceCreateViewLinkResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: InvoiceCreateViewLinkResult
        self.__token = None  # type: str
        self.__view_url = None  # type: str
        self.__expires_at = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceCreateViewLinkResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def token(self):
        """
        The encrypted token. Maximum length: 1024 characters. Note: See documentation for details.
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value
    @property
    def view_url(self):
        """
        The view url. Maximum length: 2048 characters. Note: See documentation for details.
        """
        return self.__view_url

    @view_url.setter
    def view_url(self, value):
        self.__view_url = value
    @property
    def expires_at(self):
        """
        The expiration time. Maximum length: 24 characters. Note: See documentation for details.
        """
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "token") and self.token is not None:
            params['token'] = self.token
        if hasattr(self, "view_url") and self.view_url is not None:
            params['viewUrl'] = self.view_url
        if hasattr(self, "expires_at") and self.expires_at is not None:
            params['expiresAt'] = self.expires_at
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceCreateViewLinkResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = InvoiceCreateViewLinkResult()
            self.__result.parse_rsp_body(response_body['result'])
        if 'token' in response_body:
            self.__token = response_body['token']
        if 'viewUrl' in response_body:
            self.__view_url = response_body['viewUrl']
        if 'expiresAt' in response_body:
            self.__expires_at = response_body['expiresAt']
