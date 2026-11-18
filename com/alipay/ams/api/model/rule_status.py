from enum import Enum, unique
@unique
class RuleStatus(Enum):
    """The reserve rule configuration status. This status does not indicate whether retained funds have been released."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"

    def to_ams_dict(self) -> str:
        return {
            "ACTIVE": "ACTIVE",
            "DISABLED": "DISABLED",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if RuleStatus.ACTIVE.value == value:
            return RuleStatus.ACTIVE
        if RuleStatus.DISABLED.value == value:
            return RuleStatus.DISABLED
        for member in RuleStatus:
            if member.to_ams_dict() == value:
                return member
        return None

