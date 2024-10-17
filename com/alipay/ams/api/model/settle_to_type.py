from enum import Enum, unique


@unique
class SettleToType(Enum):
    SELLER = "SELLER"
    MARKETPLACE = "MARKETPLACE"

    def to_ams_dict(self):
        return self.name