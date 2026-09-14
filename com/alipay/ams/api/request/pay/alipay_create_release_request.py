import json
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateReleaseRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateReleaseRequest, self).__init__("/ams/api/v1/payments/reserve/createRelease") 

        self.__release_request_id = None  # type: str
        self.__hold_id = None  # type: str
        self.__release_amount = None  # type: Amount
        

    @property
    def release_request_id(self):
        """
        The merchant-generated idempotency key. Reuse it only when retrying the same release instruction.
        """
        return self.__release_request_id

    @release_request_id.setter
    def release_request_id(self, value):
        self.__release_request_id = value
    @property
    def hold_id(self):
        """
        The manual hold identifier returned by createHold. The hold must belong to the calling merchant.
        """
        return self.__hold_id

    @hold_id.setter
    def hold_id(self, value):
        self.__hold_id = value
    @property
    def release_amount(self):
        """Gets the release_amount of this AlipayCreateReleaseRequest.
        
        """
        return self.__release_amount

    @release_amount.setter
    def release_amount(self, value):
        self.__release_amount = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "release_request_id") and self.release_request_id is not None:
            params['releaseRequestId'] = self.release_request_id
        if hasattr(self, "hold_id") and self.hold_id is not None:
            params['holdId'] = self.hold_id
        if hasattr(self, "release_amount") and self.release_amount is not None:
            params['releaseAmount'] = self.release_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'releaseRequestId' in response_body:
            self.__release_request_id = response_body['releaseRequestId']
        if 'holdId' in response_body:
            self.__hold_id = response_body['holdId']
        if 'releaseAmount' in response_body:
            self.__release_amount = Amount()
            self.__release_amount.parse_rsp_body(response_body['releaseAmount'])
