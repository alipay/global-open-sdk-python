from enum import Enum, unique
@unique
class DisputeEvidenceType(Enum):
    """DisputeEvidenceType枚举类"""

    TEMPLATE = "TEMPLATE"
    FILE = "FILE"
    AI = "AI"

    def to_ams_dict(self) -> str:
        return {
            "TEMPLATE": "DISPUTE_EVIDENCE_TEMPLATE",
            "FILE": "DISPUTE_EVIDENCE_FILE",
            "AI": "DISPUTE_EVIDENCE_AI",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DisputeEvidenceType.TEMPLATE.value == value:
            return DisputeEvidenceType.TEMPLATE
        if DisputeEvidenceType.FILE.value == value:
            return DisputeEvidenceType.FILE
        if DisputeEvidenceType.AI.value == value:
            return DisputeEvidenceType.AI
        for member in DisputeEvidenceType:
            if member.to_ams_dict() == value:
                return member
        return None

