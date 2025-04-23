from enum import Enum, unique


@unique
class DisputeJudgedResult(Enum):
    ACCEPT_BY_CUSTOMER = "ACCEPT_BY_CUSTOMER"
    ACCEPT_BY_MERCHANT = "ACCEPT_BY_MERCHANT"
    VALIDATE_SUCCESS = "VALIDATE_SUCCESS"
    VALIDATE_FAIL = "VALIDATE_FAIL"
def to_ams_dict(self):
    return self.name
