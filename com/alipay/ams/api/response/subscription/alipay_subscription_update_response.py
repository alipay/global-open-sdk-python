from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySubscriptionUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipaySubscriptionUpdateResponse, self).__init__()
        self.__parse_rsp_body(rsp_body)


    def __parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipaySubscriptionUpdateResponse, self).parse_rsp_body(rsp_body)
