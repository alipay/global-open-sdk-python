from enum import Enum, unique
@unique
class CardTransactionStatusFilterType(Enum):
    """CardTransactionStatusFilterType枚举类"""

    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    PROCESSING = "PROCESSING"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CardTransactionStatusFilterType.SUCCESS.value == value:
            return CardTransactionStatusFilterType.SUCCESS
        if CardTransactionStatusFilterType.FAIL.value == value:
            return CardTransactionStatusFilterType.FAIL
        if CardTransactionStatusFilterType.PROCESSING.value == value:
            return CardTransactionStatusFilterType.PROCESSING
        return None
