import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceCreateViewLinkResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
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
        Encrypted token embedding &#x60;invoiceId&#x60;, &#x60;merchantId&#x60;, and &#x60;expiryTimestamp&#x60; in the pipe-delimited format &#x60;invoiceId|merchantId|expiryTimestamp&#x60; (e.g., &#x60;inv_20260413_000123|MID_001|1713590400000&#x60;). Encrypted via AES-CBC through iBCM. Returned only when result.resultCode is SUCCESS. Maximum length: 1024 characters.
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value
    @property
    def view_url(self):
        """
        Full shareable URL for the invoice view page. Format: &#x60;{baseUrl}?token&#x3D;{encodedToken}&#x60;. Returned when &#x60;resultStatus&#x60; is &#x60;S&#x60; and &#x60;resultCode&#x60; is &#x60;SUCCESS&#x60;, and DRM &#x60;baseUrl&#x60; is configured. When DRM &#x60;baseUrl&#x60; is not configured, this field is absent; the &#x60;token&#x60; is still returned and merchants can construct the URL client-side. Maximum length: 2048 characters.
        """
        return self.__view_url

    @view_url.setter
    def view_url(self, value):
        self.__view_url = value
    @property
    def expires_at(self):
        """
        ISO 8601 absolute timestamp indicating when the token and view link expire. Calculated as &#x60;requestProcessingTime + (linkExpiryDays x 86400 seconds)&#x60;, then rounded up to the start of the following UTC day. When &#x60;linkExpiryDays&#x60; is not provided, the default of 7 days is used. Returned only when result.resultCode is SUCCESS. Maximum length: 29 characters.
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
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'token' in response_body:
            self.__token = response_body['token']
        if 'viewUrl' in response_body:
            self.__view_url = response_body['viewUrl']
        if 'expiresAt' in response_body:
            self.__expires_at = response_body['expiresAt']
