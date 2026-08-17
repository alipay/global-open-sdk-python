from enum import Enum, unique
@unique
class CardTransactionEventFilterType(Enum):
    """CardTransactionEventFilterType枚举类"""

    AUTH = "AUTH"
    AUTH_CANCEL = "AUTH_CANCEL"
    CAPTURE = "CAPTURE"
    REFUND = "REFUND"
    CHARGEBACK = "CHARGEBACK"
    REPAYMENT = "REPAYMENT"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CardTransactionEventFilterType.AUTH.value == value:
            return CardTransactionEventFilterType.AUTH
        if CardTransactionEventFilterType.AUTH_CANCEL.value == value:
            return CardTransactionEventFilterType.AUTH_CANCEL
        if CardTransactionEventFilterType.CAPTURE.value == value:
            return CardTransactionEventFilterType.CAPTURE
        if CardTransactionEventFilterType.REFUND.value == value:
            return CardTransactionEventFilterType.REFUND
        if CardTransactionEventFilterType.CHARGEBACK.value == value:
            return CardTransactionEventFilterType.CHARGEBACK
        if CardTransactionEventFilterType.REPAYMENT.value == value:
            return CardTransactionEventFilterType.REPAYMENT
        return None
