from enum import Enum, unique
@unique
class PaymentMethodScope(Enum):
    """The payment method scope to which the reserve rule applies."""

    ALL = "ALL"
    CARD = "CARD"

    def to_ams_dict(self) -> str:
        return {
            "ALL": "ALL",
            "CARD": "CARD",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PaymentMethodScope.ALL.value == value:
            return PaymentMethodScope.ALL
        if PaymentMethodScope.CARD.value == value:
            return PaymentMethodScope.CARD
        for member in PaymentMethodScope:
            if member.to_ams_dict() == value:
                return member
        return None

