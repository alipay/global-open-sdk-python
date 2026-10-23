from enum import Enum, unique
@unique
class CompanyUnitType(Enum):
    """CompanyUnitType枚举类"""

    HEADQUARTER = "HEADQUARTER"
    BRANCH = "BRANCH"

    def to_ams_dict(self) -> str:
        return {
            "HEADQUARTER": "HEADQUARTER",
            "BRANCH": "BRANCH",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CompanyUnitType.HEADQUARTER.value == value:
            return CompanyUnitType.HEADQUARTER
        if CompanyUnitType.BRANCH.value == value:
            return CompanyUnitType.BRANCH
        for member in CompanyUnitType:
            if member.to_ams_dict() == value:
                return member
        return None

