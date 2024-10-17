from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySettlementInfoUpdateResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipaySettlementInfoUpdateResponse, self).__init__()
        self.__update_status = None
        self.__parse_rsp_body(rsp_body)

    @property
    def update_status(self):
        return self.__update_status

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipaySettlementInfoUpdateResponse, self).parse_rsp_body(rsp_body)
        if 'updateStatus' in response:
            self.__update_status = response['updateStatus']