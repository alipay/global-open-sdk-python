from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayAuthNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayAuthNotify, self).__init__()
        self.__authorization_notify_type = None
        self.__auth_client_id = None
        self.__access_token = None
        self.__auth_state = None
        self.__auth_code = None
        self.__reason = None
        self.__user_login_id = None
        self.__user_id = None
        self.__parse_notify_body(notify_body)

    @property
    def authorization_notify_type(self):
        return self.__authorization_notify_type

    @property
    def auth_client_id(self):
        return self.__auth_client_id

    @property
    def access_token(self):
        return self.__access_token

    @property
    def auth_state(self):
        return self.__auth_state

    @property
    def auth_code(self):
        return self.__auth_code

    @property
    def reason(self):
        return self.__reason

    @property
    def user_login_id(self):
        return self.__user_login_id

    @property
    def user_id(self):
        return self.__user_id

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayAuthNotify, self).parse_notify_body(notify_body)
        if 'authorizationNotifyType' in notify:
            self.__authorization_notify_type = notify['authorizationNotifyType']
        if 'authClientId' in notify:
            self.__auth_client_id = notify['authClientId']
        if 'accessToken' in notify:
            self.__access_token = notify['accessToken']
        if 'authState' in notify:
            self.__auth_state = notify['authState']
        if 'authCode' in notify:
            self.__auth_code = notify['authCode']
        if 'reason' in notify:
            self.__reason = notify['reason']
        if 'userLoginId' in notify:
            self.__user_login_id = notify['userLoginId']
        if 'userId' in notify:
            self.__user_id = notify['userId']
