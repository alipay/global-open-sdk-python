from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySubscriptionCancelResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipaySubscriptionCancelResponse, self).__init__()

        self.__parse_rsp_body(rsp_body)

    def __parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipaySubscriptionCancelResponse, self).parse_rsp_body(rsp_body)
