import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class Goods:
    def __init__(self):
        
        self.__reference_goods_id = None  # type: str
        self.__goods_name = None  # type: str
        self.__goods_category = None  # type: str
        self.__goods_brand = None  # type: str
        self.__goods_unit_amount = None  # type: Amount
        self.__goods_quantity = None  # type: str
        self.__goods_sku_name = None  # type: str
        self.__goods_url = None  # type: str
        self.__delivery_method_type = None  # type: str
        self.__goods_image_url = None  # type: str
        self.__price_id = None  # type: str
        self.__goods_discount_amount = None  # type: Amount
        self.__cross_sell = None  # type: Goods
        

    @property
    def reference_goods_id(self):
        """
        The unique ID to identify the goods.  More information:  Maximum length: 64 characters
        """
        return self.__reference_goods_id

    @reference_goods_id.setter
    def reference_goods_id(self, value):
        self.__reference_goods_id = value
    @property
    def goods_name(self):
        """
        Goods name.  More information:  Maximum length: 256 characters 
        """
        return self.__goods_name

    @goods_name.setter
    def goods_name(self, value):
        self.__goods_name = value
    @property
    def goods_category(self):
        """
        The category of the goods. If the goods have multiple layers for categorization, use slashes between different categories and write the parent category before the subcategory, such as Digital Goods/Digital Vouchers/Food and Beverages.    Note: Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.  More information:  Maximum length: 64 characters
        """
        return self.__goods_category

    @goods_category.setter
    def goods_category(self, value):
        self.__goods_category = value
    @property
    def goods_brand(self):
        """Gets the goods_brand of this Goods.
        
        """
        return self.__goods_brand

    @goods_brand.setter
    def goods_brand(self, value):
        self.__goods_brand = value
    @property
    def goods_unit_amount(self):
        """Gets the goods_unit_amount of this Goods.
        
        """
        return self.__goods_unit_amount

    @goods_unit_amount.setter
    def goods_unit_amount(self, value):
        self.__goods_unit_amount = value
    @property
    def goods_quantity(self):
        """
        Quantity of goods.   Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.  More information:  Value range: 1 - unlimited
        """
        return self.__goods_quantity

    @goods_quantity.setter
    def goods_quantity(self, value):
        self.__goods_quantity = value
    @property
    def goods_sku_name(self):
        """Gets the goods_sku_name of this Goods.
        
        """
        return self.__goods_sku_name

    @goods_sku_name.setter
    def goods_sku_name(self, value):
        self.__goods_sku_name = value
    @property
    def goods_url(self):
        """
        The URL of the website where the user places an order.  Specify this parameter if you require risk control. Providing this information helps to identify black-market behavior.   More information:  Maximum length: 2048 characters
        """
        return self.__goods_url

    @goods_url.setter
    def goods_url(self, value):
        self.__goods_url = value
    @property
    def delivery_method_type(self):
        """
        The delivery method of the goods. Valid values are:  PHYSICAL: indicates that the delivery method is physical delivery. DIGITAL: indicates that the delivery method is digital delivery. Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.    More information:  Maximum length: 32 characters 
        """
        return self.__delivery_method_type

    @delivery_method_type.setter
    def delivery_method_type(self, value):
        self.__delivery_method_type = value
    @property
    def goods_image_url(self):
        """Gets the goods_image_url of this Goods.
        
        """
        return self.__goods_image_url

    @goods_image_url.setter
    def goods_image_url(self, value):
        self.__goods_image_url = value
    @property
    def price_id(self):
        """
        The ID of the Price object. One of ​priceId​ or ​referenceGoodsId​ is required.  More information:  Maximum length: 64 characters
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def goods_discount_amount(self):
        """Gets the goods_discount_amount of this Goods.
        
        """
        return self.__goods_discount_amount

    @goods_discount_amount.setter
    def goods_discount_amount(self, value):
        self.__goods_discount_amount = value
    @property
    def cross_sell(self):
        """Gets the cross_sell of this Goods.
        
        """
        return self.__cross_sell

    @cross_sell.setter
    def cross_sell(self, value):
        self.__cross_sell = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_goods_id") and self.reference_goods_id is not None:
            params['referenceGoodsId'] = self.reference_goods_id
        if hasattr(self, "goods_name") and self.goods_name is not None:
            params['goodsName'] = self.goods_name
        if hasattr(self, "goods_category") and self.goods_category is not None:
            params['goodsCategory'] = self.goods_category
        if hasattr(self, "goods_brand") and self.goods_brand is not None:
            params['goodsBrand'] = self.goods_brand
        if hasattr(self, "goods_unit_amount") and self.goods_unit_amount is not None:
            params['goodsUnitAmount'] = self.goods_unit_amount
        if hasattr(self, "goods_quantity") and self.goods_quantity is not None:
            params['goodsQuantity'] = self.goods_quantity
        if hasattr(self, "goods_sku_name") and self.goods_sku_name is not None:
            params['goodsSkuName'] = self.goods_sku_name
        if hasattr(self, "goods_url") and self.goods_url is not None:
            params['goodsUrl'] = self.goods_url
        if hasattr(self, "delivery_method_type") and self.delivery_method_type is not None:
            params['deliveryMethodType'] = self.delivery_method_type
        if hasattr(self, "goods_image_url") and self.goods_image_url is not None:
            params['goodsImageUrl'] = self.goods_image_url
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "goods_discount_amount") and self.goods_discount_amount is not None:
            params['goodsDiscountAmount'] = self.goods_discount_amount
        if hasattr(self, "cross_sell") and self.cross_sell is not None:
            params['crossSell'] = self.cross_sell
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceGoodsId' in response_body:
            self.__reference_goods_id = response_body['referenceGoodsId']
        if 'goodsName' in response_body:
            self.__goods_name = response_body['goodsName']
        if 'goodsCategory' in response_body:
            self.__goods_category = response_body['goodsCategory']
        if 'goodsBrand' in response_body:
            self.__goods_brand = response_body['goodsBrand']
        if 'goodsUnitAmount' in response_body:
            self.__goods_unit_amount = Amount()
            self.__goods_unit_amount.parse_rsp_body(response_body['goodsUnitAmount'])
        if 'goodsQuantity' in response_body:
            self.__goods_quantity = response_body['goodsQuantity']
        if 'goodsSkuName' in response_body:
            self.__goods_sku_name = response_body['goodsSkuName']
        if 'goodsUrl' in response_body:
            self.__goods_url = response_body['goodsUrl']
        if 'deliveryMethodType' in response_body:
            self.__delivery_method_type = response_body['deliveryMethodType']
        if 'goodsImageUrl' in response_body:
            self.__goods_image_url = response_body['goodsImageUrl']
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'goodsDiscountAmount' in response_body:
            self.__goods_discount_amount = Amount()
            self.__goods_discount_amount.parse_rsp_body(response_body['goodsDiscountAmount'])
        if 'crossSell' in response_body:
            self.__cross_sell = Goods()
            self.__cross_sell.parse_rsp_body(response_body['crossSell'])
