import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.attachment_type import AttachmentType
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipaySubmitAttachmentRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubmitAttachmentRequest, self).__init__(AntomPathConstants.MARKETPLACE_SUBMITATTACHMENT_PATH)
        self.__submit_attachment_request_id = None
        self.__attachment_type = None #type: AttachmentType
        self.__file_sha_256 = None

    @property
    def submit_attachment_request_id(self):
        return self.__submit_attachment_request_id

    @submit_attachment_request_id.setter
    def submit_attachment_request_id(self, value):
        self.__submit_attachment_request_id = value

    @property
    def attachment_type(self):
        return self.__attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self.__attachment_type = value

    @property
    def file_sha_256(self):
        return self.__file_sha_256

    @file_sha_256.setter
    def file_sha_256(self, value):
        self.__file_sha_256 = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, 'submit_attachment_request_id') and self.submit_attachment_request_id:
            params['submitAttachmentRequestId'] = self.__submit_attachment_request_id
        if hasattr(self, 'attachment_type') and self.attachment_type:
            params['attachmentType'] = self.__attachment_type
        if hasattr(self, 'file_sha_256') and self.file_sha_256:
            params['fileSha256'] = self.__file_sha_256
        return params