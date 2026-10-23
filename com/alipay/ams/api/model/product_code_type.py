from enum import Enum, unique
@unique
class ProductCodeType(Enum):
    """ProductCodeType枚举类"""

    CASHIER_PAYMENT = "CASHIER_PAYMENT"
    AGREEMENT_PAYMENT = "AGREEMENT_PAYMENT"
    IN_STORE_PAYMENT = "IN_STORE_PAYMENT"

    def to_ams_dict(self) -> str:
        return {
            "CASHIER_PAYMENT": "CASHIER_PAYMENT",
            "AGREEMENT_PAYMENT": "AGREEMENT_PAYMENT",
            "IN_STORE_PAYMENT": "IN_STORE_PAYMENT",
        }[self.name]

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if ProductCodeType.CASHIER_PAYMENT.value == value:
            return ProductCodeType.CASHIER_PAYMENT
        if ProductCodeType.AGREEMENT_PAYMENT.value == value:
            return ProductCodeType.AGREEMENT_PAYMENT
        if ProductCodeType.IN_STORE_PAYMENT.value == value:
            return ProductCodeType.IN_STORE_PAYMENT
        for member in ProductCodeType:
            if member.to_ams_dict() == value:
                return member
        return None

