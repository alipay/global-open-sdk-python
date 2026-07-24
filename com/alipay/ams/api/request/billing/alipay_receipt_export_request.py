import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayReceiptExportRequest(AlipayRequest):
    def __init__(self):
        super(AlipayReceiptExportRequest, self).__init__("/ams/api/v1/billing/receipt/export") 

        self.__limit = None  # type: int
        self.__status = None  # type: str
        self.__receipt_type = None  # type: str
        self.__invoice_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__start_date = None  # type: str
        self.__end_date = None  # type: str
        self.__receipt_ids = None  # type: [str]
        

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
    def status(self):
        """
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def receipt_type(self):
        """
        The receipt type. Maximum length: 16 characters.
        """
        return self.__receipt_type

    @receipt_type.setter
    def receipt_type(self, value):
        self.__receipt_type = value
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
    def subscription_id(self):
        """
        The subscription ID. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
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
    def start_date(self):
        """
        The start date. Maximum length: 24 characters.
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value
    @property
    def end_date(self):
        """
        The end date. Maximum length: 24 characters.
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value
    @property
    def receipt_ids(self):
        """
        The receipt ids.
        """
        return self.__receipt_ids

    @receipt_ids.setter
    def receipt_ids(self, value):
        self.__receipt_ids = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "receipt_type") and self.receipt_type is not None:
            params['receiptType'] = self.receipt_type
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "start_date") and self.start_date is not None:
            params['startDate'] = self.start_date
        if hasattr(self, "end_date") and self.end_date is not None:
            params['endDate'] = self.end_date
        if hasattr(self, "receipt_ids") and self.receipt_ids is not None:
            params['receiptIds'] = self.receipt_ids
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'receiptType' in response_body:
            self.__receipt_type = response_body['receiptType']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'startDate' in response_body:
            self.__start_date = response_body['startDate']
        if 'endDate' in response_body:
            self.__end_date = response_body['endDate']
        if 'receiptIds' in response_body:
            self.__receipt_ids = response_body['receiptIds']
