from com.alipay.ams.api.response.alipay_response import AlipayResponse


class SendRefundResultResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(SendRefundResultResponse, self).__init__()
        self.__parse_rsp_body(rsp_body)

    def __parse_rsp_body(self, rsp_body):
        response = super(SendRefundResultResponse, self).parse_rsp_body(rsp_body)
