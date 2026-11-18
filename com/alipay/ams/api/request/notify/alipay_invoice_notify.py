from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.invoice_payment_info import InvoicePaymentInfo
from com.alipay.ams.api.model.subscription_info import SubscriptionInfo


class AlipayInvoiceNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayInvoiceNotify, self).__init__()
        self.__invoice_request_id = None  # type: str
        self.__invoice_id = None  # type: str
        self.__invoice_status = None  # type: str
        self.__invoice_amount = None  # type: Amount
        self.__payment_info = None  # type: InvoicePaymentInfo
        self.__subscription = None  # type: SubscriptionInfo
        self.__customer_id = None  # type: str
        self.__reason = None  # type: str
        self.__reason_description = None  # type: str
        self.__parse_notify_body(notify_body)

    @property
    def invoice_request_id(self):
        return self.__invoice_request_id

    @invoice_request_id.setter
    def invoice_request_id(self, value):
        self.__invoice_request_id = value

    @property
    def invoice_id(self):
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value

    @property
    def invoice_status(self):
        return self.__invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self.__invoice_status = value

    @property
    def invoice_amount(self):
        return self.__invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self.__invoice_amount = value

    @property
    def payment_info(self):
        return self.__payment_info

    @payment_info.setter
    def payment_info(self, value):
        self.__payment_info = value

    @property
    def subscription(self):
        return self.__subscription

    @subscription.setter
    def subscription(self, value):
        self.__subscription = value

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

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

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayInvoiceNotify, self).parse_notify_body(notify_body)
        if "invoiceRequestId" in notify:
            self.__invoice_request_id = notify["invoiceRequestId"]
        if "invoiceId" in notify:
            self.__invoice_id = notify["invoiceId"]
        if "invoiceStatus" in notify:
            self.__invoice_status = notify["invoiceStatus"]
        if "invoiceAmount" in notify:
            self.__invoice_amount = Amount()
            self.__invoice_amount.parse_rsp_body(notify["invoiceAmount"])
        if "paymentInfo" in notify:
            self.__payment_info = InvoicePaymentInfo()
            payment_info_data = notify["paymentInfo"]
            if "result" in payment_info_data:
                from com.alipay.ams.api.model.result import Result
                self.__payment_info.result = Result()
                self.__payment_info.result.parse_rsp_body(payment_info_data["result"])
            if "paymentId" in payment_info_data:
                self.__payment_info.payment_id = payment_info_data["paymentId"]
            if "paymentAmount" in payment_info_data:
                self.__payment_info.payment_amount = Amount()
                self.__payment_info.payment_amount.parse_rsp_body(payment_info_data["paymentAmount"])
            if "paymentTime" in payment_info_data:
                self.__payment_info.payment_time = payment_info_data["paymentTime"]
        if "subscription" in notify:
            self.__subscription = SubscriptionInfo()
            self.__subscription.parse_rsp_body(notify["subscription"])
        if "customerId" in notify:
            self.__customer_id = notify["customerId"]
        if "reason" in notify:
            self.__reason = notify["reason"]
        if "reasonDescription" in notify:
            self.__reason_description = notify["reasonDescription"]
