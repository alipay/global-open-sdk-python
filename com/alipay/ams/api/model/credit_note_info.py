import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.credit_note_item import CreditNoteItem


class CreditNoteInfo:
    """Notification projection without detail-only merchant metadata."""
    def __init__(self):

        self.__credit_note_id = None  # type: str
        self.__type = None  # type: str
        self.__status = None  # type: str
        self.__total_amount = None  # type: Amount
        self.__refund_amount = None  # type: Amount
        self.__refund_status = None  # type: str
        self.__refund_id = None  # type: str
        self.__refund_destination = None  # type: str
        self.__reason = None  # type: str
        self.__reason_description = None  # type: str
        self.__memo = None  # type: str
        self.__effective_date = None  # type: str
        self.__issued_at = None  # type: str
        self.__refunded_at = None  # type: str
        self.__voided_at = None  # type: str
        self.__created_at = None  # type: str
        self.__items = None  # type: [CreditNoteNotificationLineItem]


    @property
    def credit_note_id(self):
        """The credit note ID. Maximum length: 64 characters."""
        return self.__credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, value):
        self.__credit_note_id = value

    @property
    def type(self):
        """The credit note type. Valid values: POST_PAYMENT, PRE_PAYMENT."""
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def status(self):
        """The current status. Valid values: ISSUED, PROCESSING, REFUNDED, REFUND_FAILED, VOIDED."""
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def total_amount(self):
        """The total credit note amount."""
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value

    @property
    def refund_amount(self):
        """Optional planned original-method refund for refund-bearing POST_PAYMENT.

        Absent/null for note-only POST_PAYMENT and PRE_PAYMENT; not proof of completion.
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value

    @property
    def refund_status(self):
        """Optional REFUND_INITIATED, REFUND_SUCCEEDED or REFUND_FAILED progress.

        Absent/null before progress or for note-only notes; PRE_PAYMENT may use NOT_APPLICABLE.
        """
        return self.__refund_status

    @refund_status.setter
    def refund_status(self, value):
        self.__refund_status = value

    @property
    def refund_id(self):
        """Optional payment-system reference when obtained; alone does not prove success.

        Absent/null beforehand, for note-only POST_PAYMENT and PRE_PAYMENT.
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = value

    @property
    def refund_destination(self):
        """Optional REFUND routing supplied at creation; null when omitted."""
        return self.__refund_destination

    @refund_destination.setter
    def refund_destination(self, value):
        self.__refund_destination = value

    @property
    def reason(self):
        """The structured reason code."""
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value

    @property
    def reason_description(self):
        """The free-text description of the reason."""
        return self.__reason_description

    @reason_description.setter
    def reason_description(self, value):
        self.__reason_description = value

    @property
    def memo(self):
        """The customer-visible memo shown on the credit note PDF."""
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value

    @property
    def effective_date(self):
        """The effective date of the credit note. ISO 8601 format."""
        return self.__effective_date

    @effective_date.setter
    def effective_date(self, value):
        self.__effective_date = value

    @property
    def issued_at(self):
        """The issuance timestamp. ISO 8601 format."""
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, value):
        self.__issued_at = value

    @property
    def refunded_at(self):
        """The refund timestamp. Present when status is REFUNDED."""
        return self.__refunded_at

    @refunded_at.setter
    def refunded_at(self, value):
        self.__refunded_at = value

    @property
    def voided_at(self):
        """The void timestamp. Present when status is VOIDED."""
        return self.__voided_at

    @voided_at.setter
    def voided_at(self, value):
        self.__voided_at = value

    @property
    def created_at(self):
        """The creation timestamp. ISO 8601 format."""
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def items(self):
        """Optional notification line items, at most 100; service returns [] when absent."""
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str):
            response_body = json.loads(response_body)
        fields = {
            'creditNoteId': 'credit_note_id',
            'type': 'type',
            'status': 'status',
            'refundStatus': 'refund_status',
            'refundId': 'refund_id',
            'refundDestination': 'refund_destination',
            'reason': 'reason',
            'reasonDescription': 'reason_description',
            'memo': 'memo',
            'effectiveDate': 'effective_date',
            'issuedAt': 'issued_at',
            'refundedAt': 'refunded_at',
            'voidedAt': 'voided_at',
            'createdAt': 'created_at',
        }
        for wire_name, attribute in fields.items():
            if wire_name in response_body:
                setattr(self, attribute, response_body[wire_name])
        for wire_name, attribute in [('totalAmount', 'total_amount'), ('refundAmount', 'refund_amount')]:
            if wire_name in response_body:
                amount = None
                if response_body[wire_name] is not None:
                    amount = Amount()
                    amount.parse_rsp_body(response_body[wire_name])
                setattr(self, attribute, amount)
        if 'items' in response_body:
            self.items = None
            if response_body['items'] is not None:
                self.items = []
                for item_body in response_body['items']:
                    item = CreditNoteNotificationLineItem()
                    item.parse_rsp_body(item_body)
                    self.items.append(item)


class CreditNoteNotificationLineItem(CreditNoteItem):
    """Notification projection reusing compatible item fields, without detail-only metadata."""

    def __init__(self):
        super(CreditNoteNotificationLineItem, self).__init__()
        self.__direction = None  # type: str

    @property
    def direction(self):
        """Required open C (credit) or D (debit); D itemAmount subtracts from credit total."""
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str):
            response_body = json.loads(response_body)
        # Optional null amounts must not be passed to the shared Amount parser.
        fields = {key: value for key, value in response_body.items() if value is not None}
        super(CreditNoteNotificationLineItem, self).parse_rsp_body(fields)
        if 'direction' in response_body:
            self.direction = response_body['direction']

    def to_ams_dict(self):
        params = super(CreditNoteNotificationLineItem, self).to_ams_dict()
        if self.direction is not None:
            params['direction'] = self.direction
        return params
