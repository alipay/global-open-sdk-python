import json




class Gaming:
    def __init__(self):
        
        self.__game_name = None  # type: str
        self.__topped_up_user = None  # type: str
        self.__topped_up_email = None  # type: str
        self.__topped_up_phone_no = None  # type: str
        

    @property
    def game_name(self):
        """
        Game name.  More information:  Maximum length: 128 characters
        """
        return self.__game_name

    @game_name.setter
    def game_name(self, value):
        self.__game_name = value
    @property
    def topped_up_user(self):
        """
        Name or ID of the user whose gaming account is topped up.  More information:  Maximum length: 128 characters
        """
        return self.__topped_up_user

    @topped_up_user.setter
    def topped_up_user(self, value):
        self.__topped_up_user = value
    @property
    def topped_up_email(self):
        """
        More information:  Maximum length: 64 characters
        """
        return self.__topped_up_email

    @topped_up_email.setter
    def topped_up_email(self, value):
        self.__topped_up_email = value
    @property
    def topped_up_phone_no(self):
        """
        More information:  Maximum length: 32 characters
        """
        return self.__topped_up_phone_no

    @topped_up_phone_no.setter
    def topped_up_phone_no(self, value):
        self.__topped_up_phone_no = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "game_name") and self.game_name is not None:
            params['gameName'] = self.game_name
        if hasattr(self, "topped_up_user") and self.topped_up_user is not None:
            params['toppedUpUser'] = self.topped_up_user
        if hasattr(self, "topped_up_email") and self.topped_up_email is not None:
            params['toppedUpEmail'] = self.topped_up_email
        if hasattr(self, "topped_up_phone_no") and self.topped_up_phone_no is not None:
            params['toppedUpPhoneNo'] = self.topped_up_phone_no
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'gameName' in response_body:
            self.__game_name = response_body['gameName']
        if 'toppedUpUser' in response_body:
            self.__topped_up_user = response_body['toppedUpUser']
        if 'toppedUpEmail' in response_body:
            self.__topped_up_email = response_body['toppedUpEmail']
        if 'toppedUpPhoneNo' in response_body:
            self.__topped_up_phone_no = response_body['toppedUpPhoneNo']
