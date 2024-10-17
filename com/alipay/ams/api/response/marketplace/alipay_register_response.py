from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayRegisterResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayRegisterResponse, self).__init__()
        self.__registration_status = None
        self.__parse_rsp_body(rsp_body)

    @property
    def registration_status(self):
        return self.__registration_status

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayRegisterResponse, self).parse_rsp_body(rsp_body)
        if 'registrationStatus' in response:
            self.__registration_status = response['registrationStatus']

