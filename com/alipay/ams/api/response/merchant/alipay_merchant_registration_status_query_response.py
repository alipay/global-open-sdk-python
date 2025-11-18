from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayMerchantRegistrationStatusQueryResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayMerchantRegistrationStatusQueryResponse, self).__init__()
        self.__registration_result = None
        self.__psp_registration_result_list = None
        self.__parse_rsp_body(rsp_body)

    @property
    def registration_result(self):
        return self.__registration_result

    @property
    def psp_registration_result_list(self):
        return self.__psp_registration_result_list

    def __parse_rsp_body(self, rsp_body):
        response = super(
            AlipayMerchantRegistrationStatusQueryResponse, self
        ).parse_rsp_body(rsp_body)
        if "registrationResult" in response:
            self.__registration_result = response["registrationResult"]

        if "pspRegistrationResultList" in response:
            self.__psp_registration_result_list = response["pspRegistrationResultList"]
