import json
from com.alipay.ams.api.model.attachment_type import AttachmentType



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipaySubmitAttachmentRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubmitAttachmentRequest, self).__init__("/ams/api/open/openapiv2_file/v1/business/attachment/submitAttachment") 

        self.__submit_attachment_request_id = None  # type: str
        self.__attachment_type = None  # type: AttachmentType
        self.__file_sha256 = None  # type: str
        

    @property
    def submit_attachment_request_id(self):
        """
        The unique ID assigned by the marketplace to identify an attachment submission request.  More information:  This field is an API idempotency field. For attachment submission requests that are initiated with the same value of attachmentSubmissionRequestId and reach a final status of S or F, the same result is to be returned for the request. Maximum length: 32 characters
        """
        return self.__submit_attachment_request_id

    @submit_attachment_request_id.setter
    def submit_attachment_request_id(self, value):
        self.__submit_attachment_request_id = value
    @property
    def attachment_type(self):
        """Gets the attachment_type of this AlipaySubmitAttachmentRequest.
        
        """
        return self.__attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self.__attachment_type = value
    @property
    def file_sha256(self):
        """
        The SHA-256 hash value of the file, used to uniquely identify and verify its integrity and authenticity.  For more information, see How to calculate the SHA256 digest of a file.  More information:  Maximum length: 64 characters
        """
        return self.__file_sha256

    @file_sha256.setter
    def file_sha256(self, value):
        self.__file_sha256 = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "submit_attachment_request_id") and self.submit_attachment_request_id is not None:
            params['submitAttachmentRequestId'] = self.submit_attachment_request_id
        if hasattr(self, "attachment_type") and self.attachment_type is not None:
            params['attachmentType'] = self.attachment_type
        if hasattr(self, "file_sha256") and self.file_sha256 is not None:
            params['fileSha256'] = self.file_sha256
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'submitAttachmentRequestId' in response_body:
            self.__submit_attachment_request_id = response_body['submitAttachmentRequestId']
        if 'attachmentType' in response_body:
            attachment_type_temp = AttachmentType.value_of(response_body['attachmentType'])
            self.__attachment_type = attachment_type_temp
        if 'fileSha256' in response_body:
            self.__file_sha256 = response_body['fileSha256']
