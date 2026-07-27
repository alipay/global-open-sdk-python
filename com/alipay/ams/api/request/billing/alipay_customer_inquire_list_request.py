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
        self.__mobile_no = None  # type: str
        

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
    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def email(self):
        """
        The email address. Maximum length: 256 characters.
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def mobile_no(self):
        """
        The mobile phone number. Maximum length: 32 characters.
        """
        return self.__mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self.__mobile_no = value


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
        if hasattr(self, "mobile_no") and self.mobile_no is not None:
            params['mobileNo'] = self.mobile_no
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
        if 'mobileNo' in response_body:
            self.__mobile_no = response_body['mobileNo']
