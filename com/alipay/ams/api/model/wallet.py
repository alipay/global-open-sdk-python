import json
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address




class Wallet:
    def __init__(self):
        
        self.__account_no = None  # type: str
        self.__account_holder_name = None  # type: UserName
        self.__phone_no = None  # type: str
        self.__email = None  # type: str
        self.__billing_address = None  # type: Address
        self.__token = None  # type: str
        self.__token_expiry_time = None  # type: str
        

    @property
    def account_no(self):
        """Gets the account_no of this Wallet.
        
        """
        return self.__account_no

    @account_no.setter
    def account_no(self, value):
        self.__account_no = value
    @property
    def account_holder_name(self):
        """Gets the account_holder_name of this Wallet.
        
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value
    @property
    def phone_no(self):
        """Gets the phone_no of this Wallet.
        
        """
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, value):
        self.__phone_no = value
    @property
    def email(self):
        """Gets the email of this Wallet.
        
        """
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    @property
    def billing_address(self):
        """Gets the billing_address of this Wallet.
        
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value
    @property
    def token(self):
        """
        Added field for wallet token
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value
    @property
    def token_expiry_time(self):
        """
        Added field for token expiry time
        """
        return self.__token_expiry_time

    @token_expiry_time.setter
    def token_expiry_time(self, value):
        self.__token_expiry_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "account_no") and self.account_no is not None:
            params['accountNo'] = self.account_no
        if hasattr(self, "account_holder_name") and self.account_holder_name is not None:
            params['accountHolderName'] = self.account_holder_name
        if hasattr(self, "phone_no") and self.phone_no is not None:
            params['phoneNo'] = self.phone_no
        if hasattr(self, "email") and self.email is not None:
            params['email'] = self.email
        if hasattr(self, "billing_address") and self.billing_address is not None:
            params['billingAddress'] = self.billing_address
        if hasattr(self, "token") and self.token is not None:
            params['token'] = self.token
        if hasattr(self, "token_expiry_time") and self.token_expiry_time is not None:
            params['tokenExpiryTime'] = self.token_expiry_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'accountNo' in response_body:
            self.__account_no = response_body['accountNo']
        if 'accountHolderName' in response_body:
            self.__account_holder_name = UserName()
            self.__account_holder_name.parse_rsp_body(response_body['accountHolderName'])
        if 'phoneNo' in response_body:
            self.__phone_no = response_body['phoneNo']
        if 'email' in response_body:
            self.__email = response_body['email']
        if 'billingAddress' in response_body:
            self.__billing_address = Address()
            self.__billing_address.parse_rsp_body(response_body['billingAddress'])
        if 'token' in response_body:
            self.__token = response_body['token']
        if 'tokenExpiryTime' in response_body:
            self.__token_expiry_time = response_body['tokenExpiryTime']
