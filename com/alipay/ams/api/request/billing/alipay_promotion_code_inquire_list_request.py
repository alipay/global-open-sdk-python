import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayPromotionCodeInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayPromotionCodeInquireListRequest, self).__init__("/ams/api/v1/billing/promotionCode/inquireList") 

        self.__coupon_id = None  # type: str
        self.__status = None  # type: str
        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        self.__include_total = None  # type: bool
        

    @property
    def coupon_id(self):
        """
        Parent coupon ID. Only promotion codes belonging to this coupon are returned. Cannot be empty.
        """
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value
    @property
    def status(self):
        """
        Filter by promotion code status. Allowed values: &#x60;ACTIVE&#x60;, &#x60;INACTIVE&#x60;. If not provided, returns all statuses.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def starting_after(self):
        """
        Forward pagination cursor. Returns promotion codes older than (created before) this promotionCodeId, in creation-time descending order (&#x60;gmt_create DESC&#x60;). Pass the &#x60;nextCursor&#x60; from the previous response. Mutually exclusive with &#x60;endingBefore&#x60;.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        Backward pagination cursor. Returns promotion codes newer than (created after) this promotionCodeId. Mutually exclusive with &#x60;startingAfter&#x60;.
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def limit(self):
        """
        Number of records per page. Value range: 1-100. Defaults to 20 if not provided.
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def include_total(self):
        """
        When &#x60;true&#x60;, an additional COUNT query is executed to populate &#x60;total&#x60; in the response. Default: &#x60;false&#x60;.
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
        if hasattr(self, "coupon_id") and self.coupon_id is not None:
            params['couponId'] = self.coupon_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
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
        if 'couponId' in response_body:
            self.__coupon_id = response_body['couponId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'includeTotal' in response_body:
            self.__include_total = response_body['includeTotal']
