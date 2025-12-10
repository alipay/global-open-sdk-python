import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.transit import Transit



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCaptureRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCaptureRequest, self).__init__("/ams/api/v1/payments/capture") 

        self.__capture_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__capture_amount = None  # type: Amount
        self.__is_last_capture = None  # type: bool
        self.__capture_type = None  # type: str
        self.__transit = None  # type: Transit
        

    @property
    def capture_request_id(self):
        """
        The unique ID that is assigned by the merchant to identify a capture request. Antom uses this field for idempotence control.    More information:  This field is an API idempotency field.For capture requests that are initiated with the same value of captureRequestId and reach a final status (S or F), the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__capture_request_id

    @capture_request_id.setter
    def capture_request_id(self, value):
        self.__capture_request_id = value
    @property
    def payment_id(self):
        """
        The unique ID that is assigned by Antom to identify a payment.    More information:  Maximum length: 64 characters
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
    @property
    def capture_amount(self):
        """Gets the capture_amount of this AlipayCaptureRequest.
        
        """
        return self.__capture_amount

    @capture_amount.setter
    def capture_amount(self, value):
        self.__capture_amount = value
    @property
    def is_last_capture(self):
        """Gets the is_last_capture of this AlipayCaptureRequest.
        
        """
        return self.__is_last_capture

    @is_last_capture.setter
    def is_last_capture(self, value):
        self.__is_last_capture = value
    @property
    def capture_type(self):
        """
        The type of capture operation
        """
        return self.__capture_type

    @capture_type.setter
    def capture_type(self, value):
        self.__capture_type = value
    @property
    def transit(self):
        """Gets the transit of this AlipayCaptureRequest.
        
        """
        return self.__transit

    @transit.setter
    def transit(self, value):
        self.__transit = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "capture_request_id") and self.capture_request_id is not None:
            params['captureRequestId'] = self.capture_request_id
        if hasattr(self, "payment_id") and self.payment_id is not None:
            params['paymentId'] = self.payment_id
        if hasattr(self, "capture_amount") and self.capture_amount is not None:
            params['captureAmount'] = self.capture_amount
        if hasattr(self, "is_last_capture") and self.is_last_capture is not None:
            params['isLastCapture'] = self.is_last_capture
        if hasattr(self, "capture_type") and self.capture_type is not None:
            params['captureType'] = self.capture_type
        if hasattr(self, "transit") and self.transit is not None:
            params['transit'] = self.transit
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'captureRequestId' in response_body:
            self.__capture_request_id = response_body['captureRequestId']
        if 'paymentId' in response_body:
            self.__payment_id = response_body['paymentId']
        if 'captureAmount' in response_body:
            self.__capture_amount = Amount()
            self.__capture_amount.parse_rsp_body(response_body['captureAmount'])
        if 'isLastCapture' in response_body:
            self.__is_last_capture = response_body['isLastCapture']
        if 'captureType' in response_body:
            self.__capture_type = response_body['captureType']
        if 'transit' in response_body:
            self.__transit = Transit()
            self.__transit.parse_rsp_body(response_body['transit'])
