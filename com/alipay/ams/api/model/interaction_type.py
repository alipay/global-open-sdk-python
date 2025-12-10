from enum import Enum, unique
@unique
class InteractionType(Enum):
    """The interaction type for the payment method."""

    QR = "QR"
    REDIRECT = "REDIRECT"
    PUSH = "PUSH"
    ATM = "ATM"
    IBANKING = "IBANKING"
    BANKCOUNTER = "BANKCOUNTER"
    OTC = "OTC"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if InteractionType.QR.value == value:
            return InteractionType.QR
        if InteractionType.REDIRECT.value == value:
            return InteractionType.REDIRECT
        if InteractionType.PUSH.value == value:
            return InteractionType.PUSH
        if InteractionType.ATM.value == value:
            return InteractionType.ATM
        if InteractionType.IBANKING.value == value:
            return InteractionType.IBANKING
        if InteractionType.BANKCOUNTER.value == value:
            return InteractionType.BANKCOUNTER
        if InteractionType.OTC.value == value:
            return InteractionType.OTC
        return None
