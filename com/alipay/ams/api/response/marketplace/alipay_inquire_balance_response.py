import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.account_balance import AccountBalance



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireBalanceResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__account_balances = None  # type: [AccountBalance]
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireBalanceResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def account_balances(self):
        """
        The list of balance accounts assigned by Alipay.  More information:Maximum length: 64 characters
        """
        return self.__account_balances

    @account_balances.setter
    def account_balances(self, value):
        self.__account_balances = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "account_balances") and self.account_balances is not None:
            params['accountBalances'] = self.account_balances
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireBalanceResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'accountBalances' in response_body:
            self.__account_balances = []
            for item in response_body['accountBalances']:
                obj = AccountBalance()
                obj.parse_rsp_body(item)
                self.__account_balances.append(obj)
