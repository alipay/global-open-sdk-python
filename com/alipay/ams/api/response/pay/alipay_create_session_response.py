import json

from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayCreateSessionResponse(AlipayResponse):

    def __init__(self,rsp_body):
        super(AlipayCreateSessionResponse, self).__init__()
        self.__payment_session_data = None
        self.__payment_session_expiry_time = None
        self.__payment_session_id = None

        self.__parse_rsp_body(rsp_body)

    @property
    def payment_session_data(self):
        return self.__payment_session_data

    @property
    def payment_session_expiry_Time(self):
        return self.__payment_session_expiry_Time

    @property
    def payment_session_id(self):
        return self.__payment_session_id

    def __parse_rsp_body(self,rsp_body):
        rsp_json = json.loads(rsp_body)
        if 'payment_session_data' in rsp_json:
            self.__payment_session_data = rsp_json['payment_session_data']
        if 'payment_session_expiry_Time' in rsp_json:
            self.__payment_session_expiry_Time = rsp_json['payment_session_expiry_time']
        if 'payment _session _id' in rsp_json:
            self.__payment_session_id = rsp_json['payment_session_id']