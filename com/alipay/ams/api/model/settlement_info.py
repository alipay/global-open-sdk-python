import json
from com.alipay.ams.api.model.settlement_bank_account import SettlementBankAccount




class SettlementInfo:
    def __init__(self):
        
        self.__settlement_currency = None  # type: str
        self.__settlement_bank_account = None  # type: SettlementBankAccount
        

    @property
    def settlement_currency(self):
        """
        The sub-merchant&#39;s settlement currency that is specified in the settlement contract. The value of this parameter is a 3-letter currency code that follows the ISO 4217 standard.   More information:  Maximum length: 3 characters 
        """
        return self.__settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self.__settlement_currency = value
    @property
    def settlement_bank_account(self):
        """Gets the settlement_bank_account of this SettlementInfo.
        
        """
        return self.__settlement_bank_account

    @settlement_bank_account.setter
    def settlement_bank_account(self, value):
        self.__settlement_bank_account = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "settlement_currency") and self.settlement_currency is not None:
            params['settlementCurrency'] = self.settlement_currency
        if hasattr(self, "settlement_bank_account") and self.settlement_bank_account is not None:
            params['settlementBankAccount'] = self.settlement_bank_account
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'settlementCurrency' in response_body:
            self.__settlement_currency = response_body['settlementCurrency']
        if 'settlementBankAccount' in response_body:
            self.__settlement_bank_account = SettlementBankAccount()
            self.__settlement_bank_account.parse_rsp_body(response_body['settlementBankAccount'])
