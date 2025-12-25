import json
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.address import Address




class CardholderInfo:
    def __init__(self):
        
        self.__card_holder_name = None  # type: UserName
        self.__bill_address = None  # type: Address
        

    @property
    def card_holder_name(self):
        """Gets the card_holder_name of this CardholderInfo.
        
        """
        return self.__card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value):
        self.__card_holder_name = value
    @property
    def bill_address(self):
        """Gets the bill_address of this CardholderInfo.
        
        """
        return self.__bill_address

    @bill_address.setter
    def bill_address(self, value):
        self.__bill_address = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "card_holder_name") and self.card_holder_name is not None:
            params['cardHolderName'] = self.card_holder_name
        if hasattr(self, "bill_address") and self.bill_address is not None:
            params['billAddress'] = self.bill_address
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'cardHolderName' in response_body:
            self.__card_holder_name = UserName()
            self.__card_holder_name.parse_rsp_body(response_body['cardHolderName'])
        if 'billAddress' in response_body:
            self.__bill_address = Address()
            self.__bill_address.parse_rsp_body(response_body['billAddress'])
