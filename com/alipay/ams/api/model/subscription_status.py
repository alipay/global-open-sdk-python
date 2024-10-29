

from enum import Enum, unique


@unique
class SubscriptionStatus(Enum):
    ACTIVE = "ACTIVE"
    TERMINATED = "TERMINATED"

    def to_ams_dict(self):
        return self.name
