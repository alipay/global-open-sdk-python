import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceExportRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceExportRequest, self).__init__("/ams/api/v1/billing/invoice/export") 

        self.__limit = None  # type: int
        self.__customer_id = None  # type: str
        self.__status = None  # type: str
        self.__subscription_id = None  # type: str
        self.__invoice_ids = None  # type: [str]
        self.__reason = None  # type: str
        self.__start_date = None  # type: str
        self.__end_date = None  # type: str
        self.__min_amount = None  # type: Amount
        self.__max_amount = None  # type: Amount
        

    @property
    def limit(self):
        """
        The limit. Note: See documentation for details.
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
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
        The current status. Maximum length: 16 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
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
    def invoice_ids(self):
        """
        The invoice ids.
        """
        return self.__invoice_ids

    @invoice_ids.setter
    def invoice_ids(self, value):
        self.__invoice_ids = value
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
    def min_amount(self):
        """Gets the min_amount of this AlipayInvoiceExportRequest.
        
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value):
        self.__min_amount = value
    @property
    def max_amount(self):
        """Gets the max_amount of this AlipayInvoiceExportRequest.
        
        """
        return self.__max_amount

    @max_amount.setter
    def max_amount(self, value):
        self.__max_amount = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "limit") and self.limit is not None:
            params['limit'] = self.limit
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "invoice_ids") and self.invoice_ids is not None:
            params['invoiceIds'] = self.invoice_ids
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "start_date") and self.start_date is not None:
            params['startDate'] = self.start_date
        if hasattr(self, "end_date") and self.end_date is not None:
            params['endDate'] = self.end_date
        if hasattr(self, "min_amount") and self.min_amount is not None:
            params['minAmount'] = self.min_amount
        if hasattr(self, "max_amount") and self.max_amount is not None:
            params['maxAmount'] = self.max_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'limit' in response_body:
            self.__limit = response_body['limit']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'invoiceIds' in response_body:
            self.__invoice_ids = response_body['invoiceIds']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'startDate' in response_body:
            self.__start_date = response_body['startDate']
        if 'endDate' in response_body:
            self.__end_date = response_body['endDate']
        if 'minAmount' in response_body:
            self.__min_amount = Amount()
            self.__min_amount.parse_rsp_body(response_body['minAmount'])
        if 'maxAmount' in response_body:
            self.__max_amount = Amount()
            self.__max_amount.parse_rsp_body(response_body['maxAmount'])
