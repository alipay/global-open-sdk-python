import json




class SubscriptionItem:
    def __init__(self):
        
        self.__item_id = None  # type: str
        self.__price_id = None  # type: str
        self.__quantity = None  # type: str
        

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
    def price_id(self):
        """
        The price ID. Maximum length: 64 characters.
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def quantity(self):
        """
        The quantity.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "item_id") and self.item_id is not None:
            params['itemId'] = self.item_id
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'itemId' in response_body:
            self.__item_id = response_body['itemId']
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
