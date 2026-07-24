import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayMeterInquireDetailsRequest(AlipayRequest):
    def __init__(self):
        super(AlipayMeterInquireDetailsRequest, self).__init__("/ams/api/v1/meter/inquireDetails") 

        self.__meter_id = None  # type: str
        

    @property
    def meter_id(self):
        """
        The meter ID. Maximum length: 64 characters.
        """
        return self.__meter_id

    @meter_id.setter
    def meter_id(self, value):
        self.__meter_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "meter_id") and self.meter_id is not None:
            params['meterId'] = self.meter_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'meterId' in response_body:
            self.__meter_id = response_body['meterId']
