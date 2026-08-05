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
    def limit(self):
        """
        The limit.
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
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
    def type(self):
        """
        The type. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def keyword(self):
        """
        The keyword. Maximum length: 128 characters.
        """
        return self.__keyword

    @keyword.setter
    def keyword(self, value):
        self.__keyword = value
    @property
    def include_total(self):
        """
        The include total.
        """
        return self.__include_total

    @include_total.setter
    def include_total(self, value):
        self.__include_total = value
    @property
    def usage_type(self):
        """
        Filter by usage type. Valid values: LICENSED, METERED. O - When provided, returns only products that have prices with matching usage type.
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
