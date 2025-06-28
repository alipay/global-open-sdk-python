from enum import Enum, unique
@unique
class DisputeEvidenceType(Enum):
    """DisputeEvidenceType枚举类"""

    TEMPLATE = "TEMPLATE"
    FILE = "FILE"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DisputeEvidenceType.TEMPLATE.value == value:
            return DisputeEvidenceType.TEMPLATE
        if DisputeEvidenceType.FILE.value == value:
            return DisputeEvidenceType.FILE
        return None
