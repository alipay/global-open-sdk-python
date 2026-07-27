import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayReceiptSendRequest(AlipayRequest):
    def __init__(self):
        super(AlipayReceiptSendRequest, self).__init__("/ams/api/v1/billing/receipt/send") 

        self.__receipt_id = None  # type: str
        self.__send_request_id = None  # type: str
        

    @property
    def receipt_id(self):
        """
        The receipt ID. Maximum length: 64 characters.
        """
        return self.__receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self.__receipt_id = value
    @property
    def send_request_id(self):
        """
        The send request id. Maximum length: 64 characters.
        """
        return self.__send_request_id

    @send_request_id.setter
    def send_request_id(self, value):
        self.__send_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "receipt_id") and self.receipt_id is not None:
            params['receiptId'] = self.receipt_id
        if hasattr(self, "send_request_id") and self.send_request_id is not None:
            params['sendRequestId'] = self.send_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'receiptId' in response_body:
            self.__receipt_id = response_body['receiptId']
        if 'sendRequestId' in response_body:
            self.__send_request_id = response_body['sendRequestId']
