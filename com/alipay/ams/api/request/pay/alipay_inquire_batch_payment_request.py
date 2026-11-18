import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireBatchPaymentRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireBatchPaymentRequest, self).__init__("/ams/api/v1/payments/inquireBatchPayment") 

        self.__batch_payment_request_id = None  # type: str
        

    @property
    def batch_payment_request_id(self):
        """
        Merchant-assigned batch request ID (maximum 64 characters), the only accepted query key. paymentId and paymentRequestId are not query keys. Repeating a query has no additional effects but returns the latest visible state, not a fixed response.
        """
        return self.__batch_payment_request_id

    @batch_payment_request_id.setter
    def batch_payment_request_id(self, value):
        self.__batch_payment_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "batch_payment_request_id") and self.batch_payment_request_id is not None:
            params['batchPaymentRequestId'] = self.batch_payment_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'batchPaymentRequestId' in response_body:
            self.__batch_payment_request_id = response_body['batchPaymentRequestId']
