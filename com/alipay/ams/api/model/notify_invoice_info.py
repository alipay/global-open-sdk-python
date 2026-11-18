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
        """The original invoice total amount before any credit notes."""
        return self.__original_amount

    @original_amount.setter
    def original_amount(self, value):
        self.__original_amount = value

    @property
    def pre_payment_credit_notes_amount(self):
        """The cumulative amount of all PRE_PAYMENT credit notes applied."""
        return self.__pre_payment_credit_notes_amount

    @pre_payment_credit_notes_amount.setter
    def pre_payment_credit_notes_amount(self, value):
        self.__pre_payment_credit_notes_amount = value

    @property
    def post_payment_credit_notes_amount(self):
        """The cumulative refunded amount of all POST_PAYMENT credit notes."""
        return self.__post_payment_credit_notes_amount

    @post_payment_credit_notes_amount.setter
    def post_payment_credit_notes_amount(self, value):
        self.__post_payment_credit_notes_amount = value

    @property
    def adjusted_amount(self):
        """The current invoice total after all PRE_PAYMENT adjustments."""
        return self.__adjusted_amount

    @adjusted_amount.setter
    def adjusted_amount(self, value):
        self.__adjusted_amount = value
