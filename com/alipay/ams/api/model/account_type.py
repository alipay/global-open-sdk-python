from enum import Enum, unique
@unique
class AccountType(Enum):
    """AccountType枚举类"""

    CHECKING = "CHECKING"
    FIXED_DEPOSIT = "FIXED_DEPOSIT"

    def to_ams_dict(self) -> str:
        return {
            "CHECKING": "CHECKING",
            "FIXED_DEPOSIT": "FIXED_DEPOSIT",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if AccountType.CHECKING.value == value:
            return AccountType.CHECKING
        if AccountType.FIXED_DEPOSIT.value == value:
            return AccountType.FIXED_DEPOSIT
        for member in AccountType:
            if member.to_ams_dict() == value:
                return member
        return None

