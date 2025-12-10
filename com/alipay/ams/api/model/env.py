import json
from com.alipay.ams.api.model.terminal_type import TerminalType
from com.alipay.ams.api.model.os_type import OsType
from com.alipay.ams.api.model.browser_info import BrowserInfo




class Env:
    def __init__(self):
        
        self.__terminal_type = None  # type: TerminalType
        self.__os_type = None  # type: OsType
        self.__user_agent = None  # type: str
        self.__device_token_id = None  # type: str
        self.__client_ip = None  # type: str
        self.__cookie_id = None  # type: str
        self.__extend_info = None  # type: str
        self.__store_terminal_id = None  # type: str
        self.__store_terminal_request_time = None  # type: str
        self.__browser_info = None  # type: BrowserInfo
        self.__color_depth = None  # type: str
        self.__screen_height = None  # type: str
        self.__screen_width = None  # type: str
        self.__time_zone_offset = None  # type: int
        self.__device_brand = None  # type: str
        self.__device_model = None  # type: str
        self.__device_language = None  # type: str
        self.__device_id = None  # type: str
        self.__os_version = None  # type: str
        

    @property
    def terminal_type(self):
        """Gets the terminal_type of this Env.
        
        """
        return self.__terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self.__terminal_type = value
    @property
    def os_type(self):
        """Gets the os_type of this Env.
        
        """
        return self.__os_type

    @os_type.setter
    def os_type(self, value):
        self.__os_type = value
    @property
    def user_agent(self):
        """Gets the user_agent of this Env.
        
        """
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value):
        self.__user_agent = value
    @property
    def device_token_id(self):
        """
        The token identifier of the device.  Note: Specify this parameter if you integrate with the Antom Device Fingerprint client, which is an SDK or JavaScript library that is used to collect device-related information, such as osType, deviceLanguage, deviceId, websiteLanguage, and userAgent. The device-related information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates. For more information about the Antom Device Fingerprint client, contact Antom Technical Support.    More information:  Maximum length: 64 characters
        """
        return self.__device_token_id

    @device_token_id.setter
    def device_token_id(self, value):
        self.__device_token_id = value
    @property
    def client_ip(self):
        """
        Client IP address of the device.
        """
        return self.__client_ip

    @client_ip.setter
    def client_ip(self, value):
        self.__client_ip = value
    @property
    def cookie_id(self):
        """Gets the cookie_id of this Env.
        
        """
        return self.__cookie_id

    @cookie_id.setter
    def cookie_id(self, value):
        self.__cookie_id = value
    @property
    def extend_info(self):
        """
        Extended information.  Specify this field if you need to use the extended information.    More information:  Maximum length: 2048 characters
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def store_terminal_id(self):
        """Gets the store_terminal_id of this Env.
        
        """
        return self.__store_terminal_id

    @store_terminal_id.setter
    def store_terminal_id(self, value):
        self.__store_terminal_id = value
    @property
    def store_terminal_request_time(self):
        """Gets the store_terminal_request_time of this Env.
        
        """
        return self.__store_terminal_request_time

    @store_terminal_request_time.setter
    def store_terminal_request_time(self, value):
        self.__store_terminal_request_time = value
    @property
    def browser_info(self):
        """Gets the browser_info of this Env.
        
        """
        return self.__browser_info

    @browser_info.setter
    def browser_info(self, value):
        self.__browser_info = value
    @property
    def color_depth(self):
        """
        The color depth of the user&#39;s browser in bits per pixel. The value is obtained by using the browser&#39;s screen.colorDepth property. Valid values are 1, 4, 8, 15, 16, 24, 30, 32, or 48. For example, 8 means 8-bit color depth.    More information:  Value range: 0 - unlimited
        """
        return self.__color_depth

    @color_depth.setter
    def color_depth(self, value):
        self.__color_depth = value
    @property
    def screen_height(self):
        """
        The screen height of the user&#39;s device in pixels.    Note: Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.    More information:  Value range: 1 - unlimited
        """
        return self.__screen_height

    @screen_height.setter
    def screen_height(self, value):
        self.__screen_height = value
    @property
    def screen_width(self):
        """
        The screen width of the user&#39;s device in pixels.    Note: Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.    More information:  Value range: 1 - unlimited
        """
        return self.__screen_width

    @screen_width.setter
    def screen_width(self, value):
        self.__screen_width = value
    @property
    def time_zone_offset(self):
        """
        The time difference between UTC time and the local time of the user&#39;s browser, in minutes. The value is obtained by using the getTimezoneOffset() property. For example, if the local time of the user&#39;s browser is UTC+2, the value of this parameter is -120.  Note: Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.  More information:  Value range: -720 - 720
        """
        return self.__time_zone_offset

    @time_zone_offset.setter
    def time_zone_offset(self, value):
        self.__time_zone_offset = value
    @property
    def device_brand(self):
        """
        The brand of the user&#39;s device.   Note: Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.    More information:  Maximum length: 64 characters
        """
        return self.__device_brand

    @device_brand.setter
    def device_brand(self, value):
        self.__device_brand = value
    @property
    def device_model(self):
        """
        The model of the user&#39;s device.   Note: Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.    More information:  Maximum length: 128 characters
        """
        return self.__device_model

    @device_model.setter
    def device_model(self, value):
        self.__device_model = value
    @property
    def device_language(self):
        """
        Device language of the user.
        """
        return self.__device_language

    @device_language.setter
    def device_language(self, value):
        self.__device_language = value
    @property
    def device_id(self):
        """
        Device ID of the user.
        """
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        self.__device_id = value
    @property
    def os_version(self):
        """
        Version of the operation system.
        """
        return self.__os_version

    @os_version.setter
    def os_version(self, value):
        self.__os_version = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "terminal_type") and self.terminal_type is not None:
            params['terminalType'] = self.terminal_type
        if hasattr(self, "os_type") and self.os_type is not None:
            params['osType'] = self.os_type
        if hasattr(self, "user_agent") and self.user_agent is not None:
            params['userAgent'] = self.user_agent
        if hasattr(self, "device_token_id") and self.device_token_id is not None:
            params['deviceTokenId'] = self.device_token_id
        if hasattr(self, "client_ip") and self.client_ip is not None:
            params['clientIp'] = self.client_ip
        if hasattr(self, "cookie_id") and self.cookie_id is not None:
            params['cookieId'] = self.cookie_id
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "store_terminal_id") and self.store_terminal_id is not None:
            params['storeTerminalId'] = self.store_terminal_id
        if hasattr(self, "store_terminal_request_time") and self.store_terminal_request_time is not None:
            params['storeTerminalRequestTime'] = self.store_terminal_request_time
        if hasattr(self, "browser_info") and self.browser_info is not None:
            params['browserInfo'] = self.browser_info
        if hasattr(self, "color_depth") and self.color_depth is not None:
            params['colorDepth'] = self.color_depth
        if hasattr(self, "screen_height") and self.screen_height is not None:
            params['screenHeight'] = self.screen_height
        if hasattr(self, "screen_width") and self.screen_width is not None:
            params['screenWidth'] = self.screen_width
        if hasattr(self, "time_zone_offset") and self.time_zone_offset is not None:
            params['timeZoneOffset'] = self.time_zone_offset
        if hasattr(self, "device_brand") and self.device_brand is not None:
            params['deviceBrand'] = self.device_brand
        if hasattr(self, "device_model") and self.device_model is not None:
            params['deviceModel'] = self.device_model
        if hasattr(self, "device_language") and self.device_language is not None:
            params['deviceLanguage'] = self.device_language
        if hasattr(self, "device_id") and self.device_id is not None:
            params['deviceId'] = self.device_id
        if hasattr(self, "os_version") and self.os_version is not None:
            params['osVersion'] = self.os_version
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'terminalType' in response_body:
            terminal_type_temp = TerminalType.value_of(response_body['terminalType'])
            self.__terminal_type = terminal_type_temp
        if 'osType' in response_body:
            os_type_temp = OsType.value_of(response_body['osType'])
            self.__os_type = os_type_temp
        if 'userAgent' in response_body:
            self.__user_agent = response_body['userAgent']
        if 'deviceTokenId' in response_body:
            self.__device_token_id = response_body['deviceTokenId']
        if 'clientIp' in response_body:
            self.__client_ip = response_body['clientIp']
        if 'cookieId' in response_body:
            self.__cookie_id = response_body['cookieId']
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'storeTerminalId' in response_body:
            self.__store_terminal_id = response_body['storeTerminalId']
        if 'storeTerminalRequestTime' in response_body:
            self.__store_terminal_request_time = response_body['storeTerminalRequestTime']
        if 'browserInfo' in response_body:
            self.__browser_info = BrowserInfo()
            self.__browser_info.parse_rsp_body(response_body['browserInfo'])
        if 'colorDepth' in response_body:
            self.__color_depth = response_body['colorDepth']
        if 'screenHeight' in response_body:
            self.__screen_height = response_body['screenHeight']
        if 'screenWidth' in response_body:
            self.__screen_width = response_body['screenWidth']
        if 'timeZoneOffset' in response_body:
            self.__time_zone_offset = response_body['timeZoneOffset']
        if 'deviceBrand' in response_body:
            self.__device_brand = response_body['deviceBrand']
        if 'deviceModel' in response_body:
            self.__device_model = response_body['deviceModel']
        if 'deviceLanguage' in response_body:
            self.__device_language = response_body['deviceLanguage']
        if 'deviceId' in response_body:
            self.__device_id = response_body['deviceId']
        if 'osVersion' in response_body:
            self.__os_version = response_body['osVersion']
