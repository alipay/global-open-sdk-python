import json
from com.alipay.ams.api.model.tax_head_office import TaxHeadOffice



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxInitializeSettingsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxInitializeSettingsRequest, self).__init__("/ams/api/v1/tax/initializeSettings") 

        self.__settings_request_id = None  # type: str
        self.__default_tax_code = None  # type: str
        self.__default_tax_behavior = None  # type: str
        self.__head_office = None  # type: TaxHeadOffice
        

    @property
    def settings_request_id(self):
        """
        The unique ID assigned by a merchant to identify a tax settings initialization request. Reuse it only with the original request body when recovering an unknown result. Maximum length: 64 characters.
        """
        return self.__settings_request_id

    @settings_request_id.setter
    def settings_request_id(self, value):
        self.__settings_request_id = value
    @property
    def default_tax_code(self):
        """
        The default tax code. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__default_tax_code

    @default_tax_code.setter
    def default_tax_code(self, value):
        self.__default_tax_code = value
    @property
    def default_tax_behavior(self):
        """
        The default tax behavior. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__default_tax_behavior

    @default_tax_behavior.setter
    def default_tax_behavior(self, value):
        self.__default_tax_behavior = value
    @property
    def head_office(self):
        """Gets the head_office of this AlipayTaxInitializeSettingsRequest.
        
        """
        return self.__head_office

    @head_office.setter
    def head_office(self, value):
        self.__head_office = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "settings_request_id") and self.settings_request_id is not None:
            params['settingsRequestId'] = self.settings_request_id
        if hasattr(self, "default_tax_code") and self.default_tax_code is not None:
            params['defaultTaxCode'] = self.default_tax_code
        if hasattr(self, "default_tax_behavior") and self.default_tax_behavior is not None:
            params['defaultTaxBehavior'] = self.default_tax_behavior
        if hasattr(self, "head_office") and self.head_office is not None:
            params['headOffice'] = self.head_office
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'settingsRequestId' in response_body:
            self.__settings_request_id = response_body['settingsRequestId']
        if 'defaultTaxCode' in response_body:
            self.__default_tax_code = response_body['defaultTaxCode']
        if 'defaultTaxBehavior' in response_body:
            self.__default_tax_behavior = response_body['defaultTaxBehavior']
        if 'headOffice' in response_body:
            self.__head_office = TaxHeadOffice()
            self.__head_office.parse_rsp_body(response_body['headOffice'])
