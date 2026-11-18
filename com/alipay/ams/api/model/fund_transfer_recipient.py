import json
from com.alipay.ams.api.model.fund_transfer_party_name import FundTransferPartyName
from com.alipay.ams.api.model.fund_transfer_party_address import FundTransferPartyAddress




class FundTransferRecipient:
    def __init__(self):
        
        self.__recipient_name = None  # type: FundTransferPartyName
        self.__address = None  # type: FundTransferPartyAddress
        self.__recipient_account_number = None  # type: str
        

    @property
    def recipient_name(self):
        """Gets the recipient_name of this FundTransferRecipient.
        
        """
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value):
        self.__recipient_name = value
    @property
    def address(self):
        """Gets the address of this FundTransferRecipient.
        
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
    @property
    def recipient_account_number(self):
        """
        The account number of the wallet receiving the top-up. Only letters, digits, and hyphens are supported. Maximum length: 64 characters.
        """
        return self.__recipient_account_number

    @recipient_account_number.setter
    def recipient_account_number(self, value):
        self.__recipient_account_number = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "recipient_name") and self.recipient_name is not None:
            params['recipientName'] = self.recipient_name
        if hasattr(self, "address") and self.address is not None:
            params['address'] = self.address
        if hasattr(self, "recipient_account_number") and self.recipient_account_number is not None:
            params['recipientAccountNumber'] = self.recipient_account_number
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'recipientName' in response_body:
            self.__recipient_name = FundTransferPartyName()
            self.__recipient_name.parse_rsp_body(response_body['recipientName'])
        if 'address' in response_body:
            self.__address = FundTransferPartyAddress()
            self.__address.parse_rsp_body(response_body['address'])
        if 'recipientAccountNumber' in response_body:
            self.__recipient_account_number = response_body['recipientAccountNumber']
