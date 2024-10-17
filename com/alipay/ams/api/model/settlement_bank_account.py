from com.alipay.ams.api.model.account_holder_type import AccountHolderType
from com.alipay.ams.api.model.account_type import AccountType
from com.alipay.ams.api.model.address import Address


class SettlementBankAccount:
    def __init__(self):
        self.__bank_account_no = None
        self.__account_holder_name = None
        self.__swift_code = None
        self.__bank_region = None
        self.__account_holder_type = None  # type: AccountHolderType
        self.__routing_number = None
        self.__branch_code = None
        self.__account_holder_tIN = None
        self.__account_type = None  # type: AccountType
        self.__bank_name = None
        self.__account_holder_address = None  # type: Address
        self.__iban = None

    @property
    def bank_account_no(self):
        return self.__bank_account_no

    @bank_account_no.setter
    def bank_account_no(self, value):
        self.__bank_account_no = value

    @property
    def account_holder_name(self):
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value

    @property
    def swift_code(self):
        return self.__swift_code

    @swift_code.setter
    def swift_code(self, value):
        self.__swift_code = value

    @property
    def bank_region(self):
        return self.__bank_region

    @bank_region.setter
    def bank_region(self, value):
        self.__bank_region = value

    @property
    def account_holder_type(self):
        return self.__account_holder_type

    @account_holder_type.setter
    def account_holder_type(self, value):
        self.__account_holder_type = value

    @property
    def routing_number(self):
        return self.__routing_number

    @routing_number.setter
    def routing_number(self, value):
        self.__routing_number = value

    @property
    def branch_code(self):
        return self.__branch_code

    @branch_code.setter
    def branch_code(self, value):
        self.__branch_code = value

    @property
    def account_holder_tIN(self):
        return self.__account_holder_tIN

    @account_holder_tIN.setter
    def account_holder_tIN(self, value):
        self.__account_holder_tIN = value

    @property
    def account_type(self):
        return self.__account_type

    @account_type.setter
    def account_type(self, value):
        self.__account_type = value

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = value

    @property
    def account_holder_address(self):
        return self.__account_holder_address

    @account_holder_address.setter
    def account_holder_address(self, value):
        self.__account_holder_address = value

    @property
    def iban(self):
        return self.__iban

    @iban.setter
    def iban(self, value):
        self.__iban = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "bank_account_no") and self.bank_account_no:
            params['bankAccountNo'] = self.bank_account_no
        if hasattr(self, "account_holder_name") and self.account_holder_name:
            params['accountHolderName'] = self.account_holder_name
        if hasattr(self, "swift_code") and self.swift_code:
            params['swiftCode'] = self.swift_code
        if hasattr(self, "bank_region") and self.bank_region:
            params['bankRegion'] = self.bank_region
        if hasattr(self, "account_holder_type") and self.account_holder_type:
            params['accountHolderType'] = self.account_holder_type.value
        if hasattr(self, "routing_number") and self.routing_number:
            params['routingNumber'] = self.routing_number
        if hasattr(self, "branch_code") and self.branch_code:
            params['branchCode'] = self.branch_code
        if hasattr(self, "account_holder_tIN") and self.account_holder_tIN:
            params['accountHolderTIN'] = self.account_holder_tIN
        if hasattr(self, "account_type") and self.account_type:
            params['accountType'] = self.account_type.value
        if hasattr(self, "bank_name") and self.bank_name:
            params['bankName'] = self.bank_name
        if hasattr(self, "account_holder_address") and self.account_holder_address:
            params['accountHolderAddress'] = self.account_holder_address.to_ams_dict()
        if hasattr(self, "iban") and self.iban:
            params['iban'] = self.iban
        return params
