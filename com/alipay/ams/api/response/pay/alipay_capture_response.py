import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCaptureResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__capture_request_id = None  # type: str
        self.__capture_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__capture_amount = None  # type: Amount
        self.__capture_time = None  # type: str
        self.__acquirer_reference_no = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCaptureResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def capture_request_id(self):
        """
        The unique ID that is assigned by a merchant to identify a capture request.  Note: This parameter is returned when the capture status is successful.  More information:  Maximum length: 64 characters
        """
        return self.__capture_request_id

    @capture_request_id.setter
    def capture_request_id(self, value):
        self.__capture_request_id = value
    @property
    def capture_id(self):
        """
        The unique ID that is assigned by Antom to identify a capture.  Note: This parameter is returned when the capture status is successful.  More information:  Maximum length: 64 characters
        """
        return self.__capture_id

    @capture_id.setter
    def capture_id(self, value):
        self.__capture_id = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.  Note: This parameter is returned when the capture status is successful.  More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def capture_amount(self):
        """Gets the capture_amount of this AlipayCaptureResponse.
        
        """
        return self.__capture_amount

    @capture_amount.setter
    def capture_amount(self, value):
        self.__capture_amount = value
    @property
    def capture_time(self):
        """
        The time when Antom captures the payment.   Note: This parameter is returned when the capture status is successful.  More information:  The value follows the ISO 8601 standard format. For example, \&quot;2019-11-27T12:01:01+08:00\&quot;.
        """
        return self.__capture_time

    @capture_time.setter
    def capture_time(self, value):
        self.__capture_time = value
    @property
    def acquirer_reference_no(self):
        """
        The unique ID assigned by the non-Antom acquirer for the transaction.    More information:  Maximum length: 64 characters
        """
        return self.__acquirer_reference_no

    @acquirer_reference_no.setter
    def acquirer_reference_no(self, value):
        self.__acquirer_reference_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "capture_request_id") and self.capture_request_id is not None:
            params['captureRequestId'] = self.capture_request_id
        if hasattr(self, "capture_id") and self.capture_id is not None:
            params['captureId'] = self.capture_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "capture_amount") and self.capture_amount is not None:
            params['captureAmount'] = self.capture_amount
        if hasattr(self, "capture_time") and self.capture_time is not None:
            params['captureTime'] = self.capture_time
        if hasattr(self, "acquirer_reference_no") and self.acquirer_reference_no is not None:
            params['acquirerReferenceNo'] = self.acquirer_reference_no
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCaptureResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'captureRequestId' in response_body:
            self.__capture_request_id = response_body['captureRequestId']
        if 'captureId' in response_body:
            self.__capture_id = response_body['captureId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'captureAmount' in response_body:
            self.__capture_amount = Amount()
            self.__capture_amount.parse_rsp_body(response_body['captureAmount'])
        if 'captureTime' in response_body:
            self.__capture_time = response_body['captureTime']
        if 'acquirerReferenceNo' in response_body:
            self.__acquirer_reference_no = response_body['acquirerReferenceNo']
