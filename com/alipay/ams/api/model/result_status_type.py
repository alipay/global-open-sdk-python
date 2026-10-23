from enum import Enum, unique
@unique
class ResultStatusType(Enum):
    """ResultStatusType枚举类"""

    S = "S"
    F = "F"
    U = "U"

    def to_ams_dict(self) -> str:
        return {
            "S": "S",
            "F": "F",
            "U": "U",
        }[self.name]

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
        for member in ResultStatusType:
            if member.to_ams_dict() == value:
                return member
        return None

