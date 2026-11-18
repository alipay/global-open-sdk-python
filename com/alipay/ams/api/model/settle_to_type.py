from enum import Enum, unique
@unique
class SettleToType(Enum):
    """SettleToType枚举类"""

    SELLER = "SELLER"
    MARKETPLACE = "MARKETPLACE"

    def to_ams_dict(self) -> str:
        return {
            "SELLER": "SELLER",
            "MARKETPLACE": "MARKETPLACE",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if SettleToType.SELLER.value == value:
            return SettleToType.SELLER
        if SettleToType.MARKETPLACE.value == value:
            return SettleToType.MARKETPLACE
        for member in SettleToType:
            if member.to_ams_dict() == value:
                return member
        return None

