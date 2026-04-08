from enum import Enum, unique
@unique
class CustomerBelongsTo(Enum):
    """CustomerBelongsTo枚举类"""

    CARD = "CARD"
    GOOGLEPAY = "GOOGLEPAY"
    APPLEPAY = "APPLEPAY"
    EPS = "EPS"
    BANCONTACT = "BANCONTACT"
    PIX = "PIX"
    MERCADOPAGO_BR = "MERCADOPAGO_BR"
    PAGALEVE = "PAGALEVE"
    PICPAY = "PICPAY"
    MERCADOPAGO_CL = "MERCADOPAGO_CL"
    ALIPAY_CN = "ALIPAY_CN"
    JKOPAY = "JKOPAY"
    ALIPAY_HK = "ALIPAY_HK"
    OCTOPUS = "OCTOPUS"
    MPAY = "MPAY"
    PAYME = "PAYME"
    UPI = "UPI"
    ONLINEBANKING_NETBANKING = "ONLINEBANKING_NETBANKING"
    DANA = "DANA"
    KREDIVO_ID = "KREDIVO_ID"
    OVO = "OVO"
    GOPAY_ID = "GOPAY_ID"
    QRIS = "QRIS"
    SHOPEEPAY_ID = "SHOPEEPAY_ID"
    LINKAJA = "LINKAJA"
    BANCOMATPAY = "BANCOMATPAY"
    SATISPAY = "SATISPAY"
    TINABA = "TINABA"
    PAYPAY = "PAYPAY"
    KONBINI = "KONBINI"
    SEVENELEVEN = "SEVENELEVEN"
    ONLINEBANKING_PAYEASY = "ONLINEBANKING_PAYEASY"
    AUPAY = "AUPAY"
    FAMIPAY = "FAMIPAY"
    MERPAY = "MERPAY"
    PAIDY = "PAIDY"
    D_BARAI_PAY = "D_BARAI_PAY"
    RAKUTEN_PAY = "RAKUTEN_PAY"
    BOOST = "BOOST"
    TNG = "TNG"
    GRABPAY_MY = "GRABPAY_MY"
    ONLINEBANKING_FPX = "ONLINEBANKING_FPX"
    SHOPEEPAY_MY = "SHOPEEPAY_MY"
    MERCADOPAGO_MX = "MERCADOPAGO_MX"
    HIPAY = "HIPAY"
    IDEAL = "IDEAL"
    MERCADOPAGO_PE = "MERCADOPAGO_PE"
    BPI = "BPI"
    GCASH = "GCASH"
    BILLEASE = "BILLEASE"
    MAYA = "MAYA"
    ONLINEBANKING_UBP = "ONLINEBANKING_UBP"
    SHOPEEPAY_PH = "SHOPEEPAY_PH"
    GRABPAY_PH = "GRABPAY_PH"
    QRPH = "QRPH"
    PAYU = "PAYU"
    P24 = "P24"
    BLIK = "BLIK"
    MB_WAY = "MB_WAY"
    GRABPAY_SG = "GRABPAY_SG"
    PAYNOW = "PAYNOW"
    SHOPEEPAY_SG = "SHOPEEPAY_SG"
    KAKAOPAY = "KAKAOPAY"
    NAVERPAY = "NAVERPAY"
    TOSSPAY = "TOSSPAY"
    BANKTRANSFER_QUICKPAY = "BANKTRANSFER_QUICKPAY"
    DIRECT_CARRIER_BILLING_KR = "DIRECT_CARRIER_BILLING_KR"
    SAMSUNG_PAY_KR = "SAMSUNG_PAY_KR"
    BIZUM = "BIZUM"
    SEQURA = "SEQURA"
    SWISH = "SWISH"
    TWINT = "TWINT"
    RABBIT_LINE_PAY = "RABBIT_LINE_PAY"
    TRUEMONEY = "TRUEMONEY"
    ONLINBANKING_KRUNGTHAIBANK = "ONLINBANKING_KRUNGTHAIBANK"
    BANKAPP_KRUNGTHAIBANK = "BANKAPP_KRUNGTHAIBANK"
    ONLINBANKING_SIAMCOMMERICALBANK = "ONLINBANKING_SIAMCOMMERICALBANK"
    BANKAPP_SIAMCOMMERICALBANK = "BANKAPP_SIAMCOMMERICALBANK"
    ONLINBANKING_BANGKOKBANK = "ONLINBANKING_BANGKOKBANK"
    BANKAPP_BANGKOKBANK = "BANKAPP_BANGKOKBANK"
    ONLINBANKING_BANKOFAYUDHYA = "ONLINBANKING_BANKOFAYUDHYA"
    BANKAPP_BANKOFAYUDHYA = "BANKAPP_BANKOFAYUDHYA"
    ONLINBANKING_KASIKORNBANK = "ONLINBANKING_KASIKORNBANK"
    BANKTRANSFER_KASIKORNBANK = "BANKTRANSFER_KASIKORNBANK"
    BANKTRANSFER_GOVERNMENTSAVINGSBANK = "BANKTRANSFER_GOVERNMENTSAVINGSBANK"
    PROMPTPAY = "PROMPTPAY"
    SHOPEEPAY_TH = "SHOPEEPAY_TH"
    KPLUS = "KPLUS"
    ONLINBANKING_YAPILY = "ONLINBANKING_YAPILY"
    ZALOPAY = "ZALOPAY"
    MOMO = "MOMO"
    BANKTRANSFER_VIA_VIETQR = "BANKTRANSFER_VIA_VIETQR"
    VIETTELMONEY = "VIETTELMONEY"
    TAMARA_SA = "TAMARA_SA"
    TAMARA_AE = "TAMARA_AE"
    TABBY = "TABBY"
    ACH_DIRECT_DEBIT = "ACH_DIRECT_DEBIT"
    DIRECT_DEBIT_SIAMCOMMERCIALBANK = "DIRECT_DEBIT_SIAMCOMMERCIALBANK"
    DIRECT_DEBIT_KRUNGTHAIBANK = "DIRECT_DEBIT_KRUNGTHAIBANK"
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    AMEX = "AMEX"
    DISCOVER = "DISCOVER"
    DINERS = "DINERS"
    CUP = "CUP"
    JCB = "JCB"
    HIPERCARD = "HIPERCARD"
    ELO = "ELO"
    MAESTRO = "MAESTRO"
    CARTES_BANCAIRES = "CARTES_BANCAIRES"
    KOOKMIN = "KOOKMIN"
    BC = "BC"
    NONGHYUP = "NONGHYUP"
    SHINHAN = "SHINHAN"
    SAMSUNG = "SAMSUNG"
    LOTTE = "LOTTE"
    HYUNDAI = "HYUNDAI"
    KEBHANA = "KEBHANA"
    WOORI = "WOORI"
    IBK_BC = "IBK_BC"
    GWANGJUBANK = "GWANGJUBANK"
    KDBBANK = "KDBBANK"
    SAEMAUL = "SAEMAUL"
    SHINHYEOP = "SHINHYEOP"
    CITI = "CITI"
    POST = "POST"
    SAVINGBANK = "SAVINGBANK"
    JEONBUKBANK = "JEONBUKBANK"
    JEJUBANK = "JEJUBANK"
    KAKAOBANK = "KAKAOBANK"
    KBANK = "KBANK"
    TOSSBANK = "TOSSBANK"
    SUHYEOP = "SUHYEOP"
    CARNET = "CARNET"
    TROY = "TROY"
    20 = "20"
    26 = "26"
    31 = "31"
    33 = "33"
    43 = "43"
    45 = "45"
    49 = "49"
    52 = "52"
    53 = "53"
    54 = "54"
    64 = "64"
    65 = "65"
    69 = "69"
    85 = "85"
    88 = "88"
    90 = "90"
    95 = "95"
    99 = "99"
    112 = "112"
    119 = "119"
    129 = "129"
    131 = "131"
    136 = "136"
    141 = "141"
    143 = "143"
    144 = "144"
    153 = "153"
    154 = "154"
    158 = "158"
    161 = "161"
    222 = "222"
    223 = "223"
    243 = "243"
    266 = "266"
    270 = "270"
    271 = "271"
    272 = "272"
    274 = "274"
    275 = "275"
    279 = "279"
    280 = "280"
    MYM2U = "MYM2U"
    MYBISM = "MYBISM"
    MYRHB = "MYRHB"
    MYHLB = "MYHLB"
    MYCIMBCLICKS = "MYCIMBCLICKS"
    MYAMB = "MYAMB"
    MYPBB = "MYPBB"
    MYABB = "MYABB"
    MYAGB = "MYAGB"
    MYABMB = "MYABMB"
    MYBMMB = "MYBMMB"
    MYBOC = "MYBOC"
    MYBKRM = "MYBKRM"
    MYBSN = "MYBSN"
    MYHSBC = "MYHSBC"
    MYKFH = "MYKFH"
    MYOCBC = "MYOCBC"
    MYSCB = "MYSCB"
    MYUOB = "MYUOB"
    IPAY-MONZO = "IPAY-MONZO"
    IPAY-SANTANDER = "IPAY-SANTANDER"
    IPAY-HSBC = "IPAY-HSBC"
    IPAY-LLOYDS = "IPAY-LLOYDS"
    IPAY-REVOLUT = "IPAY-REVOLUT"
    IPAY-BARCLAYS = "IPAY-BARCLAYS"
    IPAY-NATWEST = "IPAY-NATWEST"
    IPAY-NATIONWIDE = "IPAY-NATIONWIDE"
    BKASH = "BKASH"
    EASYPAISA = "EASYPAISA"
    DIRECTDEBIT_YAPILY = "DIRECTDEBIT_YAPILY"
    ANTIM_BIZ_ACCOUNT = "ANTIM_BIZ_ACCOUNT"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CustomerBelongsTo.CARD.value == value:
            return CustomerBelongsTo.CARD
        if CustomerBelongsTo.GOOGLEPAY.value == value:
            return CustomerBelongsTo.GOOGLEPAY
        if CustomerBelongsTo.APPLEPAY.value == value:
            return CustomerBelongsTo.APPLEPAY
        if CustomerBelongsTo.EPS.value == value:
            return CustomerBelongsTo.EPS
        if CustomerBelongsTo.BANCONTACT.value == value:
            return CustomerBelongsTo.BANCONTACT
        if CustomerBelongsTo.PIX.value == value:
            return CustomerBelongsTo.PIX
        if CustomerBelongsTo.MERCADOPAGO_BR.value == value:
            return CustomerBelongsTo.MERCADOPAGO_BR
        if CustomerBelongsTo.PAGALEVE.value == value:
            return CustomerBelongsTo.PAGALEVE
        if CustomerBelongsTo.PICPAY.value == value:
            return CustomerBelongsTo.PICPAY
        if CustomerBelongsTo.MERCADOPAGO_CL.value == value:
            return CustomerBelongsTo.MERCADOPAGO_CL
        if CustomerBelongsTo.ALIPAY_CN.value == value:
            return CustomerBelongsTo.ALIPAY_CN
        if CustomerBelongsTo.JKOPAY.value == value:
            return CustomerBelongsTo.JKOPAY
        if CustomerBelongsTo.ALIPAY_HK.value == value:
            return CustomerBelongsTo.ALIPAY_HK
        if CustomerBelongsTo.OCTOPUS.value == value:
            return CustomerBelongsTo.OCTOPUS
        if CustomerBelongsTo.MPAY.value == value:
            return CustomerBelongsTo.MPAY
        if CustomerBelongsTo.PAYME.value == value:
            return CustomerBelongsTo.PAYME
        if CustomerBelongsTo.UPI.value == value:
            return CustomerBelongsTo.UPI
        if CustomerBelongsTo.ONLINEBANKING_NETBANKING.value == value:
            return CustomerBelongsTo.ONLINEBANKING_NETBANKING
        if CustomerBelongsTo.DANA.value == value:
            return CustomerBelongsTo.DANA
        if CustomerBelongsTo.KREDIVO_ID.value == value:
            return CustomerBelongsTo.KREDIVO_ID
        if CustomerBelongsTo.OVO.value == value:
            return CustomerBelongsTo.OVO
        if CustomerBelongsTo.GOPAY_ID.value == value:
            return CustomerBelongsTo.GOPAY_ID
        if CustomerBelongsTo.QRIS.value == value:
            return CustomerBelongsTo.QRIS
        if CustomerBelongsTo.SHOPEEPAY_ID.value == value:
            return CustomerBelongsTo.SHOPEEPAY_ID
        if CustomerBelongsTo.LINKAJA.value == value:
            return CustomerBelongsTo.LINKAJA
        if CustomerBelongsTo.BANCOMATPAY.value == value:
            return CustomerBelongsTo.BANCOMATPAY
        if CustomerBelongsTo.SATISPAY.value == value:
            return CustomerBelongsTo.SATISPAY
        if CustomerBelongsTo.TINABA.value == value:
            return CustomerBelongsTo.TINABA
        if CustomerBelongsTo.PAYPAY.value == value:
            return CustomerBelongsTo.PAYPAY
        if CustomerBelongsTo.KONBINI.value == value:
            return CustomerBelongsTo.KONBINI
        if CustomerBelongsTo.SEVENELEVEN.value == value:
            return CustomerBelongsTo.SEVENELEVEN
        if CustomerBelongsTo.ONLINEBANKING_PAYEASY.value == value:
            return CustomerBelongsTo.ONLINEBANKING_PAYEASY
        if CustomerBelongsTo.AUPAY.value == value:
            return CustomerBelongsTo.AUPAY
        if CustomerBelongsTo.FAMIPAY.value == value:
            return CustomerBelongsTo.FAMIPAY
        if CustomerBelongsTo.MERPAY.value == value:
            return CustomerBelongsTo.MERPAY
        if CustomerBelongsTo.PAIDY.value == value:
            return CustomerBelongsTo.PAIDY
        if CustomerBelongsTo.D_BARAI_PAY.value == value:
            return CustomerBelongsTo.D_BARAI_PAY
        if CustomerBelongsTo.RAKUTEN_PAY.value == value:
            return CustomerBelongsTo.RAKUTEN_PAY
        if CustomerBelongsTo.BOOST.value == value:
            return CustomerBelongsTo.BOOST
        if CustomerBelongsTo.TNG.value == value:
            return CustomerBelongsTo.TNG
        if CustomerBelongsTo.GRABPAY_MY.value == value:
            return CustomerBelongsTo.GRABPAY_MY
        if CustomerBelongsTo.ONLINEBANKING_FPX.value == value:
            return CustomerBelongsTo.ONLINEBANKING_FPX
        if CustomerBelongsTo.SHOPEEPAY_MY.value == value:
            return CustomerBelongsTo.SHOPEEPAY_MY
        if CustomerBelongsTo.MERCADOPAGO_MX.value == value:
            return CustomerBelongsTo.MERCADOPAGO_MX
        if CustomerBelongsTo.HIPAY.value == value:
            return CustomerBelongsTo.HIPAY
        if CustomerBelongsTo.IDEAL.value == value:
            return CustomerBelongsTo.IDEAL
        if CustomerBelongsTo.MERCADOPAGO_PE.value == value:
            return CustomerBelongsTo.MERCADOPAGO_PE
        if CustomerBelongsTo.BPI.value == value:
            return CustomerBelongsTo.BPI
        if CustomerBelongsTo.GCASH.value == value:
            return CustomerBelongsTo.GCASH
        if CustomerBelongsTo.BILLEASE.value == value:
            return CustomerBelongsTo.BILLEASE
        if CustomerBelongsTo.MAYA.value == value:
            return CustomerBelongsTo.MAYA
        if CustomerBelongsTo.ONLINEBANKING_UBP.value == value:
            return CustomerBelongsTo.ONLINEBANKING_UBP
        if CustomerBelongsTo.SHOPEEPAY_PH.value == value:
            return CustomerBelongsTo.SHOPEEPAY_PH
        if CustomerBelongsTo.GRABPAY_PH.value == value:
            return CustomerBelongsTo.GRABPAY_PH
        if CustomerBelongsTo.QRPH.value == value:
            return CustomerBelongsTo.QRPH
        if CustomerBelongsTo.PAYU.value == value:
            return CustomerBelongsTo.PAYU
        if CustomerBelongsTo.P24.value == value:
            return CustomerBelongsTo.P24
        if CustomerBelongsTo.BLIK.value == value:
            return CustomerBelongsTo.BLIK
        if CustomerBelongsTo.MB_WAY.value == value:
            return CustomerBelongsTo.MB_WAY
        if CustomerBelongsTo.GRABPAY_SG.value == value:
            return CustomerBelongsTo.GRABPAY_SG
        if CustomerBelongsTo.PAYNOW.value == value:
            return CustomerBelongsTo.PAYNOW
        if CustomerBelongsTo.SHOPEEPAY_SG.value == value:
            return CustomerBelongsTo.SHOPEEPAY_SG
        if CustomerBelongsTo.KAKAOPAY.value == value:
            return CustomerBelongsTo.KAKAOPAY
        if CustomerBelongsTo.NAVERPAY.value == value:
            return CustomerBelongsTo.NAVERPAY
        if CustomerBelongsTo.TOSSPAY.value == value:
            return CustomerBelongsTo.TOSSPAY
        if CustomerBelongsTo.BANKTRANSFER_QUICKPAY.value == value:
            return CustomerBelongsTo.BANKTRANSFER_QUICKPAY
        if CustomerBelongsTo.DIRECT_CARRIER_BILLING_KR.value == value:
            return CustomerBelongsTo.DIRECT_CARRIER_BILLING_KR
        if CustomerBelongsTo.SAMSUNG_PAY_KR.value == value:
            return CustomerBelongsTo.SAMSUNG_PAY_KR
        if CustomerBelongsTo.BIZUM.value == value:
            return CustomerBelongsTo.BIZUM
        if CustomerBelongsTo.SEQURA.value == value:
            return CustomerBelongsTo.SEQURA
        if CustomerBelongsTo.SWISH.value == value:
            return CustomerBelongsTo.SWISH
        if CustomerBelongsTo.TWINT.value == value:
            return CustomerBelongsTo.TWINT
        if CustomerBelongsTo.RABBIT_LINE_PAY.value == value:
            return CustomerBelongsTo.RABBIT_LINE_PAY
        if CustomerBelongsTo.TRUEMONEY.value == value:
            return CustomerBelongsTo.TRUEMONEY
        if CustomerBelongsTo.ONLINBANKING_KRUNGTHAIBANK.value == value:
            return CustomerBelongsTo.ONLINBANKING_KRUNGTHAIBANK
        if CustomerBelongsTo.BANKAPP_KRUNGTHAIBANK.value == value:
            return CustomerBelongsTo.BANKAPP_KRUNGTHAIBANK
        if CustomerBelongsTo.ONLINBANKING_SIAMCOMMERICALBANK.value == value:
            return CustomerBelongsTo.ONLINBANKING_SIAMCOMMERICALBANK
        if CustomerBelongsTo.BANKAPP_SIAMCOMMERICALBANK.value == value:
            return CustomerBelongsTo.BANKAPP_SIAMCOMMERICALBANK
        if CustomerBelongsTo.ONLINBANKING_BANGKOKBANK.value == value:
            return CustomerBelongsTo.ONLINBANKING_BANGKOKBANK
        if CustomerBelongsTo.BANKAPP_BANGKOKBANK.value == value:
            return CustomerBelongsTo.BANKAPP_BANGKOKBANK
        if CustomerBelongsTo.ONLINBANKING_BANKOFAYUDHYA.value == value:
            return CustomerBelongsTo.ONLINBANKING_BANKOFAYUDHYA
        if CustomerBelongsTo.BANKAPP_BANKOFAYUDHYA.value == value:
            return CustomerBelongsTo.BANKAPP_BANKOFAYUDHYA
        if CustomerBelongsTo.ONLINBANKING_KASIKORNBANK.value == value:
            return CustomerBelongsTo.ONLINBANKING_KASIKORNBANK
        if CustomerBelongsTo.BANKTRANSFER_KASIKORNBANK.value == value:
            return CustomerBelongsTo.BANKTRANSFER_KASIKORNBANK
        if CustomerBelongsTo.BANKTRANSFER_GOVERNMENTSAVINGSBANK.value == value:
            return CustomerBelongsTo.BANKTRANSFER_GOVERNMENTSAVINGSBANK
        if CustomerBelongsTo.PROMPTPAY.value == value:
            return CustomerBelongsTo.PROMPTPAY
        if CustomerBelongsTo.SHOPEEPAY_TH.value == value:
            return CustomerBelongsTo.SHOPEEPAY_TH
        if CustomerBelongsTo.KPLUS.value == value:
            return CustomerBelongsTo.KPLUS
        if CustomerBelongsTo.ONLINBANKING_YAPILY.value == value:
            return CustomerBelongsTo.ONLINBANKING_YAPILY
        if CustomerBelongsTo.ZALOPAY.value == value:
            return CustomerBelongsTo.ZALOPAY
        if CustomerBelongsTo.MOMO.value == value:
            return CustomerBelongsTo.MOMO
        if CustomerBelongsTo.BANKTRANSFER_VIA_VIETQR.value == value:
            return CustomerBelongsTo.BANKTRANSFER_VIA_VIETQR
        if CustomerBelongsTo.VIETTELMONEY.value == value:
            return CustomerBelongsTo.VIETTELMONEY
        if CustomerBelongsTo.TAMARA_SA.value == value:
            return CustomerBelongsTo.TAMARA_SA
        if CustomerBelongsTo.TAMARA_AE.value == value:
            return CustomerBelongsTo.TAMARA_AE
        if CustomerBelongsTo.TABBY.value == value:
            return CustomerBelongsTo.TABBY
        if CustomerBelongsTo.ACH_DIRECT_DEBIT.value == value:
            return CustomerBelongsTo.ACH_DIRECT_DEBIT
        if CustomerBelongsTo.DIRECT_DEBIT_SIAMCOMMERCIALBANK.value == value:
            return CustomerBelongsTo.DIRECT_DEBIT_SIAMCOMMERCIALBANK
        if CustomerBelongsTo.DIRECT_DEBIT_KRUNGTHAIBANK.value == value:
            return CustomerBelongsTo.DIRECT_DEBIT_KRUNGTHAIBANK
        if CustomerBelongsTo.VISA.value == value:
            return CustomerBelongsTo.VISA
        if CustomerBelongsTo.MASTERCARD.value == value:
            return CustomerBelongsTo.MASTERCARD
        if CustomerBelongsTo.AMEX.value == value:
            return CustomerBelongsTo.AMEX
        if CustomerBelongsTo.DISCOVER.value == value:
            return CustomerBelongsTo.DISCOVER
        if CustomerBelongsTo.DINERS.value == value:
            return CustomerBelongsTo.DINERS
        if CustomerBelongsTo.CUP.value == value:
            return CustomerBelongsTo.CUP
        if CustomerBelongsTo.JCB.value == value:
            return CustomerBelongsTo.JCB
        if CustomerBelongsTo.HIPERCARD.value == value:
            return CustomerBelongsTo.HIPERCARD
        if CustomerBelongsTo.ELO.value == value:
            return CustomerBelongsTo.ELO
        if CustomerBelongsTo.MAESTRO.value == value:
            return CustomerBelongsTo.MAESTRO
        if CustomerBelongsTo.CARTES_BANCAIRES.value == value:
            return CustomerBelongsTo.CARTES_BANCAIRES
        if CustomerBelongsTo.KOOKMIN.value == value:
            return CustomerBelongsTo.KOOKMIN
        if CustomerBelongsTo.BC.value == value:
            return CustomerBelongsTo.BC
        if CustomerBelongsTo.NONGHYUP.value == value:
            return CustomerBelongsTo.NONGHYUP
        if CustomerBelongsTo.SHINHAN.value == value:
            return CustomerBelongsTo.SHINHAN
        if CustomerBelongsTo.SAMSUNG.value == value:
            return CustomerBelongsTo.SAMSUNG
        if CustomerBelongsTo.LOTTE.value == value:
            return CustomerBelongsTo.LOTTE
        if CustomerBelongsTo.HYUNDAI.value == value:
            return CustomerBelongsTo.HYUNDAI
        if CustomerBelongsTo.KEBHANA.value == value:
            return CustomerBelongsTo.KEBHANA
        if CustomerBelongsTo.WOORI.value == value:
            return CustomerBelongsTo.WOORI
        if CustomerBelongsTo.IBK_BC.value == value:
            return CustomerBelongsTo.IBK_BC
        if CustomerBelongsTo.GWANGJUBANK.value == value:
            return CustomerBelongsTo.GWANGJUBANK
        if CustomerBelongsTo.KDBBANK.value == value:
            return CustomerBelongsTo.KDBBANK
        if CustomerBelongsTo.SAEMAUL.value == value:
            return CustomerBelongsTo.SAEMAUL
        if CustomerBelongsTo.SHINHYEOP.value == value:
            return CustomerBelongsTo.SHINHYEOP
        if CustomerBelongsTo.CITI.value == value:
            return CustomerBelongsTo.CITI
        if CustomerBelongsTo.POST.value == value:
            return CustomerBelongsTo.POST
        if CustomerBelongsTo.SAVINGBANK.value == value:
            return CustomerBelongsTo.SAVINGBANK
        if CustomerBelongsTo.JEONBUKBANK.value == value:
            return CustomerBelongsTo.JEONBUKBANK
        if CustomerBelongsTo.JEJUBANK.value == value:
            return CustomerBelongsTo.JEJUBANK
        if CustomerBelongsTo.KAKAOBANK.value == value:
            return CustomerBelongsTo.KAKAOBANK
        if CustomerBelongsTo.KBANK.value == value:
            return CustomerBelongsTo.KBANK
        if CustomerBelongsTo.TOSSBANK.value == value:
            return CustomerBelongsTo.TOSSBANK
        if CustomerBelongsTo.SUHYEOP.value == value:
            return CustomerBelongsTo.SUHYEOP
        if CustomerBelongsTo.CARNET.value == value:
            return CustomerBelongsTo.CARNET
        if CustomerBelongsTo.TROY.value == value:
            return CustomerBelongsTo.TROY
        if CustomerBelongsTo.20.value == value:
            return CustomerBelongsTo.20
        if CustomerBelongsTo.26.value == value:
            return CustomerBelongsTo.26
        if CustomerBelongsTo.31.value == value:
            return CustomerBelongsTo.31
        if CustomerBelongsTo.33.value == value:
            return CustomerBelongsTo.33
        if CustomerBelongsTo.43.value == value:
            return CustomerBelongsTo.43
        if CustomerBelongsTo.45.value == value:
            return CustomerBelongsTo.45
        if CustomerBelongsTo.49.value == value:
            return CustomerBelongsTo.49
        if CustomerBelongsTo.52.value == value:
            return CustomerBelongsTo.52
        if CustomerBelongsTo.53.value == value:
            return CustomerBelongsTo.53
        if CustomerBelongsTo.54.value == value:
            return CustomerBelongsTo.54
        if CustomerBelongsTo.64.value == value:
            return CustomerBelongsTo.64
        if CustomerBelongsTo.65.value == value:
            return CustomerBelongsTo.65
        if CustomerBelongsTo.69.value == value:
            return CustomerBelongsTo.69
        if CustomerBelongsTo.85.value == value:
            return CustomerBelongsTo.85
        if CustomerBelongsTo.88.value == value:
            return CustomerBelongsTo.88
        if CustomerBelongsTo.90.value == value:
            return CustomerBelongsTo.90
        if CustomerBelongsTo.95.value == value:
            return CustomerBelongsTo.95
        if CustomerBelongsTo.99.value == value:
            return CustomerBelongsTo.99
        if CustomerBelongsTo.112.value == value:
            return CustomerBelongsTo.112
        if CustomerBelongsTo.119.value == value:
            return CustomerBelongsTo.119
        if CustomerBelongsTo.129.value == value:
            return CustomerBelongsTo.129
        if CustomerBelongsTo.131.value == value:
            return CustomerBelongsTo.131
        if CustomerBelongsTo.136.value == value:
            return CustomerBelongsTo.136
        if CustomerBelongsTo.141.value == value:
            return CustomerBelongsTo.141
        if CustomerBelongsTo.143.value == value:
            return CustomerBelongsTo.143
        if CustomerBelongsTo.144.value == value:
            return CustomerBelongsTo.144
        if CustomerBelongsTo.153.value == value:
            return CustomerBelongsTo.153
        if CustomerBelongsTo.154.value == value:
            return CustomerBelongsTo.154
        if CustomerBelongsTo.158.value == value:
            return CustomerBelongsTo.158
        if CustomerBelongsTo.161.value == value:
            return CustomerBelongsTo.161
        if CustomerBelongsTo.222.value == value:
            return CustomerBelongsTo.222
        if CustomerBelongsTo.223.value == value:
            return CustomerBelongsTo.223
        if CustomerBelongsTo.243.value == value:
            return CustomerBelongsTo.243
        if CustomerBelongsTo.266.value == value:
            return CustomerBelongsTo.266
        if CustomerBelongsTo.270.value == value:
            return CustomerBelongsTo.270
        if CustomerBelongsTo.271.value == value:
            return CustomerBelongsTo.271
        if CustomerBelongsTo.272.value == value:
            return CustomerBelongsTo.272
        if CustomerBelongsTo.274.value == value:
            return CustomerBelongsTo.274
        if CustomerBelongsTo.275.value == value:
            return CustomerBelongsTo.275
        if CustomerBelongsTo.279.value == value:
            return CustomerBelongsTo.279
        if CustomerBelongsTo.280.value == value:
            return CustomerBelongsTo.280
        if CustomerBelongsTo.MYM2U.value == value:
            return CustomerBelongsTo.MYM2U
        if CustomerBelongsTo.MYBISM.value == value:
            return CustomerBelongsTo.MYBISM
        if CustomerBelongsTo.MYRHB.value == value:
            return CustomerBelongsTo.MYRHB
        if CustomerBelongsTo.MYHLB.value == value:
            return CustomerBelongsTo.MYHLB
        if CustomerBelongsTo.MYCIMBCLICKS.value == value:
            return CustomerBelongsTo.MYCIMBCLICKS
        if CustomerBelongsTo.MYAMB.value == value:
            return CustomerBelongsTo.MYAMB
        if CustomerBelongsTo.MYPBB.value == value:
            return CustomerBelongsTo.MYPBB
        if CustomerBelongsTo.MYABB.value == value:
            return CustomerBelongsTo.MYABB
        if CustomerBelongsTo.MYAGB.value == value:
            return CustomerBelongsTo.MYAGB
        if CustomerBelongsTo.MYABMB.value == value:
            return CustomerBelongsTo.MYABMB
        if CustomerBelongsTo.MYBMMB.value == value:
            return CustomerBelongsTo.MYBMMB
        if CustomerBelongsTo.MYBOC.value == value:
            return CustomerBelongsTo.MYBOC
        if CustomerBelongsTo.MYBKRM.value == value:
            return CustomerBelongsTo.MYBKRM
        if CustomerBelongsTo.MYBSN.value == value:
            return CustomerBelongsTo.MYBSN
        if CustomerBelongsTo.MYHSBC.value == value:
            return CustomerBelongsTo.MYHSBC
        if CustomerBelongsTo.MYKFH.value == value:
            return CustomerBelongsTo.MYKFH
        if CustomerBelongsTo.MYOCBC.value == value:
            return CustomerBelongsTo.MYOCBC
        if CustomerBelongsTo.MYSCB.value == value:
            return CustomerBelongsTo.MYSCB
        if CustomerBelongsTo.MYUOB.value == value:
            return CustomerBelongsTo.MYUOB
        if CustomerBelongsTo.IPAY-MONZO.value == value:
            return CustomerBelongsTo.IPAY-MONZO
        if CustomerBelongsTo.IPAY-SANTANDER.value == value:
            return CustomerBelongsTo.IPAY-SANTANDER
        if CustomerBelongsTo.IPAY-HSBC.value == value:
            return CustomerBelongsTo.IPAY-HSBC
        if CustomerBelongsTo.IPAY-LLOYDS.value == value:
            return CustomerBelongsTo.IPAY-LLOYDS
        if CustomerBelongsTo.IPAY-REVOLUT.value == value:
            return CustomerBelongsTo.IPAY-REVOLUT
        if CustomerBelongsTo.IPAY-BARCLAYS.value == value:
            return CustomerBelongsTo.IPAY-BARCLAYS
        if CustomerBelongsTo.IPAY-NATWEST.value == value:
            return CustomerBelongsTo.IPAY-NATWEST
        if CustomerBelongsTo.IPAY-NATIONWIDE.value == value:
            return CustomerBelongsTo.IPAY-NATIONWIDE
        if CustomerBelongsTo.BKASH.value == value:
            return CustomerBelongsTo.BKASH
        if CustomerBelongsTo.EASYPAISA.value == value:
            return CustomerBelongsTo.EASYPAISA
        if CustomerBelongsTo.DIRECTDEBIT_YAPILY.value == value:
            return CustomerBelongsTo.DIRECTDEBIT_YAPILY
        if CustomerBelongsTo.ANTIM_BIZ_ACCOUNT.value == value:
            return CustomerBelongsTo.ANTIM_BIZ_ACCOUNT
        return None
