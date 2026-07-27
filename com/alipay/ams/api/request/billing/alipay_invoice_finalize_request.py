import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceFinalizeRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceFinalizeRequest, self).__init__("/ams/api/v1/billing/invoice/finalize") 

        self.__invoice_id = None  # type: str
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
        if 'autoSend' in response_body:
            self.__auto_send = response_body['autoSend']
        if 'invoiceNote' in response_body:
            self.__invoice_note = response_body['invoiceNote']
