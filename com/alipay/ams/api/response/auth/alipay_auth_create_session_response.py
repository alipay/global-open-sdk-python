from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayAuthCreateSessionResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayAuthCreateSessionResponse, self).__init__()
        self.__payment_session_id = None
        self.__payment_session_data = None
        self.__payment_session_expiry_time = None
        self.__parse_rsp_body(rsp_body)

    @property
    def payment_session_id(self):
        return self.__payment_session_id

    @property
    def payment_session_data(self):
        return self.__payment_session_data

    @property
    def payment_session_expiry_time(self):
        return self.__payment_session_expiry_time

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayAuthCreateSessionResponse, self).parse_rsp_body(rsp_body)
        if "paymentSessionId" in response:
            self.__payment_session_id = response["paymentSessionId"]

        if "paymentSessionData" in response:
            self.__payment_session_data = response["paymentSessionData"]

        if "paymentSessionExpiryTime" in response:
            self.__payment_session_expiry_time = response["paymentSessionExpiryTime"]
