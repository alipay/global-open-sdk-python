from enum import Enum, unique
@unique
class PassengerIdType(Enum):
    """Type of passenger identification"""

    PASSPORT = "PASSPORT"
    NATIONAL_ID_CARD = "NATIONAL_ID_CARD"
    DRIVER_LICENSE = "DRIVER_LICENSE"
    MILITARY_ID = "MILITARY_ID"
    GREEN_CARD = "GREEN_CARD"
    TRAVEL_DOCUMENT = "TRAVEL_DOCUMENT"
    ALIEN_REGISTRATION_CARD = "ALIEN_REGISTRATION_CARD"
    BIRTH_CERTIFICATE = "BIRTH_CERTIFICATE"
    OTHERS = "OTHERS"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PassengerIdType.PASSPORT.value == value:
            return PassengerIdType.PASSPORT
        if PassengerIdType.NATIONAL_ID_CARD.value == value:
            return PassengerIdType.NATIONAL_ID_CARD
        if PassengerIdType.DRIVER_LICENSE.value == value:
            return PassengerIdType.DRIVER_LICENSE
        if PassengerIdType.MILITARY_ID.value == value:
            return PassengerIdType.MILITARY_ID
        if PassengerIdType.GREEN_CARD.value == value:
            return PassengerIdType.GREEN_CARD
        if PassengerIdType.TRAVEL_DOCUMENT.value == value:
            return PassengerIdType.TRAVEL_DOCUMENT
        if PassengerIdType.ALIEN_REGISTRATION_CARD.value == value:
            return PassengerIdType.ALIEN_REGISTRATION_CARD
        if PassengerIdType.BIRTH_CERTIFICATE.value == value:
            return PassengerIdType.BIRTH_CERTIFICATE
        if PassengerIdType.OTHERS.value == value:
            return PassengerIdType.OTHERS
        return None
