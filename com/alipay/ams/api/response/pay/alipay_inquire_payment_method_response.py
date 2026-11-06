import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.inquire_payment_method_detail import InquirePaymentMethodDetail



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquirePaymentMethodResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payment_method_details = None  # type: [InquirePaymentMethodDetail]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquirePaymentMethodResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payment_method_details(self):
        """
        The payment method details. Returned when the inquiry succeeds; one token maps to one card, so the array contains at most one element and can be empty after country filtering.
        """
        return self.__payment_method_details

    @payment_method_details.setter
    def payment_method_details(self, value):
        self.__payment_method_details = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payment_method_details") and self.payment_method_details is not None:
            params['paymentMethodDetails'] = self.payment_method_details
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquirePaymentMethodResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'paymentMethodDetails' in response_body:
            self.__payment_method_details = []
            for item in response_body['paymentMethodDetails']:
                obj = InquirePaymentMethodDetail()
                obj.parse_rsp_body(item)
                self.__payment_method_details.append(obj)
