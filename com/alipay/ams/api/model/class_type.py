from enum import Enum, unique


@unique
class ClassType(Enum):
    FIRSTLEVEL = "FIRSTLEVEL"
    SECONDLEVEL = "SECONDLEVEL"
    THIRDLEVEL = "THIRDLEVEL"

    def to_ams_dict(self):
        return self.name
