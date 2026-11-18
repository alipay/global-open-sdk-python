import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.recurring_settings import RecurringSettings
from com.alipay.ams.api.model.tier import Tier



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPriceCreateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__price_id = None  # type: str
        self.__price_request_id = None  # type: str
        self.__product_id = None  # type: str
        self.__name = None  # type: str
        self.__pricing_model = None  # type: str
        self.__usage_type = None  # type: str
        self.__unit_label = None  # type: str
        self.__meter_id = None  # type: str
        self.__unit_amount = None  # type: Amount
        self.__recurring = None  # type: RecurringSettings
        self.__active = None  # type: bool
        self.__included_quantity = None  # type: int
        self.__tiers_mode = None  # type: str
        self.__tiers = None  # type: [Tier]
        self.__metadata = None  # type: str
        self.__created_at = None  # type: str
        self.__updated_at = None  # type: str
        self.__default_price = None  # type: bool
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPriceCreateResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def price_id(self):
        """
        System-generated price ID. Format: price_ prefix + alphanumeric suffix Returned only when result.resultCode is SUCCESS.
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def price_request_id(self):
        """
        Echo of the idempotent request key from the request. O - May be null in the response when the value is not set Returned only when result.resultCode is SUCCESS.
        """
        return self.__price_request_id

    @price_request_id.setter
    def price_request_id(self, value):
        self.__price_request_id = value
    @property
    def product_id(self):
        """
        Associated product ID Returned only when result.resultCode is SUCCESS.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def name(self):
        """
        Price name. O - May be null in the response when the value is not set Returned only when result.resultCode is SUCCESS.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def pricing_model(self):
        """
        Pricing model type. Always returned - either provided by merchant or derived per Default Derivation rules. Enum: PER_UNIT(per-unit pricing aligned with Stripe billing_scheme&#x3D;per_unit), TIERED(tiered pricing aligned with Stripe billing_scheme&#x3D;tiered). Forward compatibility: If a new value is added in the future, clients that do not recognize it should treat it as an unknown value and not break Returned only when result.resultCode is SUCCESS.
        """
        return self.__pricing_model

    @pricing_model.setter
    def pricing_model(self, value):
        self.__pricing_model = value
    @property
    def usage_type(self):
        """
        Usage type. O - May be null in the response when the value is not set. Enum: LICENSED(fixed license/per-seat - describes quantity tracking method), METERED(metered usage - describes quantity tracking method). Forward compatibility: If a new value is added in the future, clients that do not recognize it should treat it as an unknown value and not break Returned only when result.resultCode is SUCCESS.
        """
        return self.__usage_type

    @usage_type.setter
    def usage_type(self, value):
        self.__usage_type = value
    @property
    def unit_label(self):
        """
        Price-level unit label. O - May be null in the response when the value is not set Returned only when result.resultCode is SUCCESS.
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def meter_id(self):
        """
        External meter reference. O - May be null in the response when the value is not set Returned only when result.resultCode is SUCCESS.
        """
        return self.__meter_id

    @meter_id.setter
    def meter_id(self, value):
        self.__meter_id = value
    @property
    def unit_amount(self):
        """Gets the unit_amount of this AlipayPriceCreateResponse.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def recurring(self):
        """Gets the recurring of this AlipayPriceCreateResponse.
        
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value):
        self.__recurring = value
    @property
    def active(self):
        """
        Price active status. true&#x3D;price is active and can be used for new subscriptions, false&#x3D;price is deactivated and cannot be used for new subscriptions. Default on creation: true. Cannot be null Returned only when result.resultCode is SUCCESS.
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
    @property
    def included_quantity(self):
        """
        Included quantity for package pricing. O - May be null in the response when the value is not set Returned only when result.resultCode is SUCCESS.
        """
        return self.__included_quantity

    @included_quantity.setter
    def included_quantity(self, value):
        self.__included_quantity = value
    @property
    def tiers_mode(self):
        """
        Tiered pricing mode. O - May be null in the response when the value is not set. Enum: GRADUATED(graduated pricing - each tier priced independently, customer may cross tiers), VOLUME(volume pricing - single tier rate applies to entire quantity). Forward compatibility: If a new value is added in the future, clients that do not recognize it should treat it as an unknown value and not break Returned only when result.resultCode is SUCCESS.
        """
        return self.__tiers_mode

    @tiers_mode.setter
    def tiers_mode(self, value):
        self.__tiers_mode = value
    @property
    def tiers(self):
        """
        Tier definitions. O - May be null in the response when the value is not set Returned only when result.resultCode is SUCCESS.
        """
        return self.__tiers

    @tiers.setter
    def tiers(self, value):
        self.__tiers = value
    @property
    def metadata(self):
        """
        Metadata encoded as a JSON object string. Returned only when &#x60;result.resultCode&#x60; is &#x60;SUCCESS&#x60; and metadata was set. The SDK must expose the stored string unchanged.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def created_at(self):
        """
        ISO 8601 creation timestamp Returned only when result.resultCode is SUCCESS.
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value
    @property
    def updated_at(self):
        """
        ISO 8601 last update timestamp. O - May be null in the response when the value is not set Returned only when result.resultCode is SUCCESS.
        """
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value
    @property
    def default_price(self):
        """
        Whether this price is the default price for the product. When true, this price is the primary price shown for the product Returned only when result.resultCode is SUCCESS.
        """
        return self.__default_price

    @default_price.setter
    def default_price(self, value):
        self.__default_price = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "price_request_id") and self.price_request_id is not None:
            params['priceRequestId'] = self.price_request_id
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "pricing_model") and self.pricing_model is not None:
            params['pricingModel'] = self.pricing_model
        if hasattr(self, "usage_type") and self.usage_type is not None:
            params['usageType'] = self.usage_type
        if hasattr(self, "unit_label") and self.unit_label is not None:
            params['unitLabel'] = self.unit_label
        if hasattr(self, "meter_id") and self.meter_id is not None:
            params['meterId'] = self.meter_id
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "recurring") and self.recurring is not None:
            params['recurring'] = self.recurring
        if hasattr(self, "active") and self.active is not None:
            params['active'] = self.active
        if hasattr(self, "included_quantity") and self.included_quantity is not None:
            params['includedQuantity'] = self.included_quantity
        if hasattr(self, "tiers_mode") and self.tiers_mode is not None:
            params['tiersMode'] = self.tiers_mode
        if hasattr(self, "tiers") and self.tiers is not None:
            params['tiers'] = self.tiers
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "created_at") and self.created_at is not None:
            params['createdAt'] = self.created_at
        if hasattr(self, "updated_at") and self.updated_at is not None:
            params['updatedAt'] = self.updated_at
        if hasattr(self, "default_price") and self.default_price is not None:
            params['defaultPrice'] = self.default_price
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPriceCreateResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'priceRequestId' in response_body:
            self.__price_request_id = response_body['priceRequestId']
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'name' in response_body:
            self.__name = response_body['name']
        if 'pricingModel' in response_body:
            self.__pricing_model = response_body['pricingModel']
        if 'usageType' in response_body:
            self.__usage_type = response_body['usageType']
        if 'unitLabel' in response_body:
            self.__unit_label = response_body['unitLabel']
        if 'meterId' in response_body:
            self.__meter_id = response_body['meterId']
        if 'unitAmount' in response_body:
            self.__unit_amount = Amount()
            self.__unit_amount.parse_rsp_body(response_body['unitAmount'])
        if 'recurring' in response_body:
            self.__recurring = RecurringSettings()
            self.__recurring.parse_rsp_body(response_body['recurring'])
        if 'active' in response_body:
            self.__active = response_body['active']
        if 'includedQuantity' in response_body:
            self.__included_quantity = response_body['includedQuantity']
        if 'tiersMode' in response_body:
            self.__tiers_mode = response_body['tiersMode']
        if 'tiers' in response_body:
            self.__tiers = []
            for item in response_body['tiers']:
                obj = Tier()
                obj.parse_rsp_body(item)
                self.__tiers.append(obj)
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'createdAt' in response_body:
            self.__created_at = response_body['createdAt']
        if 'updatedAt' in response_body:
            self.__updated_at = response_body['updatedAt']
        if 'defaultPrice' in response_body:
            self.__default_price = response_body['defaultPrice']
