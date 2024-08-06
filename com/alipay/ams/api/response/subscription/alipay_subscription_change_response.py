from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySubscriptionChangeResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipaySubscriptionChangeResponse, self).__init__()

        self.__parse_rsp_body(rsp_body)

    def __parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipaySubscriptionChangeResponse, self).parse_rsp_body(rsp_body)
