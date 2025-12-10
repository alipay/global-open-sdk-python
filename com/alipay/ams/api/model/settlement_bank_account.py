import json
from com.alipay.ams.api.model.account_holder_type import AccountHolderType
from com.alipay.ams.api.model.account_type import AccountType
from com.alipay.ams.api.model.address import Address




class SettlementBankAccount:
    def __init__(self):
        
        self.__bank_account_no = None  # type: str
        self.__account_holder_name = None  # type: str
        self.__swift_code = None  # type: str
        self.__bank_region = None  # type: str
        self.__account_holder_type = None  # type: AccountHolderType
        self.__routing_number = None  # type: str
        self.__branch_code = None  # type: str
        self.__account_holder_tin = None  # type: str
        self.__account_type = None  # type: AccountType
        self.__bank_name = None  # type: str
        self.__account_holder_address = None  # type: Address
        self.__iban = None  # type: str
        

    @property
    def bank_account_no(self):
        """
        The international bank account number.  The standardized formats in different areas are:  Brazil: ^[0-9]{0,20}$ such as 123456789 More information:  Maximum length: 64 characters
        """
        return self.__bank_account_no

    @bank_account_no.setter
    def bank_account_no(self, value):
        self.__bank_account_no = value
    @property
    def account_holder_name(self):
        """
        The full name of the account holder.  The standardized formats in different areas are:  Brazil: ^[A-Za-z0-9/() .,\\-?:&#39;+]{0,50}$ More information:  Maximum length: 64 characters
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value
    @property
    def swift_code(self):
        """
        The eight-character or eleven-character BIC or SWIFT code of the bank.  Specify this parameter when the bank card issuing country is Brazil.    More information:  Maximum length: 11 characters
        """
        return self.__swift_code

    @swift_code.setter
    def swift_code(self, value):
        self.__swift_code = value
    @property
    def bank_region(self):
        """
        The region where the bank is located.   The value of this parameter is a 2-letter region or country code that follows the ISO 3166 Country Codes standard.    More information:  Maximum length: 2 characters 
        """
        return self.__bank_region

    @bank_region.setter
    def bank_region(self, value):
        self.__bank_region = value
    @property
    def account_holder_type(self):
        """Gets the account_holder_type of this SettlementBankAccount.
        
        """
        return self.__account_holder_type

    @account_holder_type.setter
    def account_holder_type(self, value):
        self.__account_holder_type = value
    @property
    def routing_number(self):
        """
        The routing number. See Bank routing number for valid values.  Specify this parameter when the issuing bank is in Brazil.    More information:  Maximum length: 9 characters 
        """
        return self.__routing_number

    @routing_number.setter
    def routing_number(self, value):
        self.__routing_number = value
    @property
    def branch_code(self):
        """
        The branch code of the bank. See Bank branch code for valid value s.  Specify this parameter when the issuing bank is in Brazil.    More information:  Maximum length: 32 characters
        """
        return self.__branch_code

    @branch_code.setter
    def branch_code(self, value):
        self.__branch_code = value
    @property
    def account_holder_tin(self):
        """
        The tax identification number (TIN) of the account holder.  For the account holder in Brazil:  If the account holder is an individual, the value of this parameter is an eleven-character tax ID known as CPF.  If the account holder is a legal entity, the value of this parameter is a fourteen-character tax ID known as CNPJ.  Specify this parameter when the issuing bank is in Brazil.    More information:  Maximum length: 32 characters
        """
        return self.__account_holder_tin

    @account_holder_tin.setter
    def account_holder_tin(self, value):
        self.__account_holder_tin = value
    @property
    def account_type(self):
        """Gets the account_type of this SettlementBankAccount.
        
        """
        return self.__account_type

    @account_type.setter
    def account_type(self, value):
        self.__account_type = value
    @property
    def bank_name(self):
        """
        The name of the bank.  Specify this parameter when the card issuing country is the United States.    More information:  Maximum length: 256 characters
        """
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = value
    @property
    def account_holder_address(self):
        """Gets the account_holder_address of this SettlementBankAccount.
        
        """
        return self.__account_holder_address

    @account_holder_address.setter
    def account_holder_address(self, value):
        self.__account_holder_address = value
    @property
    def iban(self):
        """
        The International Bank Account Number (IBAN) used to identify a bank account.  Specify this parameter when the card issuing country is the United Kingdom or belongs to the European Union.    More information:  Maximum length: 34 characters
        """
        return self.__iban

    @iban.setter
    def iban(self, value):
        self.__iban = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "bank_account_no") and self.bank_account_no is not None:
            params['bankAccountNo'] = self.bank_account_no
        if hasattr(self, "account_holder_name") and self.account_holder_name is not None:
            params['accountHolderName'] = self.account_holder_name
        if hasattr(self, "swift_code") and self.swift_code is not None:
            params['swiftCode'] = self.swift_code
        if hasattr(self, "bank_region") and self.bank_region is not None:
            params['bankRegion'] = self.bank_region
        if hasattr(self, "account_holder_type") and self.account_holder_type is not None:
            params['accountHolderType'] = self.account_holder_type
        if hasattr(self, "routing_number") and self.routing_number is not None:
            params['routingNumber'] = self.routing_number
        if hasattr(self, "branch_code") and self.branch_code is not None:
            params['branchCode'] = self.branch_code
        if hasattr(self, "account_holder_tin") and self.account_holder_tin is not None:
            params['accountHolderTIN'] = self.account_holder_tin
        if hasattr(self, "account_type") and self.account_type is not None:
            params['accountType'] = self.account_type
        if hasattr(self, "bank_name") and self.bank_name is not None:
            params['bankName'] = self.bank_name
        if hasattr(self, "account_holder_address") and self.account_holder_address is not None:
            params['accountHolderAddress'] = self.account_holder_address
        if hasattr(self, "iban") and self.iban is not None:
            params['iban'] = self.iban
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'bankAccountNo' in response_body:
            self.__bank_account_no = response_body['bankAccountNo']
        if 'accountHolderName' in response_body:
            self.__account_holder_name = response_body['accountHolderName']
        if 'swiftCode' in response_body:
            self.__swift_code = response_body['swiftCode']
        if 'bankRegion' in response_body:
            self.__bank_region = response_body['bankRegion']
        if 'accountHolderType' in response_body:
            account_holder_type_temp = AccountHolderType.value_of(response_body['accountHolderType'])
            self.__account_holder_type = account_holder_type_temp
        if 'routingNumber' in response_body:
            self.__routing_number = response_body['routingNumber']
        if 'branchCode' in response_body:
            self.__branch_code = response_body['branchCode']
        if 'accountHolderTIN' in response_body:
            self.__account_holder_tin = response_body['accountHolderTIN']
        if 'accountType' in response_body:
            account_type_temp = AccountType.value_of(response_body['accountType'])
            self.__account_type = account_type_temp
        if 'bankName' in response_body:
            self.__bank_name = response_body['bankName']
        if 'accountHolderAddress' in response_body:
            self.__account_holder_address = Address()
            self.__account_holder_address.parse_rsp_body(response_body['accountHolderAddress'])
        if 'iban' in response_body:
            self.__iban = response_body['iban']
