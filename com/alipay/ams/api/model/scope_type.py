from enum import Enum, unique
@unique
class ScopeType(Enum):
    """ScopeType枚举类"""

    BASE_USER_INFO = "BASE_USER_INFO"
    AGREEMENT_PAY = "AGREEMENT_PAY"
    USER_INFO = "USER_INFO"
    USER_LOGIN_ID = "USER_LOGIN_ID"
    HASH_LOGIN_ID = "HASH_LOGIN_ID"
    SEND_OTP = "SEND_OTP"
    TAOBAO_REBIND = "TAOBAO_REBIND"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ScopeType.BASE_USER_INFO.value == value:
            return ScopeType.BASE_USER_INFO
        if ScopeType.AGREEMENT_PAY.value == value:
            return ScopeType.AGREEMENT_PAY
        if ScopeType.USER_INFO.value == value:
            return ScopeType.USER_INFO
        if ScopeType.USER_LOGIN_ID.value == value:
            return ScopeType.USER_LOGIN_ID
        if ScopeType.HASH_LOGIN_ID.value == value:
            return ScopeType.HASH_LOGIN_ID
        if ScopeType.SEND_OTP.value == value:
            return ScopeType.SEND_OTP
        if ScopeType.TAOBAO_REBIND.value == value:
            return ScopeType.TAOBAO_REBIND
        return None
