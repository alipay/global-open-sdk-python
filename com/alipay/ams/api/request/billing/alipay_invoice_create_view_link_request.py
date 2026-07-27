import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceCreateViewLinkRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceCreateViewLinkRequest, self).__init__("/ams/api/v1/billing/invoice/createViewLink") 

        self.__invoice_id = None  # type: str
        self.__invoice_request_id = None  # type: str
        self.__link_expiry_days = None  # type: int
        

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
    @property
    def link_expiry_days(self):
        """
        The link expiry days.
        """
        return self.__link_expiry_days

    @link_expiry_days.setter
    def link_expiry_days(self, value):
        self.__link_expiry_days = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "invoice_request_id") and self.invoice_request_id is not None:
            params['invoiceRequestId'] = self.invoice_request_id
        if hasattr(self, "link_expiry_days") and self.link_expiry_days is not None:
            params['linkExpiryDays'] = self.link_expiry_days
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'invoiceRequestId' in response_body:
            self.__invoice_request_id = response_body['invoiceRequestId']
        if 'linkExpiryDays' in response_body:
            self.__link_expiry_days = response_body['linkExpiryDays']
