from enum import Enum, unique
@unique
class ClassType(Enum):
    """ClassType枚举类"""

    FIRSTLEVEL = "FIRSTLEVEL"
    SECONDLEVEL = "SECONDLEVEL"
    THIRDLEVEL = "THIRDLEVEL"

    def to_ams_dict(self) -> str:
        return {
            "FIRSTLEVEL": "FIRSTLEVEL",
            "SECONDLEVEL": "SECONDLEVEL",
            "THIRDLEVEL": "THIRDLEVEL",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ClassType.FIRSTLEVEL.value == value:
            return ClassType.FIRSTLEVEL
        if ClassType.SECONDLEVEL.value == value:
            return ClassType.SECONDLEVEL
        if ClassType.THIRDLEVEL.value == value:
            return ClassType.THIRDLEVEL
        for member in ClassType:
            if member.to_ams_dict() == value:
                return member
        return None

