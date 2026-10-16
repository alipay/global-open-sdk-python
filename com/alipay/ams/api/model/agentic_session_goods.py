import json
from com.alipay.ams.api.model.agentic_amount import AgenticAmount




class AgenticSessionGoods:
    def __init__(self):
        
        self.__reference_goods_id = None  # type: str
        self.__goods_name = None  # type: str
        self.__goods_unit_amount = None  # type: AgenticAmount
        self.__goods_quantity = None  # type: str
        self.__goods_url = None  # type: str
        self.__goods_category = None  # type: str
        

    @property
    def reference_goods_id(self):
        """
        Goods identifier.
        """
        return self.__reference_goods_id

    @reference_goods_id.setter
    def reference_goods_id(self, value):
        self.__reference_goods_id = value
    @property
    def goods_name(self):
        """
        Goods name.
        """
        return self.__goods_name

    @goods_name.setter
    def goods_name(self, value):
        self.__goods_name = value
    @property
    def goods_unit_amount(self):
        """Gets the goods_unit_amount of this AgenticSessionGoods.
        
        """
        return self.__goods_unit_amount

    @goods_unit_amount.setter
    def goods_unit_amount(self, value):
        self.__goods_unit_amount = value
    @property
    def goods_quantity(self):
        """
        Goods quantity as a positive integer string. Zero, fractions, negative signs and exponents are not allowed. Provide when the source line item includes this value.
        """
        return self.__goods_quantity

    @goods_quantity.setter
    def goods_quantity(self, value):
        self.__goods_quantity = value
    @property
    def goods_url(self):
        """
        Goods URL.
        """
        return self.__goods_url

    @goods_url.setter
    def goods_url(self, value):
        self.__goods_url = value
    @property
    def goods_category(self):
        """
        Goods category.
        """
        return self.__goods_category

    @goods_category.setter
    def goods_category(self, value):
        self.__goods_category = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_goods_id") and self.reference_goods_id is not None:
            params['referenceGoodsId'] = self.reference_goods_id
        if hasattr(self, "goods_name") and self.goods_name is not None:
            params['goodsName'] = self.goods_name
        if hasattr(self, "goods_unit_amount") and self.goods_unit_amount is not None:
            params['goodsUnitAmount'] = self.goods_unit_amount
        if hasattr(self, "goods_quantity") and self.goods_quantity is not None:
            params['goodsQuantity'] = self.goods_quantity
        if hasattr(self, "goods_url") and self.goods_url is not None:
            params['goodsUrl'] = self.goods_url
        if hasattr(self, "goods_category") and self.goods_category is not None:
            params['goodsCategory'] = self.goods_category
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceGoodsId' in response_body:
            self.__reference_goods_id = response_body['referenceGoodsId']
        if 'goodsName' in response_body:
            self.__goods_name = response_body['goodsName']
        if 'goodsUnitAmount' in response_body:
            self.__goods_unit_amount = AgenticAmount()
            self.__goods_unit_amount.parse_rsp_body(response_body['goodsUnitAmount'])
        if 'goodsQuantity' in response_body:
            self.__goods_quantity = response_body['goodsQuantity']
        if 'goodsUrl' in response_body:
            self.__goods_url = response_body['goodsUrl']
        if 'goodsCategory' in response_body:
            self.__goods_category = response_body['goodsCategory']
