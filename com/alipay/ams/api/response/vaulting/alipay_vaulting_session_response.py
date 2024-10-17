from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayVaultingSessionResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayVaultingSessionResponse, self).__init__()
        self.__vaulting_session_data = None
        self.__vaulting_session_id = None
        self.__vaulting_session_expiry_time = None
        self.__parse_rsp_body(rsp_body)

    @property
    def vaulting_session_data(self):
        return self.__vaulting_session_data

    @property
    def vaulting_session_id(self):
        return self.__vaulting_session_id
    @property
    def vaulting_session_expiry_time(self):
        return self.__vaulting_session_expiry_time

    def __parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipayVaultingSessionResponse, self).parse_rsp_body(rsp_body)
        if 'vaultingSessionData' in rsp_dict:
            self.__vaulting_session_data = rsp_dict['vaultingSessionData']
        if 'vaultingSessionId' in rsp_dict:
            self.__vaulting_session_id = rsp_dict['vaultingSessionId']
        if 'vaultingSessionExpiryTime' in rsp_dict:
            self.__vaulting_session_expiry_time = rsp_dict['vaultingSessionExpiryTime']

