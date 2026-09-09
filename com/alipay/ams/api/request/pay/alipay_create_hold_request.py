import json
from com.alipay.ams.api.model.amount import Amount



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreateHoldRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreateHoldRequest, self).__init__("/ams/api/v1/payments/reserve/createHold") 

        self.__hold_request_id = None  # type: str
        self.__hold_amount = None  # type: Amount
        self.__release_time = None  # type: str
        

    @property
    def hold_request_id(self):
        """
        The merchant-generated idempotency key. Reuse it only when retrying the same hold instruction.
        """
        return self.__hold_request_id

    @hold_request_id.setter
    def hold_request_id(self, value):
        self.__hold_request_id = value
    @property
    def hold_amount(self):
        """Gets the hold_amount of this AlipayCreateHoldRequest.
        
        """
        return self.__hold_amount

    @hold_amount.setter
    def hold_amount(self, value):
        self.__hold_amount = value
    @property
    def release_time(self):
        """
        The automatic release time as an ISO 8601 offset date-time. It must be later than the current time.
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
        if hasattr(self, "hold_request_id") and self.hold_request_id is not None:
            params['holdRequestId'] = self.hold_request_id
        if hasattr(self, "hold_amount") and self.hold_amount is not None:
            params['holdAmount'] = self.hold_amount
        if hasattr(self, "release_time") and self.release_time is not None:
            params['releaseTime'] = self.release_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'holdRequestId' in response_body:
            self.__hold_request_id = response_body['holdRequestId']
        if 'holdAmount' in response_body:
            self.__hold_amount = Amount()
            self.__hold_amount.parse_rsp_body(response_body['holdAmount'])
        if 'releaseTime' in response_body:
            self.__release_time = response_body['releaseTime']
