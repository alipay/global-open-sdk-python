import json




class TaxCalculationLineItem:
    def __init__(self):
        
        self.__goods_reference_id = None  # type: str
        self.__unit_amount = None  # type: str
        self.__quantity = None  # type: int
        self.__tax_code = None  # type: str
        self.__product_id = None  # type: str
        self.__tax_behavior = None  # type: str
        

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
    def unit_amount(self):
        """
        The unit amount. Maximum length: 19 characters.
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
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
        The tax code. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__tax_code

    @tax_code.setter
    def tax_code(self, value):
        self.__tax_code = value
    @property
    def product_id(self):
        """
        The product ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def tax_behavior(self):
        """
        The tax behavior. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__tax_behavior

    @tax_behavior.setter
    def tax_behavior(self, value):
        self.__tax_behavior = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "goods_reference_id") and self.goods_reference_id is not None:
            params['goodsReferenceId'] = self.goods_reference_id
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "tax_code") and self.tax_code is not None:
            params['taxCode'] = self.tax_code
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "tax_behavior") and self.tax_behavior is not None:
            params['taxBehavior'] = self.tax_behavior
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'goodsReferenceId' in response_body:
            self.__goods_reference_id = response_body['goodsReferenceId']
        if 'unitAmount' in response_body:
            self.__unit_amount = response_body['unitAmount']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
        if 'taxCode' in response_body:
            self.__tax_code = response_body['taxCode']
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'taxBehavior' in response_body:
            self.__tax_behavior = response_body['taxBehavior']
