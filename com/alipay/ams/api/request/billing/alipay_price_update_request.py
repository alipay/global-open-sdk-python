import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPriceUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPriceUpdateRequest, self).__init__("/ams/api/v1/billing/price/update") 

        self.__price_id = None  # type: str
        self.__name = None  # type: str
        self.__metadata = None  # type: str
        self.__active = None  # type: bool
        self.__default_price = None  # type: bool
        

    @property
    def price_id(self):
        """
        Price ID to update. Cannot be null. Format: price_ prefix + alphanumeric suffix. This field serves as the idempotent key for this operation
        """
        return self.__price_id

    @price_id.setter
    def price_id(self, value):
        self.__price_id = value
    @property
    def name(self):
        """
        Price name. O - Present with value: update; present with null: clear; absent: no change. Can be null
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def metadata(self):
        """
        Custom metadata encoded as a JSON object string. When provided, the value fully replaces the existing metadata; keys are not merged. When omitted, the existing value is unchanged. PII must not be stored.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
    @property
    def active(self):
        """
        Price active status. O - explicit true&#x3D;activate, explicit false&#x3D;deactivate, absent or null&#x3D;no change. There is no \&quot;clear\&quot; semantic for active - it is always either true or false. For Boolean fields on update APIs, null/absent means \&quot;no change\&quot; (not \&quot;set to null\&quot;). See Section 6.8 Update API Null/Absent Semantics for the authoritative definition. When deactivated (active&#x3D;false), the price cannot be used for new subscriptions; existing subscriptions continue using the price
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
    @property
    def default_price(self):
        """
        Whether to set this price as the default price for the product. When provided, only &#x60;true&#x60; is accepted; &#x60;false&#x60; is rejected with &#x60;DEFAULT_PRICE_REMOVAL_FORBIDDEN&#x60;, while omission means no change. When set to &#x60;true&#x60;, this price becomes the product default and the previous default price is automatically unset. &#x60;defaultPrice&#x3D;true&#x60; cannot be combined with &#x60;active&#x3D;false&#x60; in the same request because the default price must remain active. A product must always retain a default price.
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
        if hasattr(self, "price_id") and self.price_id is not None:
            params['priceId'] = self.price_id
        if hasattr(self, "name") and self.name is not None:
            params['name'] = self.name
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
        if hasattr(self, "active") and self.active is not None:
            params['active'] = self.active
        if hasattr(self, "default_price") and self.default_price is not None:
            params['defaultPrice'] = self.default_price
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'priceId' in response_body:
            self.__price_id = response_body['priceId']
        if 'name' in response_body:
            self.__name = response_body['name']
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']
        if 'active' in response_body:
            self.__active = response_body['active']
        if 'defaultPrice' in response_body:
            self.__default_price = response_body['defaultPrice']
