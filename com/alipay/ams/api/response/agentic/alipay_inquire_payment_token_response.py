import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.agentic_payment_token import AgenticPaymentToken



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquirePaymentTokenResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payment_token = None  # type: AgenticPaymentToken
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquirePaymentTokenResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payment_token(self):
        """Gets the payment_token of this AlipayInquirePaymentTokenResponse.
        
        """
        return self.__payment_token

    @payment_token.setter
    def payment_token(self, value):
        self.__payment_token = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payment_token") and self.payment_token is not None:
            params['paymentToken'] = self.payment_token
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquirePaymentTokenResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'paymentToken' in response_body:
            self.__payment_token = AgenticPaymentToken()
            self.__payment_token.parse_rsp_body(response_body['paymentToken'])
