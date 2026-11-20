import json




class Amount:
    def __init__(self, currency=None, value=None):
        
        self.__currency = currency  # type: str
        self.__value = value  # type: str
        

    @property
    def currency(self):
        """
        The transaction currency that is specified in the contract. A 3-letter currency code that follows the ISO 4217 standard.  More information:  Maximum length: 3 characters
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def value(self):
        """
        The amount to charge as a positive integer in the smallest currency unit. (That is, 100 cents to charge $1.00, or 100 to charge JPY 100, a 0-decimal currency).  Note: For details about the smallest currency unit, see Smallest unit of the currency.   More information:  Value range: 1 - unlimited
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
