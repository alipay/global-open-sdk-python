import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceSendRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceSendRequest, self).__init__("/ams/api/v1/billing/invoice/send") 

        self.__invoice_id = None  # type: str
        self.__cc_emails = None  # type: [str]
        self.__internal_note = None  # type: str
        self.__include_payment_link = None  # type: bool
        

    @property
    def invoice_id(self):
        """
        Invoice ID to send. Must be in OPEN or PAID status and belong to the requesting merchant. Validated before any email dispatch. Cannot be null.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def cc_emails(self):
        """
        CC email addresses to include in the invoice email. Optional; when omitted, only the primary customer email is used.
        """
        return self.__cc_emails

    @cc_emails.setter
    def cc_emails(self, value):
        self.__cc_emails = value
    @property
    def internal_note(self):
        """
        Internal note attached to the send request for merchant reference. Not visible to the customer.
        """
        return self.__internal_note

    @internal_note.setter
    def internal_note(self, value):
        self.__internal_note = value
    @property
    def include_payment_link(self):
        """
        Whether to include the payment link in the invoice email. Default: &#x60;true&#x60;. When &#x60;false&#x60;, the email is sent without a payment link.
        """
        return self.__include_payment_link

    @include_payment_link.setter
    def include_payment_link(self, value):
        self.__include_payment_link = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "cc_emails") and self.cc_emails is not None:
            params['ccEmails'] = self.cc_emails
        if hasattr(self, "internal_note") and self.internal_note is not None:
            params['internalNote'] = self.internal_note
        if hasattr(self, "include_payment_link") and self.include_payment_link is not None:
            params['includePaymentLink'] = self.include_payment_link
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'ccEmails' in response_body:
            self.__cc_emails = response_body['ccEmails']
        if 'internalNote' in response_body:
            self.__internal_note = response_body['internalNote']
        if 'includePaymentLink' in response_body:
            self.__include_payment_link = response_body['includePaymentLink']
