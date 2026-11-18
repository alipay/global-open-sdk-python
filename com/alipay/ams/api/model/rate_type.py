from enum import Enum, unique
@unique
class RateType(Enum):
    """RateType枚举类"""

    TRADE = "TRADE"
    REFERENCE = "REFERENCE"
    REFERENCE_TRADE = "REFERENCE_TRADE"

    def to_ams_dict(self) -> str:
        return {
            "TRADE": "TRADE",
            "REFERENCE": "REFERENCE",
            "REFERENCE_TRADE": "REFERENCE_TRADE",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if RateType.TRADE.value == value:
            return RateType.TRADE
        if RateType.REFERENCE.value == value:
            return RateType.REFERENCE
        if RateType.REFERENCE_TRADE.value == value:
            return RateType.REFERENCE_TRADE
        for member in RateType:
            if member.to_ams_dict() == value:
                return member
        return None

