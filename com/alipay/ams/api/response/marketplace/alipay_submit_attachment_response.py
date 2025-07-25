import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.attachment_type import AttachmentType



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipaySubmitAttachmentResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__submit_attachment_request_id = None  # type: str
        self.__attachment_type = None  # type: AttachmentType
        self.__attachment_key = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipaySubmitAttachmentResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def submit_attachment_request_id(self):
        """
        The unique ID assigned by the marketplace to identify an attachment submission request.  This parameter is returned when the value of result.resultStatus is S.  More information:  Maximum length: 32 characters
        """
        return self.__submit_attachment_request_id

    @submit_attachment_request_id.setter
    def submit_attachment_request_id(self, value):
        self.__submit_attachment_request_id = value
    @property
    def attachment_type(self):
        """Gets the attachment_type of this AlipaySubmitAttachmentResponse.
        
        """
        return self.__attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self.__attachment_type = value
    @property
    def attachment_key(self):
        """
        The unique key value of the attachment that you submit. The value of this parameter is used by the fileKeys or fileKey parameters in the register API.  This parameter is returned when the value of result.resultStatus is S.  More information:  Maximum length: 256 characters
        """
        return self.__attachment_key

    @attachment_key.setter
    def attachment_key(self, value):
        self.__attachment_key = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "submit_attachment_request_id") and self.submit_attachment_request_id is not None:
            params['submitAttachmentRequestId'] = self.submit_attachment_request_id
        if hasattr(self, "attachment_type") and self.attachment_type is not None:
            params['attachmentType'] = self.attachment_type
        if hasattr(self, "attachment_key") and self.attachment_key is not None:
            params['attachmentKey'] = self.attachment_key
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipaySubmitAttachmentResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'submitAttachmentRequestId' in response_body:
            self.__submit_attachment_request_id = response_body['submitAttachmentRequestId']
        if 'attachmentType' in response_body:
            attachment_type_temp = AttachmentType.value_of(response_body['attachmentType'])
            self.__attachment_type = attachment_type_temp
        if 'attachmentKey' in response_body:
            self.__attachment_key = response_body['attachmentKey']
