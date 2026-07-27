import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInvoiceExportResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__status = None  # type: str
        self.__download_url = None  # type: str
        self.__expires_at = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInvoiceExportResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def download_url(self):
        """
        The download url. Maximum length: 2048 characters. Note: See documentation for details.
        """
        return self.__download_url

    @download_url.setter
    def download_url(self, value):
        self.__download_url = value
    @property
    def expires_at(self):
        """
        The expiration time. Maximum length: 24 characters.
        """
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "download_url") and self.download_url is not None:
            params['downloadUrl'] = self.download_url
        if hasattr(self, "expires_at") and self.expires_at is not None:
            params['expiresAt'] = self.expires_at
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInvoiceExportResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'downloadUrl' in response_body:
            self.__download_url = response_body['downloadUrl']
        if 'expiresAt' in response_body:
            self.__expires_at = response_body['expiresAt']
