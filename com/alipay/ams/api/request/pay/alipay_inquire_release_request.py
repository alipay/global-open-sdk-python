import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireReleaseRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireReleaseRequest, self).__init__("/ams/api/v1/payments/reserve/inquireRelease") 

        self.__release_id = None  # type: str
        self.__release_request_id = None  # type: str
        

    @property
    def release_id(self):
        """
        The release identifier returned by createRelease. Provide exactly one of releaseId and releaseRequestId.
        """
        return self.__release_id

    @release_id.setter
    def release_id(self, value):
        self.__release_id = value
    @property
    def release_request_id(self):
        """
        The original request identifier submitted to createRelease. Provide exactly one of releaseId and releaseRequestId.
        """
        return self.__release_request_id

    @release_request_id.setter
    def release_request_id(self, value):
        self.__release_request_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "release_id") and self.release_id is not None:
            params['releaseId'] = self.release_id
        if hasattr(self, "release_request_id") and self.release_request_id is not None:
            params['releaseRequestId'] = self.release_request_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'releaseId' in response_body:
            self.__release_id = response_body['releaseId']
        if 'releaseRequestId' in response_body:
            self.__release_request_id = response_body['releaseRequestId']
