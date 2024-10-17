from enum import Enum, unique


@unique
class LegalEntityType(Enum):
    COMPANY = "COMPANY"
    INDIVIDUAL = "INDIVIDUAL"

    def to_ams_dict(self):
        return self.name