from enum import Enum, unique
@unique
class TransactionType(Enum):
    """TransactionType枚举类"""

    PAYMENT = "PAYMENT"
    REFUND = "REFUND"
    CAPTURE = "CAPTURE"
    CANCEL = "CANCEL"
    AUTHORIZATION = "AUTHORIZATION"
    VOID = "VOID"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TransactionType.PAYMENT.value == value:
            return TransactionType.PAYMENT
        if TransactionType.REFUND.value == value:
            return TransactionType.REFUND
        if TransactionType.CAPTURE.value == value:
            return TransactionType.CAPTURE
        if TransactionType.CANCEL.value == value:
            return TransactionType.CANCEL
        if TransactionType.AUTHORIZATION.value == value:
            return TransactionType.AUTHORIZATION
        if TransactionType.VOID.value == value:
            return TransactionType.VOID
        return None
