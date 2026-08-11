import json




class PriceItem:
    def __init__(self):
        
        self.__price_id = None  # type: str
        self.__quantity = None  # type: int
        

    @property
    def price_id(self):
        """
        Price ID referencing pre-created Recurring Price. Not null
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def quantity(self):
        """
        Quantity for licensed type. Default: 1, Min: 1. Can be null (defaults to 1)
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
