import json
from com.alipay.ams.api.model.grant_type import GrantType
from com.alipay.ams.api.model.customer_belongs_to import CustomerBelongsTo



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayAuthApplyTokenRequest(AlipayRequest):
    def __init__(self):
        super(AlipayAuthApplyTokenRequest, self).__init__("/ams/api/v1/authorizations/applyToken") 

        self.__merchant_account_id = None  # type: str
        self.__grant_type = None  # type: GrantType
        self.__customer_belongs_to = None  # type: CustomerBelongsTo
        self.__auth_code = None  # type: str
        self.__refresh_token = None  # type: str
        self.__extend_info = None  # type: str
        self.__merchant_region = None  # type: str
        

    @property
    def merchant_account_id(self):
        """
        The merchant account ID
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value
    @property
    def grant_type(self):
        """Gets the grant_type of this AlipayAuthApplyTokenRequest.
        
        """
        return self.__grant_type

    @grant_type.setter
    def grant_type(self, value):
        self.__grant_type = value
    @property
    def customer_belongs_to(self):
        """Gets the customer_belongs_to of this AlipayAuthApplyTokenRequest.
        
        """
        return self.__customer_belongs_to

    @customer_belongs_to.setter
    def customer_belongs_to(self, value):
        self.__customer_belongs_to = value
    @property
    def auth_code(self):
        """
        The authorization code, used for getting an access token. The value of this field is obtained from the reconstructed redirection URL returned by the wallet.  Note: Specify this field when the value of grantType is AUTHORIZATION_CODE.  More information:  Maximum length: 128 characters
        """
        return self.__auth_code

    @auth_code.setter
    def auth_code(self, value):
        self.__auth_code = value
    @property
    def refresh_token(self):
        """
        The refresh token, used for getting a new access token when the access token is about to expire. The refresh token is obtained from the response of the successfully called applyToken API.  Note: Specify this field when the value of grantType is REFRESH_TOKEN.  More information:  Maximum length: 128 characters
        """
        return self.__refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self.__refresh_token = value
    @property
    def extend_info(self):
        """Gets the extend_info of this AlipayAuthApplyTokenRequest.
        
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def merchant_region(self):
        """
        The country or region where the merchant or secondary merchant operates the business. The parameter is a 2-letter country/region code that follows ISO 3166 Country Codes standard. Only US, JP, PK, SG are supported now.  Note: This field is required when you use the Global Acquirer Gateway (GAGW) product.  More information:  Maximum length: 2 characters
        """
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        if hasattr(self, "grant_type") and self.grant_type is not None:
            params['grantType'] = self.grant_type
        if hasattr(self, "customer_belongs_to") and self.customer_belongs_to is not None:
            params['customerBelongsTo'] = self.customer_belongs_to
        if hasattr(self, "auth_code") and self.auth_code is not None:
            params['authCode'] = self.auth_code
        if hasattr(self, "refresh_token") and self.refresh_token is not None:
            params['refreshToken'] = self.refresh_token
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "merchant_region") and self.merchant_region is not None:
            params['merchantRegion'] = self.merchant_region
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
        if 'grantType' in response_body:
            grant_type_temp = GrantType.value_of(response_body['grantType'])
            self.__grant_type = grant_type_temp
        if 'customerBelongsTo' in response_body:
            customer_belongs_to_temp = CustomerBelongsTo.value_of(response_body['customerBelongsTo'])
            self.__customer_belongs_to = customer_belongs_to_temp
        if 'authCode' in response_body:
            self.__auth_code = response_body['authCode']
        if 'refreshToken' in response_body:
            self.__refresh_token = response_body['refreshToken']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'merchantRegion' in response_body:
            self.__merchant_region = response_body['merchantRegion']
