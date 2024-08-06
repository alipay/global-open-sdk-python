from enum import Enum, unique


@unique
class FundingType(Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"


PREPAID = "PREPAID"
CHARGE = "CHARGE"
DEFERRED_DEBIT = "DEFERRED_DEBIT"


def to_ams_dict(self):
    return self.name
