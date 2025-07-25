from enum import Enum, unique
@unique
class PaymentMethodCategoryType(Enum):
    """PaymentMethodCategoryType枚举类"""

    ALIPAY_PLUS = "ALIPAY_PLUS"
    WALLET = "WALLET"
    MOBILE_BANKING_APP = "MOBILE_BANKING_APP"
    BANK_TRANSFER = "BANK_TRANSFER"
    ONLINE_BANKING = "ONLINE_BANKING"
    CARD = "CARD"
    OTC = "OTC"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if PaymentMethodCategoryType.ALIPAY_PLUS.value == value:
            return PaymentMethodCategoryType.ALIPAY_PLUS
        if PaymentMethodCategoryType.WALLET.value == value:
            return PaymentMethodCategoryType.WALLET
        if PaymentMethodCategoryType.MOBILE_BANKING_APP.value == value:
            return PaymentMethodCategoryType.MOBILE_BANKING_APP
        if PaymentMethodCategoryType.BANK_TRANSFER.value == value:
            return PaymentMethodCategoryType.BANK_TRANSFER
        if PaymentMethodCategoryType.ONLINE_BANKING.value == value:
            return PaymentMethodCategoryType.ONLINE_BANKING
        if PaymentMethodCategoryType.CARD.value == value:
            return PaymentMethodCategoryType.CARD
        if PaymentMethodCategoryType.OTC.value == value:
            return PaymentMethodCategoryType.OTC
        return None
