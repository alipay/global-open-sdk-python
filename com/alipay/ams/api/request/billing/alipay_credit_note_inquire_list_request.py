import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditNoteInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditNoteInquireListRequest, self).__init__("/ams/api/v1/billing/creditNote/inquireList") 

        self.__invoice_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__status = None  # type: str
        self.__type = None  # type: str
        self.__reason = None  # type: str
        self.__start_date = None  # type: str
        self.__end_date = None  # type: str
        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        self.__include_total = None  # type: bool
        

    @property
    def invoice_id(self):
        """
        The invoice ID. Maximum length: 64 characters.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
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
    def status(self):
        """
        The current status. Maximum length: 128 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def type(self):
        """
        The type. Maximum length: 32 characters.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def reason(self):
        """
        The reason for the status change. Maximum length: 32 characters.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def start_date(self):
        """
        The start date. Maximum length: 29 characters.
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value
    @property
    def end_date(self):
        """
        The end date. Maximum length: 29 characters.
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value
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
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "start_date") and self.start_date is not None:
            params['startDate'] = self.start_date
        if hasattr(self, "end_date") and self.end_date is not None:
            params['endDate'] = self.end_date
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
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'startDate' in response_body:
            self.__start_date = response_body['startDate']
        if 'endDate' in response_body:
            self.__end_date = response_body['endDate']
        if 'startingAfter' in response_body:
            self.__starting_after = response_body['startingAfter']
        if 'endingBefore' in response_body:
            self.__ending_before = response_body['endingBefore']
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'includeTotal' in response_body:
            self.__include_total = response_body['includeTotal']
