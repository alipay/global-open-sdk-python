import json

from com.alipay.ams.api.model.amount import Amount


class AccountBalance:
    def __init__(self):
        self.__account_balance = None
        self.__currency = None
        self.__available_balance = None #type: Amount
        self.__frozen_balance = None #type: Amount
        self.__total_balance = None #type: Amount

    @property
    def account_balance(self):
        return self.__account_balance
    @property
    def currency(self):
        return self.__currency

    @property
    def available_balance(self):
        return self.__available_balance

    @property
    def frozen_balance(self):
        return self.__frozen_balance

    @property
    def total_balance(self):
        return self.__total_balance

    def parse_rsp_body(self, response_body):
        if type(response_body) == str:
            response_body = json.loads(response_body)

        if 'accountBalance' in response_body:
            self.__account_balance = response_body['accountBalance']
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'availableBalance' in response_body:
            self.__available_balance = Amount()
            self.__available_balance.parse_rsp_body(response_body['availableBalance'])
        if 'frozenBalance' in response_body:
            self.__frozen_balance = Amount()
            self.__frozen_balance.parse_rsp_body(response_body['frozenBalance'])
        if 'totalBalance' in response_body:
            self.__total_balance = Amount()
            self.__total_balance.parse_rsp_body(response_body['totalBalance'])
