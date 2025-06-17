import json
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.store import Store
from com.alipay.ams.api.model.merchant_type import MerchantType




class Merchant:
    def __init__(self):
        
        self.__reference_merchant_id = None  # type: str
        self.__merchant_mcc = None  # type: str
        self.__merchant_name = None  # type: str
        self.__merchant_display_name = None  # type: str
        self.__merchant_address = None  # type: Address
        self.__merchant_register_date = None  # type: str
        self.__store = None  # type: Store
        self.__merchant_type = None  # type: MerchantType
        

    @property
    def reference_merchant_id(self):
        """Gets the reference_merchant_id of this Merchant.
        
        """
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value
    @property
    def merchant_mcc(self):
        """Gets the merchant_mcc of this Merchant.
        
        """
        return self.__merchant_mcc

    @merchant_mcc.setter
    def merchant_mcc(self, value):
        self.__merchant_mcc = value
    @property
    def merchant_name(self):
        """Gets the merchant_name of this Merchant.
        
        """
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self.__merchant_name = value
    @property
    def merchant_display_name(self):
        """Gets the merchant_display_name of this Merchant.
        
        """
        return self.__merchant_display_name

    @merchant_display_name.setter
    def merchant_display_name(self, value):
        self.__merchant_display_name = value
    @property
    def merchant_address(self):
        """Gets the merchant_address of this Merchant.
        
        """
        return self.__merchant_address

    @merchant_address.setter
    def merchant_address(self, value):
        self.__merchant_address = value
    @property
    def merchant_register_date(self):
        """Gets the merchant_register_date of this Merchant.
        
        """
        return self.__merchant_register_date

    @merchant_register_date.setter
    def merchant_register_date(self, value):
        self.__merchant_register_date = value
    @property
    def store(self):
        """Gets the store of this Merchant.
        
        """
        return self.__store

    @store.setter
    def store(self, value):
        self.__store = value
    @property
    def merchant_type(self):
        """Gets the merchant_type of this Merchant.
        
        """
        return self.__merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self.__merchant_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id is not None:
            params['referenceMerchantId'] = self.reference_merchant_id
        if hasattr(self, "merchant_mcc") and self.merchant_mcc is not None:
            params['merchantMCC'] = self.merchant_mcc
        if hasattr(self, "merchant_name") and self.merchant_name is not None:
            params['merchantName'] = self.merchant_name
        if hasattr(self, "merchant_display_name") and self.merchant_display_name is not None:
            params['merchantDisplayName'] = self.merchant_display_name
        if hasattr(self, "merchant_address") and self.merchant_address is not None:
            params['merchantAddress'] = self.merchant_address
        if hasattr(self, "merchant_register_date") and self.merchant_register_date is not None:
            params['merchantRegisterDate'] = self.merchant_register_date
        if hasattr(self, "store") and self.store is not None:
            params['store'] = self.store
        if hasattr(self, "merchant_type") and self.merchant_type is not None:
            params['merchantType'] = self.merchant_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceMerchantId' in response_body:
            self.__reference_merchant_id = response_body['referenceMerchantId']
        if 'merchantMCC' in response_body:
            self.__merchant_mcc = response_body['merchantMCC']
        if 'merchantName' in response_body:
            self.__merchant_name = response_body['merchantName']
        if 'merchantDisplayName' in response_body:
            self.__merchant_display_name = response_body['merchantDisplayName']
        if 'merchantAddress' in response_body:
            self.__merchant_address = Address()
            self.__merchant_address.parse_rsp_body(response_body['merchantAddress'])
        if 'merchantRegisterDate' in response_body:
            self.__merchant_register_date = response_body['merchantRegisterDate']
        if 'store' in response_body:
            self.__store = Store()
            self.__store.parse_rsp_body(response_body['store'])
        if 'merchantType' in response_body:
            merchant_type_temp = MerchantType.value_of(response_body['merchantType'])
            self.__merchant_type = merchant_type_temp
