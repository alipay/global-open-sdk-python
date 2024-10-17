from com.alipay.ams.api.model.settlement_bank_account import SettlementBankAccount


class SettlementInfo:
    def __init__(self):
        self.__settlement_currency = None
        self.__settlement_bank_account = None #type: SettlementBankAccount

    @property
    def settlement_currency(self):
        return self.__settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self.__settlement_currency = value

    @property
    def settlement_bank_account(self):
        return self.__settlement_bank_account

    @settlement_bank_account.setter
    def settlement_bank_account(self, value):
        self.__settlement_bank_account = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'settlement_currency') and self.settlement_currency:
            params['settlementCurrency'] = self.settlement_currency
        if hasattr(self, 'settlement_bank_account') and self.settlement_bank_account:
            params['settlementBankAccount'] = self.settlement_bank_account.to_ams_dict()
        return params