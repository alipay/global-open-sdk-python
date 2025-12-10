import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.payment_method_detail import PaymentMethodDetail



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayVaultingQueryResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__vaulting_request_id = None  # type: str
        self.__normal_url = None  # type: str
        self.__scheme_url = None  # type: str
        self.__applink_url = None  # type: str
        self.__vaulting_status = None  # type: str
        self.__payment_method_detail = None  # type: PaymentMethodDetail
        self.__metadata = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayVaultingQueryResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def vaulting_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a card vaulting request.    More information:  Maximum length: 64 characters
        """
        return self.__vaulting_request_id

    @vaulting_request_id.setter
    def vaulting_request_id(self, value):
        self.__vaulting_request_id = value
    @property
    def normal_url(self):
        """
        The URL that redirects users to a WAP or WEB page in the default browser or the embedded WebView.  Note:  When the value of result.resultStatus is S and the value of vaultingStatus is PROCESSING, one or more of the following URLs may be returned: schemeUrl, applinkUrl, and normalUrl.   When the value of paymentMethodType is CARD, the user is required to complete the 3DS authentication on the page accessed through this URL.   More information:  Maximum length: 2048 characters
        """
        return self.__normal_url

    @normal_url.setter
    def normal_url(self, value):
        self.__normal_url = value
    @property
    def scheme_url(self):
        """
        The URL scheme that redirects users to open an App in an Android or iOS system when the target App is installed.  Note: When the value of result.resultStatus is S and the value of vaultingStatus is PROCESSING, one or more of the following URLs may be returned: schemeUrl, applinkUrl, and normalUrl.    More information:  Maximum length: 2048 characters
        """
        return self.__scheme_url

    @scheme_url.setter
    def scheme_url(self, value):
        self.__scheme_url = value
    @property
    def applink_url(self):
        """
        The URL that redirects users to open an app when the target app is installed, or to open a WAP page when the target app is not installed. For Android, the URL is a Native App Link. For iOS, the URL is a Universal Link.  Note: When the value of result.resultStatus is S and the value of vaultingStatus is PROCESSING, one or more of the following URLs may be returned: schemeUrl, applinkUrl, and normalUrl.  More information:  Maximum length: 2048 characters 
        """
        return self.__applink_url

    @applink_url.setter
    def applink_url(self, value):
        self.__applink_url = value
    @property
    def vaulting_status(self):
        """
        Indicates the payment method&#39;s vaulting status. Valid values are:  SUCCESS: indicates that the vaulting is successful.  FAIL: indicates that the vaulting failed. PROCESSING: indicates that the vaulting is under process.  This parameter is returned when the value of result.resultStatus is S.    More information:  Maximum length: 10 characters
        """
        return self.__vaulting_status

    @vaulting_status.setter
    def vaulting_status(self, value):
        self.__vaulting_status = value
    @property
    def payment_method_detail(self):
        """Gets the payment_method_detail of this AlipayVaultingQueryResponse.
        
        """
        return self.__payment_method_detail

    @payment_method_detail.setter
    def payment_method_detail(self, value):
        self.__payment_method_detail = value
    @property
    def metadata(self):
        """
        Metadata for custom data transmission
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "vaulting_request_id") and self.vaulting_request_id is not None:
            params['vaultingRequestId'] = self.vaulting_request_id
        if hasattr(self, "normal_url") and self.normal_url is not None:
            params['normalUrl'] = self.normal_url
        if hasattr(self, "scheme_url") and self.scheme_url is not None:
            params['schemeUrl'] = self.scheme_url
        if hasattr(self, "applink_url") and self.applink_url is not None:
            params['applinkUrl'] = self.applink_url
        if hasattr(self, "vaulting_status") and self.vaulting_status is not None:
            params['vaultingStatus'] = self.vaulting_status
        if hasattr(self, "payment_method_detail") and self.payment_method_detail is not None:
            params['paymentMethodDetail'] = self.payment_method_detail
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayVaultingQueryResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'vaultingRequestId' in response_body:
            self.__vaulting_request_id = response_body['vaultingRequestId']
        if 'normalUrl' in response_body:
            self.__normal_url = response_body['normalUrl']
        if 'schemeUrl' in response_body:
            self.__scheme_url = response_body['schemeUrl']
        if 'applinkUrl' in response_body:
            self.__applink_url = response_body['applinkUrl']
        if 'vaultingStatus' in response_body:
            self.__vaulting_status = response_body['vaultingStatus']
        if 'paymentMethodDetail' in response_body:
            self.__payment_method_detail = PaymentMethodDetail()
            self.__payment_method_detail.parse_rsp_body(response_body['paymentMethodDetail'])
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
