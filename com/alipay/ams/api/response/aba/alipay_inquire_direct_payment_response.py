import json
from com.alipay.ams.api.model.transaction_status_type import TransactionStatusType
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireDirectPaymentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__payment_status = None  # type: TransactionStatusType
        self.__payment_result_message = None  # type: str
        self.__payment_result_code = None  # type: str
        self.__payment_id = None  # type: str
        self.__payment_request_id = None  # type: str
        self.__pay_to_method = None  # type: PaymentMethod
        self.__payment_amount = None  # type: Amount
        self.__pay_to_amount = None  # type: Amount
        self.__payment_time = None  # type: str
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def payment_status(self):
        """Gets the payment_status of this AlipayInquireDirectPaymentResponse.
        
        """
        return self.__payment_status

    @payment_status.setter
    def payment_status(self, value):
        self.__payment_status = value
    @property
    def payment_result_message(self):
        """
        The result message that explains the payment result code.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 256 characters
        """
        return self.__payment_result_message

    @payment_result_message.setter
    def payment_result_message(self, value):
        self.__payment_result_message = value
    @property
    def payment_result_code(self):
        """
        The result code for different payment statuses. Possible payment result codes are listed in the Payment result codes table.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__payment_result_code

    @payment_result_code.setter
    def payment_result_code(self, value):
        self.__payment_result_code = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def payment_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a payment request.  Note: This field is returned when the API is called successfully (the value of result.resultStatus is S).  More information:  Maximum length: 64 characters
        """
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value
    @property
    def pay_to_method(self):
        """Gets the pay_to_method of this AlipayInquireDirectPaymentResponse.
        
        """
        return self.__pay_to_method

    @pay_to_method.setter
    def pay_to_method(self, value):
        self.__pay_to_method = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayInquireDirectPaymentResponse.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value
    @property
    def pay_to_amount(self):
        """Gets the pay_to_amount of this AlipayInquireDirectPaymentResponse.
        
        """
        return self.__pay_to_amount

    @pay_to_amount.setter
    def pay_to_amount(self, value):
        self.__pay_to_amount = value
    @property
    def payment_time(self):
        """
        The date and time when the payment reaches a final state of success.  Note: This field is returned only when the payment reaches a final state of success (the value of paymentStatus is SUCCESS).  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
    @property
    def result(self):
        """Gets the result of this AlipayInquireDirectPaymentResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_status") and self.payment_status is not None:
            params['paymentStatus'] = self.payment_status
        if hasattr(self, "payment_result_message") and self.payment_result_message is not None:
            params['paymentResultMessage'] = self.payment_result_message
        if hasattr(self, "payment_result_code") and self.payment_result_code is not None:
            params['paymentResultCode'] = self.payment_result_code
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "payment_request_id") and self.payment_request_id is not None:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "pay_to_method") and self.pay_to_method is not None:
            params['payToMethod'] = self.pay_to_method
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        if hasattr(self, "pay_to_amount") and self.pay_to_amount is not None:
            params['payToAmount'] = self.pay_to_amount
        if hasattr(self, "payment_time") and self.payment_time is not None:
            params['paymentTime'] = self.payment_time
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireDirectPaymentResponse, self).parse_rsp_body(response_body)
        if 'paymentStatus' in response_body:
            payment_status_temp = TransactionStatusType.value_of(response_body['paymentStatus'])
            self.__payment_status = payment_status_temp
        if 'paymentResultMessage' in response_body:
            self.__payment_result_message = response_body['paymentResultMessage']
        if 'paymentResultCode' in response_body:
            self.__payment_result_code = response_body['paymentResultCode']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'paymentRequestId' in response_body:
            self.__payment_request_id = response_body['paymentRequestId']
        if 'payToMethod' in response_body:
            self.__pay_to_method = PaymentMethod()
            self.__pay_to_method.parse_rsp_body(response_body['payToMethod'])
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
        if 'payToAmount' in response_body:
            self.__pay_to_amount = Amount()
            self.__pay_to_amount.parse_rsp_body(response_body['payToAmount'])
        if 'paymentTime' in response_body:
            self.__payment_time = response_body['paymentTime']
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
