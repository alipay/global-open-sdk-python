import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayReceiptExportResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__file_format = None  # type: str
        self.__expires_at = None  # type: str
        self.__file_url = None  # type: str
        self.__file_size = None  # type: int
        self.__file_name = None  # type: str
        self.__mode = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayReceiptExportResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def file_format(self):
        """
        MIME type of the generated file. The response returns the MIME type corresponding to the requested format: &#x60;csv&#x60; -&gt; &#x60;text/csv&#x60;, &#x60;xlsx&#x60; -&gt; &#x60;application/vnd.openxmlformats-officedocument.spreadsheetml.sheet&#x60;. Note: the response &#x60;fileFormat&#x60; returns the MIME type, not the request format code. The request accepts &#x60;csv&#x60;/&#x60;xlsx&#x60;. Maximum length: 128 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__file_format

    @file_format.setter
    def file_format(self, value):
        self.__file_format = value
    @property
    def expires_at(self):
        """
        Expiry timestamp of the signed &#x60;fileUrl&#x60; in ISO 8601 format. Maximum length: 29 characters. After this time, accessing the URL returns HTTP 403. Returned only when result.resultCode is SUCCESS.
        """
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value
    @property
    def file_url(self):
        """
        Signed OSS URL for file download. URL is time-limited; see &#x60;expiresAt&#x60;. After expiry, accessing the URL returns HTTP 403. Maximum length: 2048 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__file_url

    @file_url.setter
    def file_url(self, value):
        self.__file_url = value
    @property
    def file_size(self):
        """
        File size in bytes. Returned only when result.resultCode is SUCCESS.
        """
        return self.__file_size

    @file_size.setter
    def file_size(self, value):
        self.__file_size = value
    @property
    def file_name(self):
        """
        Generated file name (e.g., &#x60;receipts_20260401_20260430_1685000000.csv&#x60;). Maximum length: 256 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value
    @property
    def mode(self):
        """
        Execution mode of the export request. The returned value is &#x60;SYNC&#x60;, indicating synchronous export. Maximum length: 8 characters. Returned only when result.resultCode is SUCCESS.
        """
        return self.__mode

    @mode.setter
    def mode(self, value):
        self.__mode = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "file_format") and self.file_format is not None:
            params['fileFormat'] = self.file_format
        if hasattr(self, "expires_at") and self.expires_at is not None:
            params['expiresAt'] = self.expires_at
        if hasattr(self, "file_url") and self.file_url is not None:
            params['fileUrl'] = self.file_url
        if hasattr(self, "file_size") and self.file_size is not None:
            params['fileSize'] = self.file_size
        if hasattr(self, "file_name") and self.file_name is not None:
            params['fileName'] = self.file_name
        if hasattr(self, "mode") and self.mode is not None:
            params['mode'] = self.mode
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayReceiptExportResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'fileFormat' in response_body:
            self.__file_format = response_body['fileFormat']
        if 'expiresAt' in response_body:
            self.__expires_at = response_body['expiresAt']
        if 'fileUrl' in response_body:
            self.__file_url = response_body['fileUrl']
        if 'fileSize' in response_body:
            self.__file_size = response_body['fileSize']
        if 'fileName' in response_body:
            self.__file_name = response_body['fileName']
        if 'mode' in response_body:
            self.__mode = response_body['mode']
