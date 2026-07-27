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
        self.__metadata = None  # type: {str: (str,)}
        

    @property
    def price_request_id(self):
        """
        The price request id. Maximum length: 64 characters.
        """
        return self.__price_request_id

    @price_request_id.setter
    def price_request_id(self, value):
        self.__price_request_id = value
    @property
    def product_id(self):
        """
        The product ID. Maximum length: 32 characters.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def name(self):
        """
        The name. Maximum length: 128 characters.
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def pricing_model(self):
        """
        The pricing model. Maximum length: 24 characters.
        """
        return self.__pricing_model

    @pricing_model.setter
    def pricing_model(self, value):
        self.__pricing_model = value
    @property
    def usage_type(self):
        """
        The usage type. Maximum length: 16 characters. Note: See documentation for details.
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
        The unit label. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__unit_label

    @unit_label.setter
    def unit_label(self, value):
        self.__unit_label = value
    @property
    def meter_id(self):
        """
        The meter ID. Maximum length: 32 characters. Note: See documentation for details.
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
        The included quantity. Note: See documentation for details.
        """
        return self.__included_quantity

    @included_quantity.setter
    def included_quantity(self, value):
        self.__included_quantity = value
    @property
    def tiers_mode(self):
        """
        The tiers mode. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__tiers_mode

    @tiers_mode.setter
    def tiers_mode(self, value):
        self.__tiers_mode = value
    @property
    def tiers(self):
        """
        The tiers. Maximum length: 20 characters. Note: See documentation for details.
        """
        return self.__tiers

    @tiers.setter
    def tiers(self, value):
        self.__tiers = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases. Note: See documentation for details.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


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
