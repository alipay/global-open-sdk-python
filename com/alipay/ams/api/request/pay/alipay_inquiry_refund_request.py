import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquiryRefundRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquiryRefundRequest, self).__init__("/ams/api/v1/payments/inquiryRefund") 

        self.__refund_request_id = None  # type: str
        self.__refund_id = None  # type: str
        self.__merchant_account_id = None  # type: str
        

    @property
    def refund_request_id(self):
        """
        The unique ID assigned by a merchant to identify a refund request. refundRequestId and refundId cannot both be null. Special characters are not supported. If both refundRequestId and refundId are specified, refundId takes precedence.  More information:  Maximum length: 64 characters
        """
        return self.__refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self.__refund_request_id = value
    @property
    def refund_id(self):
        """
        The unique ID assigned by Antom to identify a refund. refundRequestId and refundId cannot both be null. A one-to-one correspondence between refundId and refundRequestId exists. If both refundRequestId and refundId are specified, refundId takes precedence.  More information:  Maximum length: 64 characters
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value
    @property
    def merchant_account_id(self):
        """Gets the merchant_account_id of this AlipayInquiryRefundRequest.
        
        """
        return self.__merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, value):
        self.__merchant_account_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "refund_request_id") and self.refund_request_id is not None:
            params['refundRequestId'] = self.refund_request_id
        if hasattr(self, "refund_id") and self.refund_id is not None:
            params['refundId'] = self.refund_id
        if hasattr(self, "merchant_account_id") and self.merchant_account_id is not None:
            params['merchantAccountId'] = self.merchant_account_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'refundRequestId' in response_body:
            self.__refund_request_id = response_body['refundRequestId']
        if 'refundId' in response_body:
            self.__refund_id = response_body['refundId']
        if 'merchantAccountId' in response_body:
            self.__merchant_account_id = response_body['merchantAccountId']
