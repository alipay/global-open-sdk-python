from enum import Enum, unique


@unique
class DisputeEvidenceType(Enum):
    DISPUTE_EVIDENCE_TEMPLATE = "DISPUTE_EVIDENCE_TEMPLATE"
    DISPUTE_EVIDENCE_FILE = "DISPUTE_EVIDENCE_FILE"

    def to_ams_dict(self):
        return self.name
