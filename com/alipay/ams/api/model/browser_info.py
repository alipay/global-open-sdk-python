import json




class BrowserInfo:
    def __init__(self):
        
        self.__accept_header = None  # type: str
        self.__java_enabled = None  # type: bool
        self.__java_script_enabled = None  # type: bool
        self.__language = None  # type: str
        self.__user_agent = None  # type: str
        

    @property
    def accept_header(self):
        """
        The accept header of the user&#39;s browser
        """
        return self.__accept_header

    @accept_header.setter
    def accept_header(self, value):
        self.__accept_header = value
    @property
    def java_enabled(self):
        """
        Indicates whether the user&#39;s browser is able to run Java
        """
        return self.__java_enabled

    @java_enabled.setter
    def java_enabled(self, value):
        self.__java_enabled = value
    @property
    def java_script_enabled(self):
        """
        Indicates whether the user&#39;s browser is able to run Java
        """
        return self.__java_script_enabled

    @java_script_enabled.setter
    def java_script_enabled(self, value):
        self.__java_script_enabled = value
    @property
    def language(self):
        """
        The language of the user&#39;s browser
        """
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value
    @property
    def user_agent(self):
        """
        The user agent of the user&#39;s browser
        """
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value):
        self.__user_agent = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "accept_header") and self.accept_header is not None:
            params['acceptHeader'] = self.accept_header
        if hasattr(self, "java_enabled") and self.java_enabled is not None:
            params['javaEnabled'] = self.java_enabled
        if hasattr(self, "java_script_enabled") and self.java_script_enabled is not None:
            params['javaScriptEnabled'] = self.java_script_enabled
        if hasattr(self, "language") and self.language is not None:
            params['language'] = self.language
        if hasattr(self, "user_agent") and self.user_agent is not None:
            params['userAgent'] = self.user_agent
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'acceptHeader' in response_body:
            self.__accept_header = response_body['acceptHeader']
        if 'javaEnabled' in response_body:
            self.__java_enabled = response_body['javaEnabled']
        if 'javaScriptEnabled' in response_body:
            self.__java_script_enabled = response_body['javaScriptEnabled']
        if 'language' in response_body:
            self.__language = response_body['language']
        if 'userAgent' in response_body:
            self.__user_agent = response_body['userAgent']
