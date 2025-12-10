from enum import Enum, unique
@unique
class TerminalType(Enum):
    """TerminalType枚举类"""

    WEB = "WEB"
    WAP = "WAP"
    APP = "APP"
    MINI_APP = "MINI_APP"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if TerminalType.WEB.value == value:
            return TerminalType.WEB
        if TerminalType.WAP.value == value:
            return TerminalType.WAP
        if TerminalType.APP.value == value:
            return TerminalType.APP
        if TerminalType.MINI_APP.value == value:
            return TerminalType.MINI_APP
        return None
