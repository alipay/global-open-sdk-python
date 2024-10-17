from enum import Enum, unique


@unique
class AccountHolderType(Enum):
    INDIVIDUAL = "INDIVIDUAL"
    ENTERPRISE = "ENTERPRISE"

    def to_ams_dict(self):
        return self.name
