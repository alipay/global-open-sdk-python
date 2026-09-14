from enum import Enum, unique
@unique
class ReleaseType(Enum):
    """The release schedule type. FIXED_TIME uses releaseTime and INTERVAL_TIME uses retentionTime."""

    FIXED_TIME = "FIXED_TIME"
    INTERVAL_TIME = "INTERVAL_TIME"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ReleaseType.FIXED_TIME.value == value:
            return ReleaseType.FIXED_TIME
        if ReleaseType.INTERVAL_TIME.value == value:
            return ReleaseType.INTERVAL_TIME
        return None
