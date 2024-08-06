from enum import Enum, unique


@unique
class RefundFromType(Enum):
    SELLER = "SELLER"
    MARKETPLACE = "MARKETPLACE"
    UNSETTLED_FUNDS = "UNSETTLED_FUNDS"

    def to_ams_dict(self):
        return self.name
