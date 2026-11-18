import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayReceiptInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayReceiptInquireListRequest, self).__init__("/ams/api/v1/billing/receipt/inquireList") 

        self.__starting_after = None  # type: str
        self.__ending_before = None  # type: str
        self.__limit = None  # type: int
        self.__include_total = None  # type: bool
        self.__customer_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__status = None  # type: str
        self.__receipt_type = None  # type: str
        self.__start_date = None  # type: str
        self.__end_date = None  # type: str
        

    @property
    def starting_after(self):
        """
        Cursor for forward pagination - return receipts after this &#x60;receiptId&#x60;. Think of it as a bookmark: pass the &#x60;nextCursor&#x60; from the previous response to get the next batch of receipts. Mutually exclusive with &#x60;endingBefore&#x60; (both -&gt; &#x60;PARAM_ILLEGAL&#x60;). When omitted, returns the first page (newest receipts first). Always use the LAST receipt&#39;s ID from the current page - using the first ID will skip records. Can be null (first page).
        """
        return self.__starting_after

    @starting_after.setter
    def starting_after(self, value):
        self.__starting_after = value
    @property
    def ending_before(self):
        """
        Cursor for backward pagination - return receipts before this &#x60;receiptId&#x60;. Pass the first receipt&#39;s &#x60;receiptId&#x60; from the current page to go back to the previous page. Mutually exclusive with &#x60;startingAfter&#x60;. Can be null (not used).
        """
        return self.__ending_before

    @ending_before.setter
    def ending_before(self, value):
        self.__ending_before = value
    @property
    def limit(self):
        """
        Maximum number of receipts per page. Internally, &#x60;limit + 1&#x60; rows are fetched to determine &#x60;hasMore&#x60; - the extra row is not returned. Can be null (defaults to 20).
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def include_total(self):
        """
        Whether to include the &#x60;total&#x60; count of matching records in the response. &#x60;true&#x60; &#x3D; include total count (an additional &#x60;COUNT&#x60; query is executed); &#x60;false&#x60; or omitted &#x3D; exclude total count (better performance). Can be null (defaults to false).
        """
        return self.__include_total

    @include_total.setter
    def include_total(self, value):
        self.__include_total = value
    @property
    def customer_id(self):
        """
        Filter by customer ID. Returns only receipts belonging to this customer. Can be null (no filter).
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def invoice_id(self):
        """
        Filter by associated invoice ID. Returns receipts linked to this invoice. Can be null (no filter).
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def subscription_id(self):
        """
        Filter by associated subscription ID. Returns receipts linked to this subscription. Can be null (no filter).
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def status(self):
        """
        Filter by receipt status. Allowed values: &#x60;ACTIVE&#x60; (payment receipt with no refunds), &#x60;PARTIALLY_REFUNDED&#x60; (some amount refunded), &#x60;REFUNDED&#x60; (fully refunded). Unknown status values are silently ignored (treated as no filter for that value). Can be null (no filter).
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def receipt_type(self):
        """
        Filter by receipt type. Allowed values: &#x60;PAYMENT&#x60; (receipt for a payment), &#x60;REFUND&#x60; (receipt for a refund). Unknown type values are silently ignored (treated as no filter for that value). Can be null (no filter).
        """
        return self.__receipt_type

    @receipt_type.setter
    def receipt_type(self, value):
        self.__receipt_type = value
    @property
    def start_date(self):
        """
        Date range start for receipt creation time (ISO 8601 format, e.g., &#x60;2026-04-01T00:00:00+00:00&#x60;). Can be null (no lower bound).
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value
    @property
    def end_date(self):
        """
        Date range end for receipt creation time (ISO 8601 format, e.g., &#x60;2026-04-30T23:59:59+00:00&#x60;). Can be null (no upper bound).
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value


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
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "receipt_type") and self.receipt_type is not None:
            params['receiptType'] = self.receipt_type
        if hasattr(self, "start_date") and self.start_date is not None:
            params['startDate'] = self.start_date
        if hasattr(self, "end_date") and self.end_date is not None:
            params['endDate'] = self.end_date
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
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'receiptType' in response_body:
            self.__receipt_type = response_body['receiptType']
        if 'startDate' in response_body:
            self.__start_date = response_body['startDate']
        if 'endDate' in response_body:
            self.__end_date = response_body['endDate']
