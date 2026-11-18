from enum import Enum, unique
@unique
class FundsType(Enum):
    """The funds type. The current version supports COLLATERAL only."""

    COLLATERAL = "COLLATERAL"

    def to_ams_dict(self) -> str:
        return {
            "COLLATERAL": "COLLATERAL",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if FundsType.COLLATERAL.value == value:
            return FundsType.COLLATERAL
        for member in FundsType:
            if member.to_ams_dict() == value:
                return member
        return None

