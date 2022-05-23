from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayMerchantRegistrationResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayMerchantRegistrationResponse, self).__init__()
        self.__pass_through_info = None
        self.__parse_rsp_body(rsp_body)

    @property
    def pass_through_info(self):
        return self.__pass_through_info

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayMerchantRegistrationResponse, self).parse_rsp_body(rsp_body)

        if 'passThroughInfo' in response:
            pass_through_info = response['passThroughInfo']
            self.__pass_through_info = pass_through_info
