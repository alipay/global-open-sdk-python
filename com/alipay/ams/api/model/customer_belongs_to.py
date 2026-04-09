from enum import Enum, unique
@unique
class CustomerBelongsTo(Enum):
    """CustomerBelongsTo枚举类"""

    ALIPAY_CN = "ALIPAY_CN"
    ALIPAY_HK = "ALIPAY_HK"
    MPAY = "MPAY"
    DANA = "DANA"
    PAYPAY = "PAYPAY"
    BOOST = "BOOST"
    TNG = "TNG"
    GRABPAY_MY = "GRABPAY_MY"
    HIPAY = "HIPAY"
    GCASH = "GCASH"
    MAYA = "MAYA"
    GRABPAY_PH = "GRABPAY_PH"
    GRABPAY_SG = "GRABPAY_SG"
    KAKAOPAY = "KAKAOPAY"
    NAVERPAY = "NAVERPAY"
    TOSSPAY = "TOSSPAY"
    RABBIT_LINE_PAY = "RABBIT_LINE_PAY"
    TRUEMONEY = "TRUEMONEY"
    KPLUS = "KPLUS"
    DIRECT_DEBIT_SIAMCOMMERCIALBANK = "DIRECT_DEBIT_SIAMCOMMERCIALBANK"
    DIRECT_DEBIT_KRUNGTHAIBANK = "DIRECT_DEBIT_KRUNGTHAIBANK"
    ACH_DIRECT_DEBIT = "ACH_DIRECT_DEBIT"
    ZALOPAY = "ZALOPAY"
    MOMO = "MOMO"
    VIETTELMONEY = "VIETTELMONEY"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CustomerBelongsTo.ALIPAY_CN.value == value:
            return CustomerBelongsTo.ALIPAY_CN
        if CustomerBelongsTo.ALIPAY_HK.value == value:
            return CustomerBelongsTo.ALIPAY_HK
        if CustomerBelongsTo.MPAY.value == value:
            return CustomerBelongsTo.MPAY
        if CustomerBelongsTo.DANA.value == value:
            return CustomerBelongsTo.DANA
        if CustomerBelongsTo.PAYPAY.value == value:
            return CustomerBelongsTo.PAYPAY
        if CustomerBelongsTo.BOOST.value == value:
            return CustomerBelongsTo.BOOST
        if CustomerBelongsTo.TNG.value == value:
            return CustomerBelongsTo.TNG
        if CustomerBelongsTo.GRABPAY_MY.value == value:
            return CustomerBelongsTo.GRABPAY_MY
        if CustomerBelongsTo.HIPAY.value == value:
            return CustomerBelongsTo.HIPAY
        if CustomerBelongsTo.GCASH.value == value:
            return CustomerBelongsTo.GCASH
        if CustomerBelongsTo.MAYA.value == value:
            return CustomerBelongsTo.MAYA
        if CustomerBelongsTo.GRABPAY_PH.value == value:
            return CustomerBelongsTo.GRABPAY_PH
        if CustomerBelongsTo.GRABPAY_SG.value == value:
            return CustomerBelongsTo.GRABPAY_SG
        if CustomerBelongsTo.KAKAOPAY.value == value:
            return CustomerBelongsTo.KAKAOPAY
        if CustomerBelongsTo.NAVERPAY.value == value:
            return CustomerBelongsTo.NAVERPAY
        if CustomerBelongsTo.TOSSPAY.value == value:
            return CustomerBelongsTo.TOSSPAY
        if CustomerBelongsTo.RABBIT_LINE_PAY.value == value:
            return CustomerBelongsTo.RABBIT_LINE_PAY
        if CustomerBelongsTo.TRUEMONEY.value == value:
            return CustomerBelongsTo.TRUEMONEY
        if CustomerBelongsTo.KPLUS.value == value:
            return CustomerBelongsTo.KPLUS
        if CustomerBelongsTo.DIRECT_DEBIT_SIAMCOMMERCIALBANK.value == value:
            return CustomerBelongsTo.DIRECT_DEBIT_SIAMCOMMERCIALBANK
        if CustomerBelongsTo.DIRECT_DEBIT_KRUNGTHAIBANK.value == value:
            return CustomerBelongsTo.DIRECT_DEBIT_KRUNGTHAIBANK
        if CustomerBelongsTo.ACH_DIRECT_DEBIT.value == value:
            return CustomerBelongsTo.ACH_DIRECT_DEBIT
        if CustomerBelongsTo.ZALOPAY.value == value:
            return CustomerBelongsTo.ZALOPAY
        if CustomerBelongsTo.MOMO.value == value:
            return CustomerBelongsTo.MOMO
        if CustomerBelongsTo.VIETTELMONEY.value == value:
            return CustomerBelongsTo.VIETTELMONEY
        return None
