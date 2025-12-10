from enum import Enum, unique
@unique
class ChallengeTriggerSourceType(Enum):
    """ChallengeTriggerSourceType枚举类"""

    AMS = "AMS"
    CHANNEL = "CHANNEL"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ChallengeTriggerSourceType.AMS.value == value:
            return ChallengeTriggerSourceType.AMS
        if ChallengeTriggerSourceType.CHANNEL.value == value:
            return ChallengeTriggerSourceType.CHANNEL
        return None
