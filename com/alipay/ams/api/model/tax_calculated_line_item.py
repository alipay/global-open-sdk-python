import json
from com.alipay.ams.api.model.tax_breakdown import TaxBreakdown




class TaxCalculatedLineItem:
    def __init__(self):
        
        self.__goods_reference_id = None  # type: str
        self.__amount = None  # type: str
        self.__quantity = None  # type: int
        self.__tax_code = None  # type: str
        self.__tax_behavior = None  # type: str
        self.__tax_amount = None  # type: str
        self.__tax_breakdown = None  # type: [TaxBreakdown]
        

    @property
    def goods_reference_id(self):
        """
        The goods reference ID. Maximum length: 128 characters.
        """
        return self.__goods_reference_id

    @goods_reference_id.setter
    def goods_reference_id(self, value):
        self.__goods_reference_id = value
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
    def quantity(self):
        """
        The quantity.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    @property
    def tax_code(self):
        """
        The tax code. Maximum length: 32 characters.
        """
        return self.__tax_code

    @tax_code.setter
    def tax_code(self, value):
        self.__tax_code = value
    @property
    def tax_behavior(self):
        """
        The tax behavior. Maximum length: 16 characters.
        """
        return self.__tax_behavior

    @tax_behavior.setter
    def tax_behavior(self, value):
        self.__tax_behavior = value
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
        if hasattr(self, "goods_reference_id") and self.goods_reference_id is not None:
            params['goodsReferenceId'] = self.goods_reference_id
        if hasattr(self, "amount") and self.amount is not None:
            params['amount'] = self.amount
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "tax_code") and self.tax_code is not None:
            params['taxCode'] = self.tax_code
        if hasattr(self, "tax_behavior") and self.tax_behavior is not None:
            params['taxBehavior'] = self.tax_behavior
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "tax_breakdown") and self.tax_breakdown is not None:
            params['taxBreakdown'] = self.tax_breakdown
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'goodsReferenceId' in response_body:
            self.__goods_reference_id = response_body['goodsReferenceId']
        if 'amount' in response_body:
            self.__amount = response_body['amount']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
        if 'taxCode' in response_body:
            self.__tax_code = response_body['taxCode']
        if 'taxBehavior' in response_body:
            self.__tax_behavior = response_body['taxBehavior']
        if 'taxAmount' in response_body:
            self.__tax_amount = response_body['taxAmount']
        if 'taxBreakdown' in response_body:
            self.__tax_breakdown = []
            for item in response_body['taxBreakdown']:
                obj = TaxBreakdown()
                obj.parse_rsp_body(item)
                self.__tax_breakdown.append(obj)
