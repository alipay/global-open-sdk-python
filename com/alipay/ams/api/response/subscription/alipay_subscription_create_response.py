import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipaySubscriptionCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__scheme_url = None  # type: str
        self.__applink_url = None  # type: str
        self.__normal_url = None  # type: str
        self.__app_identifier = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipaySubscriptionCreateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def scheme_url(self):
        """
        The URL scheme that redirects users to open an app in an Android or iOS system when the target app is installed.  Note: When the value of result.resultCode is S, at least one of schemeUrl, applinkUrl, and normalUrl is to be returned.  More information:  Maximum length: 2048 characters
        """
        return self.__scheme_url

    @scheme_url.setter
    def scheme_url(self, value):
        self.__scheme_url = value
    @property
    def applink_url(self):
        """
        The URL that redirects users to open an app when the target app is installed, or to open a WAP page when the target app is not installed. For Android, the URL is a Native App Link. For iOS, the URL is a Universal Link.  Note: When the value of result.resultCode is S, at least one of schemeUrl, applinkUrl, and normalUrl is to be returned.  More information:  Maximum length: 2048 characters
        """
        return self.__applink_url

    @applink_url.setter
    def applink_url(self, value):
        self.__applink_url = value
    @property
    def normal_url(self):
        """
        The URL that redirects users to a WAP or Web page in the default browser or the embedded WebView.  Note: When the value of result.resultCode is S, at least one of schemeUrl, applinkUrl, and normalUrl is to be returned.  More information:  Maximum length: 2048 characters
        """
        return self.__normal_url

    @normal_url.setter
    def normal_url(self, value):
        self.__normal_url = value
    @property
    def app_identifier(self):
        """
        An Android package name, which is used for Android app to open a cashier page.  Note: This field is returned when result.resultCode is S and terminalType is APP or WAP.  More information:  Maximum length: 128 characters
        """
        return self.__app_identifier

    @app_identifier.setter
    def app_identifier(self, value):
        self.__app_identifier = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "scheme_url") and self.scheme_url is not None:
            params['schemeUrl'] = self.scheme_url
        if hasattr(self, "applink_url") and self.applink_url is not None:
            params['applinkUrl'] = self.applink_url
        if hasattr(self, "normal_url") and self.normal_url is not None:
            params['normalUrl'] = self.normal_url
        if hasattr(self, "app_identifier") and self.app_identifier is not None:
            params['appIdentifier'] = self.app_identifier
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipaySubscriptionCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'schemeUrl' in response_body:
            self.__scheme_url = response_body['schemeUrl']
        if 'applinkUrl' in response_body:
            self.__applink_url = response_body['applinkUrl']
        if 'normalUrl' in response_body:
            self.__normal_url = response_body['normalUrl']
        if 'appIdentifier' in response_body:
            self.__app_identifier = response_body['appIdentifier']
