import json




class PromotionCodeInquireDetailsMinAmount:
    def __init__(self):
        
        self.__value = None  # type: str
        self.__currency = None  # type: str
        

    @property
    def value(self):
        """
        The value of the amount as a positive integer in the smallest currency unit. Maximum length: 16 characters.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    @property
    def currency(self):
        """
        The 3-letter currency code that follows the ISO 4217 standard.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'value' in response_body:
            self.__value = response_body['value']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
