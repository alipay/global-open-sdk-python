import json
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayUpdateHoldResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__hold_id = None  # type: str
        self.__release_time = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayUpdateHoldResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def hold_id(self):
        """
        The updated manual hold identifier. Returned when result.resultStatus is S.
        """
        return self.__hold_id

    @hold_id.setter
    def hold_id(self, value):
        self.__hold_id = value
    @property
    def release_time(self):
        """
        The persisted automatic release time in UTC ISO 8601 format. Returned when result.resultStatus is S.
        """
        return self.__release_time

    @release_time.setter
    def release_time(self, value):
        self.__release_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "hold_id") and self.hold_id is not None:
            params['holdId'] = self.hold_id
        if hasattr(self, "release_time") and self.release_time is not None:
            params['releaseTime'] = self.release_time
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayUpdateHoldResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'holdId' in response_body:
            self.__hold_id = response_body['holdId']
        if 'releaseTime' in response_body:
            self.__release_time = response_body['releaseTime']
