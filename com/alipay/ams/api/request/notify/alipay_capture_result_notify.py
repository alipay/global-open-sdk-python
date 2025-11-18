from com.alipay.ams.api.model.acquirer_info import AcquirerInfo
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayCaptureResultNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayCaptureResultNotify, self).__init__()
        self.__capture_request_id = None
        self.__payment_id = None
        self.__capture_id = None
        self.__capture_amount = None
        self.__capture_time = None
        self.__acquirer_reference_no = None
        self.__acquirer_info = None  # type: AcquirerInfo
        self.__parse_notify_body(notify_body)

    @property
    def capture_request_id(self):
        return self.__capture_request_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def capture_id(self):
        return self.__capture_id

    @property
    def capture_amount(self):
        return self.__capture_amount

    @property
    def capture_time(self):
        return self.__capture_time

    @property
    def acquirer_reference_no(self):
        return self.__acquirer_reference_no

    @property
    def acquirer_info(self):
        return self.__acquirer_info

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayCaptureResultNotify, self).parse_notify_body(notify_body)
        if "captureRequestId" in notify:
            self.__capture_request_id = notify["captureRequestId"]
        if "paymentId" in notify:
            self.__payment_id = notify["paymentId"]
        if "captureId" in notify:
            self.__capture_id = notify["captureId"]
        if "captureAmount" in notify:
            self.__capture_amount = notify["captureAmount"]
        if "captureTime" in notify:
            self.__capture_time = notify["captureTime"]
        if "acquirerReferenceNo" in notify:
            self.__acquirer_reference_no = notify["acquirerReferenceNo"]
        if "acquirerInfo" in notify:
            self.__acquirer_info = acquirer_info = AcquirerInfo()
            acquirer_info.parse_rsp_body(notify["acquirerInfo"])
