import json




class AuthMetaData:
    def __init__(self):
        
        self.__account_holder_name = None  # type: str
        self.__account_holder_cert_no = None  # type: str
        

    @property
    def account_holder_name(self):
        """Gets the account_holder_name of this AuthMetaData.
        
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value
    @property
    def account_holder_cert_no(self):
        """Gets the account_holder_cert_no of this AuthMetaData.
        
        """
        return self.__account_holder_cert_no

    @account_holder_cert_no.setter
    def account_holder_cert_no(self, value):
        self.__account_holder_cert_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "account_holder_name") and self.account_holder_name is not None:
            params['accountHolderName'] = self.account_holder_name
        if hasattr(self, "account_holder_cert_no") and self.account_holder_cert_no is not None:
            params['accountHolderCertNo'] = self.account_holder_cert_no
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'accountHolderName' in response_body:
            self.__account_holder_name = response_body['accountHolderName']
        if 'accountHolderCertNo' in response_body:
            self.__account_holder_cert_no = response_body['accountHolderCertNo']
