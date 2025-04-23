from enum import Enum, unique


@unique
class DisputeJudgedResult(Enum):
    CHARGEBACK = "CHARGEBACK"
    RETRIEVAL_REQUEST = "RETRIEVAL_REQUEST"
    COMPLIANCE_REQUEST = "COMPLIANCE_REQUEST"
def to_ams_dict(self):
    return self.name