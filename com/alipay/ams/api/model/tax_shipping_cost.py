import json




class TaxShippingCost:
    def __init__(self):
        
        self.__amount = None  # type: str
        

    @property
    def amount(self):
        """
        The amount. Maximum length: 19 characters. Note: See documentation for details.
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "amount") and self.amount is not None:
            params['amount'] = self.amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'amount' in response_body:
            self.__amount = response_body['amount']
