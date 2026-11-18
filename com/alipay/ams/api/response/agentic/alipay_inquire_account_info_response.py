import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.agentic_bound_payment_method import AgenticBoundPaymentMethod



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireAccountInfoResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payment_methods = None  # type: [AgenticBoundPaymentMethod]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireAccountInfoResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payment_methods(self):
        """
        Complete supported asset list, required when result.resultStatus&#x3D;S. No silent truncation or pagination. Returns [] when no assets match. Subject to the total AMS response-size limit.
        """
        return self.__payment_methods

    @payment_methods.setter
    def payment_methods(self, value):
        self.__payment_methods = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payment_methods") and self.payment_methods is not None:
            params['paymentMethods'] = self.payment_methods
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireAccountInfoResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'paymentMethods' in response_body:
            self.__payment_methods = []
            for item in response_body['paymentMethods']:
                obj = AgenticBoundPaymentMethod()
                obj.parse_rsp_body(item)
                self.__payment_methods.append(obj)
