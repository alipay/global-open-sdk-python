from enum import Enum, unique


@unique
class CreditPayFeeType(Enum):
    PERCENTAGE = "PERCENTAGE"

    def to_ams_dict(self):
        return self.name
