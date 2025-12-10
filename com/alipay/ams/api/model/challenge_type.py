from enum import Enum, unique
@unique
class ChallengeType(Enum):
    """ChallengeType枚举类"""

    SMS_OTP = "SMS_OTP"
    PLAINTEXT_CARD_NO = "PLAINTEXT_CARD_NO"
    CARD_EXPIRE_DATE = "CARD_EXPIRE_DATE"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ChallengeType.SMS_OTP.value == value:
            return ChallengeType.SMS_OTP
        if ChallengeType.PLAINTEXT_CARD_NO.value == value:
            return ChallengeType.PLAINTEXT_CARD_NO
        if ChallengeType.CARD_EXPIRE_DATE.value == value:
            return ChallengeType.CARD_EXPIRE_DATE
        return None
