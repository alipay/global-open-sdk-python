import json
from com.alipay.ams.api.model.tax_breakdown import TaxBreakdown




class TaxCalculatedShippingCost:
    def __init__(self):
        
        self.__amount = None  # type: str
        self.__tax_amount = None  # type: str
        self.__tax_breakdown = None  # type: [TaxBreakdown]
        

    @property
    def amount(self):
        """
        The amount. Maximum length: 19 characters.
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value
    @property
    def tax_amount(self):
        """
        The tax amount. Maximum length: 19 characters.
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value
    @property
    def tax_breakdown(self):
        """
        The tax breakdown.
        """
        return self.__tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, value):
        self.__tax_breakdown = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "amount") and self.amount is not None:
            params['amount'] = self.amount
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "tax_breakdown") and self.tax_breakdown is not None:
            params['taxBreakdown'] = self.tax_breakdown
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'amount' in response_body:
            self.__amount = response_body['amount']
        if 'taxAmount' in response_body:
            self.__tax_amount = response_body['taxAmount']
        if 'taxBreakdown' in response_body:
            self.__tax_breakdown = []
            for item in response_body['taxBreakdown']:
                obj = TaxBreakdown()
                obj.parse_rsp_body(item)
                self.__tax_breakdown.append(obj)
