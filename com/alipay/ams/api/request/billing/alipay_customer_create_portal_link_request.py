import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCustomerCreatePortalLinkRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCustomerCreatePortalLinkRequest, self).__init__("/ams/api/v1/billing/customer/createPortalLink") 

        self.__customer_id = None  # type: str
        self.__email = None  # type: str
        self.__expiry_days = None  # type: int
        self.__features = None  # type: [str]
        self.__auto_send = None  # type: bool
        self.__setting_id = None  # type: str
        

    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def email(self):
        """
        The email address. Maximum length: 254 characters. Note: See documentation for details.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def expiry_days(self):
        """
        The token validity period in days.
        """
        return self.__expiry_days

    @expiry_days.setter
    def expiry_days(self, value):
        self.__expiry_days = value
    @property
    def features(self):
        """
        The feature list. Note: See documentation for details.
        """
        return self.__features

    @features.setter
    def features(self, value):
        self.__features = value
    @property
    def auto_send(self):
        """
        Indicates whether to automatically send the notification.
        """
        return self.__auto_send

    @auto_send.setter
    def auto_send(self, value):
        self.__auto_send = value
    @property
    def setting_id(self):
        """
        The setting configuration ID. Maximum length: 64 characters.
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
        if hasattr(self, "expiry_days") and self.expiry_days is not None:
            params['expiryDays'] = self.expiry_days
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
        if 'expiryDays' in response_body:
            self.__expiry_days = response_body['expiryDays']
        if 'features' in response_body:
            self.__features = response_body['features']
        if 'autoSend' in response_body:
            self.__auto_send = response_body['autoSend']
        if 'settingId' in response_body:
            self.__setting_id = response_body['settingId']
