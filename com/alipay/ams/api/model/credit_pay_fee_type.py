from enum import Enum, unique
@unique
class CreditPayFeeType(Enum):
    """CreditPayFeeType枚举类"""

    PERCENTAGE = "PERCENTAGE"

    def to_ams_dict(self) -> str:
        return {
            "PERCENTAGE": "PERCENTAGE",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CreditPayFeeType.PERCENTAGE.value == value:
            return CreditPayFeeType.PERCENTAGE
        for member in CreditPayFeeType:
            if member.to_ams_dict() == value:
                return member
        return None

