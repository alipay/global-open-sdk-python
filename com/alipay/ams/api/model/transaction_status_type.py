from enum import Enum, unique
@unique
class TransactionStatusType(Enum):
    """TransactionStatusType枚举类"""

    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    PROCESSING = "PROCESSING"
    CANCELLED = "CANCELLED"
    PENDING = "PENDING"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TransactionStatusType.SUCCESS.value == value:
            return TransactionStatusType.SUCCESS
        if TransactionStatusType.FAIL.value == value:
            return TransactionStatusType.FAIL
        if TransactionStatusType.PROCESSING.value == value:
            return TransactionStatusType.PROCESSING
        if TransactionStatusType.CANCELLED.value == value:
            return TransactionStatusType.CANCELLED
        if TransactionStatusType.PENDING.value == value:
            return TransactionStatusType.PENDING
        return None
