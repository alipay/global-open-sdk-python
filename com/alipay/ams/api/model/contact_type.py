from enum import Enum, unique
@unique
class ContactType(Enum):
    """ContactType枚举类"""

    EMAIL = "EMAIL"
    PHONE_NO = "PHONE_NO"
    COMMERCIAL_PHONE_NO = "COMMERCIAL_PHONE_NO"

    def to_ams_dict(self) -> str:
        return {
            "EMAIL": "EMAIL",
            "PHONE_NO": "PHONE_NO",
            "COMMERCIAL_PHONE_NO": "COMMERCIAL_PHONE_NO",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ContactType.EMAIL.value == value:
            return ContactType.EMAIL
        if ContactType.PHONE_NO.value == value:
            return ContactType.PHONE_NO
        if ContactType.COMMERCIAL_PHONE_NO.value == value:
            return ContactType.COMMERCIAL_PHONE_NO
        for member in ContactType:
            if member.to_ams_dict() == value:
                return member
        return None

