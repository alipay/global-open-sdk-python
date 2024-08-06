from enum import Enum, unique


@unique
class CardBrandType(Enum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    AMEX = "AMEX"
    HIPERCARD = "HIPERCARD"
    ELO = "ELO"

    def to_ams_dict(self):
        return self.name
