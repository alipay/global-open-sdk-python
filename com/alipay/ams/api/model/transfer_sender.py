import json
from com.alipay.ams.api.model.fund_transfer_name import FundTransferName
from com.alipay.ams.api.model.fund_transfer_address import FundTransferAddress




class TransferSender:
    def __init__(self):
        
        self.__sender_name = None  # type: FundTransferName
        self.__address = None  # type: FundTransferAddress
        

    @property
    def sender_name(self):
        """Gets the sender_name of this TransferSender.
        
        """
        return self.__sender_name

    @sender_name.setter
    def sender_name(self, value):
        self.__sender_name = value
    @property
    def address(self):
        """Gets the address of this TransferSender.
        
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "sender_name") and self.sender_name is not None:
            params['senderName'] = self.sender_name
        if hasattr(self, "address") and self.address is not None:
            params['address'] = self.address
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'senderName' in response_body:
            self.__sender_name = FundTransferName()
            self.__sender_name.parse_rsp_body(response_body['senderName'])
        if 'address' in response_body:
            self.__address = FundTransferAddress()
            self.__address.parse_rsp_body(response_body['address'])
