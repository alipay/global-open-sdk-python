from com.alipay.ams.api.model.account_balance import AccountBalance
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayInquireBalanceResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayInquireBalanceResponse, self).__init__()
        self.__account_balances = None #type: list[AccountBalance]
        self.__parse_rsp_body(rsp_body)



    @property
    def account_balances(self):
        return self.__account_balances


    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayInquireBalanceResponse, self).parse_rsp_body(rsp_body)
        if 'accountBalances' in response:
            accountBalances = []
            for accountBalance_body in response['accountBalances']:
                accountBalance = AccountBalance()
                accountBalance.parse_rsp_body(accountBalance_body)
                accountBalances.append(accountBalance)
            self.__account_balances = accountBalances