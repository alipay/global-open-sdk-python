import json




class PriceItemChange:
    def __init__(self):
        
        self.__type = None  # type: str
        self.__item_id = None  # type: str
        self.__current_price_id = None  # type: str
        self.__new_price_id = None  # type: str
        self.__new_quantity = None  # type: int
        

    @property
    def type(self):
        """
        The change type. Valid values are CHANGE, ADD, and REMOVE. Maximum length: 7 characters.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def item_id(self):
        """
        The subscription item ID. Provide it when the item to change or remove is known. Maximum length: 64 characters.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value
    @property
    def current_price_id(self):
        """
        The current price id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__current_price_id

    @current_price_id.setter
    def current_price_id(self, value):
        self.__current_price_id = value
    @property
    def new_price_id(self):
        """
        The new price id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__new_price_id

    @new_price_id.setter
    def new_price_id(self, value):
        self.__new_price_id = value
    @property
    def new_quantity(self):
        """
        The new quantity. Applicable when type is CHANGE or ADD. Value range: 1-999999.
        """
        return self.__new_quantity

    @new_quantity.setter
    def new_quantity(self, value):
        self.__new_quantity = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "item_id") and self.item_id is not None:
            params['itemId'] = self.item_id
        if hasattr(self, "current_price_id") and self.current_price_id is not None:
            params['currentPriceId'] = self.current_price_id
        if hasattr(self, "new_price_id") and self.new_price_id is not None:
            params['newPriceId'] = self.new_price_id
        if hasattr(self, "new_quantity") and self.new_quantity is not None:
            params['newQuantity'] = self.new_quantity
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'itemId' in response_body:
            self.__item_id = response_body['itemId']
        if 'currentPriceId' in response_body:
            self.__current_price_id = response_body['currentPriceId']
        if 'newPriceId' in response_body:
            self.__new_price_id = response_body['newPriceId']
        if 'newQuantity' in response_body:
            self.__new_quantity = response_body['newQuantity']
