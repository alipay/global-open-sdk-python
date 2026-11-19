import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquirePaymentMethodRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquirePaymentMethodRequest, self).__init__("/ams/api/v1/paymentMethods/inquirePaymentMethod") 

        self.__card_token = None  # type: str
        

    @property
    def card_token(self):
        """
        The permanent card token provided to the merchant after payment.
        """
        return self.__card_token

    @card_token.setter
    def card_token(self, value):
        self.__card_token = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_token") and self.card_token is not None:
            params['cardToken'] = self.card_token
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardToken' in response_body:
            self.__card_token = response_body['cardToken']
