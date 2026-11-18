import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateReleaseResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__release_request_id = None  # type: str
        self.__release_id = None  # type: str
        self.__hold_id = None  # type: str
        self.__release_amount = None  # type: Amount
        self.__release_status = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreateReleaseResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def release_request_id(self):
        """
        The merchant idempotency key originally used to create the release. Returned when result.resultStatus is S.
        """
        return self.__release_request_id

    @release_request_id.setter
    def release_request_id(self, value):
        self.__release_request_id = value
    @property
    def release_id(self):
        """
        The identifier of this manual hold release. Use it in inquireRelease. Returned when result.resultStatus is S.
        """
        return self.__release_id

    @release_id.setter
    def release_id(self, value):
        self.__release_id = value
    @property
    def hold_id(self):
        """
        The source manual hold identifier. Returned when result.resultStatus is S.
        """
        return self.__hold_id

    @hold_id.setter
    def hold_id(self, value):
        self.__hold_id = value
    @property
    def release_amount(self):
        """Gets the release_amount of this AlipayCreateReleaseResponse.
        
        """
        return self.__release_amount

    @release_amount.setter
    def release_amount(self, value):
        self.__release_amount = value
    @property
    def release_status(self):
        """
        The release status. Possible values are SUCCESS, FAIL, and PROCESSING. SUCCESS and FAIL are terminal; PROCESSING is non-terminal. Returned when result.resultStatus is S.
        """
        return self.__release_status

    @release_status.setter
    def release_status(self, value):
        self.__release_status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "release_request_id") and self.release_request_id is not None:
            params['releaseRequestId'] = self.release_request_id
        if hasattr(self, "release_id") and self.release_id is not None:
            params['releaseId'] = self.release_id
        if hasattr(self, "hold_id") and self.hold_id is not None:
            params['holdId'] = self.hold_id
        if hasattr(self, "release_amount") and self.release_amount is not None:
            params['releaseAmount'] = self.release_amount
        if hasattr(self, "release_status") and self.release_status is not None:
            params['releaseStatus'] = self.release_status
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateReleaseResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'releaseRequestId' in response_body:
            self.__release_request_id = response_body['releaseRequestId']
        if 'releaseId' in response_body:
            self.__release_id = response_body['releaseId']
        if 'holdId' in response_body:
            self.__hold_id = response_body['holdId']
        if 'releaseAmount' in response_body:
            self.__release_amount = Amount()
            self.__release_amount.parse_rsp_body(response_body['releaseAmount'])
        if 'releaseStatus' in response_body:
            self.__release_status = response_body['releaseStatus']
