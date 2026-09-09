import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireHoldListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireHoldListRequest, self).__init__("/ams/api/v1/payments/reserve/inquireHoldList") 

        self.__hold_request_id = None  # type: str
        self.__hold_id = None  # type: str
        self.__limit = None  # type: int
        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        

    @property
    def hold_request_id(self):
        """
        The original createHold request identifier used to retrieve or recover one hold. Do not combine it with holdId, startingAfter, or endingBefore. This exact-query mode returns at most one record and hasMore is false.
        """
        return self.__hold_request_id

    @hold_request_id.setter
    def hold_request_id(self, value):
        self.__hold_request_id = value
    @property
    def hold_id(self):
        """
        The known manual hold identifier used to retrieve one hold. Do not combine it with holdRequestId, startingAfter, or endingBefore. This exact-query mode returns at most one record and hasMore is false.
        """
        return self.__hold_id

    @hold_id.setter
    def hold_id(self, value):
        self.__hold_id = value
    @property
    def limit(self):
        """
        The page size for list and pagination mode. The default is 10. Values outside 1 through 100 are rejected rather than capped. Exact-query mode still returns at most one record.
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def starting_after(self):
        """
        The exclusive cursor for records older than the specified holdId in descending holdId order. Pass the last holdId from the current page. Do not combine it with endingBefore, holdId, or holdRequestId.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        The exclusive cursor for records newer than the specified holdId, returned in descending holdId order. Pass the first holdId from the current page. Do not combine it with startingAfter, holdId, or holdRequestId.
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "hold_request_id") and self.hold_request_id is not None:
            params['holdRequestId'] = self.hold_request_id
        if hasattr(self, "hold_id") and self.hold_id is not None:
            params['holdId'] = self.hold_id
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
        if hasattr(self, "starting_after") and self.starting_after is not None:
            params['startingAfter'] = self.starting_after
        if hasattr(self, "ending_before") and self.ending_before is not None:
            params['endingBefore'] = self.ending_before
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'holdRequestId' in response_body:
            self.__hold_request_id = response_body['holdRequestId']
        if 'holdId' in response_body:
            self.__hold_id = response_body['holdId']
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
