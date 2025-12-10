from enum import Enum, unique
@unique
class AssociationType(Enum):
    """AssociationType枚举类"""

    LEGAL_REPRESENTATIVE = "LEGAL_REPRESENTATIVE"
    UBO = "UBO"
    CONTACT = "CONTACT"
    DIRECTOR = "DIRECTOR"
    AUTHORIZER = "AUTHORIZER"
    BOARD_MEMBER = "BOARD_MEMBER"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if AssociationType.LEGAL_REPRESENTATIVE.value == value:
            return AssociationType.LEGAL_REPRESENTATIVE
        if AssociationType.UBO.value == value:
            return AssociationType.UBO
        if AssociationType.CONTACT.value == value:
            return AssociationType.CONTACT
        if AssociationType.DIRECTOR.value == value:
            return AssociationType.DIRECTOR
        if AssociationType.AUTHORIZER.value == value:
            return AssociationType.AUTHORIZER
        if AssociationType.BOARD_MEMBER.value == value:
            return AssociationType.BOARD_MEMBER
        return None
