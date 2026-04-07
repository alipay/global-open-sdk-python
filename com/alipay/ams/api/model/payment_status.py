from enum import Enum, unique
@unique
class PaymentStatus(Enum):
    """Indicates the payment status. Valid values are: - SUCCESS: Indicates that the payment succeeds. - FAIL: Indicates that the payment fails."""

    SUCCESS = "SUCCESS"
    FAIL = "FAIL"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PaymentStatus.SUCCESS.value == value:
            return PaymentStatus.SUCCESS
        if PaymentStatus.FAIL.value == value:
            return PaymentStatus.FAIL
        return None
