from enum import Enum, unique
@unique
class DisplayType(Enum):
    """DisplayType枚举类"""

    TEXT = "TEXT"
    MIDDLEIMAGE = "MIDDLEIMAGE"
    SMALLIMAGE = "SMALLIMAGE"
    BIGIMAGE = "BIGIMAGE"
    IMAGE = "IMAGE"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if DisplayType.TEXT.value == value:
            return DisplayType.TEXT
        if DisplayType.MIDDLEIMAGE.value == value:
            return DisplayType.MIDDLEIMAGE
        if DisplayType.SMALLIMAGE.value == value:
            return DisplayType.SMALLIMAGE
        if DisplayType.BIGIMAGE.value == value:
            return DisplayType.BIGIMAGE
        if DisplayType.IMAGE.value == value:
            return DisplayType.IMAGE
        return None
