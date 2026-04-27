from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.refund_from_method import RefundFromMethod
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayDirectRefundNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayDirectRefundNotify, self).__init__()
        self.__refund_status = None
        self.__refund_id = None
        self.__payment_id = None
        self.__refund_request_id = None
        self.__refund_time = None
        self.__refund_from_method = None  # type: RefundFromMethod
        self.__refund_to_amount = None  # type: Amount
        self.__refund_from_amount = None  # type: Amount
        self.__parse_notify_body(notify_body)

    @property
    def refund_status(self):
        return self.__refund_status

    @property
    def refund_id(self):
        return self.__refund_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def refund_request_id(self):
        return self.__refund_request_id

    @property
    def refund_time(self):
        return self.__refund_time

    @property
    def refund_from_method(self):
        return self.__refund_from_method

    @property
    def refund_to_amount(self):
        return self.__refund_to_amount

    @property
    def refund_from_amount(self):
        return self.__refund_from_amount

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayDirectRefundNotify, self).parse_notify_body(notify_body)
        if "refundStatus" in notify:
            self.__refund_status = notify["refundStatus"]
        if "refundId" in notify:
            self.__refund_id = notify["refundId"]
        if "paymentId" in notify:
            self.__payment_id = notify["paymentId"]
        if "refundRequestId" in notify:
            self.__refund_request_id = notify["refundRequestId"]
        if "refundTime" in notify:
            self.__refund_time = notify["refundTime"]
        if "refundFromMethod" in notify:
            refund_from_method = RefundFromMethod()
            refund_from_method.parse_rsp_body(notify["refundFromMethod"])
            self.__refund_from_method = refund_from_method
        if "refundToAmount" in notify:
            self.__refund_to_amount = Amount(notify["refundToAmount"])
        if "refundFromAmount" in notify:
            self.__refund_from_amount = Amount(notify["refundFromAmount"])
