import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.transfer_from_detail import TransferFromDetail
from com.alipay.ams.api.model.transfer_to_detail import TransferToDetail



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayCreateTransferResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__transfer_id = None  # type: str
        self.__transfer_request_id = None  # type: str
        self.__transfer_from_detail = None  # type: TransferFromDetail
        self.__transfer_to_detail = None  # type: TransferToDetail
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayCreateTransferResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def transfer_id(self):
        """
        The unique ID assigned by Antom to identify a transfer.  This parameter is returned when the value of result.resultStatus is U.   More information:  Maximum length: 64 characters
        """
        return self.__transfer_id

    @transfer_id.setter
    def transfer_id(self, value):
        self.__transfer_id = value
    @property
    def transfer_request_id(self):
        """
        The unique ID assigned by the marketplace to identify a transfer request.  This parameter is returned when the value of result.resultStatus is U.   More information:  Maximum length: 64 characters
        """
        return self.__transfer_request_id

    @transfer_request_id.setter
    def transfer_request_id(self, value):
        self.__transfer_request_id = value
    @property
    def transfer_from_detail(self):
        """Gets the transfer_from_detail of this AlipayCreateTransferResponse.
        
        """
        return self.__transfer_from_detail

    @transfer_from_detail.setter
    def transfer_from_detail(self, value):
        self.__transfer_from_detail = value
    @property
    def transfer_to_detail(self):
        """Gets the transfer_to_detail of this AlipayCreateTransferResponse.
        
        """
        return self.__transfer_to_detail

    @transfer_to_detail.setter
    def transfer_to_detail(self, value):
        self.__transfer_to_detail = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "transfer_id") and self.transfer_id is not None:
            params['transferId'] = self.transfer_id
        if hasattr(self, "transfer_request_id") and self.transfer_request_id is not None:
            params['transferRequestId'] = self.transfer_request_id
        if hasattr(self, "transfer_from_detail") and self.transfer_from_detail is not None:
            params['transferFromDetail'] = self.transfer_from_detail
        if hasattr(self, "transfer_to_detail") and self.transfer_to_detail is not None:
            params['transferToDetail'] = self.transfer_to_detail
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayCreateTransferResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'transferId' in response_body:
            self.__transfer_id = response_body['transferId']
        if 'transferRequestId' in response_body:
            self.__transfer_request_id = response_body['transferRequestId']
        if 'transferFromDetail' in response_body:
            self.__transfer_from_detail = TransferFromDetail()
            self.__transfer_from_detail.parse_rsp_body(response_body['transferFromDetail'])
        if 'transferToDetail' in response_body:
            self.__transfer_to_detail = TransferToDetail()
            self.__transfer_to_detail.parse_rsp_body(response_body['transferToDetail'])
