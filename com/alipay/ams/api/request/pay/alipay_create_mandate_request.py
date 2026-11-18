import json
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateMandateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateMandateRequest, self).__init__("/ams/api/v1/payments/createMandate") 

        self.__mandate_request_id = None  # type: str
        self.__access_token = None  # type: str
        self.__payment_amount = None  # type: Amount
        

    @property
    def mandate_request_id(self):
        """
        Merchant-assigned idempotency key, scoped by the current merchantId. Keep the original value and amount/currency when recovering a result. Existing operations replay the stored result or reject nonterminal duplicates without another channel call. Never reuse for another intent.
        """
        return self.__mandate_request_id

    @mandate_request_id.setter
    def mandate_request_id(self, value):
        self.__mandate_request_id = value
    @property
    def access_token(self):
        """
        The Antom agreement token, not a channel agreement number. Required and non-empty for all requests. For a new operation it must resolve to a valid agreement owned by the current merchant. For an existing operation the newly supplied token is not resolved and may differ without changing the original binding. Do not log the token.
        """
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value
    @property
    def payment_amount(self):
        """Gets the payment_amount of this AlipayCreateMandateRequest.
        
        """
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "mandate_request_id") and self.mandate_request_id is not None:
            params['mandateRequestId'] = self.mandate_request_id
        if hasattr(self, "access_token") and self.access_token is not None:
            params['accessToken'] = self.access_token
        if hasattr(self, "payment_amount") and self.payment_amount is not None:
            params['paymentAmount'] = self.payment_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'mandateRequestId' in response_body:
            self.__mandate_request_id = response_body['mandateRequestId']
        if 'accessToken' in response_body:
            self.__access_token = response_body['accessToken']
        if 'paymentAmount' in response_body:
            self.__payment_amount = Amount()
            self.__payment_amount.parse_rsp_body(response_body['paymentAmount'])
