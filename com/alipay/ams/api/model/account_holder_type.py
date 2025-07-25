from enum import Enum, unique
@unique
class AccountHolderType(Enum):
    """AccountHolderType枚举类"""

    INDIVIDUAL = "INDIVIDUAL"
    ENTERPRISE = "ENTERPRISE"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if AccountHolderType.INDIVIDUAL.value == value:
            return AccountHolderType.INDIVIDUAL
        if AccountHolderType.ENTERPRISE.value == value:
            return AccountHolderType.ENTERPRISE
        return None
