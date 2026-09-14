import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class ReserveHoldDetail:
    def __init__(self):
        
        self.__hold_request_id = None  # type: str
        self.__hold_id = None  # type: str
        self.__hold_amount = None  # type: Amount
        self.__releasable_amount = None  # type: Amount
        self.__release_time = None  # type: str
        self.__hold_status = None  # type: str
        self.__release_status = None  # type: str
        

    @property
    def hold_request_id(self):
        """
        The original createHold request identifier.
        """
        return self.__hold_request_id

    @hold_request_id.setter
    def hold_request_id(self, value):
        self.__hold_request_id = value
    @property
    def hold_id(self):
        """
        The manual hold identifier.
        """
        return self.__hold_id

    @hold_id.setter
    def hold_id(self, value):
        self.__hold_id = value
    @property
    def hold_amount(self):
        """Gets the hold_amount of this ReserveHoldDetail.
        
        """
        return self.__hold_amount

    @hold_amount.setter
    def hold_amount(self, value):
        self.__hold_amount = value
    @property
    def releasable_amount(self):
        """Gets the releasable_amount of this ReserveHoldDetail.
        
        """
        return self.__releasable_amount

    @releasable_amount.setter
    def releasable_amount(self, value):
        self.__releasable_amount = value
    @property
    def release_time(self):
        """
        The automatic release time in UTC ISO 8601 format.
        """
        return self.__release_time

    @release_time.setter
    def release_time(self, value):
        self.__release_time = value
    @property
    def hold_status(self):
        """
        The hold creation status. Possible values are SUCCESS, FAIL, and PROCESSING.
        """
        return self.__hold_status

    @hold_status.setter
    def hold_status(self, value):
        self.__hold_status = value
    @property
    def release_status(self):
        """
        The hold release lifecycle status. Current values are INIT, UNRELEASED, RELEASING, and RELEASED. Treat an unknown future value as not releasable and retrieve the hold again before taking a funds action.
        """
        return self.__release_status

    @release_status.setter
    def release_status(self, value):
        self.__release_status = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "hold_request_id") and self.hold_request_id is not None:
            params['holdRequestId'] = self.hold_request_id
        if hasattr(self, "hold_id") and self.hold_id is not None:
            params['holdId'] = self.hold_id
        if hasattr(self, "hold_amount") and self.hold_amount is not None:
            params['holdAmount'] = self.hold_amount
        if hasattr(self, "releasable_amount") and self.releasable_amount is not None:
            params['releasableAmount'] = self.releasable_amount
        if hasattr(self, "release_time") and self.release_time is not None:
            params['releaseTime'] = self.release_time
        if hasattr(self, "hold_status") and self.hold_status is not None:
            params['holdStatus'] = self.hold_status
        if hasattr(self, "release_status") and self.release_status is not None:
            params['releaseStatus'] = self.release_status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'holdRequestId' in response_body:
            self.__hold_request_id = response_body['holdRequestId']
        if 'holdId' in response_body:
            self.__hold_id = response_body['holdId']
        if 'holdAmount' in response_body:
            self.__hold_amount = Amount()
            self.__hold_amount.parse_rsp_body(response_body['holdAmount'])
        if 'releasableAmount' in response_body:
            self.__releasable_amount = Amount()
            self.__releasable_amount.parse_rsp_body(response_body['releasableAmount'])
        if 'releaseTime' in response_body:
            self.__release_time = response_body['releaseTime']
        if 'holdStatus' in response_body:
            self.__hold_status = response_body['holdStatus']
        if 'releaseStatus' in response_body:
            self.__release_status = response_body['releaseStatus']
