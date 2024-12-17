from enum import Enum, unique


@unique
class DisputeNotificationType(Enum):
    ACCEPT_BY_CUSTOMER = "ACCEPT_BY_CUSTOMER"
    ACCEPT_BY_MERCHANT = "ACCEPT_BY_MERCHANT"

    def to_ams_dict(self):
        return self.name
