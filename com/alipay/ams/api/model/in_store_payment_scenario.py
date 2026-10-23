from enum import Enum, unique
@unique
class InStorePaymentScenario(Enum):
    """InStorePaymentScenario枚举类"""

    PAYMENTCODE = "PAYMENTCODE"
    ORDERCODE = "ORDERCODE"
    ENTRYCODE = "ENTRYCODE"

    def to_ams_dict(self) -> str:
        return {
            "PAYMENTCODE": "PaymentCode",
            "ORDERCODE": "OrderCode",
            "ENTRYCODE": "EntryCode",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if InStorePaymentScenario.PAYMENTCODE.value == value:
            return InStorePaymentScenario.PAYMENTCODE
        if InStorePaymentScenario.ORDERCODE.value == value:
            return InStorePaymentScenario.ORDERCODE
        if InStorePaymentScenario.ENTRYCODE.value == value:
            return InStorePaymentScenario.ENTRYCODE
        for member in InStorePaymentScenario:
            if member.to_ams_dict() == value:
                return member
        return None

