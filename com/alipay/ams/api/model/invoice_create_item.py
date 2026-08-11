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
        Human-readable description of the invoice. Appears on the invoice PDF and hosted page. HTML tags are stripped for XSS prevention. Can be null.
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
        Price identifier from the Antom price catalog. The unit amount and currency are resolved from the price catalog entry. Use this for items linked to the product/price catalog. Can be null when using &#x60;itemAmount&#x60; or &#x60;unitAmount&#x60; pricing models.
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def product_id(self):
        """
        External product identifier associated with this line item. Stored in item metadata; used for reconciliation and reporting. Can be null.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def quantity(self):
        """
        Quantity of units. Integer only; decimal quantities are not supported in v1. Defaults to 1 if omitted. Required for unit-amount and price-object pricing models, and ignored for fixed-amount pricing. Value range: 1 to 999999.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    @property
    def item_id(self):
        """
        Item identifier for upsert during update operations. When provided in an update request, the system queries by itemId + merchantId to determine whether to update an existing item or create a new one. Omit for create operations. Can be null.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value
    @property
    def supply_start(self):
        """
        Service/goods supply period start date (ISO 8601 format, e.g. &#x60;\&quot;2026-01-15T00:00:00Z\&quot;&#x60;). NULL if not applicable. Complements billing period coverage fields. Can be null.
        """
        return self.__supply_start

    @supply_start.setter
    def supply_start(self, value):
        self.__supply_start = value
    @property
    def supply_end(self):
        """
        Service/goods supply period end date (ISO 8601 format, e.g. &#x60;\&quot;2026-01-31T23:59:59Z\&quot;&#x60;). NULL if not applicable. If both &#x60;supplyStart&#x60; and &#x60;supplyEnd&#x60; are provided, &#x60;supplyStart&#x60; must be before &#x60;supplyEnd&#x60;. Can be null.
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
