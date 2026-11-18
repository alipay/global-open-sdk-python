from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.transfer_from_detail import TransferFromDetail
from com.alipay.ams.api.model.transfer_to_detail import TransferToDetail
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayAbaTransferNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayAbaTransferNotify, self).__init__()
        self.__transfer_request_id = None  # type: str
        self.__transfer_id = None  # type: str
        self.__transfer_result = None  # type: Result
        self.__transfer_finish_time = None  # type: str
        self.__transfer_from_detail = None  # type: TransferFromDetail
        self.__transfer_to_detail = None  # type: TransferToDetail
        self.__parse_notify_body(notify_body)

    @property
    def transfer_request_id(self):
        """
        The unique ID assigned by the merchant to identify a transfer request.
        Maximum length: 64 characters
        """
        return self.__transfer_request_id

    @property
    def transfer_id(self):
        """
        The unique ID assigned by Antom to identify a transfer.
        Maximum length: 64 characters
        """
        return self.__transfer_id

    @property
    def transfer_result(self):
        """
        The result of the transfer request.
        """
        return self.__transfer_result

    @property
    def transfer_finish_time(self):
        """
        The finishing time of a transfer.
        """
        return self.__transfer_finish_time

    @property
    def transfer_from_detail(self):
        """
        The detail of the transfer from.
        """
        return self.__transfer_from_detail

    @property
    def transfer_to_detail(self):
        """
        The detail of the transfer to.
        """
        return self.__transfer_to_detail

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayAbaTransferNotify, self).parse_notify_body(notify_body)

        if "transferRequestId" in notify:
            self.__transfer_request_id = notify["transferRequestId"]
        if "transferId" in notify:
            self.__transfer_id = notify["transferId"]
        if "transferResult" in notify:
            transfer_result = Result()
            transfer_result.parse_rsp_body(notify["transferResult"])
            self.__transfer_result = transfer_result
        if "transferFinishTime" in notify:
            self.__transfer_finish_time = notify["transferFinishTime"]
        if "transferFromDetail" in notify:
            transfer_from_detail = TransferFromDetail()
            transfer_from_detail.parse_rsp_body(notify["transferFromDetail"])
            self.__transfer_from_detail = transfer_from_detail
        if "transferToDetail" in notify:
            transfer_to_detail = TransferToDetail()
            transfer_to_detail.parse_rsp_body(notify["transferToDetail"])
            self.__transfer_to_detail = transfer_to_detail