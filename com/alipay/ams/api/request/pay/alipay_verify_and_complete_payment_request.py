import json
from com.alipay.ams.api.model.verify_method import VerifyMethod



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayVerifyAndCompletePaymentRequest(AlipayRequest):
    def __init__(self):
        super(AlipayVerifyAndCompletePaymentRequest, self).__init__("/ams/api/v1/payments/verifyAndCompletePayment") 

        self.__verify_method = None  # type: VerifyMethod
        self.__verify_request_id = None  # type: str
        self.__payment_id = None  # type: str
        

    @property
    def verify_method(self):
        """Gets the verify_method of this AlipayVerifyAndCompletePaymentRequest.
        
        """
        return self.__verify_method

    @verify_method.setter
    def verify_method(self, value):
        self.__verify_method = value
    @property
    def verify_request_id(self):
        """Gets the verify_request_id of this AlipayVerifyAndCompletePaymentRequest.
        
        """
        return self.__verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self.__verify_request_id = value
    @property
    def payment_id(self):
        """Gets the payment_id of this AlipayVerifyAndCompletePaymentRequest.
        
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "verify_method") and self.verify_method is not None:
            params['verifyMethod'] = self.verify_method
        if hasattr(self, "verify_request_id") and self.verify_request_id is not None:
            params['verifyRequestId'] = self.verify_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'verifyMethod' in response_body:
            self.__verify_method = VerifyMethod()
            self.__verify_method.parse_rsp_body(response_body['verifyMethod'])
        if 'verifyRequestId' in response_body:
            self.__verify_request_id = response_body['verifyRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
