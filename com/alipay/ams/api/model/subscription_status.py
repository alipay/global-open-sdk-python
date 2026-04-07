from enum import Enum, unique
@unique
class SubscriptionStatus(Enum):
    """The subscription status. Valid values are: - ACTIVE: indicates that the subscription is active. - CANCELLED: indicates that the subscription is cancelled. - TERMINATED: indicates that the subscription is terminated."""

    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    TERMINATED = "TERMINATED"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if SubscriptionStatus.ACTIVE.value == value:
            return SubscriptionStatus.ACTIVE
        if SubscriptionStatus.CANCELLED.value == value:
            return SubscriptionStatus.CANCELLED
        if SubscriptionStatus.TERMINATED.value == value:
            return SubscriptionStatus.TERMINATED
        return None
