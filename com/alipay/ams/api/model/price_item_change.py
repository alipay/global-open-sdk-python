import json




class PriceItemChange:
    def __init__(self):
        
        self.__change_type = None  # type: str
        self.__current_price_id = None  # type: str
        self.__new_price_id = None  # type: str
        self.__quantity = None  # type: int
        

    @property
    def change_type(self):
        """
        The change type. Maximum length: 7 characters.
        """
        return self.__change_type

    @change_type.setter
    def change_type(self, value):
        self.__change_type = value
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
    def quantity(self):
        """
        The quantity. Note: See documentation for details.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "change_type") and self.change_type is not None:
            params['changeType'] = self.change_type
        if hasattr(self, "current_price_id") and self.current_price_id is not None:
            params['currentPriceId'] = self.current_price_id
        if hasattr(self, "new_price_id") and self.new_price_id is not None:
            params['newPriceId'] = self.new_price_id
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'changeType' in response_body:
            self.__change_type = response_body['changeType']
        if 'currentPriceId' in response_body:
            self.__current_price_id = response_body['currentPriceId']
        if 'newPriceId' in response_body:
            self.__new_price_id = response_body['newPriceId']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
