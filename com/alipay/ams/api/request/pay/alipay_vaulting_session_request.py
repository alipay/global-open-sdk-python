import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayVaultingSessionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayVaultingSessionRequest, self).__init__("/ams/api/v1/vaults/createVaultingSession") 

        self.__payment_method_type = None  # type: str
        self.__vaulting_request_id = None  # type: str
        self.__vaulting_notification_url = None  # type: str
        self.__redirect_url = None  # type: str
        self.__merchant_region = None  # type: str
        self.__is3_ds_authentication = None  # type: bool
        

    @property
    def payment_method_type(self):
        """
        The payment method type is included in payment method options. See Payment methods to check the valid values for card payments.    More information:  Maximum length: 64 characters
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value):
        self.__payment_method_type = value
    @property
    def vaulting_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a card vaulting request.   More information:  Maximum length: 64 characters 
        """
        return self.__vaulting_request_id

    @vaulting_request_id.setter
    def vaulting_request_id(self, value):
        self.__vaulting_request_id = value
    @property
    def vaulting_notification_url(self):
        """
        The URL that is used to receive the vaulting result notification.   More information:  Maximum length: 2048 characters
        """
        return self.__vaulting_notification_url

    @vaulting_notification_url.setter
    def vaulting_notification_url(self, value):
        self.__vaulting_notification_url = value
    @property
    def redirect_url(self):
        """
        The merchant page URL that the buyer is redirected to after the vaulting is completed.   Note: Specify this parameter if you want to redirect the buyer to your page directly after the vaulting is completed.  More information:  Maximum length: 2048 characters 
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value
    @property
    def merchant_region(self):
        """
        The country or region where the merchant operates the business. The value of this parameter is a 2-letter country or region code based on the ISO 3166 Country Codes standard.  Some possible values are US, SG, HK, PK, JP, CN, BR, AU, and MY.  Note: Specify this parameter when you use the Global Acquirer Gateway (GAGW) product.  More information:  Maximum length: 2 characters
        """
        return self.__merchant_region

    @merchant_region.setter
    def merchant_region(self, value):
        self.__merchant_region = value
    @property
    def is3_ds_authentication(self):
        """
        Indicates whether the transaction authentication type is 3D secure. Specify this parameter when the value of paymentMethodType is CARD.
        """
        return self.__is3_ds_authentication

    @is3_ds_authentication.setter
    def is3_ds_authentication(self, value):
        self.__is3_ds_authentication = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_type") and self.payment_method_type is not None:
            params['paymentMethodType'] = self.payment_method_type
        if hasattr(self, "vaulting_request_id") and self.vaulting_request_id is not None:
            params['vaultingRequestId'] = self.vaulting_request_id
        if hasattr(self, "vaulting_notification_url") and self.vaulting_notification_url is not None:
            params['vaultingNotificationUrl'] = self.vaulting_notification_url
        if hasattr(self, "redirect_url") and self.redirect_url is not None:
            params['redirectUrl'] = self.redirect_url
        if hasattr(self, "merchant_region") and self.merchant_region is not None:
            params['merchantRegion'] = self.merchant_region
        if hasattr(self, "is3_ds_authentication") and self.is3_ds_authentication is not None:
            params['is3DSAuthentication'] = self.is3_ds_authentication
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodType' in response_body:
            self.__payment_method_type = response_body['paymentMethodType']
        if 'vaultingRequestId' in response_body:
            self.__vaulting_request_id = response_body['vaultingRequestId']
        if 'vaultingNotificationUrl' in response_body:
            self.__vaulting_notification_url = response_body['vaultingNotificationUrl']
        if 'redirectUrl' in response_body:
            self.__redirect_url = response_body['redirectUrl']
        if 'merchantRegion' in response_body:
            self.__merchant_region = response_body['merchantRegion']
        if 'is3DSAuthentication' in response_body:
            self.__is3_ds_authentication = response_body['is3DSAuthentication']
