import json




class AgenticAmount:
    def __init__(self):
        
        self.__currency = None  # type: str
        self.__value = None  # type: str
        

    @property
    def currency(self):
        """
        ISO 4217 three-letter currency code. Required when the amount object is present.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def value(self):
        """
        A positive integer amount in the smallest currency unit, encoded as a quoted decimal-digit string in JSON. Maximum length: 16 characters. Zero, fractions, negative signs, exponents and separators are not allowed.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'value' in response_body:
            self.__value = response_body['value']
