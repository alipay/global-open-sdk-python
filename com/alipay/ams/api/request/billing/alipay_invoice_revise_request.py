import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceReviseRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceReviseRequest, self).__init__("/ams/api/v1/billing/invoice/revise") 

        self.__invoice_id = None  # type: str
        self.__invoice_request_id = None  # type: str
        self.__invoice_revision_request_id = None  # type: str
        self.__void = None  # type: bool
        self.__invoice_notify_url = None  # type: str
        

    @property
    def invoice_id(self):
        """
        Invoice ID of the DRAFT or OPEN invoice to revise. Format: &#x60;inv_&#x60; + 10-char alphanumeric. Can be null if &#x60;invoiceRequestId&#x60; is provided.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def invoice_request_id(self):
        """
        Alternative lookup by idempotency key. Can be null if &#x60;invoiceId&#x60; is provided.
        """
        return self.__invoice_request_id

    @invoice_request_id.setter
    def invoice_request_id(self, value):
        self.__invoice_request_id = value
    @property
    def invoice_revision_request_id(self):
        """
        Idempotency key for the revision operation. Stored as &#x60;invoiceRequestId&#x60; on the new invoice. Backed by UK &#x60;(merchant_id, invoice_revision_request_id)&#x60;. Accepts alphanumeric, hyphens, underscores. Cannot be null.
        """
        return self.__invoice_revision_request_id

    @invoice_revision_request_id.setter
    def invoice_revision_request_id(self, value):
        self.__invoice_revision_request_id = value
    @property
    def void(self):
        """
        Controls the revision mode: &#x60;true&#x60; &#x3D; void original invoice + create new (atomic); &#x60;false&#x60; &#x3D; clone original without voiding (original untouched). Cannot be null.
        """
        return self.__void

    @void.setter
    def void(self, value):
        self.__void = value
    @property
    def invoice_notify_url(self):
        """
        Updated HTTPS URL that receives invoice payment-status notifications for the revised invoice. Maximum length: 2048 characters.
        """
        return self.__invoice_notify_url

    @invoice_notify_url.setter
    def invoice_notify_url(self, value):
        self.__invoice_notify_url = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "invoice_request_id") and self.invoice_request_id is not None:
            params['invoiceRequestId'] = self.invoice_request_id
        if hasattr(self, "invoice_revision_request_id") and self.invoice_revision_request_id is not None:
            params['invoiceRevisionRequestId'] = self.invoice_revision_request_id
        if hasattr(self, "void") and self.void is not None:
            params['void'] = self.void
        if hasattr(self, "invoice_notify_url") and self.invoice_notify_url is not None:
            params['invoiceNotifyUrl'] = self.invoice_notify_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'invoiceRequestId' in response_body:
            self.__invoice_request_id = response_body['invoiceRequestId']
        if 'invoiceRevisionRequestId' in response_body:
            self.__invoice_revision_request_id = response_body['invoiceRevisionRequestId']
        if 'void' in response_body:
            self.__void = response_body['void']
        if 'invoiceNotifyUrl' in response_body:
            self.__invoice_notify_url = response_body['invoiceNotifyUrl']
