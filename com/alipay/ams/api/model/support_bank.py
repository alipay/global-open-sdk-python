import json
from com.alipay.ams.api.model.logo import Logo




class SupportBank:
    def __init__(self):
        
        self.__bank_identifier_code = None  # type: str
        self.__bank_short_name = None  # type: str
        self.__bank_logo = None  # type: Logo
        

    @property
    def bank_identifier_code(self):
        """
        The unique code of the bank. See the Bank list to check the valid values. 
        """
        return self.__bank_identifier_code

    @bank_identifier_code.setter
    def bank_identifier_code(self, value):
        self.__bank_identifier_code = value
    @property
    def bank_short_name(self):
        """
        The short name of the bank. The unique code of the bank. See the Bank list to check the valid values. 
        """
        return self.__bank_short_name

    @bank_short_name.setter
    def bank_short_name(self, value):
        self.__bank_short_name = value
    @property
    def bank_logo(self):
        """Gets the bank_logo of this SupportBank.
        
        """
        return self.__bank_logo

    @bank_logo.setter
    def bank_logo(self, value):
        self.__bank_logo = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "bank_identifier_code") and self.bank_identifier_code is not None:
            params['bankIdentifierCode'] = self.bank_identifier_code
        if hasattr(self, "bank_short_name") and self.bank_short_name is not None:
            params['bankShortName'] = self.bank_short_name
        if hasattr(self, "bank_logo") and self.bank_logo is not None:
            params['bankLogo'] = self.bank_logo
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'bankIdentifierCode' in response_body:
            self.__bank_identifier_code = response_body['bankIdentifierCode']
        if 'bankShortName' in response_body:
            self.__bank_short_name = response_body['bankShortName']
        if 'bankLogo' in response_body:
            self.__bank_logo = Logo()
            self.__bank_logo.parse_rsp_body(response_body['bankLogo'])
