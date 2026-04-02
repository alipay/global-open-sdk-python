import json
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class CreateDirectPaymentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__payment_id = None  # type: str
        self.__payment_request_id = None  # type: str
        self.__pay_to_method = None  # type: PaymentMethod
        self.__pay_from_amount = None  # type: Amount
        self.__pay_to_amount = None  # type: Amount
        self.__payment_time = None  # type: str
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def payment_id(self):
        """Gets the payment_id of this CreateDirectPaymentResponse.
        
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def payment_request_id(self):
        """Gets the payment_request_id of this CreateDirectPaymentResponse.
        
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def pay_to_method(self):
        """Gets the pay_to_method of this CreateDirectPaymentResponse.
        
        """
        return self.__pay_to_method

    @pay_to_method.setter
    def pay_to_method(self, value):
        self.__pay_to_method = value
    @property
    def pay_from_amount(self):
        """Gets the pay_from_amount of this CreateDirectPaymentResponse.
        
        """
        return self.__pay_from_amount

    @pay_from_amount.setter
    def pay_from_amount(self, value):
        self.__pay_from_amount = value
    @property
    def pay_to_amount(self):
        """Gets the pay_to_amount of this CreateDirectPaymentResponse.
        
        """
        return self.__pay_to_amount

    @pay_to_amount.setter
    def pay_to_amount(self, value):
        self.__pay_to_amount = value
    @property
    def payment_time(self):
        """Gets the payment_time of this CreateDirectPaymentResponse.
        
        """
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
    @property
    def result(self):
        """Gets the result of this CreateDirectPaymentResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "pay_to_method") and self.pay_to_method is not None:
            params['payToMethod'] = self.pay_to_method
        if hasattr(self, "pay_from_amount") and self.pay_from_amount is not None:
            params['payFromAmount'] = self.pay_from_amount
        if hasattr(self, "pay_to_amount") and self.pay_to_amount is not None:
            params['payToAmount'] = self.pay_to_amount
        if hasattr(self, "payment_time") and self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(CreateDirectPaymentResponse, self).parse_rsp_body(response_body)
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'payToMethod' in response_body:
            self.__pay_to_method = PaymentMethod()
            self.__pay_to_method.parse_rsp_body(response_body['payToMethod'])
        if 'payFromAmount' in response_body:
            self.__pay_from_amount = Amount()
            self.__pay_from_amount.parse_rsp_body(response_body['payFromAmount'])
        if 'payToAmount' in response_body:
            self.__pay_to_amount = Amount()
            self.__pay_to_amount.parse_rsp_body(response_body['payToAmount'])
        if 'paymentTime' in response_body:
            self.__payment_time = response_body['paymentTime']
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
