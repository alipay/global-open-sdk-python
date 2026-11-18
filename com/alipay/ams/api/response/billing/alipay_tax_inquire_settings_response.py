import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.tax_head_office import TaxHeadOffice



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayTaxInquireSettingsResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__default_tax_code = None  # type: str
        self.__default_tax_behavior = None  # type: str
        self.__head_office = None  # type: TaxHeadOffice
        self.__status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayTaxInquireSettingsResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def default_tax_code(self):
        """
        The default tax code. Returned only when the API call succeeds. Maximum length: 32 characters.
        """
        return self.__default_tax_code

    @default_tax_code.setter
    def default_tax_code(self, value):
        self.__default_tax_code = value
    @property
    def default_tax_behavior(self):
        """
        The default tax behavior. Returned only when the API call succeeds. Maximum length: 16 characters.
        """
        return self.__default_tax_behavior

    @default_tax_behavior.setter
    def default_tax_behavior(self, value):
        self.__default_tax_behavior = value
    @property
    def head_office(self):
        """Gets the head_office of this AlipayTaxInquireSettingsResponse.
        
        """
        return self.__head_office

    @head_office.setter
    def head_office(self, value):
        self.__head_office = value
    @property
    def status(self):
        """
        The tax settings status. Valid values are ACTIVE and PENDING. Returned only when the API call succeeds. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "default_tax_code") and self.default_tax_code is not None:
            params['defaultTaxCode'] = self.default_tax_code
        if hasattr(self, "default_tax_behavior") and self.default_tax_behavior is not None:
            params['defaultTaxBehavior'] = self.default_tax_behavior
        if hasattr(self, "head_office") and self.head_office is not None:
            params['headOffice'] = self.head_office
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayTaxInquireSettingsResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'defaultTaxCode' in response_body:
            self.__default_tax_code = response_body['defaultTaxCode']
        if 'defaultTaxBehavior' in response_body:
            self.__default_tax_behavior = response_body['defaultTaxBehavior']
        if 'headOffice' in response_body:
            self.__head_office = TaxHeadOffice()
            self.__head_office.parse_rsp_body(response_body['headOffice'])
        if 'status' in response_body:
            self.__status = response_body['status']
