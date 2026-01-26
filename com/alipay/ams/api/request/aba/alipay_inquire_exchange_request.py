import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireExchangeRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireExchangeRequest, self).__init__("/ams/v1/aba/funds/inquireExchange") 

        self.__exchange_request_id = None  # type: str
        

    @property
    def exchange_request_id(self):
        """Gets the exchange_request_id of this AlipayInquireExchangeRequest.
        
        """
        return self.__exchange_request_id

    @exchange_request_id.setter
    def exchange_request_id(self, value):
        self.__exchange_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "exchange_request_id") and self.exchange_request_id is not None:
            params['exchangeRequestId'] = self.exchange_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'exchangeRequestId' in response_body:
            self.__exchange_request_id = response_body['exchangeRequestId']
