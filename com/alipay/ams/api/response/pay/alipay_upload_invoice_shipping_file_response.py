from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayUploadInvoiceShippingFileResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayUploadInvoiceShippingFileResponse, self).__init__()
        self.__parse_rsp_body(rsp_body)

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipayUploadInvoiceShippingFileResponse, self).parse_rsp_body(rsp_body)
