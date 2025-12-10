import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayPayCancelResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payment_id = None  # type: str
        self.__payment_request_id = None  # type: str
        self.__cancel_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayPayCancelResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.  Note: This field is returned when the cancellation succeeds (the value of result.resultStatus is S).   More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def payment_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a payment request.   Note: This field is returned when the cancellation succeeds (the value of result.resultStatus is S).   More information:  Maximum length: 64 characters
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def cancel_time(self):
        """
        The actual execution completion time of the payment cancellation process, which is the date and time when the payment cancellation succeeds.  Note: This field is returned when the cancellation succeeds (the value of result.resultStatus is S).  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self.__cancel_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "cancel_time") and self.cancel_time is not None:
            params['cancelTime'] = self.cancel_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayPayCancelResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'cancelTime' in response_body:
            self.__cancel_time = response_body['cancelTime']
