import json
from com.alipay.ams.api.model.tax_address import TaxAddress




class TaxHeadOffice:
    def __init__(self):
        
        self.__address = None  # type: TaxAddress
        

    @property
    def address(self):
        """Gets the address of this TaxHeadOffice.
        
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "address") and self.address is not None:
            params['address'] = self.address
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'address' in response_body:
            self.__address = TaxAddress()
            self.__address.parse_rsp_body(response_body['address'])
