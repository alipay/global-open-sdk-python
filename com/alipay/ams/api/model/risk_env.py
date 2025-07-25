import json




class RiskEnv:
    def __init__(self):
        
        self.__ip_address_type = None  # type: str
        

    @property
    def ip_address_type(self):
        """
        The type of an IP address
        """
        return self.__ip_address_type

    @ip_address_type.setter
    def ip_address_type(self, value):
        self.__ip_address_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "ip_address_type") and self.ip_address_type is not None:
            params['ipAddressType'] = self.ip_address_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'ipAddressType' in response_body:
            self.__ip_address_type = response_body['ipAddressType']
