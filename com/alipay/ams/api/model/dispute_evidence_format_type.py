from enum import Enum, unique
@unique
class DisputeEvidenceFormatType(Enum):
    """DisputeEvidenceFormatType枚举类"""

    PDF = "PDF"
    WORD = "WORD"
    ZIP = "ZIP"
    JPG = "JPG"

    def to_ams_dict(self) -> str:
        return {
            "PDF": "PDF",
            "WORD": "WORD",
            "ZIP": "ZIP",
            "JPG": "JPG",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DisputeEvidenceFormatType.PDF.value == value:
            return DisputeEvidenceFormatType.PDF
        if DisputeEvidenceFormatType.WORD.value == value:
            return DisputeEvidenceFormatType.WORD
        if DisputeEvidenceFormatType.ZIP.value == value:
            return DisputeEvidenceFormatType.ZIP
        if DisputeEvidenceFormatType.JPG.value == value:
            return DisputeEvidenceFormatType.JPG
        for member in DisputeEvidenceFormatType:
            if member.to_ams_dict() == value:
                return member
        return None

