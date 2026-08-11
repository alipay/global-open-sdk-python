import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayProductInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayProductInquireListRequest, self).__init__("/ams/api/v1/billing/product/inquireList") 

        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        self.__active = None  # type: bool
        self.__type = None  # type: str
        self.__keyword = None  # type: str
        self.__include_total = None  # type: bool
        self.__usage_type = None  # type: str
        

    @property
    def starting_after(self):
        """
        Cursor: product ID after which to return results (forward pagination). O - When provided, returns products sorted by createdAt DESC, productId DESC whose createdAt is strictly before the product identified by startingAfter. Can be null; default null. Must not be combined with endingBefore (returns PARAM_ILLEGAL). The cursor product ID must exist and belong to the merchant (returns PARAM_ILLEGAL if not found). Aligned with Stripe cursor-based pagination pattern
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        Cursor: product ID before which to return results (backward pagination). O - When provided, returns products sorted by createdAt DESC, productId DESC whose createdAt is strictly after the product identified by endingBefore. Can be null; default null. Must not be combined with startingAfter (returns PARAM_ILLEGAL). The cursor product ID must exist and belong to the merchant (returns PARAM_ILLEGAL if not found). Aligned with Stripe cursor-based pagination pattern
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def limit(self):
        """
        Maximum number of products to return per page. O - Default: 10. Can be null; default 10. Out-of-range values (e.g., 0, negative, or &gt;100) return PARAM_ILLEGAL error. Aligned with Stripe cursor-based pagination pattern
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def active(self):
        """
        Filter by active status. O - true&#x3D;return only active products, false&#x3D;return only deactivated products, absent or null&#x3D;return all products. No default value
        """
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
    @property
    def type(self):
        """
        Filter by product type. O - When provided, returns only products of the specified type; when absent, returns all types. Enum: SERVICE, GOOD. Can be null; default null. Invalid values return PARAM_ILLEGAL error
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def keyword(self):
        """
        Search keyword. O - When provided, returns only products whose name or description contains the keyword (case-insensitive). Can be null; default null. Search behavior: (1) Tokenization: keyword is matched as a full string (not split on whitespace); partial matches are supported via prefix matching. (2) Special characters: characters &amp; &#39; \&quot; are stripped from the keyword before matching. (3) Language support: Unicode-aware matching supporting English, Chinese, Japanese, Korean, and other UTF-8 characters. (4) Consistency: eventual consistency with approximately 1-second delay after create/update before new/modified products appear in search results
        """
        return self.__keyword

    @keyword.setter
    def keyword(self, value):
        self.__keyword = value
    @property
    def include_total(self):
        """
        Request total count in response. O - When set to true (or absent, as default is true), the response includes total field. Default: true. Setting to false omits the total field to avoid COUNT query latency. Can be null; default true
        """
        return self.__include_total

    @include_total.setter
    def include_total(self, value):
        self.__include_total = value
    @property
    def usage_type(self):
        """
        Filter by usage type (LICENSED or METERED). Returns only products that have prices with matching usage_type.
        """
        return self.__usage_type

    @usage_type.setter
    def usage_type(self, value):
        self.__usage_type = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "starting_after") and self.starting_after is not None:
            params['startingAfter'] = self.starting_after
        if hasattr(self, "ending_before") and self.ending_before is not None:
            params['endingBefore'] = self.ending_before
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
        if hasattr(self, "active") and self.active is not None:
            params['active'] = self.active
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "keyword") and self.keyword is not None:
            params['keyword'] = self.keyword
        if hasattr(self, "include_total") and self.include_total is not None:
            params['includeTotal'] = self.include_total
        if hasattr(self, "usage_type") and self.usage_type is not None:
            params['usageType'] = self.usage_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'active' in response_body:
            self.__active = response_body['active']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'keyword' in response_body:
            self.__keyword = response_body['keyword']
        if 'includeTotal' in response_body:
            self.__include_total = response_body['includeTotal']
        if 'usageType' in response_body:
            self.__usage_type = response_body['usageType']
