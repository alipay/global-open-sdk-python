
class AuthorizationError:
    def __init__(self):
        self.__error_code = None
        self.__error_message = None

    @property
    def error_code(self):
        return self.__error_code
    @error_code.setter
    def error_code(self, value):
        self.__error_code = value
    @property
    def error_message(self):
        return self.__error_message
    @error_message.setter
    def error_message(self, value):
        self.__error_message = value

    def to_ams_dict(self):
        params = dict()
        if self.error_code is not None:
            params['errorCode'] = self.error_code
        if self.error_message is not None:
            params['errorMessage'] = self.error_message
        return params

