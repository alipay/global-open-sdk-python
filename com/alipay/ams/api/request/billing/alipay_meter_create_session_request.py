import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayMeterCreateSessionRequest(AlipayRequest):
    def __init__(self):
        super(AlipayMeterCreateSessionRequest, self).__init__("/ams/api/v1/meter/createSession") 

        self.__request_id = None  # type: str
        

    @property
    def request_id(self):
        """
        The request id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "request_id") and self.request_id is not None:
            params['requestId'] = self.request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'requestId' in response_body:
            self.__request_id = response_body['requestId']
