import json




class Amount:
    def __init__(self, currency=None, value=None):
        
        self.__currency = currency  # type: str
        self.__value = value  # type: str
        

    @property
    def currency(self):
        """
        The 3-letter currency code that follows the ISO 4217 standard.   More information:  Maximum length: 3 characters
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def value(self):
        """
        The value of the amount as a positive integer in the smallest currency unit. For example, if the currency is USD and the amount is $1.00, set the value of this parameter to 100; or if the currency is JPY and the amount is ￥1, set the value of this parameter to 1.    For details about the smallest currency unit, see Smallest unit of the currency .  For details about the minimum payment amount allowed for each payment method, see Minimum amount rules.   Note: Due to the currency practices in Indonesia, when the currency is IDR, round the amount with banker&#39;s rounding and fix the last two digits of this parameter as 00.    More information:  Value range: 0 - unlimited 
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
