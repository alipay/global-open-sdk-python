from enum import Enum, unique
@unique
class ResultStatusType(Enum):
    """ResultStatusType枚举类"""

    S = "S"
    F = "F"
    U = "U"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ResultStatusType.S.value == value:
            return ResultStatusType.S
        if ResultStatusType.F.value == value:
            return ResultStatusType.F
        if ResultStatusType.U.value == value:
            return ResultStatusType.U
        return None
