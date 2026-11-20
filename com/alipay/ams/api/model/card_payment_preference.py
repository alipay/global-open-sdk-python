import json




class CardPaymentPreference:
    def __init__(self):
        
        self.__currency_order = None  # type: [str]
        

    @property
    def currency_order(self):
        """
        Complete ordered list of 1–9 unique, non-null uppercase three-letter funding currencies: USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY and NZD; these differ from allowedCurrencies transaction currencies. For customization, supply the complete list without normalization, filtering, truncation, reordering or partial acceptance; null and empty arrays are invalid, exhaustion fails without account-policy fallback, and transaction currency has no automatic priority.
        """
        return self.__currency_order

    @currency_order.setter
    def currency_order(self, value):
        self.__currency_order = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "currency_order") and self.currency_order is not None:
            params['currencyOrder'] = self.currency_order
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currencyOrder' in response_body:
            self.__currency_order = response_body['currencyOrder']
