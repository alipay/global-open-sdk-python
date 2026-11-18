from enum import Enum, unique
@unique
class PromotionType(Enum):
    """PromotionType枚举类"""

    DISCOUNT = "DISCOUNT"
    INTEREST_FREE = "INTEREST_FREE"

    def to_ams_dict(self) -> str:
        return {
            "DISCOUNT": "DISCOUNT",
            "INTEREST_FREE": "INTEREST_FREE",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PromotionType.DISCOUNT.value == value:
            return PromotionType.DISCOUNT
        if PromotionType.INTEREST_FREE.value == value:
            return PromotionType.INTEREST_FREE
        for member in PromotionType:
            if member.to_ams_dict() == value:
                return member
        return None

