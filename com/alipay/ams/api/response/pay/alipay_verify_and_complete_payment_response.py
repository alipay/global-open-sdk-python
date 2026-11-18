import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.acquirer_info import AcquirerInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayVerifyAndCompletePaymentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__payment_request_id = None  # type: str
        self.__verify_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__payment_amount = None  # type: Amount
        self.__payment_create_time = None  # type: str
        self.__acquirer_info = None  # type: AcquirerInfo
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayVerifyAndCompletePaymentResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def payment_request_id(self):
        """Gets the payment_request_id of this AlipayVerifyAndCompletePaymentResponse.
        
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def verify_request_id(self):
        """Gets the verify_request_id of this AlipayVerifyAndCompletePaymentResponse.
        
        """
        return self.__verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self.__verify_request_id = value
    @property
    def payment_id(self):
        """Gets the payment_id of this AlipayVerifyAndCompletePaymentResponse.
        
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayVerifyAndCompletePaymentResponse.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def payment_create_time(self):
        """Gets the payment_create_time of this AlipayVerifyAndCompletePaymentResponse.
        
        """
        return self.__payment_create_time

    @payment_create_time.setter
    def payment_create_time(self, value):
        self.__payment_create_time = value
    @property
    def acquirer_info(self):
        """Gets the acquirer_info of this AlipayVerifyAndCompletePaymentResponse.
        
        """
        return self.__acquirer_info

    @acquirer_info.setter
    def acquirer_info(self, value):
        self.__acquirer_info = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "verify_request_id") and self.verify_request_id is not None:
            params['verifyRequestId'] = self.verify_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "payment_create_time") and self.payment_create_time is not None:
            params['paymentCreateTime'] = self.payment_create_time
        if hasattr(self, "acquirer_info") and self.acquirer_info is not None:
            params['acquirerInfo'] = self.acquirer_info
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayVerifyAndCompletePaymentResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'verifyRequestId' in response_body:
            self.__verify_request_id = response_body['verifyRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'paymentCreateTime' in response_body:
            self.__payment_create_time = response_body['paymentCreateTime']
        if 'acquirerInfo' in response_body:
            self.__acquirer_info = AcquirerInfo()
            self.__acquirer_info.parse_rsp_body(response_body['acquirerInfo'])
