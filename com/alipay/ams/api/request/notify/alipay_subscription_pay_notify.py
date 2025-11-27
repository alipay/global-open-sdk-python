from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify
from com.alipay.ams.api.request.notify.alipay_pay_result_notify import (
    AlipayPayResultNotify,
)


class AlipaySubscriptionPayNotify(AlipayPayResultNotify):

    def __init__(self, notify_body):
        super(AlipaySubscriptionPayNotify, self).__init__(notify_body)
        self.__subscription_request_id = None
        self.__subscription_id = None
        self.__period_start_time = None
        self.__period_end_time = None
        self.__phase_no = None
        self.__parse_notify_body(notify_body)

    @property
    def subscription_request_id(self):
        return self.__subscription_request_id

    @property
    def subscription_id(self):
        return self.__subscription_id

    @property
    def period_start_time(self):
        return self.__period_start_time

    @property
    def period_end_time(self):
        return self.__period_end_time

    @property
    def phase_no(self):
        return self.__phase_no

    def __parse_notify_body(self, notify_body):
        notify = super(AlipaySubscriptionPayNotify, self).parse_notify_body(notify_body)
        if "subscriptionRequestId" in notify:
            self.__subscription_request_id = notify["subscriptionRequestId"]
        if "subscriptionId" in notify:
            self.__subscription_id = notify["subscriptionId"]
        if "periodStartTime" in notify:
            self.__period_start_time = notify["periodStartTime"]
        if "periodEndTime" in notify:
            self.__period_end_time = notify["periodEndTime"]
        if "phaseNo" in notify:
            self.__phase_no = notify["phaseNo"]
