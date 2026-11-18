import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCustomerCreatePortalLinkRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCustomerCreatePortalLinkRequest, self).__init__("/ams/api/v1/billing/customer/createPortalLink") 

        self.__customer_id = None  # type: str
        self.__email = None  # type: str
        self.__features = None  # type: [str]
        self.__auto_send = None  # type: bool
        self.__setting_id = None  # type: str
        

    @property
    def customer_id(self):
        """
        Customer ID to target. Either &#x60;customerId&#x60; or &#x60;email&#x60; must be provided. When both are provided, &#x60;email&#x60; must match the registered account email of this customer; otherwise, the API returns &#x60;PARAM_ILLEGAL&#x60;. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def email(self):
        """
        Customer email for lookup. Either &#x60;customerId&#x60; or &#x60;email&#x60; must be provided. When multiple customers share the email, the most recently created customer by &#x60;gmtCreate&#x60; descending is selected. When both fields are provided, this value must match the registered account email of the specified customer; otherwise, the API returns &#x60;PARAM_ILLEGAL&#x60;. Maximum length: 254 characters (RFC 5322).
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def features(self):
        """
        Feature set enabled for this portal session. Allowed values: &#x60;SUBSCRIPTION&#x60;, &#x60;INVOICE&#x60;, &#x60;PAYMENT_METHOD&#x60;. An empty or absent list enables all features by default. The portal settings referenced by &#x60;settingId&#x60; may further restrict which features are shown at render time. Maximum size: 3 elements.
        """
        return self.__features

    @features.setter
    def features(self, value):
        self.__features = value
    @property
    def auto_send(self):
        """
        When &#x60;true&#x60;, best-effort email the portal URL to the customer. Default: &#x60;false&#x60;. Failure never blocks link creation.
        """
        return self.__auto_send

    @auto_send.setter
    def auto_send(self, value):
        self.__auto_send = value
    @property
    def setting_id(self):
        """
        Portal setting configuration ID passed through the token payload. Maximum length: 64 characters.
        """
        return self.__setting_id

    @setting_id.setter
    def setting_id(self, value):
        self.__setting_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "features") and self.features is not None:
            params['features'] = self.features
        if hasattr(self, "auto_send") and self.auto_send is not None:
            params['autoSend'] = self.auto_send
        if hasattr(self, "setting_id") and self.setting_id is not None:
            params['settingId'] = self.setting_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'features' in response_body:
            self.__features = response_body['features']
        if 'autoSend' in response_body:
            self.__auto_send = response_body['autoSend']
        if 'settingId' in response_body:
            self.__setting_id = response_body['settingId']
