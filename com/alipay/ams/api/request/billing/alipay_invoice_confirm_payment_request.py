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
    def confirmation_type(self):
        """
        The confirmation type. Maximum length: 32 characters.
        """
        return self.__confirmation_type

    @confirmation_type.setter
    def confirmation_type(self, value):
        self.__confirmation_type = value
    @property
    def payment_method(self):
        """
        The payment method. Maximum length: 32 characters.
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value
    @property
    def reference(self):
        """
        The reference. Maximum length: 256 characters.
        """
        return self.__reference

    @reference.setter
    def reference(self, value):
        self.__reference = value
    @property
    def auto_send(self):
        """
        Indicates whether to automatically send the notification.
        """
        return self.__auto_send

    @auto_send.setter
    def auto_send(self, value):
        self.__auto_send = value
    @property
    def invoice_note(self):
        """
        The invoice note. Maximum length: 512 characters.
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
