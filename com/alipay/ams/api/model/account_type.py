
from enum import Enum, unique


@unique
class AccountType(Enum):
    CHECKING = "CHECKING"
    FIXED_DEPOSIT = "FIXED_DEPOSIT"

    def to_ams_dict(self):
        return self.name
