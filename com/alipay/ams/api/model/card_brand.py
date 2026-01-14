from enum import Enum, unique
@unique
class CardBrand(Enum):
    """CardBrand枚举类"""

    AMEX = "AMEX"
    BC = "BC"
    CARNET = "CARNET"
    CARTES_BANCAIRES = "CARTES_BANCAIRES"
    CITI = "CITI"
    CUP = "CUP"
    DINERS = "DINERS"
    DISCOVER = "DISCOVER"
    ELO = "ELO"
    GWANGJUBANK = "GWANGJUBANK"
    HIPERCARD = "HIPERCARD"
    HYUNDAI = "HYUNDAI"
    IBK_BC = "IBK_BC"
    JCB = "JCB"
    JEJUBANK = "JEJUBANK"
    JEONBUKBANK = "JEONBUKBANK"
    KAKAOBANK = "KAKAOBANK"
    KBANK = "KBANK"
    KDBBANK = "KDBBANK"
    KEBHANA = "KEBHANA"
    KOOKMIN = "KOOKMIN"
    LOTTE = "LOTTE"
    MAESTRO = "MAESTRO"
    MASTERCARD = "MASTERCARD"
    MIR = "MIR"
    NONGHYUP = "NONGHYUP"
    POST = "POST"
    SAEMAUL = "SAEMAUL"
    SAMSUNG = "SAMSUNG"
    SAVINGBANK = "SAVINGBANK"
    SHINHAN = "SHINHAN"
    SHINHYEOP = "SHINHYEOP"
    SUHYEOP = "SUHYEOP"
    TOSSBANK = "TOSSBANK"
    TROY = "TROY"
    VISA = "VISA"
    WOORI = "WOORI"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CardBrand.AMEX.value == value:
            return CardBrand.AMEX
        if CardBrand.BC.value == value:
            return CardBrand.BC
        if CardBrand.CARNET.value == value:
            return CardBrand.CARNET
        if CardBrand.CARTES_BANCAIRES.value == value:
            return CardBrand.CARTES_BANCAIRES
        if CardBrand.CITI.value == value:
            return CardBrand.CITI
        if CardBrand.CUP.value == value:
            return CardBrand.CUP
        if CardBrand.DINERS.value == value:
            return CardBrand.DINERS
        if CardBrand.DISCOVER.value == value:
            return CardBrand.DISCOVER
        if CardBrand.ELO.value == value:
            return CardBrand.ELO
        if CardBrand.GWANGJUBANK.value == value:
            return CardBrand.GWANGJUBANK
        if CardBrand.HIPERCARD.value == value:
            return CardBrand.HIPERCARD
        if CardBrand.HYUNDAI.value == value:
            return CardBrand.HYUNDAI
        if CardBrand.IBK_BC.value == value:
            return CardBrand.IBK_BC
        if CardBrand.JCB.value == value:
            return CardBrand.JCB
        if CardBrand.JEJUBANK.value == value:
            return CardBrand.JEJUBANK
        if CardBrand.JEONBUKBANK.value == value:
            return CardBrand.JEONBUKBANK
        if CardBrand.KAKAOBANK.value == value:
            return CardBrand.KAKAOBANK
        if CardBrand.KBANK.value == value:
            return CardBrand.KBANK
        if CardBrand.KDBBANK.value == value:
            return CardBrand.KDBBANK
        if CardBrand.KEBHANA.value == value:
            return CardBrand.KEBHANA
        if CardBrand.KOOKMIN.value == value:
            return CardBrand.KOOKMIN
        if CardBrand.LOTTE.value == value:
            return CardBrand.LOTTE
        if CardBrand.MAESTRO.value == value:
            return CardBrand.MAESTRO
        if CardBrand.MASTERCARD.value == value:
            return CardBrand.MASTERCARD
        if CardBrand.MIR.value == value:
            return CardBrand.MIR
        if CardBrand.NONGHYUP.value == value:
            return CardBrand.NONGHYUP
        if CardBrand.POST.value == value:
            return CardBrand.POST
        if CardBrand.SAEMAUL.value == value:
            return CardBrand.SAEMAUL
        if CardBrand.SAMSUNG.value == value:
            return CardBrand.SAMSUNG
        if CardBrand.SAVINGBANK.value == value:
            return CardBrand.SAVINGBANK
        if CardBrand.SHINHAN.value == value:
            return CardBrand.SHINHAN
        if CardBrand.SHINHYEOP.value == value:
            return CardBrand.SHINHYEOP
        if CardBrand.SUHYEOP.value == value:
            return CardBrand.SUHYEOP
        if CardBrand.TOSSBANK.value == value:
            return CardBrand.TOSSBANK
        if CardBrand.TROY.value == value:
            return CardBrand.TROY
        if CardBrand.VISA.value == value:
            return CardBrand.VISA
        if CardBrand.WOORI.value == value:
            return CardBrand.WOORI
        return None
