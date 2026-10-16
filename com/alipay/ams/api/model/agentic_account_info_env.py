import json




class AgenticAccountInfoEnv:
    def __init__(self):
        
        self.__terminal_type = None  # type: str
        self.__os_type = None  # type: str
        self.__device_id = None  # type: str
        self.__device_token_id = None  # type: str
        self.__client_ip = None  # type: str
        self.__extend_info = None  # type: str
        self.__device_language = None  # type: str
        self.__user_agent = None  # type: str
        

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
    def os_type(self):
        """
        Operating system type. Closed, case-sensitive values: IOS, ANDROID. Other values return PARAM_ILLEGAL/F. Supported values (case-sensitive): IOS, ANDROID.
        """
        return self.__os_type

    @os_type.setter
    def os_type(self, value):
        self.__os_type = value
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
    def device_token_id(self):
        """
        Device token identifier.
        """
        return self.__device_token_id

    @device_token_id.setter
    def device_token_id(self, value):
        self.__device_token_id = value
    @property
    def client_ip(self):
        """
        Client IP supplied in the request body. Must be a valid IPv4 or IPv6 text value.
        """
        return self.__client_ip

    @client_ip.setter
    def client_ip(self, value):
        self.__client_ip = value
    @property
    def extend_info(self):
        """
        Extended environment information.
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def device_language(self):
        """
        Device language.
        """
        return self.__device_language

    @device_language.setter
    def device_language(self, value):
        self.__device_language = value
    @property
    def user_agent(self):
        """
        User-Agent.
        """
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value):
        self.__user_agent = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "terminal_type") and self.terminal_type is not None:
            params['terminalType'] = self.terminal_type
        if hasattr(self, "os_type") and self.os_type is not None:
            params['osType'] = self.os_type
        if hasattr(self, "device_id") and self.device_id is not None:
            params['deviceId'] = self.device_id
        if hasattr(self, "device_token_id") and self.device_token_id is not None:
            params['deviceTokenId'] = self.device_token_id
        if hasattr(self, "client_ip") and self.client_ip is not None:
            params['clientIp'] = self.client_ip
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "device_language") and self.device_language is not None:
            params['deviceLanguage'] = self.device_language
        if hasattr(self, "user_agent") and self.user_agent is not None:
            params['userAgent'] = self.user_agent
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'terminalType' in response_body:
            self.__terminal_type = response_body['terminalType']
        if 'osType' in response_body:
            self.__os_type = response_body['osType']
        if 'deviceId' in response_body:
            self.__device_id = response_body['deviceId']
        if 'deviceTokenId' in response_body:
            self.__device_token_id = response_body['deviceTokenId']
        if 'clientIp' in response_body:
            self.__client_ip = response_body['clientIp']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'deviceLanguage' in response_body:
            self.__device_language = response_body['deviceLanguage']
        if 'userAgent' in response_body:
            self.__user_agent = response_body['userAgent']
