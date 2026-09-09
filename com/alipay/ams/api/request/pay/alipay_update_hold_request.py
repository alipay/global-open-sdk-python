import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayUpdateHoldRequest(AlipayRequest):
    def __init__(self):
        super(AlipayUpdateHoldRequest, self).__init__("/ams/api/v1/payments/reserve/updateHold") 

        self.__hold_id = None  # type: str
        self.__release_time = None  # type: str
        

    @property
    def hold_id(self):
        """
        The manual hold identifier returned by createHold. It identifies the single hold whose automatic release time is replaced.
        """
        return self.__hold_id

    @hold_id.setter
    def hold_id(self, value):
        self.__hold_id = value
    @property
    def release_time(self):
        """
        The new automatic release time as an ISO 8601 offset date-time. It fully replaces the current release time and must be later than the current time.
        """
        return self.__release_time

    @release_time.setter
    def release_time(self, value):
        self.__release_time = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "hold_id") and self.hold_id is not None:
            params['holdId'] = self.hold_id
        if hasattr(self, "release_time") and self.release_time is not None:
            params['releaseTime'] = self.release_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'holdId' in response_body:
            self.__hold_id = response_body['holdId']
        if 'releaseTime' in response_body:
            self.__release_time = response_body['releaseTime']
