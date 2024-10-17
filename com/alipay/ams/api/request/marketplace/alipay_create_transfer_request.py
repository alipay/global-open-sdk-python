import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.transfer_from_detail import TransferFromDetail
from com.alipay.ams.api.model.transfer_to_detail import TransferToDetail
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCreateTransferRequest(AlipayRequest):

    def __init__(self):
        super(AlipayCreateTransferRequest, self).__init__(AntomPathConstants.MARKETPLACE_CREATETRANSFER_PATH)
        self.__transfer_request_id = None
        self.__transfer_from_detail = None  # type: TransferFromDetail
        self.__transfer_to_detail = None  # type: TransferToDetail

    @property
    def transfer_request_id(self):
        return self.__transfer_request_id

    @transfer_request_id.setter
    def transfer_request_id(self, value):
        self.__transfer_request_id = value

    @property
    def transfer_from_detail(self):
        return self.__transfer_from_detail

    @transfer_from_detail.setter
    def transfer_from_detail(self, value):
        self.__transfer_from_detail = value

    @property
    def transfer_to_detail(self):
        return self.__transfer_to_detail

    @transfer_to_detail.setter
    def transfer_to_detail(self, value):
        self.__transfer_to_detail = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_request_id") and self.transfer_request_id:
            params['transferRequestId'] = self.transfer_request_id
        if hasattr(self, "transfer_from_detail") and self.transfer_from_detail:
            params['transferFromDetail'] = self.transfer_from_detail.to_ams_dict()
        if hasattr(self, "transfer_to_detail") and self.transfer_to_detail:
            params['transferToDetail'] = self.transfer_to_detail.to_ams_dict()
        return params
