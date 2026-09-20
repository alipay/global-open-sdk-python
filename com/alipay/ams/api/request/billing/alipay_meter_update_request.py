import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayMeterUpdateRequest(AlipayRequest):
    def __init__(self):
        super(AlipayMeterUpdateRequest, self).__init__("/ams/api/v1/meter/update") 

        self.__meter_id = None  # type: str
        self.__meter_name = None  # type: str
        self.__status = None  # type: str
        

    @property
    def meter_id(self):
        """
        The unique identifier of the Meter. The resource must belong to the authenticated merchant. Maximum length: 64 characters.
        """
        return self.__meter_id

    @meter_id.setter
    def meter_id(self, value):
        self.__meter_id = value
    @property
    def meter_name(self):
        """
        The merchant-facing name of the Meter. Send this field to rename the Meter; omit to keep the current name. At least one of meterName and status must be provided. Maximum length: 255 characters.
        """
        return self.__meter_name

    @meter_name.setter
    def meter_name(self, value):
        self.__meter_name = value
    @property
    def status(self):
        """
        The Meter status. Valid values are ACTIVE and INACTIVE. Send this field to activate or deactivate the Meter; omit to keep the current state. At least one of meterName and status must be provided. Maximum length: 8 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "meter_id") and self.meter_id is not None:
            params['meterId'] = self.meter_id
        if hasattr(self, "meter_name") and self.meter_name is not None:
            params['meterName'] = self.meter_name
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'meterId' in response_body:
            self.__meter_id = response_body['meterId']
        if 'meterName' in response_body:
            self.__meter_name = response_body['meterName']
        if 'status' in response_body:
            self.__status = response_body['status']
