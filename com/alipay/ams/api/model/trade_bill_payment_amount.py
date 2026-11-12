import json




class TradeBillPaymentAmount:
    def __init__(self):
        
        self.__currency = None  # type: str
        self.__value = None  # type: str
        

    @property
    def currency(self):
        """
        The merchant-supplied currency code following ISO 4217. Required when paymentAmount is present and nonempty.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def value(self):
        """
        The merchant-supplied amount in the smallest currency unit, transmitted as a string. Required when paymentAmount is present and nonempty.
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
