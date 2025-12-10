from enum import Enum, unique
@unique
class SettleToType(Enum):
    """SettleToType枚举类"""

    SELLER = "SELLER"
    MARKETPLACE = "MARKETPLACE"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if SettleToType.SELLER.value == value:
            return SettleToType.SELLER
        if SettleToType.MARKETPLACE.value == value:
            return SettleToType.MARKETPLACE
        return None
