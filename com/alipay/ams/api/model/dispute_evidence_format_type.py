from enum import Enum, unique
@unique
class DisputeEvidenceFormatType(Enum):
    """DisputeEvidenceFormatType枚举类"""

    PDF = "PDF"
    WORD = "WORD"

    def to_ams_dict(self) -> str:
        return {
            "PDF": "PDF",
            "WORD": "WORD",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DisputeEvidenceFormatType.PDF.value == value:
            return DisputeEvidenceFormatType.PDF
        if DisputeEvidenceFormatType.WORD.value == value:
            return DisputeEvidenceFormatType.WORD
        for member in DisputeEvidenceFormatType:
            if member.to_ams_dict() == value:
                return member
        return None

