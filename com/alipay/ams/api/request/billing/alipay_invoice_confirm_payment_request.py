import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceConfirmPaymentRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceConfirmPaymentRequest, self).__init__("/ams/api/v1/billing/invoice/confirmPayment") 

        self.__invoice_id = None  # type: str
        self.__confirmation_type = None  # type: str
        self.__payment_method = None  # type: str
        self.__reference = None  # type: str
        self.__auto_send = None  # type: bool
        self.__invoice_note = None  # type: str
        self.__cc_emails = None  # type: [str]
        

    @property
    def invoice_id(self):
        """
        Invoice ID to confirm payment for. Must be in OPEN or UNCOLLECTIBLE status and belong to the requesting merchant. Validated before any state transition. Cannot be null.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def confirmation_type(self):
        """
        Payment confirmation type. Currently only &#x60;OFFLINE&#x60; is supported - indicates a manual offline payment (bank transfer, cash, check) was received by the merchant. This field is an extensibility point for future confirmation types (e.g., &#x60;CREDIT_NOTE_OFFSET&#x60;). Cannot be null. Allowed values: &#x60;OFFLINE&#x60;. Note: Future values may be added; merchants should handle unknown values gracefully.
        """
        return self.__confirmation_type

    @confirmation_type.setter
    def confirmation_type(self, value):
        self.__confirmation_type = value
    @property
    def payment_method(self):
        """
        Offline payment method used by the customer. Must be one of: &#x60;BANK_TRANSFER&#x60; - payment received via bank/wire transfer; &#x60;CASH&#x60; - cash payment received in person; &#x60;CHECK&#x60; - payment by physical check; &#x60;WIRE_TRANSFER&#x60; - domestic or international wire transfer; &#x60;OTHER&#x60; - any other offline payment method not listed above. Validated against &#x60;OfflinePaymentMethodEnum&#x60; when provided. When not provided or blank, defaults to &#x60;OTHER&#x60;. Helps merchants categorize payments for reconciliation. Note: Future enum values may be added; merchants should handle unknown values as &#x60;OTHER&#x60;. Can be null.
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def reference(self):
        """
        Merchant-supplied payment reference for audit trail (e.g., bank transfer number, check number). Stored on the payment record for reconciliation. Can be null.
        """
        return self.__reference

    @reference.setter
    def reference(self, value):
        self.__reference = value
    @property
    def auto_send(self):
        """
        Whether to automatically send the receipt email to the customer after successful payment confirmation. &#x60;true&#x60; &#x3D; send receipt email; &#x60;false&#x60; &#x3D; do not send; not set &#x3D; treat as &#x60;false&#x60;. Can be null (defaults to false).
        """
        return self.__auto_send

    @auto_send.setter
    def auto_send(self, value):
        self.__auto_send = value
    @property
    def invoice_note(self):
        """
        Optional note attached to the invoice for this payment confirmation action. Stored as an entry in the &#x60;invoiceNotes&#x60; array in the invoice metadata with &#x60;action&#x3D;paid&#x60;. Enables merchants to attach contextual notes (e.g., \&quot;Payment received via bank transfer\&quot;) to the invoice audit trail. Can be null (defaults to null - no note provided).
        """
        return self.__invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self.__invoice_note = value
    @property
    def cc_emails(self):
        """
        CC email addresses for receipt notification. Optional. When &#x60;autoSend&#x60; is true, the receipt email is also sent to these addresses. Can be null.
        """
        return self.__cc_emails

    @cc_emails.setter
    def cc_emails(self, value):
        self.__cc_emails = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "confirmation_type") and self.confirmation_type is not None:
            params['confirmationType'] = self.confirmation_type
        if hasattr(self, "payment_method") and self.payment_method is not None:
            params['paymentMethod'] = self.payment_method
        if hasattr(self, "reference") and self.reference is not None:
            params['reference'] = self.reference
        if hasattr(self, "auto_send") and self.auto_send is not None:
            params['autoSend'] = self.auto_send
        if hasattr(self, "invoice_note") and self.invoice_note is not None:
            params['invoiceNote'] = self.invoice_note
        if hasattr(self, "cc_emails") and self.cc_emails is not None:
            params['ccEmails'] = self.cc_emails
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'confirmationType' in response_body:
            self.__confirmation_type = response_body['confirmationType']
        if 'paymentMethod' in response_body:
            self.__payment_method = response_body['paymentMethod']
        if 'reference' in response_body:
            self.__reference = response_body['reference']
        if 'autoSend' in response_body:
            self.__auto_send = response_body['autoSend']
        if 'invoiceNote' in response_body:
            self.__invoice_note = response_body['invoiceNote']
        if 'ccEmails' in response_body:
            self.__cc_emails = response_body['ccEmails']
