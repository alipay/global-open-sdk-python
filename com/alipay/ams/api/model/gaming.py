class Gaming(object):

    def __init__(self):
        self.__game_name = None
        self.__topped_up_user = None
        self.__topped_up_email = None
        self.__topped_up_phone_no = None

    @property
    def game_name(self):
        return self.__game_name

    @game_name.setter
    def game_name(self, value):
        self.__game_name = value

    @property
    def topped_up_user(self):
        return self.__topped_up_user

    @topped_up_user.setter
    def topped_up_user(self, value):
        self.__topped_up_user = value

    @property
    def topped_up_email(self):
        return self.__topped_up_email

    @topped_up_email.setter
    def topped_up_email(self, value):
        self.__topped_up_email = value

    @property
    def topped_up_phone_no(self):
        return self.__topped_up_phone_no

    @topped_up_phone_no.setter
    def topped_up_phone_no(self, value):
        self.__topped_up_phone_no = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "game_name") and self.game_name:
            params['gameName'] = self.game_name

        if hasattr(self, "topped_up_user") and self.topped_up_user:
            params['toppedUpUser'] = self.topped_up_user.to_ams_dict()

        if hasattr(self, "topped_up_email") and self.topped_up_email:
            params['toppedUpEmail'] = self.topped_up_email

        if hasattr(self, "topped_up_phone_no") and self.topped_up_phone_no:
            params['toppedUpPhoneNo'] = self.topped_up_phone_no

        return params
