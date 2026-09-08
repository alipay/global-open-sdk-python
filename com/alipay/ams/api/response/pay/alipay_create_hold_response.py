import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateHoldResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__hold_request_id = None  # type: str
        self.__hold_id = None  # type: str
        self.__hold_amount = None  # type: Amount
        self.__release_time = None  # type: str
        self.__hold_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreateHoldResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def hold_request_id(self):
        """
        The merchant idempotency key originally used to create the hold. Returned when result.resultStatus is S.
        """
        return self.__hold_request_id

    @hold_request_id.setter
    def hold_request_id(self, value):
        self.__hold_request_id = value
    @property
    def hold_id(self):
        """
        The identifier of the created manual hold. Use it in createRelease. Returned when result.resultStatus is S.
        """
        return self.__hold_id

    @hold_id.setter
    def hold_id(self, value):
        self.__hold_id = value
    @property
    def hold_amount(self):
        """Gets the hold_amount of this AlipayCreateHoldResponse.
        
        """
        return self.__hold_amount

    @hold_amount.setter
    def hold_amount(self, value):
        self.__hold_amount = value
    @property
    def release_time(self):
        """
        The automatic release time in UTC ISO 8601 format. Returned when result.resultStatus is S.
        """
        return self.__release_time

    @release_time.setter
    def release_time(self, value):
        self.__release_time = value
    @property
    def hold_status(self):
        """
        The hold creation status. Possible values are SUCCESS, FAIL, and PROCESSING. SUCCESS and FAIL are terminal; PROCESSING is non-terminal. Returned when result.resultStatus is S.
        """
        return self.__hold_status

    @hold_status.setter
    def hold_status(self, value):
        self.__hold_status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "hold_request_id") and self.hold_request_id is not None:
            params['holdRequestId'] = self.hold_request_id
        if hasattr(self, "hold_id") and self.hold_id is not None:
            params['holdId'] = self.hold_id
        if hasattr(self, "hold_amount") and self.hold_amount is not None:
            params['holdAmount'] = self.hold_amount
        if hasattr(self, "release_time") and self.release_time is not None:
            params['releaseTime'] = self.release_time
        if hasattr(self, "hold_status") and self.hold_status is not None:
            params['holdStatus'] = self.hold_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateHoldResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'holdRequestId' in response_body:
            self.__hold_request_id = response_body['holdRequestId']
        if 'holdId' in response_body:
            self.__hold_id = response_body['holdId']
        if 'holdAmount' in response_body:
            self.__hold_amount = Amount()
            self.__hold_amount.parse_rsp_body(response_body['holdAmount'])
        if 'releaseTime' in response_body:
            self.__release_time = response_body['releaseTime']
        if 'holdStatus' in response_body:
            self.__hold_status = response_body['holdStatus']
