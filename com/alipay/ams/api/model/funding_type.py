from enum import Enum, unique
@unique
class FundingType(Enum):
    """The funding source type for the payment method"""

    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    PREPAID = "PREPAID"
    CHARGE = "CHARGE"
    DEFERRED_DEBIT = "DEFERRED_DEBIT"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if FundingType.CREDIT.value == value:
            return FundingType.CREDIT
        if FundingType.DEBIT.value == value:
            return FundingType.DEBIT
        if FundingType.PREPAID.value == value:
            return FundingType.PREPAID
        if FundingType.CHARGE.value == value:
            return FundingType.CHARGE
        if FundingType.DEFERRED_DEBIT.value == value:
            return FundingType.DEFERRED_DEBIT
        return None
