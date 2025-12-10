import json




class SettlementStrategy:
    def __init__(self):
        
        self.__settlement_currency = None  # type: str
        

    @property
    def settlement_currency(self):
        """
        The ISO currency code of the currency that the merchant wants to be settled against. The field is required if the merchant signed up for multiple currencies to settle.   More information:  Maximum length: 3 characters
        """
        return self.__settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self.__settlement_currency = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "settlement_currency") and self.settlement_currency is not None:
            params['settlementCurrency'] = self.settlement_currency
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'settlementCurrency' in response_body:
            self.__settlement_currency = response_body['settlementCurrency']
