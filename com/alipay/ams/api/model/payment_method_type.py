
from enum import Enum, unique


@unique
class PaymentMethodType(Enum):
    DISCOUNT = "DISCOUNT"
    INTEREST_FREE = "INTEREST_FREE"
    BALANCE_ACCOUNT = "BALANCE_ACCOUNT"
    SETTLEMENT_CARD = "SETTLEMENT_CARD"
    def to_ams_dict(self):
        return self.name