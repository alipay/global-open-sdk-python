import json




class ApplyCardPaymentPreference:
    def __init__(self):
        
        self.__currency_order = None  # type: [str]
        

    @property
    def currency_order(self):
        """
        The complete funding-currency order, preserved exactly as stored or submitted. Currency codes are uppercase three-letter strings; supported values are USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY, and NZD. A custom order contains one to nine unique, non-null codes. Do not sort, truncate, change case, filter, or partially accept the order. Required when customizing the policy; it may be omitted when inheriting the account policy. An explicit null or empty array is invalid. Customization and each currency must be enabled for the merchant. Funding follows this order, skips insufficient balances, and fails when the order is exhausted without falling back to the account order or automatically prioritizing the transaction currency. requestId remains the idempotency key: reusing it with a different body or currency order returns REPEAT_REQ_INCONSISTENT and preserves the first accepted policy. No new status or message values are defined.
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
