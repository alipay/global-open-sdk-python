class BrowserInfo(object):
    def __init__(self):
        self.__accept_header = None
        self.__java_enabled = None
        self.__java_script_enabled = None
        self.__language = None
        self.__user_agent = None

    @property
    def accept_header(self):
        return self.__accept_header

    @accept_header.setter
    def accept_header(self, value):
        self.__accept_header = value

    @property
    def java_enabled(self):
        return self.__java_enabled

    @java_enabled.setter
    def java_enabled(self, value):
        self.__java_enabled = value

    @property
    def java_script_enabled(self):
        return self.__java_script_enabled

    @java_script_enabled.setter
    def java_script_enabled(self, value):
        self.__java_script_enabled = value

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    @property
    def user_agent(self):
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value):
        self.__user_agent = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "accept_header") and self.accept_header:
            params['acceptHeader'] = self.accept_header

        if hasattr(self, "java_enabled") and self.java_enabled:
            params['javaEnabled'] = self.java_enabled

        if hasattr(self, "java_script_enabled") and self.java_script_enabled:
            params['javaScriptEnabled'] = self.java_script_enabled

        if hasattr(self, "language") and self.language:
            params['language'] = self.language

        if hasattr(self, "user_agent") and self.user_agent:
            params['userAgent'] = self.user_agent
        return params
