import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.goods import Goods
from com.alipay.ams.api.model.shipping import Shipping



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AmsApiV1PaymentsCapturePostRequest(AlipayRequest):
    def __init__(self):
        super(AmsApiV1PaymentsCapturePostRequest, self).__init__("/ams/api/v1/payments/capture") 

        self.__capture_request_id = None  # type: str
        self.__payment_id = None  # type: str
        self.__capture_amount = None  # type: Amount
        self.__is_last_capture = None  # type: bool
        self.__capture_type = None  # type: str
        self.__goods = None  # type: [Goods]
        self.__shippings = None  # type: [Shipping]
        

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
        """Gets the capture_amount of this AmsApiV1PaymentsCapturePostRequest.
        
        """
        return self.__capture_amount

    @capture_amount.setter
    def capture_amount(self, value):
        self.__capture_amount = value
    @property
    def is_last_capture(self):
        """Gets the is_last_capture of this AmsApiV1PaymentsCapturePostRequest.
        
        """
        return self.__is_last_capture

    @is_last_capture.setter
    def is_last_capture(self, value):
        self.__is_last_capture = value
    @property
    def capture_type(self):
        """
        The type of capture operation. Valid values are FINAL (the final capture) and NON_FINAL (a non-final capture). The default value is FINAL.
        """
        return self.__capture_type

    @capture_type.setter
    def capture_type(self, value):
        self.__capture_type = value
    @property
    def goods(self):
        """
        The goods included in this capture. When using KLARNA, provide the goods information required for the capture.
        """
        return self.__goods

    @goods.setter
    def goods(self, value):
        self.__goods = value
    @property
    def shippings(self):
        """
        The shipment information for this capture. When using KLARNA, this field can be provided to display shipment tracking information in the payment method app.
        """
        return self.__shippings

    @shippings.setter
    def shippings(self, value):
        self.__shippings = value


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
        if hasattr(self, "goods") and self.goods is not None:
            params['goods'] = self.goods
        if hasattr(self, "shippings") and self.shippings is not None:
            params['shippings'] = self.shippings
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
        if 'goods' in response_body:
            self.__goods = []
            for item in response_body['goods']:
                obj = Goods()
                obj.parse_rsp_body(item)
                self.__goods.append(obj)
        if 'shippings' in response_body:
            self.__shippings = []
            for item in response_body['shippings']:
                obj = Shipping()
                obj.parse_rsp_body(item)
                self.__shippings.append(obj)
