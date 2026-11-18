from enum import Enum, unique
@unique
class ChallengeTriggerSourceType(Enum):
    """ChallengeTriggerSourceType枚举类"""

    AMS = "AMS"
    CHANNEL = "CHANNEL"

    def to_ams_dict(self) -> str:
        return {
            "AMS": "AMS",
            "CHANNEL": "CHANNEL",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ChallengeTriggerSourceType.AMS.value == value:
            return ChallengeTriggerSourceType.AMS
        if ChallengeTriggerSourceType.CHANNEL.value == value:
            return ChallengeTriggerSourceType.CHANNEL
        for member in ChallengeTriggerSourceType:
            if member.to_ams_dict() == value:
                return member
        return None

