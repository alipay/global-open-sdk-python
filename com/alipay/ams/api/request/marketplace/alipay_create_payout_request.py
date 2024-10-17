import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.transfer_from_detail import TransferFromDetail
from com.alipay.ams.api.model.transfer_to_detail import TransferToDetail
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayCreatePayoutRequest(AlipayRequest):

    def __init__(self):
        super(AlipayCreatePayoutRequest, self).__init__(AntomPathConstants.MARKETPLACE_CREATEPAYOUT_PATH)
        self.__transfer_requestId = None
        self.__transfer_from_detail = None  # type: TransferFromDetail
        self.__transfer_to_detail = None  # type: TransferToDetail

    @property
    def transfer_requestId(self):
        return self.__transfer_requestId

    @transfer_requestId.setter
    def transfer_requestId(self, value):
        self.__transfer_requestId = value

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
        if self.__transfer_requestId is not None:
            params['transferRequestId'] = self.__transfer_requestId
        if self.__transfer_from_detail is not None:
            params['transferFromDetail'] = self.__transfer_from_detail.to_ams_dict()
        if self.__transfer_to_detail is not None:
            params['transferToDetail'] = self.__transfer_to_detail.to_ams_dict()
        return params
