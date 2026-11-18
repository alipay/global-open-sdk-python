import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceInquireListRequest, self).__init__("/ams/api/v1/billing/invoice/inquireList") 

        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        self.__include_total = None  # type: bool
        self.__subscription_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__status = None  # type: str
        self.__reason = None  # type: str
        self.__start_date = None  # type: str
        self.__end_date = None  # type: str
        self.__min_amount = None  # type: Amount
        self.__max_amount = None  # type: Amount
        self.__exclude_draft = None  # type: bool
        

    @property
    def starting_after(self):
        """
        Cursor for forward pagination - return invoices after this &#x60;invoiceId&#x60;. Think of it as a bookmark: pass the &#x60;nextCursor&#x60; from the previous response to get the next batch of invoices. Mutually exclusive with &#x60;endingBefore&#x60; (both -&gt; &#x60;INVALID_PARAMETER&#x60;). When omitted, returns the first page (newest invoices first). Always use the LAST invoice&#39;s ID from the current page - using the first ID will skip records. Can be null (first page).
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        Cursor for backward pagination - return invoices before this &#x60;invoiceId&#x60;. Pass the first invoice&#39;s &#x60;invoiceId&#x60; from the current page to go back to the previous page. Mutually exclusive with &#x60;startingAfter&#x60;. Can be null (not used).
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def limit(self):
        """
        Maximum number of invoices per page. Integer value; range 1-100. Internally, &#x60;limit + 1&#x60; rows are fetched to determine &#x60;hasMore&#x60; - the extra row is not returned. Can be null (defaults to 20).
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def include_total(self):
        """
        Whether to include the &#x60;total&#x60; count of matching records in the response. When &#x60;true&#x60;, an additional &#x60;COUNT&#x60; query is executed. Default &#x60;false&#x60; to avoid the performance cost of counting when not needed. Can be null (defaults to false).
        """
        return self.__include_total

    @include_total.setter
    def include_total(self, value):
        self.__include_total = value
    @property
    def subscription_id(self):
        """
        Filter invoices by associated subscription ID. Returns only invoices linked to this subscription. Can be null (no filter).
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def customer_id(self):
        """
        Filter invoices by customer ID. Returns only invoices belonging to this customer. Can be null (no filter).
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def invoice_id(self):
        """
        Filter by exact invoice ID. Returns the single matching invoice if found. Format: &#x60;inv_&#x60; + 10-char alphanumeric. Unlike the planned &#x60;invoiceNumber&#x60; fuzzy search, this is an exact match. Can be null (no filter).
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def status(self):
        """
        Filter by invoice status. Allowed values: &#x60;DRAFT&#x60;, &#x60;OPEN&#x60;, &#x60;PAID&#x60;, &#x60;&#x60;UNCOLLECTIBLE&#x60;&#x60;, &#x60;VOID&#x60;. Can be null (no filter).
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def reason(self):
        """
        Filter by invoice reason. Allowed values: &#x60;SUBSCRIPTION_CREATION&#x60;, &#x60;SUBSCRIPTION_RECURRENCE&#x60;, &#x60;SUBSCRIPTION_UPDATE&#x60;. Can be null (no filter).
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def start_date(self):
        """
        Date range start for invoice creation time (ISO 8601 format, e.g., 2026-04-01T00:00:00+00:00). Can be null (no lower bound).
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value
    @property
    def end_date(self):
        """
        Date range end for invoice creation time (ISO 8601 format, e.g., 2026-04-30T23:59:59+00:00). Can be null (no upper bound).
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value
    @property
    def min_amount(self):
        """Gets the min_amount of this AlipayInvoiceInquireListRequest.
        
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value):
        self.__min_amount = value
    @property
    def max_amount(self):
        """Gets the max_amount of this AlipayInvoiceInquireListRequest.
        
        """
        return self.__max_amount

    @max_amount.setter
    def max_amount(self, value):
        self.__max_amount = value
    @property
    def exclude_draft(self):
        """
        When &#x60;true&#x60;, excludes &#x60;DRAFT&#x60; invoices from results. Can be null (defaults to false).
        """
        return self.__exclude_draft

    @exclude_draft.setter
    def exclude_draft(self, value):
        self.__exclude_draft = value


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
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
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
        if hasattr(self, "exclude_draft") and self.exclude_draft is not None:
            params['excludeDraft'] = self.exclude_draft
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
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'status' in response_body:
            self.__status = response_body['status']
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
        if 'excludeDraft' in response_body:
            self.__exclude_draft = response_body['excludeDraft']
