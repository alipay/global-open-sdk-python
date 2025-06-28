from enum import Enum, unique
@unique
class CustomerBelongsTo(Enum):
    """CustomerBelongsTo枚举类"""

    RABBIT_LINE_PAY = "RABBIT_LINE_PAY"
    TRUEMONEY = "TRUEMONEY"
    ALIPAY_HK = "ALIPAY_HK"
    TNG = "TNG"
    ALIPAY_CN = "ALIPAY_CN"
    GCASH = "GCASH"
    DANA = "DANA"
    KAKAOPAY = "KAKAOPAY"
    BKASH = "BKASH"
    EASYPAISA = "EASYPAISA"
    PAYPAY = "PAYPAY"
    BOOST = "BOOST"
    GRABPAY_MY = "GRABPAY_MY"
    MAYA = "MAYA"
    GRABPAY_PH = "GRABPAY_PH"
    GRABPAY_SG = "GRABPAY_SG"
    NAVERPAY = "NAVERPAY"
    JKOPAY = "JKOPAY"
    KPLUS = "KPLUS"
    DIRECT_DEBIT_SIAMCOMMERCIALBANK = "DIRECT_DEBIT_SIAMCOMMERCIALBANK"
    DIRECT_DEBIT_KRUNGTHAIBANK = "DIRECT_DEBIT_KRUNGTHAIBANK"
    ZALOPAY = "ZALOPAY"
    DIRECTDEBIT_YAPILY = "DIRECTDEBIT_YAPILY"
    TOSSPAY = "TOSSPAY"
    MOMO = "MOMO"
    ANTOM_BIZ_ACCOUNT = "ANTOM_BIZ_ACCOUNT"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CustomerBelongsTo.RABBIT_LINE_PAY.value == value:
            return CustomerBelongsTo.RABBIT_LINE_PAY
        if CustomerBelongsTo.TRUEMONEY.value == value:
            return CustomerBelongsTo.TRUEMONEY
        if CustomerBelongsTo.ALIPAY_HK.value == value:
            return CustomerBelongsTo.ALIPAY_HK
        if CustomerBelongsTo.TNG.value == value:
            return CustomerBelongsTo.TNG
        if CustomerBelongsTo.ALIPAY_CN.value == value:
            return CustomerBelongsTo.ALIPAY_CN
        if CustomerBelongsTo.GCASH.value == value:
            return CustomerBelongsTo.GCASH
        if CustomerBelongsTo.DANA.value == value:
            return CustomerBelongsTo.DANA
        if CustomerBelongsTo.KAKAOPAY.value == value:
            return CustomerBelongsTo.KAKAOPAY
        if CustomerBelongsTo.BKASH.value == value:
            return CustomerBelongsTo.BKASH
        if CustomerBelongsTo.EASYPAISA.value == value:
            return CustomerBelongsTo.EASYPAISA
        if CustomerBelongsTo.PAYPAY.value == value:
            return CustomerBelongsTo.PAYPAY
        if CustomerBelongsTo.BOOST.value == value:
            return CustomerBelongsTo.BOOST
        if CustomerBelongsTo.GRABPAY_MY.value == value:
            return CustomerBelongsTo.GRABPAY_MY
        if CustomerBelongsTo.MAYA.value == value:
            return CustomerBelongsTo.MAYA
        if CustomerBelongsTo.GRABPAY_PH.value == value:
            return CustomerBelongsTo.GRABPAY_PH
        if CustomerBelongsTo.GRABPAY_SG.value == value:
            return CustomerBelongsTo.GRABPAY_SG
        if CustomerBelongsTo.NAVERPAY.value == value:
            return CustomerBelongsTo.NAVERPAY
        if CustomerBelongsTo.JKOPAY.value == value:
            return CustomerBelongsTo.JKOPAY
        if CustomerBelongsTo.KPLUS.value == value:
            return CustomerBelongsTo.KPLUS
        if CustomerBelongsTo.DIRECT_DEBIT_SIAMCOMMERCIALBANK.value == value:
            return CustomerBelongsTo.DIRECT_DEBIT_SIAMCOMMERCIALBANK
        if CustomerBelongsTo.DIRECT_DEBIT_KRUNGTHAIBANK.value == value:
            return CustomerBelongsTo.DIRECT_DEBIT_KRUNGTHAIBANK
        if CustomerBelongsTo.ZALOPAY.value == value:
            return CustomerBelongsTo.ZALOPAY
        if CustomerBelongsTo.DIRECTDEBIT_YAPILY.value == value:
            return CustomerBelongsTo.DIRECTDEBIT_YAPILY
        if CustomerBelongsTo.TOSSPAY.value == value:
            return CustomerBelongsTo.TOSSPAY
        if CustomerBelongsTo.MOMO.value == value:
            return CustomerBelongsTo.MOMO
        if CustomerBelongsTo.ANTOM_BIZ_ACCOUNT.value == value:
            return CustomerBelongsTo.ANTOM_BIZ_ACCOUNT
        return None
