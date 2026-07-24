import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPriceInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPriceInquireListRequest, self).__init__("/ams/api/v1/billing/price/inquireList") 

        self.__product_id = None  # type: str
        self.__pricing_model = None  # type: str
        self.__active = None  # type: bool
        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__list = None  # type: int
        self.__include_total = None  # type: bool
        

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
    def pricing_model(self):
        """
        The pricing model. Maximum length: 24 characters.
        """
        return self.__pricing_model

    @pricing_model.setter
    def pricing_model(self, value):
        self.__pricing_model = value
    @property
    def active(self):
        """
        The active.
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
    @property
    def starting_after(self):
        """
        The starting after. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        The ending before. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def list(self):
        """
        The list. Maximum length: 32 characters.
        """
        return self.__list

    @list.setter
    def list(self, value):
        self.__list = value
    @property
    def include_total(self):
        """
        The include total.
        """
        return self.__include_total

    @include_total.setter
    def include_total(self, value):
        self.__include_total = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "product_id") and self.product_id is not None:
            params['productId'] = self.product_id
        if hasattr(self, "pricing_model") and self.pricing_model is not None:
            params['pricingModel'] = self.pricing_model
        if hasattr(self, "active") and self.active is not None:
            params['active'] = self.active
        if hasattr(self, "starting_after") and self.starting_after is not None:
            params['startingAfter'] = self.starting_after
        if hasattr(self, "ending_before") and self.ending_before is not None:
            params['endingBefore'] = self.ending_before
        if hasattr(self, "list") and self.list is not None:
            params['list'] = self.list
        if hasattr(self, "include_total") and self.include_total is not None:
            params['includeTotal'] = self.include_total
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'productId' in response_body:
            self.__product_id = response_body['productId']
        if 'pricingModel' in response_body:
            self.__pricing_model = response_body['pricingModel']
        if 'active' in response_body:
            self.__active = response_body['active']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
        if 'list' in response_body:
            self.__list = response_body['list']
        if 'includeTotal' in response_body:
            self.__include_total = response_body['includeTotal']
