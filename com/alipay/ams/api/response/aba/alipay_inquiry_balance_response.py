import json
from com.alipay.ams.api.model.account_balance import AccountBalance
from com.alipay.ams.api.model.result import Result



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquiryBalanceResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__account_balances = None  # type: [AccountBalance]
        self.__result = None  # type: Result
        self.parse_rsp_body(rsp_body) 


    @property
    def account_balances(self):
        """Gets the account_balances of this AlipayInquiryBalanceResponse.
        
        """
        return self.__account_balances

    @account_balances.setter
    def account_balances(self, value):
        self.__account_balances = value
    @property
    def result(self):
        """Gets the result of this AlipayInquiryBalanceResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "account_balances") and self.account_balances is not None:
            params['accountBalances'] = self.account_balances
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquiryBalanceResponse, self).parse_rsp_body(response_body)
        if 'accountBalances' in response_body:
            self.__account_balances = []
            for item in response_body['accountBalances']:
                obj = AccountBalance()
                obj.parse_rsp_body(item)
                self.__account_balances.append(obj)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
