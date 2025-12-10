import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPaymentSessionResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payment_session_data = None  # type: str
        self.__payment_session_expiry_time = None  # type: str
        self.__payment_session_id = None  # type: str
        self.__normal_url = None  # type: str
        self.__url = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPaymentSessionResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payment_session_data(self):
        """
        The encrypted payment session data. Pass the data to your front end to initiate the client-side SDK.    More information:  Maximum length: 4096 characters
        """
        return self.__payment_session_data

    @payment_session_data.setter
    def payment_session_data(self, value):
        self.__payment_session_data = value
    @property
    def payment_session_expiry_time(self):
        """
        The specific date and time after which the payment session will expire.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__payment_session_expiry_time

    @payment_session_expiry_time.setter
    def payment_session_expiry_time(self, value):
        self.__payment_session_expiry_time = value
    @property
    def payment_session_id(self):
        """
        The encrypted ID that is assigned by Antom to identify a payment session.    More information:  Maximum length: 64 characters
        """
        return self.__payment_session_id

    @payment_session_id.setter
    def payment_session_id(self, value):
        self.__payment_session_id = value
    @property
    def normal_url(self):
        """
        The URL used to redirect to the Checkout Page.  More information:  Maximum length: 2048 characters
        """
        return self.__normal_url

    @normal_url.setter
    def normal_url(self, value):
        self.__normal_url = value
    @property
    def url(self):
        """
        The URL for payment session
        """
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payment_session_data") and self.payment_session_data is not None:
            params['paymentSessionData'] = self.payment_session_data
        if hasattr(self, "payment_session_expiry_time") and self.payment_session_expiry_time is not None:
            params['paymentSessionExpiryTime'] = self.payment_session_expiry_time
        if hasattr(self, "payment_session_id") and self.payment_session_id is not None:
            params['paymentSessionId'] = self.payment_session_id
        if hasattr(self, "normal_url") and self.normal_url is not None:
            params['normalUrl'] = self.normal_url
        if hasattr(self, "url") and self.url is not None:
            params['url'] = self.url
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPaymentSessionResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'paymentSessionData' in response_body:
            self.__payment_session_data = response_body['paymentSessionData']
        if 'paymentSessionExpiryTime' in response_body:
            self.__payment_session_expiry_time = response_body['paymentSessionExpiryTime']
        if 'paymentSessionId' in response_body:
            self.__payment_session_id = response_body['paymentSessionId']
        if 'normalUrl' in response_body:
            self.__normal_url = response_body['normalUrl']
        if 'url' in response_body:
            self.__url = response_body['url']
