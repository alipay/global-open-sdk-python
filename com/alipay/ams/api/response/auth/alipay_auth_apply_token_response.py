import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.psp_customer_info import PspCustomerInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayAuthApplyTokenResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__access_token = None  # type: str
        self.__access_token_expiry_time = None  # type: str
        self.__refresh_token = None  # type: str
        self.__refresh_token_expiry_time = None  # type: str
        self.__extend_info = None  # type: str
        self.__user_login_id = None  # type: str
        self.__psp_customer_info = None  # type: PspCustomerInfo
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayAuthApplyTokenResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def access_token(self):
        """
        The access token that is used to access the corresponding scope of the user resource.   Note: This field is returned when the API is called successfully.  More information:  Maximum length: 128 characters 
        """
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value
    @property
    def access_token_expiry_time(self):
        """
        The time after which the access token expires. After the access token expires, the access token cannot be used to deduct money from the user&#39;s account.   Note: This field is returned when accessToken is returned.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;. 
        """
        return self.__access_token_expiry_time

    @access_token_expiry_time.setter
    def access_token_expiry_time(self, value):
        self.__access_token_expiry_time = value
    @property
    def refresh_token(self):
        """
        The refresh token that is used to exchange for a new access token when the access token is about to expire.   Note: This field is returned when the wallet supports refreshing the token. If this field is not returned, it indicates that the access token has a quite long valid period.  More information:  Maximum length: 128 characters
        """
        return self.__refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self.__refresh_token = value
    @property
    def refresh_token_expiry_time(self):
        """
        The time after which the refresh token expires. After the refresh token expires, the refresh token cannot be used to retrieve a new access token.   Note: This field is returned when refreshToken is returned.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__refresh_token_expiry_time

    @refresh_token_expiry_time.setter
    def refresh_token_expiry_time(self, value):
        self.__refresh_token_expiry_time = value
    @property
    def extend_info(self):
        """
        Extended information.  Note: This field is returned when extended information exists.  More information:  Maximum length: 2048 characters
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def user_login_id(self):
        """
        The login ID that the user used to register in the wallet. The login ID can be the user&#39;s email address or phone number, which is masked when returned to Alipay+ payment methods . This field can inform the merchant of the users who are registered.  Note: This field is returned when result.resultCode is SUCCESS and the value of the scopes field in the consult API is AGREEMENT_PAY.  More information:  Maximum length: 64 characters
        """
        return self.__user_login_id

    @user_login_id.setter
    def user_login_id(self, value):
        self.__user_login_id = value
    @property
    def psp_customer_info(self):
        """Gets the psp_customer_info of this AlipayAuthApplyTokenResponse.
        
        """
        return self.__psp_customer_info

    @psp_customer_info.setter
    def psp_customer_info(self, value):
        self.__psp_customer_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "access_token") and self.access_token is not None:
            params['accessToken'] = self.access_token
        if hasattr(self, "access_token_expiry_time") and self.access_token_expiry_time is not None:
            params['accessTokenExpiryTime'] = self.access_token_expiry_time
        if hasattr(self, "refresh_token") and self.refresh_token is not None:
            params['refreshToken'] = self.refresh_token
        if hasattr(self, "refresh_token_expiry_time") and self.refresh_token_expiry_time is not None:
            params['refreshTokenExpiryTime'] = self.refresh_token_expiry_time
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "user_login_id") and self.user_login_id is not None:
            params['userLoginId'] = self.user_login_id
        if hasattr(self, "psp_customer_info") and self.psp_customer_info is not None:
            params['pspCustomerInfo'] = self.psp_customer_info
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayAuthApplyTokenResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'accessToken' in response_body:
            self.__access_token = response_body['accessToken']
        if 'accessTokenExpiryTime' in response_body:
            self.__access_token_expiry_time = response_body['accessTokenExpiryTime']
        if 'refreshToken' in response_body:
            self.__refresh_token = response_body['refreshToken']
        if 'refreshTokenExpiryTime' in response_body:
            self.__refresh_token_expiry_time = response_body['refreshTokenExpiryTime']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'userLoginId' in response_body:
            self.__user_login_id = response_body['userLoginId']
        if 'pspCustomerInfo' in response_body:
            self.__psp_customer_info = PspCustomerInfo()
            self.__psp_customer_info.parse_rsp_body(response_body['pspCustomerInfo'])
