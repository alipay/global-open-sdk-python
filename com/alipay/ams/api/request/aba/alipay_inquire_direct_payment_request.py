import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireDirectPaymentRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireDirectPaymentRequest, self).__init__("/ams/aba/funds/inquireDirectPayment") 

        self.__payment_id = None  # type: str
        self.__payment_request_id = None  # type: str
        

    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment. paymentRequestId and paymentId cannot both be null. A one-to-one correspondence between paymentId and paymentRequestId exists. If both paymentRequestId and paymentId are specified, paymentId takes precedence.  More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def payment_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a payment request. paymentRequestId and paymentId cannot both be null. Special characters are not supported. If both paymentRequestId and paymentId are specified, paymentId takes precedence.  More information:  Maximum length: 64 characters
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
