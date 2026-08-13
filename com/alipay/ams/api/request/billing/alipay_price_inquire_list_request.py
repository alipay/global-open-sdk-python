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
        self.__limit = None  # type: int
        self.__include_total = None  # type: bool
        

    @property
    def product_id(self):
        """
        M - Product ID to filter by. Cannot be null.
        """
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value
    @property
    def pricing_model(self):
        """
        Filter by pricing model. O - When provided, returns only prices with the specified pricing model; when absent, returns all pricing models. Enum: PER_UNIT, TIERED. Can be null; default null. Invalid values return PARAM_ILLEGAL error
        """
        return self.__pricing_model

    @pricing_model.setter
    def pricing_model(self, value):
        self.__pricing_model = value
    @property
    def active(self):
        """
        Filter by active status. O - true&#x3D;return only active prices, false&#x3D;return only deactivated prices, absent or null&#x3D;return all prices. No default value
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
    @property
    def starting_after(self):
        """
        Cursor: price ID after which to return results (forward pagination). O - When provided, returns prices sorted by createdAt DESC, priceId DESC whose createdAt is strictly before the price identified by startingAfter. Can be null; default null. Must not be combined with endingBefore (returns PARAM_ILLEGAL). The cursor price ID must exist and belong to the merchant (returns PARAM_ILLEGAL if not found). Sort order: primary createdAt DESC, secondary priceId DESC (tiebreaker for prices with identical timestamps). Aligned with Stripe cursor-based pagination pattern
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        Cursor: price ID before which to return results (backward pagination). O - When provided, returns prices sorted by createdAt DESC, priceId DESC whose createdAt is strictly after the price identified by endingBefore. Can be null; default null. Must not be combined with startingAfter (returns PARAM_ILLEGAL). The cursor price ID must exist and belong to the merchant (returns PARAM_ILLEGAL if not found). Sort order: primary createdAt DESC, secondary priceId DESC (tiebreaker for prices with identical timestamps). Aligned with Stripe cursor-based pagination pattern
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def limit(self):
        """
        Maximum number of prices to return per page. O - Default: 10. Can be null; default 10. Out-of-range values (e.g., 0, negative, or &gt;100) return PARAM_ILLEGAL error. Aligned with Stripe cursor-based pagination pattern
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def include_total(self):
        """
        Request total count in response. O - When explicitly set to false, the response omits the total field. Default: true. Setting to false avoids a COUNT query which may reduce latency. Can be null; default true
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
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
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
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'includeTotal' in response_body:
            self.__include_total = response_body['includeTotal']
