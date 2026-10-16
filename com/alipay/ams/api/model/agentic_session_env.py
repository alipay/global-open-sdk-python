import json




class AgenticSessionEnv:
    def __init__(self):
        
        self.__terminal_type = None  # type: str
        self.__device_brand = None  # type: str
        self.__device_id = None  # type: str
        self.__os_type = None  # type: str
        self.__client_ip = None  # type: str
        

    @property
    def terminal_type(self):
        """
        Terminal type. Closed, case-sensitive values: WEB, WAP, APP, MINI_APP. Other values return PARAM_ILLEGAL/F. Supported values (case-sensitive): WEB, WAP, APP, MINI_APP.
        """
        return self.__terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self.__terminal_type = value
    @property
    def device_brand(self):
        """
        Device brand, for example Apple.
        """
        return self.__device_brand

    @device_brand.setter
    def device_brand(self, value):
        self.__device_brand = value
    @property
    def device_id(self):
        """
        Device identifier.
        """
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        self.__device_id = value
    @property
    def os_type(self):
        """
        Operating system type. Closed, case-sensitive values: IOS, ANDROID. Other values return PARAM_ILLEGAL/F. Supported values (case-sensitive): IOS, ANDROID.
        """
        return self.__os_type

    @os_type.setter
    def os_type(self, value):
        self.__os_type = value
    @property
    def client_ip(self):
        """
        Client IP supplied in the request body. Must be a valid IPv4 or IPv6 text value.
        """
        return self.__client_ip

    @client_ip.setter
    def client_ip(self, value):
        self.__client_ip = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "terminal_type") and self.terminal_type is not None:
            params['terminalType'] = self.terminal_type
        if hasattr(self, "device_brand") and self.device_brand is not None:
            params['deviceBrand'] = self.device_brand
        if hasattr(self, "device_id") and self.device_id is not None:
            params['deviceId'] = self.device_id
        if hasattr(self, "os_type") and self.os_type is not None:
            params['osType'] = self.os_type
        if hasattr(self, "client_ip") and self.client_ip is not None:
            params['clientIp'] = self.client_ip
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'terminalType' in response_body:
            self.__terminal_type = response_body['terminalType']
        if 'deviceBrand' in response_body:
            self.__device_brand = response_body['deviceBrand']
        if 'deviceId' in response_body:
            self.__device_id = response_body['deviceId']
        if 'osType' in response_body:
            self.__os_type = response_body['osType']
        if 'clientIp' in response_body:
            self.__client_ip = response_body['clientIp']
