import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayReceiptInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayReceiptInquireDetailsRequest, self).__init__("/ams/api/v1/billing/receipt/inquireDetails") 

        self.__receipt_id = None  # type: str
        self.__invoice_id = None  # type: str
        

    @property
    def receipt_id(self):
        """
        Receipt ID. When provided, looks up the receipt directly. Can be null (when &#x60;invoiceId&#x60; is provided instead).
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    @property
    def invoice_id(self):
        """
        Alternative lookup by associated invoice ID. When provided, finds the receipt associated with this invoice. Can be null (when &#x60;receiptId&#x60; is provided instead).
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "receipt_id") and self.receipt_id is not None:
            params['receiptId'] = self.receipt_id
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'receiptId' in response_body:
            self.__receipt_id = response_body['receiptId']
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
