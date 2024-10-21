
class AuthMetaData:
    def __init__(self):
        self.__account_holder_name = None
        self.__account_holder_certNo = None


    @property
    def account_holder_name(self):
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value

    @property
    def account_holder_certNo(self):
        return self.__account_holder_certNo

    @account_holder_certNo.setter
    def account_holder_certNo(self, value):
        self.__account_holder_certNo = value


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "account_holder_name") and self.account_holder_name:
            params['accountHolderName'] = self.account_holder_name
        if hasattr(self, "account_holder_certNo") and self.account_holder_certNo:
            params['accountHolderCertNo'] = self.account_holder_certNo

        return params