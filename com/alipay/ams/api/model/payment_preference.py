import json




class PaymentPreference:
    def __init__(self):
        
        self.__currency_order = None  # type: [str]
        

    @property
    def currency_order(self):
        """
        Complete funding order of 1–9 unique, non-null uppercase three-letter currency codes; supported values are USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY, and NZD. Preserve the supplied order without normalization; omit this field for inheritance, and supply a non-null, non-empty list for a custom order.
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
