

from enum import Enum, unique


@unique
class SubscriptionNotificationType(Enum):
    CREATE = "CREATE"
    CHANGE = "CHANGE"
    CANCEL = "CANCEL"
    TERMINATE = "TERMINATE"

    def to_ams_dict(self):
        return self.name