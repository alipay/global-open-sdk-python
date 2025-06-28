from enum import Enum, unique
@unique
class LegalEntityType(Enum):
    """LegalEntityType枚举类"""

    COMPANY = "COMPANY"
    INDIVIDUAL = "INDIVIDUAL"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if LegalEntityType.COMPANY.value == value:
            return LegalEntityType.COMPANY
        if LegalEntityType.INDIVIDUAL.value == value:
            return LegalEntityType.INDIVIDUAL
        return None
