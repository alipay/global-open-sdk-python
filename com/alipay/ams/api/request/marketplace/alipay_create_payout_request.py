import json
from com.alipay.ams.api.model.transfer_from_detail import TransferFromDetail
from com.alipay.ams.api.model.transfer_to_detail import TransferToDetail



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreatePayoutRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreatePayoutRequest, self).__init__("/ams/api/v1/funds/createPayout") 

        self.__transfer_request_id = None  # type: str
        self.__transfer_from_detail = None  # type: TransferFromDetail
        self.__transfer_to_detail = None  # type: TransferToDetail
        

    @property
    def transfer_request_id(self):
        """
        The unique ID assigned by the marketplace to identify a payout request.   More information:  This field is an API idempotency field.For requests that are initiated with the same value of transferRequestId and reach a final status (S or F), the same result is to be returned for the request. Maximum length: 64 characters
        """
        return self.__transfer_request_id

    @transfer_request_id.setter
    def transfer_request_id(self, value):
        self.__transfer_request_id = value
    @property
    def transfer_from_detail(self):
        """Gets the transfer_from_detail of this AlipayCreatePayoutRequest.
        
        """
        return self.__transfer_from_detail

    @transfer_from_detail.setter
    def transfer_from_detail(self, value):
        self.__transfer_from_detail = value
    @property
    def transfer_to_detail(self):
        """Gets the transfer_to_detail of this AlipayCreatePayoutRequest.
        
        """
        return self.__transfer_to_detail

    @transfer_to_detail.setter
    def transfer_to_detail(self, value):
        self.__transfer_to_detail = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_request_id") and self.transfer_request_id is not None:
            params['transferRequestId'] = self.transfer_request_id
        if hasattr(self, "transfer_from_detail") and self.transfer_from_detail is not None:
            params['transferFromDetail'] = self.transfer_from_detail
        if hasattr(self, "transfer_to_detail") and self.transfer_to_detail is not None:
            params['transferToDetail'] = self.transfer_to_detail
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'transferRequestId' in response_body:
            self.__transfer_request_id = response_body['transferRequestId']
        if 'transferFromDetail' in response_body:
            self.__transfer_from_detail = TransferFromDetail()
            self.__transfer_from_detail.parse_rsp_body(response_body['transferFromDetail'])
        if 'transferToDetail' in response_body:
            self.__transfer_to_detail = TransferToDetail()
            self.__transfer_to_detail.parse_rsp_body(response_body['transferToDetail'])
