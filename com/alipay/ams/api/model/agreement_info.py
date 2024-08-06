import json


class AgreementInfo(object):
    def __init__(self):
        self.__auth_state = None
        self.__user_login_id = None

    @property
    def auth_state(self):
        return self.__auth_state

    @auth_state.setter
    def auth_state(self, value):
        self.__auth_state = value

    @property
    def user_login_id(self):
        return self.__user_login_id

    @user_login_id.setter
    def user_login_id(self, value):
        self.__user_login_id = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__auth_state is not None:
            params['authState'] = self.__auth_state
        if self.__user_login_id is not None:
            params['userLoginId'] = self.__user_login_id
        return params
