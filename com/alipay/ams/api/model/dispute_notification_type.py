from enum import Enum, unique


@unique
class DisputeNotificationType(Enum):
    DISPUTE_CREATED = "DISPUTE_CREATED"
    DISPUTE_JUDGED = "DISPUTE_JUDGED"
    DISPUTE_CANCELLED = "DISPUTE_CANCELLED"
    DEFENSE_SUPPLIED = "DEFENSE_SUPPLIED"
    DEFENSE_DUE_ALERT = "DEFENSE_DUE_ALERT"
    DISPUTE_ACCEPTED = "DISPUTE_ACCEPTED"
    RDR_RESOLVED = "RDR_RESOLVED"

    def to_ams_dict(self):
        return self.name
