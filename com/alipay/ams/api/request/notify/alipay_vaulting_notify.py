from com.alipay.ams.api.model.acquirer_info import AcquirerInfo
from com.alipay.ams.api.model.payment_method_detail import PaymentMethodDetail
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayVaultingNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayVaultingNotify, self).__init__()
        self.__vaulting_request_id = None
        self.__payment_method_detail = None  # type: PaymentMethodDetail
        self.__vaulting_create_time = None
        self.__acquirer_info = None  # type: AcquirerInfo
        self.__metadata = None  # type: str
        self.__parse_notify_body(notify_body)

    @property
    def vaulting_request_id(self):
        return self.__vaulting_request_id

    @property
    def payment_method_detail(self):
        return self.__payment_method_detail

    @property
    def vaulting_create_time(self):
        return self.__vaulting_create_time
    @property
    def metadata(self):
        return self.__metadata

    @property
    def acquirer_info(self):
        return self.__acquirer_info

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayVaultingNotify, self).parse_notify_body(notify_body)
        if "vaultingRequestId" in notify:
            self.__vaulting_request_id = notify["vaultingRequestId"]
        if "paymentMethodDetail" in notify:
            payment_method_detail = PaymentMethodDetail()
            payment_method_detail.parse_rsp_body(notify["paymentMethodDetail"])
            self.__payment_method_detail = payment_method_detail
        if "vaultingCreateTime" in notify:
            self.__vaulting_create_time = notify["vaultingCreateTime"]
        if "acquirerInfo" in notify:
            acquirer_info = AcquirerInfo()
            acquirer_info.parse_rsp_body(notify["acquirerInfo"])
            self.__acquirer_info = acquirer_info
        if "metadata" in notify:
            self.__metadata = notify["metadata"]