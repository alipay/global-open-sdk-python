import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayReceiptSendRequest(AlipayRequest):
    def __init__(self):
        super(AlipayReceiptSendRequest, self).__init__("/ams/api/v1/billing/receipt/send") 

        self.__receipt_id = None  # type: str
        self.__cc_emails = None  # type: [str]
        

    @property
    def receipt_id(self):
        """
        Receipt ID to send. Must belong to the merchant. Cannot be null.
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    @property
    def cc_emails(self):
        """
        CC email addresses to receive a copy of the receipt email in addition to the customer&#39;s registered email. Can be null.
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
        if hasattr(self, "receipt_id") and self.receipt_id is not None:
            params['receiptId'] = self.receipt_id
        if hasattr(self, "cc_emails") and self.cc_emails is not None:
            params['ccEmails'] = self.cc_emails
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'receiptId' in response_body:
            self.__receipt_id = response_body['receiptId']
        if 'ccEmails' in response_body:
            self.__cc_emails = response_body['ccEmails']
