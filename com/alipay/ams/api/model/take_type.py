from enum import Enum, unique
@unique
class TakeType(Enum):
    """The collateral collection type. The current version supports ROLLING only."""

    ROLLING = "ROLLING"

    def to_ams_dict(self) -> str:
        return {
            "ROLLING": "ROLLING",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TakeType.ROLLING.value == value:
            return TakeType.ROLLING
        for member in TakeType:
            if member.to_ams_dict() == value:
                return member
        return None

