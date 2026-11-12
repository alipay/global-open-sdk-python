from enum import Enum, unique
@unique
class DisputeEvidenceType(Enum):
    """DisputeEvidenceType枚举类"""

    TEMPLATE = "TEMPLATE"
    FILE = "FILE"
    AI = "AI"

    def to_ams_dict(self) -> str:
        if self is DisputeEvidenceType.AI:
            return "DISPUTE_EVIDENCE_AI"
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DisputeEvidenceType.TEMPLATE.value == value:
            return DisputeEvidenceType.TEMPLATE
        if DisputeEvidenceType.FILE.value == value:
            return DisputeEvidenceType.FILE
        if value in (DisputeEvidenceType.AI.value, "DISPUTE_EVIDENCE_AI"):
            return DisputeEvidenceType.AI
        return None
