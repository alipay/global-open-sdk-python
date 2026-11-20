import json




class ApplyCardPaymentPreference:
    def __init__(self):
        
        self.__currency_order = None  # type: [str]
        

    @property
    def currency_order(self):
        """
        An ordered list of 1–9 unique non-null uppercase currency codes from USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY, or NZD, requiring merchant enablement for customization and each currency. Preserve submitted values and order exactly, with an absent array inheriting the account policy and an explicit null or empty array rejected.
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
