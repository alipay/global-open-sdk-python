from com.alipay.ams.api.model.attachment_type import AttachmentType
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipaySubmitAttachmentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipaySubmitAttachmentResponse, self).__init__()
        self.__submit_attachment_request_id = None
        self.__attachment_type = None #type: AttachmentType
        self.__attachment_key = None
        self.__parse_rsp_body(rsp_body)

    @property
    def submit_attachment_request_id(self):
        return self.__submit_attachment_request_id

    @property
    def attachment_type(self):
        return self.__attachment_type

    @property
    def attachment_key(self):
        return self.__attachment_key

    def __parse_rsp_body(self, rsp_body):
        response = super(AlipaySubmitAttachmentResponse, self).parse_rsp_body(rsp_body)