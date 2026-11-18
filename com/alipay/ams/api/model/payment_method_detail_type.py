from enum import Enum, unique
@unique
class PaymentMethodDetailType(Enum):
    """PaymentMethodDetailType枚举类"""

    CARD = "CARD"
    EXTERNALACCOUNT = "EXTERNALACCOUNT"
    COUPON = "COUPON"
    DISCOUNT = "DISCOUNT"

    def to_ams_dict(self) -> str:
        return {
            "CARD": "CARD",
            "EXTERNALACCOUNT": "EXTERNALACCOUNT",
            "COUPON": "COUPON",
            "DISCOUNT": "DISCOUNT",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PaymentMethodDetailType.CARD.value == value:
            return PaymentMethodDetailType.CARD
        if PaymentMethodDetailType.EXTERNALACCOUNT.value == value:
            return PaymentMethodDetailType.EXTERNALACCOUNT
        if PaymentMethodDetailType.COUPON.value == value:
            return PaymentMethodDetailType.COUPON
        if PaymentMethodDetailType.DISCOUNT.value == value:
            return PaymentMethodDetailType.DISCOUNT
        for member in PaymentMethodDetailType:
            if member.to_ams_dict() == value:
                return member
        return None

