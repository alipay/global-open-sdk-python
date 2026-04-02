import json
from com.alipay.ams.api.model.refund_from_method import RefundFromMethod
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class CreateDirectRefundResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__payment_id = None  # type: str
        self.__refund_id = None  # type: str
        self.__refund_request_id = None  # type: str
        self.__refund_time = None  # type: str
        self.__refund_from_method = None  # type: RefundFromMethod
        self.__refund_from_amount = None  # type: Amount
        self.__refund_to_amount = None  # type: Amount
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def payment_id(self):
        """
        The unique ID assigned by Antom for the original payment to be refunded.  Note: This field is returned when the refund succeeds (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def refund_id(self):
        """
        The unique ID that is assigned by Antom to identify a refund. A one-to-one correspondence between refundId and refundRequestId exists.  Note: This field is returned when the refund succeeds (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value
    @property
    def refund_request_id(self):
        """
        The unique ID that is assigned by the merchant to identify a refund request.  Note: This field is returned when the refund succeeds (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self.__refund_request_id = value
    @property
    def refund_time(self):
        """
        The date and time when the refund reaches the state of success, failure, or unknown.  Note: This field is returned when the refund succeeds (the value of result.resultStatus is S).  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__refund_time

    @refund_time.setter
    def refund_time(self, value):
        self.__refund_time = value
    @property
    def refund_from_method(self):
        """Gets the refund_from_method of this CreateDirectRefundResponse.
        
        """
        return self.__refund_from_method

    @refund_from_method.setter
    def refund_from_method(self, value):
        self.__refund_from_method = value
    @property
    def refund_from_amount(self):
        """Gets the refund_from_amount of this CreateDirectRefundResponse.
        
        """
        return self.__refund_from_amount

    @refund_from_amount.setter
    def refund_from_amount(self, value):
        self.__refund_from_amount = value
    @property
    def refund_to_amount(self):
        """Gets the refund_to_amount of this CreateDirectRefundResponse.
        
        """
        return self.__refund_to_amount

    @refund_to_amount.setter
    def refund_to_amount(self, value):
        self.__refund_to_amount = value
    @property
    def result(self):
        """Gets the result of this CreateDirectRefundResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "refund_id") and self.refund_id is not None:
            params['refundId'] = self.refund_id
        if hasattr(self, "refund_request_id") and self.refund_request_id is not None:
            params['refundRequestId'] = self.refund_request_id
        if hasattr(self, "refund_time") and self.refund_time is not None:
            params['refundTime'] = self.refund_time
        if hasattr(self, "refund_from_method") and self.refund_from_method is not None:
            params['refundFromMethod'] = self.refund_from_method
        if hasattr(self, "refund_from_amount") and self.refund_from_amount is not None:
            params['refundFromAmount'] = self.refund_from_amount
        if hasattr(self, "refund_to_amount") and self.refund_to_amount is not None:
            params['refundToAmount'] = self.refund_to_amount
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(CreateDirectRefundResponse, self).parse_rsp_body(response_body)
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'refundId' in response_body:
            self.__refund_id = response_body['refundId']
        if 'refundRequestId' in response_body:
            self.__refund_request_id = response_body['refundRequestId']
        if 'refundTime' in response_body:
            self.__refund_time = response_body['refundTime']
        if 'refundFromMethod' in response_body:
            self.__refund_from_method = RefundFromMethod()
            self.__refund_from_method.parse_rsp_body(response_body['refundFromMethod'])
        if 'refundFromAmount' in response_body:
            self.__refund_from_amount = Amount()
            self.__refund_from_amount.parse_rsp_body(response_body['refundFromAmount'])
        if 'refundToAmount' in response_body:
            self.__refund_to_amount = Amount()
            self.__refund_to_amount.parse_rsp_body(response_body['refundToAmount'])
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
