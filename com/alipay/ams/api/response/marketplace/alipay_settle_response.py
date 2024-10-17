from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySettleResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipaySettleResponse, self).__init__()
        self.__settlement_request_id = None
        self.__settlement_id = None
        self.__parse_rsp_body(rsp_body)

    @property
    def settlement_request_id(self):
        return self.__settlement_request_id


    @property
    def settlement_id(self):
        return self.__settlement_id

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipaySettleResponse, self).parse_rsp_body(rsp_body)
        if 'settlementRequestId' in response:
            self.__settlement_request_id = response['settlementRequestId']
        if 'settlementId' in response:
            self.__settlement_id = response['settlementId']