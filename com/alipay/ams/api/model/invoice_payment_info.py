from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.amount import Amount


class InvoicePaymentInfo:
    def __init__(self):

        self.__result = None  # type: Result
        self.__payment_id = None  # type: str
        self.__payment_amount = None  # type: Amount
        self.__payment_time = None  # type: str


    @property
    def result(self):
        """Payment result details. resultStatus=S for success, F for failure."""
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    @property
    def payment_id(self):
        """The unique ID assigned by Antom to identify the payment for this invoice."""
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def payment_amount(self):
        """The payment amount."""
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value

    @property
    def payment_time(self):
        """The date and time when the payment reached a final state of success. ISO 8601 format."""
        return self.__payment_time

    @payment_time.setter
    def payment_time(self, value):
        self.__payment_time = value
