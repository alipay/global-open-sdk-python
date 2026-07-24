import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionInquireListRequest, self).__init__("/ams/api/v1/billing/subscription/inquireList") 

        self.__status = None  # type: str
        self.__customer_id = None  # type: str
        self.__expires_before = None  # type: str
        self.__expires_after = None  # type: str
        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        self.__include_total = None  # type: bool
        

    @property
    def status(self):
        """
        The current status. Maximum length: 20 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def expires_before(self):
        """
        The expires before.
        """
        return self.__expires_before

    @expires_before.setter
    def expires_before(self, value):
        self.__expires_before = value
    @property
    def expires_after(self):
        """
        The expires after.
        """
        return self.__expires_after

    @expires_after.setter
    def expires_after(self, value):
        self.__expires_after = value
    @property
    def starting_after(self):
        """
        The starting after. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        The ending before. Maximum length: 64 characters. Note: See documentation for details.
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
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "expires_before") and self.expires_before is not None:
            params['expiresBefore'] = self.expires_before
        if hasattr(self, "expires_after") and self.expires_after is not None:
            params['expiresAfter'] = self.expires_after
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
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'expiresBefore' in response_body:
            self.__expires_before = response_body['expiresBefore']
        if 'expiresAfter' in response_body:
            self.__expires_after = response_body['expiresAfter']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'includeTotal' in response_body:
            self.__include_total = response_body['includeTotal']
