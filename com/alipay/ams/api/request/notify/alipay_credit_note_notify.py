from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify
from com.alipay.ams.api.model.credit_note_info import CreditNoteInfo
from com.alipay.ams.api.model.notify_invoice_info import NotifyInvoiceInfo


class AlipayCreditNoteNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayCreditNoteNotify, self).__init__()
        self.__notify_id = None  # type: str
        self.__credit_note_request_id = None  # type: str
        self.__credit_note_notification_type = None  # type: str
        self.__customer_id = None  # type: str
        self.__credit_note = None  # type: CreditNoteInfo
        self.__invoice = None  # type: NotifyInvoiceInfo
        self.__parse_notify_body(notify_body)

    @property
    def notify_id(self):
        return self.__notify_id

    @notify_id.setter
    def notify_id(self, value):
        self.__notify_id = value

    @property
    def credit_note_request_id(self):
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
        if "notifyId" in notify:
            self.__notify_id = notify["notifyId"]
        if "creditNoteRequestId" in notify:
            self.__credit_note_request_id = notify["creditNoteRequestId"]
        if "creditNoteNotificationType" in notify:
            self.__credit_note_notification_type = notify["creditNoteNotificationType"]
        if "customerId" in notify:
            self.__customer_id = notify["customerId"]
        if "creditNote" in notify:
            self.__credit_note = CreditNoteInfo()
            # parse creditNote fields
            cn = notify["creditNote"]
            if "creditNoteId" in cn:
                self.__credit_note.credit_note_id = cn["creditNoteId"]
            if "type" in cn:
                self.__credit_note.type = cn["type"]
            if "status" in cn:
                self.__credit_note.status = cn["status"]
            if "totalAmount" in cn:
                from com.alipay.ams.api.model.amount import Amount
                self.__credit_note.total_amount = Amount()
                self.__credit_note.total_amount.parse_rsp_body(cn["totalAmount"])
            if "refundAmount" in cn:
                from com.alipay.ams.api.model.amount import Amount
                self.__credit_note.refund_amount = Amount()
                self.__credit_note.refund_amount.parse_rsp_body(cn["refundAmount"])
            if "refundStatus" in cn:
                self.__credit_note.refund_status = cn["refundStatus"]
            if "refundId" in cn:
                self.__credit_note.refund_id = cn["refundId"]
            if "refundDestination" in cn:
                self.__credit_note.refund_destination = cn["refundDestination"]
            if "reason" in cn:
                self.__credit_note.reason = cn["reason"]
            if "reasonDescription" in cn:
                self.__credit_note.reason_description = cn["reasonDescription"]
            if "memo" in cn:
                self.__credit_note.memo = cn["memo"]
            if "effectiveDate" in cn:
                self.__credit_note.effective_date = cn["effectiveDate"]
            if "issuedAt" in cn:
                self.__credit_note.issued_at = cn["issuedAt"]
            if "refundedAt" in cn:
                self.__credit_note.refunded_at = cn["refundedAt"]
            if "voidedAt" in cn:
                self.__credit_note.voided_at = cn["voidedAt"]
            if "createdAt" in cn:
                self.__credit_note.created_at = cn["createdAt"]
        if "invoice" in notify:
            self.__invoice = NotifyInvoiceInfo()
            inv = notify["invoice"]
            if "invoiceId" in inv:
                self.__invoice.invoice_id = inv["invoiceId"]
            if "invoiceStatus" in inv:
                self.__invoice.invoice_status = inv["invoiceStatus"]
            if "originalAmount" in inv:
                from com.alipay.ams.api.model.amount import Amount
                self.__invoice.original_amount = Amount()
                self.__invoice.original_amount.parse_rsp_body(inv["originalAmount"])
            if "prePaymentCreditNotesAmount" in inv:
                from com.alipay.ams.api.model.amount import Amount
                self.__invoice.pre_payment_credit_notes_amount = Amount()
                self.__invoice.pre_payment_credit_notes_amount.parse_rsp_body(inv["prePaymentCreditNotesAmount"])
            if "postPaymentCreditNotesAmount" in inv:
                from com.alipay.ams.api.model.amount import Amount
                self.__invoice.post_payment_credit_notes_amount = Amount()
                self.__invoice.post_payment_credit_notes_amount.parse_rsp_body(inv["postPaymentCreditNotesAmount"])
            if "adjustedAmount" in inv:
                from com.alipay.ams.api.model.amount import Amount
                self.__invoice.adjusted_amount = Amount()
                self.__invoice.adjusted_amount.parse_rsp_body(inv["adjustedAmount"])
