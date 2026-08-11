import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class BillingSubscriptionPriceItem:
    def __init__(self):
        
        self.__current_period_end = None  # type: str
        self.__current_period_start = None  # type: str
        self.__item_amount = None  # type: Amount
        self.__item_id = None  # type: str
        self.__nickname = None  # type: str
        self.__price_id = None  # type: str
        self.__price_type = None  # type: str
        self.__pricing_model = None  # type: str
        self.__product_id = None  # type: str
        self.__product_name = None  # type: str
        self.__quantity = None  # type: int
        self.__recurring_interval = None  # type: str
        self.__recurring_interval_count = None  # type: int
        self.__unit_amount = None  # type: Amount
        self.__usage_type = None  # type: str
        

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
    def current_period_start(self):
        """
        The start of the current billing period in ISO 8601 format.
        """
        return self.__current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self.__current_period_start = value
    @property
    def item_amount(self):
        """Gets the item_amount of this BillingSubscriptionPriceItem.
        
        """
        return self.__item_amount

    @item_amount.setter
    def item_amount(self, value):
        self.__item_amount = value
    @property
    def item_id(self):
        """
        The subscription item ID. Maximum length: 64 characters.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value
    @property
    def nickname(self):
        """
        The display nickname of the price.
        """
        return self.__nickname

    @nickname.setter
    def nickname(self, value):
        self.__nickname = value
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
    def price_type(self):
        """
        The price type, such as RECURRING or ONE_TIME.
        """
        return self.__price_type

    @price_type.setter
    def price_type(self, value):
        self.__price_type = value
    @property
    def pricing_model(self):
        """
        The pricing model. Valid values are PER_UNIT and TIERED.
        """
        return self.__pricing_model

    @pricing_model.setter
    def pricing_model(self, value):
        self.__pricing_model = value
    @property
    def product_id(self):
        """
        The associated product ID. Maximum length: 64 characters.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def product_name(self):
        """
        The associated product name.
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value
    @property
    def quantity(self):
        """
        The quantity of this subscription item.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    @property
    def recurring_interval(self):
        """
        The recurring interval. Valid values include DAY, WEEK, MONTH, and YEAR.
        """
        return self.__recurring_interval

    @recurring_interval.setter
    def recurring_interval(self, value):
        self.__recurring_interval = value
    @property
    def recurring_interval_count(self):
        """
        The number of recurring intervals in each billing period.
        """
        return self.__recurring_interval_count

    @recurring_interval_count.setter
    def recurring_interval_count(self, value):
        self.__recurring_interval_count = value
    @property
    def unit_amount(self):
        """Gets the unit_amount of this BillingSubscriptionPriceItem.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def usage_type(self):
        """
        The usage type. Valid values include LICENSED and METERED.
        """
        return self.__usage_type

    @usage_type.setter
    def usage_type(self, value):
        self.__usage_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "current_period_end") and self.current_period_end is not None:
            params['currentPeriodEnd'] = self.current_period_end
        if hasattr(self, "current_period_start") and self.current_period_start is not None:
            params['currentPeriodStart'] = self.current_period_start
        if hasattr(self, "item_amount") and self.item_amount is not None:
            params['itemAmount'] = self.item_amount
        if hasattr(self, "item_id") and self.item_id is not None:
            params['itemId'] = self.item_id
        if hasattr(self, "nickname") and self.nickname is not None:
            params['nickname'] = self.nickname
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "price_type") and self.price_type is not None:
            params['priceType'] = self.price_type
        if hasattr(self, "pricing_model") and self.pricing_model is not None:
            params['pricingModel'] = self.pricing_model
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "product_name") and self.product_name is not None:
            params['productName'] = self.product_name
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "recurring_interval") and self.recurring_interval is not None:
            params['recurringInterval'] = self.recurring_interval
        if hasattr(self, "recurring_interval_count") and self.recurring_interval_count is not None:
            params['recurringIntervalCount'] = self.recurring_interval_count
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "usage_type") and self.usage_type is not None:
            params['usageType'] = self.usage_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currentPeriodEnd' in response_body:
            self.__current_period_end = response_body['currentPeriodEnd']
        if 'currentPeriodStart' in response_body:
            self.__current_period_start = response_body['currentPeriodStart']
        if 'itemAmount' in response_body:
            self.__item_amount = Amount()
            self.__item_amount.parse_rsp_body(response_body['itemAmount'])
        if 'itemId' in response_body:
            self.__item_id = response_body['itemId']
        if 'nickname' in response_body:
            self.__nickname = response_body['nickname']
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'priceType' in response_body:
            self.__price_type = response_body['priceType']
        if 'pricingModel' in response_body:
            self.__pricing_model = response_body['pricingModel']
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'productName' in response_body:
            self.__product_name = response_body['productName']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
        if 'recurringInterval' in response_body:
            self.__recurring_interval = response_body['recurringInterval']
        if 'recurringIntervalCount' in response_body:
            self.__recurring_interval_count = response_body['recurringIntervalCount']
        if 'unitAmount' in response_body:
            self.__unit_amount = Amount()
            self.__unit_amount.parse_rsp_body(response_body['unitAmount'])
        if 'usageType' in response_body:
            self.__usage_type = response_body['usageType']
