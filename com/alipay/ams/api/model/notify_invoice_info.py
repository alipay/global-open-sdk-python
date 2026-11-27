import json

from com.alipay.ams.api.model.amount import Amount


class NotifyInvoiceInfo:
    def __init__(self):

        self.__invoice_id = None  # type: str
        self.__invoice_status = None  # type: str
        self.__original_amount = None  # type: Amount
        self.__pre_payment_credit_notes_amount = None  # type: Amount
        self.__post_payment_credit_notes_amount = None  # type: Amount
        self.__adjusted_amount = None  # type: Amount


    @property
    def invoice_id(self):
        """The invoice ID adjusted by this credit note."""
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value

    @property
    def invoice_status(self):
        """The invoice status at the time of the credit note event."""
        return self.__invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self.__invoice_status = value

    @property
    def original_amount(self):
        """Immutable original invoice total at finalization."""
        return self.__original_amount

    @original_amount.setter
    def original_amount(self, value):
        self.__original_amount = value

    @property
    def pre_payment_credit_notes_amount(self):
        """Cumulative non-voided PRE_PAYMENT amount; reduces invoice total. Zero when none."""
        return self.__pre_payment_credit_notes_amount

    @pre_payment_credit_notes_amount.setter
    def pre_payment_credit_notes_amount(self, value):
        self.__pre_payment_credit_notes_amount = value

    @property
    def post_payment_credit_notes_amount(self):
        """Cumulative non-voided POST_PAYMENT amount, including processing/failed refunds until void.

        Does not change invoice total and is not the successfully-refunded amount.
        """
        return self.__post_payment_credit_notes_amount

    @post_payment_credit_notes_amount.setter
    def post_payment_credit_notes_amount(self, value):
        self.__post_payment_credit_notes_amount = value

    @property
    def adjusted_amount(self):
        """Current totalAmount after PRE_PAYMENT reductions; POST_PAYMENT refunds do not change it.

        Zero may transition the invoice to PAID.
        """
        return self.__adjusted_amount

    @adjusted_amount.setter
    def adjusted_amount(self, value):
        self.__adjusted_amount = value


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str):
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.invoice_id = response_body['invoiceId']
        if 'invoiceStatus' in response_body:
            self.invoice_status = response_body['invoiceStatus']
        fields = {
            'originalAmount': 'original_amount',
            'prePaymentCreditNotesAmount': 'pre_payment_credit_notes_amount',
            'postPaymentCreditNotesAmount': 'post_payment_credit_notes_amount',
            'adjustedAmount': 'adjusted_amount',
        }
        for wire_name, attribute in fields.items():
            if wire_name in response_body:
                amount = None
                if response_body[wire_name] is not None:
                    amount = Amount()
                    amount.parse_rsp_body(response_body[wire_name])
                setattr(self, attribute, amount)
