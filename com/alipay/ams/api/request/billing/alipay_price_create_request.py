import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.recurring_settings import RecurringSettings
from com.alipay.ams.api.model.tier import Tier



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPriceCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPriceCreateRequest, self).__init__("/ams/api/v1/billing/price/create") 

        self.__price_request_id = None  # type: str
        self.__product_id = None  # type: str
        self.__name = None  # type: str
        self.__pricing_model = None  # type: str
        self.__usage_type = None  # type: str
        self.__unit_amount = None  # type: Amount
        self.__unit_label = None  # type: str
        self.__meter_id = None  # type: str
        self.__recurring = None  # type: RecurringSettings
        self.__included_quantity = None  # type: int
        self.__tiers_mode = None  # type: str
        self.__tiers = None  # type: [Tier]
        self.__metadata = None  # type: str
        self.__default_price = None  # type: bool
        

    @property
    def price_request_id(self):
        """
        Idempotent request key. O - Optional idempotent request key. When provided, prevents duplicate price creation from network retries. If a request with the same priceRequestId from the same merchant has been successfully processed within 24 hours, the original response is returned without re-processing. Max 64 characters, alphanumeric, hyphens and underscores allowed. This field serves as the idempotent key for this operation. Since priceId is system-generated and no natural business key exists for deduplication, priceRequestId is the sole dedup mechanism - omitting it risks duplicate price creation on network retries
        """
        return self.__price_request_id

    @price_request_id.setter
    def price_request_id(self, value):
        self.__price_request_id = value
    @property
    def product_id(self):
        """
        Product ID to attach price to. Cannot be null. Format: prod_ prefix + alphanumeric suffix (e.g., prod_2xK8mN3pQ7)
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def name(self):
        """
        Price name. O - Optional display name for the price; default null. Can be null. Characters &amp; &#39; \&quot; are not allowed. Max 128 characters
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def pricing_model(self):
        """
        Pricing model type. O - If absent, derived from other fields per Pricing Model Default Derivation rules. Enum: PER_UNIT(per-unit pricing aligned with Stripe billing_scheme&#x3D;per_unit - charge is unitAmount x quantity; when includedQuantity is present, charge &#x3D; ceil(quantity / includedQuantity) x unitAmount for package pricing), TIERED(tiered pricing aligned with Stripe billing_scheme&#x3D;tiered - tier-based pricing with tiersMode GRADUATED or VOLUME; actual pricing comes from tier definitions). Can be null; derived when absent
        """
        return self.__pricing_model

    @pricing_model.setter
    def pricing_model(self, value):
        self.__pricing_model = value
    @property
    def usage_type(self):
        """
        Usage type. O - Optional. When provided, must be a valid enum value (LICENSED or METERED). Can be null; default null. Enum: LICENSED(fixed quantity billing - subscription item quantity is set at subscription creation and changed manually via update API; system bills unitAmount x quantity automatically each period), METERED(metered usage billing - quantity is tracked by external metering system iusage and reported via Usage Report API; system bills based on actual reported usage in arrears at end of billing period)
        """
        return self.__usage_type

    @usage_type.setter
    def usage_type(self, value):
        self.__usage_type = value
    @property
    def unit_amount(self):
        """Gets the unit_amount of this AlipayPriceCreateRequest.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def unit_label(self):
        """
        Price-level unit label. O - Optional. Price-level unitLabel overrides Product-level unitLabel when both are set; if Price-level is absent, Product-level is inherited. Can be null; default null. Characters &amp; &#39; \&quot; are not allowed
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def meter_id(self):
        """
        External meter reference. C - Required when usageType&#x3D;METERED; otherwise forbidden. References external metering system contract. Format: alphanumeric + underscore, max 32 chars. Validated at price creation: format check (regex: ^[a-zA-Z0-9_]{1,32}$) AND existence check against iusage meter registry. Returns METER_NOT_FOUND if meter definition does not exist in iusage. This ensures fail-fast validation - merchants are alerted to invalid meter references immediately rather than discovering the error at subscription creation time
        """
        return self.__meter_id

    @meter_id.setter
    def meter_id(self, value):
        self.__meter_id = value
    @property
    def recurring(self):
        """Gets the recurring of this AlipayPriceCreateRequest.
        
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value):
        self.__recurring = value
    @property
    def included_quantity(self):
        """
        Included quantity for package pricing. O - Number of units included in the base price. When present, indicates package pricing (aligned with Stripe&#39;s transform_quantity): the total charge &#x3D; ceil(quantity / includedQuantity) x unitAmount. When absent (null), indicates flat-rate PER_UNIT pricing: charge &#x3D; unitAmount x quantity. Forbidden when pricingModel&#x3D;TIERED. Can be null; default null
        """
        return self.__included_quantity

    @included_quantity.setter
    def included_quantity(self, value):
        self.__included_quantity = value
    @property
    def tiers_mode(self):
        """
        Tiered pricing mode. C - Required when pricingModel&#x3D;TIERED; forbidden otherwise. Enum: GRADUATED(graduated pricing - each tier is priced independently, customer may cross tiers with different unit rates), VOLUME(volume pricing - single tier rate applies to the entire quantity based on which tier the total volume falls into). Can be null; default null
        """
        return self.__tiers_mode

    @tiers_mode.setter
    def tiers_mode(self, value):
        self.__tiers_mode = value
    @property
    def tiers(self):
        """
        Tier definitions. Required when &#x60;pricingModel&#x60; is &#x60;TIERED&#x60; and forbidden otherwise. Maximum size: 20 elements; exceeding the limit returns &#x60;TOO_MANY_TIERS&#x60;.
        """
        return self.__tiers

    @tiers.setter
    def tiers(self, value):
        self.__tiers = value
    @property
    def metadata(self):
        """
        Optional metadata encoded as a JSON object string. The SDK must forward the string unchanged. Maximum size: 20 entries. Keys must use lowerCamelCase alphanumeric text and be at most 40 characters. Values are at most 500 characters and cannot contain &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&amp;&#x60;, &#x60;&#39;&#x60;, or &#x60;\&quot;&#x60;. PII must not be stored. Invalid keys, values, or entry counts return &#x60;INVALID_METADATA_KEY&#x60;, &#x60;INVALID_METADATA_VALUE&#x60;, or &#x60;INVALID_METADATA_SIZE&#x60;.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def default_price(self):
        """
        Whether this price is the default price for the product. O - Optional. Only &#x60;true&#x60; is accepted; &#x60;false&#x60; or absent means the price is not the default. Only one price per product can be the default price - creating a new default price automatically un-defaults any previous default price of that product. Can be null; default null
        """
        return self.__default_price

    @default_price.setter
    def default_price(self, value):
        self.__default_price = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
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
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "unit_label") and self.unit_label is not None:
            params['unitLabel'] = self.unit_label
        if hasattr(self, "meter_id") and self.meter_id is not None:
            params['meterId'] = self.meter_id
        if hasattr(self, "recurring") and self.recurring is not None:
            params['recurring'] = self.recurring
        if hasattr(self, "included_quantity") and self.included_quantity is not None:
            params['includedQuantity'] = self.included_quantity
        if hasattr(self, "tiers_mode") and self.tiers_mode is not None:
            params['tiersMode'] = self.tiers_mode
        if hasattr(self, "tiers") and self.tiers is not None:
            params['tiers'] = self.tiers
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "default_price") and self.default_price is not None:
            params['defaultPrice'] = self.default_price
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
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
        if 'unitAmount' in response_body:
            self.__unit_amount = Amount()
            self.__unit_amount.parse_rsp_body(response_body['unitAmount'])
        if 'unitLabel' in response_body:
            self.__unit_label = response_body['unitLabel']
        if 'meterId' in response_body:
            self.__meter_id = response_body['meterId']
        if 'recurring' in response_body:
            self.__recurring = RecurringSettings()
            self.__recurring.parse_rsp_body(response_body['recurring'])
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
        if 'defaultPrice' in response_body:
            self.__default_price = response_body['defaultPrice']
