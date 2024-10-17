from enum import Enum, unique


@unique
class CompanyUnitType(Enum):
    HEADQUARTER = "HEADQUARTER"
    BRANCH = "BRANCH"

    def to_ams_dict(self):
        return self.name