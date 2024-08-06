from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySupplyDefenseDocumentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipaySupplyDefenseDocumentResponse, self).__init__()
        self.__dispute_id = None
        self.__dispute_resolution_time = None
        self.parse_rsp_body(rsp_body)

    @property
    def dispute_id(self):
        return self.__dispute_id

    @property
    def dispute_resolution_time(self):
        return self.__dispute_resolution_time

    def parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipaySupplyDefenseDocumentResponse, self).parse_rsp_body(rsp_body)
        if 'disputeId' in rsp_dict:
            self.__dispute_id = rsp_dict['disputeId']
        if 'disputeResolutionTime' in rsp_dict:
            self.__dispute_resolution_time = rsp_dict['disputeResolutionTime']
