import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayBillingSubscriptionInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayBillingSubscriptionInquireListRequest, self).__init__("/ams/api/v1/billing/subscription/inquireList") 

        self.__status = None  # type: str
        self.__customer_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__gmt_create_start = None  # type: str
        self.__gmt_create_end = None  # type: str
        self.__sort_order = None  # type: str
        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        

    @property
    def status(self):
        """
        Filters subscriptions by status. To provide multiple values, use a comma-separated string such as ACTIVE,PAUSED. Up to eight values are supported. Valid values are INCOMPLETE, TRIALING, ACTIVE, PAST_DUE, PAUSED, CANCELLED, TERMINATED, and UNPAID. Each status value has a maximum length of 20 characters.
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
    def subscription_id(self):
        """
        Filters by an exact subscription ID. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def gmt_create_start(self):
        """
        Filters subscriptions whose &#x60;createTime&#x60; is greater than or equal to this ISO 8601 date-time.
        """
        return self.__gmt_create_start

    @gmt_create_start.setter
    def gmt_create_start(self, value):
        self.__gmt_create_start = value
    @property
    def gmt_create_end(self):
        """
        Filters subscriptions whose &#x60;createTime&#x60; is less than or equal to this ISO 8601 date-time.
        """
        return self.__gmt_create_end

    @gmt_create_end.setter
    def gmt_create_end(self, value):
        self.__gmt_create_end = value
    @property
    def sort_order(self):
        """
        The creation-time sort order. Valid values are ASC and DESC. The default value is DESC. Maximum length: 4 characters.
        """
        return self.__sort_order

    @sort_order.setter
    def sort_order(self, value):
        self.__sort_order = value
    @property
    def starting_after(self):
        """
        The forward-pagination cursor. This field is mutually exclusive with &#x60;endingBefore&#x60;. Maximum length: 64 characters.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        The backward-pagination cursor. This field is mutually exclusive with &#x60;startingAfter&#x60;. Maximum length: 64 characters.
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def limit(self):
        """
        The maximum number of results per page. Value range: 1-100. The default value is 20.
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "gmt_create_start") and self.gmt_create_start is not None:
            params['gmtCreateStart'] = self.gmt_create_start
        if hasattr(self, "gmt_create_end") and self.gmt_create_end is not None:
            params['gmtCreateEnd'] = self.gmt_create_end
        if hasattr(self, "sort_order") and self.sort_order is not None:
            params['sortOrder'] = self.sort_order
        if hasattr(self, "starting_after") and self.starting_after is not None:
            params['startingAfter'] = self.starting_after
        if hasattr(self, "ending_before") and self.ending_before is not None:
            params['endingBefore'] = self.ending_before
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'gmtCreateStart' in response_body:
            self.__gmt_create_start = response_body['gmtCreateStart']
        if 'gmtCreateEnd' in response_body:
            self.__gmt_create_end = response_body['gmtCreateEnd']
        if 'sortOrder' in response_body:
            self.__sort_order = response_body['sortOrder']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
        if 'limit' in response_body:
            self.__limit = response_body['limit']
