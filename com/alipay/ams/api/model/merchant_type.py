from enum import Enum, unique
@unique
class MerchantType(Enum):
    """MerchantType枚举类"""

    INDIVIDUAL = "INDIVIDUAL"
    ENTERPRISE = "ENTERPRISE"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if MerchantType.INDIVIDUAL.value == value:
            return MerchantType.INDIVIDUAL
        if MerchantType.ENTERPRISE.value == value:
            return MerchantType.ENTERPRISE
        return None
