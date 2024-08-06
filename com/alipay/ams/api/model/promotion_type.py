from enum import Enum, unique


@unique
class PromotionType(Enum):
    DISCOUNT = "DISCOUNT"
    INTEREST_FREE = "INTEREST_FREE"

    def to_ams_dict(self):
        return self.name
