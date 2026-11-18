import json
from com.alipay.ams.api.model.amount import Amount




class TaxShippingCost:
    def __init__(self):
        
        self.__amount = None  # type: Amount
        

    @property
    def amount(self):
        """Gets the amount of this TaxShippingCost.
        
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
            self.__amount = Amount()
            self.__amount.parse_rsp_body(response_body['amount'])
