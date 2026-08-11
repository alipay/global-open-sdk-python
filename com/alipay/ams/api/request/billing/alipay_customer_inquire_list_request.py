import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCustomerInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCustomerInquireListRequest, self).__init__("/ams/api/v1/billing/customer/inquireList") 

        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        self.__include_total = None  # type: bool
        self.__status = None  # type: str
        self.__email = None  # type: str
        self.__phone_no = None  # type: str
        self.__country_code = None  # type: str
        self.__gmt_create_end = None  # type: str
        self.__customer_id = None  # type: str
        self.__country = None  # type: [str]
        self.__email_prefix = None  # type: str
        self.__gmt_create_start = None  # type: str
        

    @property
    def starting_after(self):
        """
        Cursor for forward pagination - return customers created before this &#x60;customerId&#x60; (older items). Pass the &#x60;nextCursor&#x60; from the previous response. Mutually exclusive with &#x60;endingBefore&#x60;.
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        Cursor for backward pagination - return customers created after this &#x60;customerId&#x60; (newer items). Mutually exclusive with &#x60;startingAfter&#x60;.
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def limit(self):
        """
        Page size. Value range: 1-100. Default: 20.
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
    @property
    def status(self):
        """
        Filter by customer status. Allowed values: &#x60;ACTIVE&#x60;, &#x60;DELETED&#x60;. If not provided, returns customers of all statuses.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def email(self):
        """
        Filter by exact email address match. Maximum length: 256 characters.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def phone_no(self):
        """
        Filter by phone number (canonical). Cross-field constraint: when &#x60;phoneNo&#x60; is provided, &#x60;countryCode&#x60; is REQUIRED - omitting it returns &#x60;PARAM_ILLEGAL&#x60;.
        """
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, value):
        self.__phone_no = value
    @property
    def country_code(self):
        """
        ISO 3166-1 alpha-2 country code paired with &#x60;phoneNo&#x60;. Required when &#x60;phoneNo&#x60; is provided.
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value
    @property
    def gmt_create_end(self):
        """
        Inclusive end of the creation-timestamp range. Closed interval with &#x60;gmtCreateStart&#x60;.
        """
        return self.__gmt_create_end

    @gmt_create_end.setter
    def gmt_create_end(self, value):
        self.__gmt_create_end = value
    @property
    def customer_id(self):
        """
        Filter by exact customer ID (single exact match).
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def country(self):
        """
        Filter by billing country codes (ISO 3166-1 alpha-2) using SQL &#x60;IN&#x60; clause. Maximum size: 50 elements.
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value
    @property
    def email_prefix(self):
        """
        Filter by email LIKE prefix% (e.g. &#x60;\&quot;alice\&quot;&#x60; matches &#x60;alice@example.com&#x60;, &#x60;alice.smith@example.com&#x60;). Maximum length: 256 characters.
        """
        return self.__email_prefix

    @email_prefix.setter
    def email_prefix(self, value):
        self.__email_prefix = value
    @property
    def gmt_create_start(self):
        """
        Inclusive start of the creation-timestamp range. Closed interval with &#x60;gmtCreateEnd&#x60;.
        """
        return self.__gmt_create_start

    @gmt_create_start.setter
    def gmt_create_start(self, value):
        self.__gmt_create_start = value


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
        if hasattr(self, "include_total") and self.include_total is not None:
            params['includeTotal'] = self.include_total
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "phone_no") and self.phone_no is not None:
            params['phoneNo'] = self.phone_no
        if hasattr(self, "country_code") and self.country_code is not None:
            params['countryCode'] = self.country_code
        if hasattr(self, "gmt_create_end") and self.gmt_create_end is not None:
            params['gmtCreateEnd'] = self.gmt_create_end
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "country") and self.country is not None:
            params['country'] = self.country
        if hasattr(self, "email_prefix") and self.email_prefix is not None:
            params['emailPrefix'] = self.email_prefix
        if hasattr(self, "gmt_create_start") and self.gmt_create_start is not None:
            params['gmtCreateStart'] = self.gmt_create_start
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
        if 'includeTotal' in response_body:
            self.__include_total = response_body['includeTotal']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'phoneNo' in response_body:
            self.__phone_no = response_body['phoneNo']
        if 'countryCode' in response_body:
            self.__country_code = response_body['countryCode']
        if 'gmtCreateEnd' in response_body:
            self.__gmt_create_end = response_body['gmtCreateEnd']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'country' in response_body:
            self.__country = response_body['country']
        if 'emailPrefix' in response_body:
            self.__email_prefix = response_body['emailPrefix']
        if 'gmtCreateStart' in response_body:
            self.__gmt_create_start = response_body['gmtCreateStart']
