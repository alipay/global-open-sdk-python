import json
from com.alipay.ams.api.model.user_name import UserName




class RefundToBankInfo:
    def __init__(self):
        
        self.__bank_code = None  # type: str
        self.__account_holder_name = None  # type: UserName
        self.__account_no = None  # type: str
        

    @property
    def bank_code(self):
        """Gets the bank_code of this RefundToBankInfo.
        
        """
        return self.__bank_code

    @bank_code.setter
    def bank_code(self, value):
        self.__bank_code = value
    @property
    def account_holder_name(self):
        """Gets the account_holder_name of this RefundToBankInfo.
        
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value
    @property
    def account_no(self):
        """Gets the account_no of this RefundToBankInfo.
        
        """
        return self.__account_no

    @account_no.setter
    def account_no(self, value):
        self.__account_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "bank_code") and self.bank_code is not None:
            params['bankCode'] = self.bank_code
        if hasattr(self, "account_holder_name") and self.account_holder_name is not None:
            params['accountHolderName'] = self.account_holder_name
        if hasattr(self, "account_no") and self.account_no is not None:
            params['accountNo'] = self.account_no
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'bankCode' in response_body:
            self.__bank_code = response_body['bankCode']
        if 'accountHolderName' in response_body:
            self.__account_holder_name = UserName()
            self.__account_holder_name.parse_rsp_body(response_body['accountHolderName'])
        if 'accountNo' in response_body:
            self.__account_no = response_body['accountNo']
