from enum import Enum, unique
@unique
class TakeType(Enum):
    """The collateral collection type. The current version supports ROLLING only."""

    ROLLING = "ROLLING"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TakeType.ROLLING.value == value:
            return TakeType.ROLLING
        return None
