from com.alipay.ams.api.model.transfer_from_detail import TransferFromDetail
from com.alipay.ams.api.model.transfer_to_detail import TransferToDetail
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayCreatePayoutResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayCreatePayoutResponse, self).__init__()
        self.__transfer_id = None
        self.__transfer_request_id = None
        self.__transfer_from_detail = None #type: TransferFromDetail
        self.__transfer_to_detail = None #type: TransferToDetail
        self.__parse_rsp_body(rsp_body)

    @property
    def transfer_id(self):
        return self.__transfer_id

    @property
    def transfer_request_id(self):
        return self.__transfer_request_id

    @property
    def transfer_from_detail(self):
        return self.__transfer_from_detail

    @property
    def transfer_to_detail(self):
        return self.__transfer_to_detail

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayCreatePayoutResponse, self).parse_rsp_body(rsp_body)
        if "transferId" in response:
            self.__transfer_id = response["transferId"]
        if "transferRequestId" in response:
            self.__transfer_request_id = response["transferRequestId"]
        if "transferFromDetail" in response:
            self.__transfer_from_detail = TransferFromDetail()
            self.__transfer_from_detail.parse_rsp_body(response["transferFromDetail"])
        if "transferToDetail" in response:
            self.__transfer_to_detail = TransferToDetail()
            self.__transfer_to_detail.parse_rsp_body(response["transferToDetail"])