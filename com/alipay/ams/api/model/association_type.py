
from enum import Enum, unique


@unique
class AssociationType(Enum):
    LEGAL_REPRESENTATIVE = "LEGAL_REPRESENTATIVE"
    UBO = "UBO"
    CONTACT = "CONTACT"
    DIRECTOR = "DIRECTOR"
    AUTHORIZER = "AUTHORIZER"
    BOARD_MEMBER = "BOARD_MEMBER"

    def to_ams_dict(self):
        return self.name