import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class InvoiceCreateItem:
    def __init__(self):
        
        self.__description = None  # type: str
        self.__item_amount = None  # type: Amount
        self.__unit_amount = None  # type: Amount
        self.__price_id = None  # type: str
        self.__product_id = None  # type: str
        self.__quantity = None  # type: int
        self.__item_id = None  # type: str
        self.__supply_start = None  # type: str
        self.__supply_end = None  # type: str
        

    @property
    def description(self):
        """
        The description. Maximum length: 256 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def item_amount(self):
        """Gets the item_amount of this InvoiceCreateItem.
        
        """
        return self.__item_amount

    @item_amount.setter
    def item_amount(self, value):
        self.__item_amount = value
    @property
    def unit_amount(self):
        """Gets the unit_amount of this InvoiceCreateItem.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def price_id(self):
        """
        The price ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def product_id(self):
        """
        The product ID. Maximum length: 64 characters.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
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
    def item_id(self):
        """
        The item id. Maximum length: 64 characters.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value
    @property
    def supply_start(self):
        """
        The supply start.
        """
        return self.__supply_start

    @supply_start.setter
    def supply_start(self, value):
        self.__supply_start = value
    @property
    def supply_end(self):
        """
        The supply end. Note: See documentation for details.
        """
        return self.__supply_end

    @supply_end.setter
    def supply_end(self, value):
        self.__supply_end = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "item_amount") and self.item_amount is not None:
            params['itemAmount'] = self.item_amount
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "item_id") and self.item_id is not None:
            params['itemId'] = self.item_id
        if hasattr(self, "supply_start") and self.supply_start is not None:
            params['supplyStart'] = self.supply_start
        if hasattr(self, "supply_end") and self.supply_end is not None:
            params['supplyEnd'] = self.supply_end
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'itemAmount' in response_body:
            self.__item_amount = Amount()
            self.__item_amount.parse_rsp_body(response_body['itemAmount'])
        if 'unitAmount' in response_body:
            self.__unit_amount = Amount()
            self.__unit_amount.parse_rsp_body(response_body['unitAmount'])
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
        if 'itemId' in response_body:
            self.__item_id = response_body['itemId']
        if 'supplyStart' in response_body:
            self.__supply_start = response_body['supplyStart']
        if 'supplyEnd' in response_body:
            self.__supply_end = response_body['supplyEnd']
