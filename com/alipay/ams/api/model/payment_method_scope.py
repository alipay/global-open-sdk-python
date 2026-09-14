from enum import Enum, unique
@unique
class PaymentMethodScope(Enum):
    """The payment method scope to which the reserve rule applies."""

    ALL = "ALL"
    CARD = "CARD"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PaymentMethodScope.ALL.value == value:
            return PaymentMethodScope.ALL
        if PaymentMethodScope.CARD.value == value:
            return PaymentMethodScope.CARD
        return None
