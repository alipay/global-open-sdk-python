from enum import Enum, unique


@unique
class DisputeAcceptReasonType(Enum):
    MERCHANT_ACCEPTED = "MERCHANT_ACCEPTED"
    TIMEOUT = "TIMEOUT"
    MANUAL_PROCESSING_ACCEPTED = "MANUAL_PROCESSING_ACCEPTED"

    def to_ams_dict(self):
        return self.name
