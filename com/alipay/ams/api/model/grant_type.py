from enum import Enum, unique
@unique
class GrantType(Enum):
    """GrantType枚举类"""

    AUTHORIZATION_CODE = "AUTHORIZATION_CODE"
    REFRESH_TOKEN = "REFRESH_TOKEN"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if GrantType.AUTHORIZATION_CODE.value == value:
            return GrantType.AUTHORIZATION_CODE
        if GrantType.REFRESH_TOKEN.value == value:
            return GrantType.REFRESH_TOKEN
        return None
