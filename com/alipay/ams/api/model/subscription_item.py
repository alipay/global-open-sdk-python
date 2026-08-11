import json




class SubscriptionItem:
    def __init__(self):
        
        self.__item_id = None  # type: str
        self.__price_id = None  # type: str
        self.__quantity = None  # type: int
        self.__current_period_start = None  # type: str
        self.__current_period_end = None  # type: str
        self.__recurring_interval_count = None  # type: int
        

    @property
    def item_id(self):
        """
        Subscription item ID. Maximum length: 64 characters.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value
    @property
    def price_id(self):
        """
        Price ID. Maximum length: 64 characters.
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def quantity(self):
        """
        The quantity of the subscription item.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    @property
    def current_period_start(self):
        """
        The start of the current billing period in ISO 8601 format.
        """
        return self.__current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self.__current_period_start = value
    @property
    def current_period_end(self):
        """
        The end of the current billing period in ISO 8601 format.
        """
        return self.__current_period_end

    @current_period_end.setter
    def current_period_end(self, value):
        self.__current_period_end = value
    @property
    def recurring_interval_count(self):
        """
        The number of recurring intervals in each billing period.
        """
        return self.__recurring_interval_count

    @recurring_interval_count.setter
    def recurring_interval_count(self, value):
        self.__recurring_interval_count = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "item_id") and self.item_id is not None:
            params['itemId'] = self.item_id
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "current_period_start") and self.current_period_start is not None:
            params['currentPeriodStart'] = self.current_period_start
        if hasattr(self, "current_period_end") and self.current_period_end is not None:
            params['currentPeriodEnd'] = self.current_period_end
        if hasattr(self, "recurring_interval_count") and self.recurring_interval_count is not None:
            params['recurringIntervalCount'] = self.recurring_interval_count
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
        if 'currentPeriodStart' in response_body:
            self.__current_period_start = response_body['currentPeriodStart']
        if 'currentPeriodEnd' in response_body:
            self.__current_period_end = response_body['currentPeriodEnd']
        if 'recurringIntervalCount' in response_body:
            self.__recurring_interval_count = response_body['recurringIntervalCount']
