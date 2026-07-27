from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayBillingSubscriptionNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayBillingSubscriptionNotify, self).__init__()
        self.__merchant_request_id = None  # type: str
        self.__event_time = None  # type: str
        self.__subscription_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__status = None  # type: str
        self.__reason = None  # type: str
        self.__reason_description = None  # type: str
        self.__previous_status = None  # type: str
        self.__parse_notify_body(notify_body)

    @property
    def merchant_request_id(self):
        return self.__merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self.__merchant_request_id = value

    @property
    def event_time(self):
        return self.__event_time

    @event_time.setter
    def event_time(self, value):
        self.__event_time = value

    @property
    def subscription_id(self):
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value

    @property
    def invoice_id(self):
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value

    @property
    def reason_description(self):
        return self.__reason_description

    @reason_description.setter
    def reason_description(self, value):
        self.__reason_description = value

    @property
    def previous_status(self):
        return self.__previous_status

    @previous_status.setter
    def previous_status(self, value):
        self.__previous_status = value

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayBillingSubscriptionNotify, self).parse_notify_body(notify_body)
        if "merchantRequestId" in notify:
            self.__merchant_request_id = notify["merchantRequestId"]
        if "eventTime" in notify:
            self.__event_time = notify["eventTime"]
        if "subscriptionId" in notify:
            self.__subscription_id = notify["subscriptionId"]
        if "invoiceId" in notify:
            self.__invoice_id = notify["invoiceId"]
        if "status" in notify:
            self.__status = notify["status"]
        if "reason" in notify:
            self.__reason = notify["reason"]
        if "reasonDescription" in notify:
            self.__reason_description = notify["reasonDescription"]
        if "previousStatus" in notify:
            self.__previous_status = notify["previousStatus"]
