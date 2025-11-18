from com.alipay.ams.api.response.alipay_response import AlipayResponse


class RiskReportResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(RiskReportResponse, self).__init__()
        self.__parse_rsp_body(rsp_body)

    def __parse_rsp_body(self, rsp_body):
        response = super(RiskReportResponse, self).parse_rsp_body(rsp_body)
