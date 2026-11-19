import json




class InquireCardDetailPaymentPreference:
    def __init__(self):
        
        self.__currency_order = None  # type: [str]
        

    @property
    def currency_order(self):
        """
        The complete funding-currency order, preserved exactly as stored or submitted. Currency codes are uppercase three-letter strings; supported values are USD, EUR, GBP, HKD, AUD, CAD, CNH, JPY, and NZD. A custom order contains one to nine unique, non-null codes. Do not sort, truncate, change case, filter, or partially accept the order. Returned only for a custom policy; this member may be omitted from the preference object. Historical cards are not rechecked against current creation eligibility, and existing policies are not migrated. Missing, null, or entirely blank provider values follow this operation&#39;s no-policy behavior. If a nonempty provider value that must be displayed contains an invalid code, an empty token, duplicates, or too many entries, the entire inquiry fails with only the existing result (resultCode PARAM_ILLEGAL and resultStatus F); no card data, partial policy, or sensitive credentials are returned. Existing permitted omission boundaries do not introduce new read-validation requirements. A provider failure must not be treated as an absent policy.
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
