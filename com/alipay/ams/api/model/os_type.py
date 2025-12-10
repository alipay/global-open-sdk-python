from enum import Enum, unique
@unique
class OsType(Enum):
    """OsType枚举类"""

    IOS = "IOS"
    ANDROID = "ANDROID"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if OsType.IOS.value == value:
            return OsType.IOS
        if OsType.ANDROID.value == value:
            return OsType.ANDROID
        return None
