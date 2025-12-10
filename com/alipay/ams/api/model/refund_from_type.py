from enum import Enum, unique
@unique
class RefundFromType(Enum):
    """RefundFromType枚举类"""

    SELLER = "SELLER"
    MARKETPLACE = "MARKETPLACE"
    UNSETTLED_FUNDS = "UNSETTLED_FUNDS"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if RefundFromType.SELLER.value == value:
            return RefundFromType.SELLER
        if RefundFromType.MARKETPLACE.value == value:
            return RefundFromType.MARKETPLACE
        if RefundFromType.UNSETTLED_FUNDS.value == value:
            return RefundFromType.UNSETTLED_FUNDS
        return None
