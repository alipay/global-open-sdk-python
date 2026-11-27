from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify
from com.alipay.ams.api.model.credit_note_info import CreditNoteInfo
from com.alipay.ams.api.model.notify_invoice_info import NotifyInvoiceInfo


class AlipayCreditNoteNotify(AlipayNotify):
    """CREDIT_NOTE_RESULT payload; inherited result uses the shared Antom Result.

    ACK is a separate Result envelope: SUCCESS / S / success.
    Delivery deduplication uses outer notify_id, never a notify_body member.
    """

    def __init__(self, notify_body):
        super(AlipayCreditNoteNotify, self).__init__()
        self.__credit_note_request_id = None  # type: str
        self.__credit_note_notification_type = None  # type: str
        self.__customer_id = None  # type: str
        self.__credit_note = None  # type: CreditNoteInfo
        self.__invoice = None  # type: NotifyInvoiceInfo
        self.__parse_notify_body(notify_body)

    @property
    def credit_note_request_id(self):
        """Required creation request ID shared by all events; correlation, not deduplication."""
        return self.__credit_note_request_id

    @credit_note_request_id.setter
    def credit_note_request_id(self, value):
        self.__credit_note_request_id = value

    @property
    def credit_note_notification_type(self):
        return self.__credit_note_notification_type

    @credit_note_notification_type.setter
    def credit_note_notification_type(self, value):
        self.__credit_note_notification_type = value

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def credit_note(self):
        return self.__credit_note

    @credit_note.setter
    def credit_note(self, value):
        self.__credit_note = value

    @property
    def invoice(self):
        return self.__invoice

    @invoice.setter
    def invoice(self, value):
        self.__invoice = value

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayCreditNoteNotify, self).parse_notify_body(notify_body)
        if "creditNoteRequestId" in notify:
            self.__credit_note_request_id = notify["creditNoteRequestId"]
        if "creditNoteNotificationType" in notify:
            self.__credit_note_notification_type = notify["creditNoteNotificationType"]
        if "customerId" in notify:
            self.__customer_id = notify["customerId"]
        if notify.get("creditNote") is not None:
            self.__credit_note = CreditNoteInfo()
            self.__credit_note.parse_rsp_body(notify["creditNote"])
        if notify.get("invoice") is not None:
            self.__invoice = NotifyInvoiceInfo()
            self.__invoice.parse_rsp_body(notify["invoice"])
