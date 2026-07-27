import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceInquireDetailsRequest, self).__init__("/ams/api/v1/billing/invoice/inquireDetails") 

        self.__invoice_id = None  # type: str
        self.__invoice_request_id = None  # type: str
        

    @property
    def invoice_id(self):
        """
        The invoice ID. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def invoice_request_id(self):
        """
        The invoice request id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__invoice_request_id

    @invoice_request_id.setter
    def invoice_request_id(self, value):
        self.__invoice_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "invoice_request_id") and self.invoice_request_id is not None:
            params['invoiceRequestId'] = self.invoice_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'invoiceRequestId' in response_body:
            self.__invoice_request_id = response_body['invoiceRequestId']
