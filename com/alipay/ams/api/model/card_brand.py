from enum import Enum, unique
@unique
class CardBrand(Enum):
    """CardBrand枚举类"""

    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    MAESTRO = "MAESTRO"
    AMEX = "AMEX"
    JCB = "JCB"
    DINERS = "DINERS"
    DISCOVER = "DISCOVER"
    CUP = "CUP"
    MIR = "MIR"
    ELO = "ELO"
    HIPERCARD = "HIPERCARD"
    TROY = "TROY"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CardBrand.VISA.value == value:
            return CardBrand.VISA
        if CardBrand.MASTERCARD.value == value:
            return CardBrand.MASTERCARD
        if CardBrand.MAESTRO.value == value:
            return CardBrand.MAESTRO
        if CardBrand.AMEX.value == value:
            return CardBrand.AMEX
        if CardBrand.JCB.value == value:
            return CardBrand.JCB
        if CardBrand.DINERS.value == value:
            return CardBrand.DINERS
        if CardBrand.DISCOVER.value == value:
            return CardBrand.DISCOVER
        if CardBrand.CUP.value == value:
            return CardBrand.CUP
        if CardBrand.MIR.value == value:
            return CardBrand.MIR
        if CardBrand.ELO.value == value:
            return CardBrand.ELO
        if CardBrand.HIPERCARD.value == value:
            return CardBrand.HIPERCARD
        if CardBrand.TROY.value == value:
            return CardBrand.TROY
        return None
