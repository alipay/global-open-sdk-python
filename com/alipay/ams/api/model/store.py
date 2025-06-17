import json
from com.alipay.ams.api.model.address import Address




class Store:
    def __init__(self):
        
        self.__reference_store_id = None  # type: str
        self.__store_name = None  # type: str
        self.__store_mcc = None  # type: str
        self.__store_display_name = None  # type: str
        self.__store_terminal_id = None  # type: str
        self.__store_operator_id = None  # type: str
        self.__store_address = None  # type: Address
        self.__store_phone_no = None  # type: str
        

    @property
    def reference_store_id(self):
        """Gets the reference_store_id of this Store.
        
        """
        return self.__reference_store_id

    @reference_store_id.setter
    def reference_store_id(self, value):
        self.__reference_store_id = value
    @property
    def store_name(self):
        """Gets the store_name of this Store.
        
        """
        return self.__store_name

    @store_name.setter
    def store_name(self, value):
        self.__store_name = value
    @property
    def store_mcc(self):
        """Gets the store_mcc of this Store.
        
        """
        return self.__store_mcc

    @store_mcc.setter
    def store_mcc(self, value):
        self.__store_mcc = value
    @property
    def store_display_name(self):
        """Gets the store_display_name of this Store.
        
        """
        return self.__store_display_name

    @store_display_name.setter
    def store_display_name(self, value):
        self.__store_display_name = value
    @property
    def store_terminal_id(self):
        """Gets the store_terminal_id of this Store.
        
        """
        return self.__store_terminal_id

    @store_terminal_id.setter
    def store_terminal_id(self, value):
        self.__store_terminal_id = value
    @property
    def store_operator_id(self):
        """Gets the store_operator_id of this Store.
        
        """
        return self.__store_operator_id

    @store_operator_id.setter
    def store_operator_id(self, value):
        self.__store_operator_id = value
    @property
    def store_address(self):
        """Gets the store_address of this Store.
        
        """
        return self.__store_address

    @store_address.setter
    def store_address(self, value):
        self.__store_address = value
    @property
    def store_phone_no(self):
        """Gets the store_phone_no of this Store.
        
        """
        return self.__store_phone_no

    @store_phone_no.setter
    def store_phone_no(self, value):
        self.__store_phone_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_store_id") and self.reference_store_id is not None:
            params['referenceStoreId'] = self.reference_store_id
        if hasattr(self, "store_name") and self.store_name is not None:
            params['storeName'] = self.store_name
        if hasattr(self, "store_mcc") and self.store_mcc is not None:
            params['storeMCC'] = self.store_mcc
        if hasattr(self, "store_display_name") and self.store_display_name is not None:
            params['storeDisplayName'] = self.store_display_name
        if hasattr(self, "store_terminal_id") and self.store_terminal_id is not None:
            params['storeTerminalId'] = self.store_terminal_id
        if hasattr(self, "store_operator_id") and self.store_operator_id is not None:
            params['storeOperatorId'] = self.store_operator_id
        if hasattr(self, "store_address") and self.store_address is not None:
            params['storeAddress'] = self.store_address
        if hasattr(self, "store_phone_no") and self.store_phone_no is not None:
            params['storePhoneNo'] = self.store_phone_no
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceStoreId' in response_body:
            self.__reference_store_id = response_body['referenceStoreId']
        if 'storeName' in response_body:
            self.__store_name = response_body['storeName']
        if 'storeMCC' in response_body:
            self.__store_mcc = response_body['storeMCC']
        if 'storeDisplayName' in response_body:
            self.__store_display_name = response_body['storeDisplayName']
        if 'storeTerminalId' in response_body:
            self.__store_terminal_id = response_body['storeTerminalId']
        if 'storeOperatorId' in response_body:
            self.__store_operator_id = response_body['storeOperatorId']
        if 'storeAddress' in response_body:
            self.__store_address = Address()
            self.__store_address.parse_rsp_body(response_body['storeAddress'])
        if 'storePhoneNo' in response_body:
            self.__store_phone_no = response_body['storePhoneNo']
