import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceVoidRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceVoidRequest, self).__init__("/ams/api/v1/billing/invoice/void") 

        self.__invoice_id = None  # type: str
        self.__invoice_note = None  # type: str
        

    @property
    def invoice_id(self):
        """
        Invoice ID to void. Must belong to the requesting merchant. Format: &#x60;inv_&#x60; + 10-char alphanumeric. Validated before any state transition. Cannot be null.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def invoice_note(self):
        """
        Optional note attached to the invoice for this void action. Stored as an entry in the &#x60;invoiceNotes&#x60; array in the invoice metadata with &#x60;action&#x3D;void&#x60;. Enables merchants to attach contextual notes (e.g., \&quot;Voided due to customer request\&quot;) to the invoice audit trail. Can be null (defaults to null - no note provided).
        """
        return self.__invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self.__invoice_note = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "invoice_note") and self.invoice_note is not None:
            params['invoiceNote'] = self.invoice_note
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'invoiceNote' in response_body:
            self.__invoice_note = response_body['invoiceNote']
