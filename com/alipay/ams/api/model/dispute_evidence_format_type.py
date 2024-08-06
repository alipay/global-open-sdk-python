from enum import Enum, unique


@unique
class DisputeEvidenceFormatType(Enum):
    PDF = "PDF"
    WORD = "WORD"

    def to_ams_dict(self):
        return self.name
