import json




class ApplyCardPaymentPreference:
    def __init__(self):
        
        self.__currency_order = None  # type: [str]
        

    @property
    def currency_order(self):
        """
        Ordered funding currencies: 1-9 unique, non-null, three-letter uppercase strings matching [A-Z]{3}, from USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY, and NZD. Preserve the supplied order; do not normalize, filter, truncate, or return partial data. Null or empty arrays are invalid. Customization and each currency must be enabled for the merchant. Keep the first accepted request body and currency order for requestId; a different body or order under the same requestId is rejected with REPEAT_REQ_INCONSISTENT. currencyOrder is required for customization and absent when inheriting the account policy.
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
