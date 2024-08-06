class SupportBank(object):
    def __init__(self):
        self.__bank_identifier_code = None
        self.__bank_short_name = None
        self.__bank_logo = None

    @property
    def bank_identifier_code(self):
        return self.__bank_identifier_code

    @bank_identifier_code.setter
    def bank_identifier_code(self, value):
        self.__bank_identifier_code = value

    @property
    def bank_short_name(self):
        return self.__bank_short_name

    @bank_short_name.setter
    def bank_short_name(self, value):
        self.__bank_short_name = value

    @property
    def bank_logo(self):
        return self.__bank_logo

    @bank_logo.setter
    def bank_logo(self, value):
        self.__bank_logo = value

    def to_ams_dict(self):
        params = dict()
        if self.__bank_identifier_code is not None:
            params['bankIdentifierCode'] = self.__bank_identifier_code
        if self.__bank_short_name is not None:
            params['bankShortName'] = self.__bank_short_name
        if self.__bank_logo is not None:
            params['bankLogo'] = self.__bank_logo
        return params

    def parse_rsp_body(self, support_bank_body):
        if support_bank_body is None:
            return
        if 'bankIdentifierCode' in support_bank_body:
            self.bank_identifier_code = support_bank_body['bankIdentifierCode']
        if 'bankShortName' in support_bank_body:
            self.bank_short_name = support_bank_body['bankShortName']
        if 'bankLogo' in support_bank_body:
            self.bank_logo = support_bank_body['bankLogo']
