from enum import Enum, unique
@unique
class StatementTransactionType(Enum):
    """The type of transaction.  Valid values: - OVERFLOW_DEBIT: Indicates a fund outflow from the main account to the overflow account. Applicable to MY region merchants only. - OVERFLOW_CREDIT: Indicates a fund inflow to the main account back from the overflow account. Applicable to MY region merchants only. - CASH_BACK: Indicates a fund inflow for cashBack credit settlement to the merchant&#39;s main account. Applicable to CN and HK region merchants with VCC cashback feature enabled only."""

    PAYMENT = "PAYMENT"
    PAYMENT_REFUND = "PAYMENT_REFUND"
    CHARGE = "CHARGE"
    CHARGE_REFUND = "CHARGE_REFUND"
    TOPUP = "TOPUP"
    SETTLEMENT = "SETTLEMENT"
    WITHDRAW = "WITHDRAW"
    WITHDRAW_RETURN = "WITHDRAW_RETURN"
    TRANSFER = "TRANSFER"
    TRANSFER_RETURN = "TRANSFER_RETURN"
    TRANSFER_TO_CHINA = "TRANSFER_TO_CHINA"
    TRANSFER_RECIPIENT = "TRANSFER_RECIPIENT"
    EXCHANGE = "EXCHANGE"
    CREDIT_LOAN = "CREDIT_LOAN"
    CREDIT_REPAY = "CREDIT_REPAY"
    CREDIT_REPAYMENT = "CREDIT_REPAYMENT"
    DIRECT_PAYMENT = "DIRECT_PAYMENT"
    DIRECT_REFUND = "DIRECT_REFUND"
    CARD_PAYMENT = "CARD_PAYMENT"
    CARD_REFUND = "CARD_REFUND"
    OVERFLOW_DEBIT = "OVERFLOW_DEBIT"
    OVERFLOW_CREDIT = "OVERFLOW_CREDIT"
    CASH_BACK = "CASH_BACK"

    def to_ams_dict(self) -> str:
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if StatementTransactionType.PAYMENT.value == value:
            return StatementTransactionType.PAYMENT
        if StatementTransactionType.PAYMENT_REFUND.value == value:
            return StatementTransactionType.PAYMENT_REFUND
        if StatementTransactionType.CHARGE.value == value:
            return StatementTransactionType.CHARGE
        if StatementTransactionType.CHARGE_REFUND.value == value:
            return StatementTransactionType.CHARGE_REFUND
        if StatementTransactionType.TOPUP.value == value:
            return StatementTransactionType.TOPUP
        if StatementTransactionType.SETTLEMENT.value == value:
            return StatementTransactionType.SETTLEMENT
        if StatementTransactionType.WITHDRAW.value == value:
            return StatementTransactionType.WITHDRAW
        if StatementTransactionType.WITHDRAW_RETURN.value == value:
            return StatementTransactionType.WITHDRAW_RETURN
        if StatementTransactionType.TRANSFER.value == value:
            return StatementTransactionType.TRANSFER
        if StatementTransactionType.TRANSFER_RETURN.value == value:
            return StatementTransactionType.TRANSFER_RETURN
        if StatementTransactionType.TRANSFER_TO_CHINA.value == value:
            return StatementTransactionType.TRANSFER_TO_CHINA
        if StatementTransactionType.TRANSFER_RECIPIENT.value == value:
            return StatementTransactionType.TRANSFER_RECIPIENT
        if StatementTransactionType.EXCHANGE.value == value:
            return StatementTransactionType.EXCHANGE
        if StatementTransactionType.CREDIT_LOAN.value == value:
            return StatementTransactionType.CREDIT_LOAN
        if StatementTransactionType.CREDIT_REPAY.value == value:
            return StatementTransactionType.CREDIT_REPAY
        if StatementTransactionType.CREDIT_REPAYMENT.value == value:
            return StatementTransactionType.CREDIT_REPAYMENT
        if StatementTransactionType.DIRECT_PAYMENT.value == value:
            return StatementTransactionType.DIRECT_PAYMENT
        if StatementTransactionType.DIRECT_REFUND.value == value:
            return StatementTransactionType.DIRECT_REFUND
        if StatementTransactionType.CARD_PAYMENT.value == value:
            return StatementTransactionType.CARD_PAYMENT
        if StatementTransactionType.CARD_REFUND.value == value:
            return StatementTransactionType.CARD_REFUND
        if StatementTransactionType.OVERFLOW_DEBIT.value == value:
            return StatementTransactionType.OVERFLOW_DEBIT
        if StatementTransactionType.OVERFLOW_CREDIT.value == value:
            return StatementTransactionType.OVERFLOW_CREDIT
        if StatementTransactionType.CASH_BACK.value == value:
            return StatementTransactionType.CASH_BACK
        return None
