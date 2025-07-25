import json




class Attachment:
    def __init__(self):
        
        self.__attachment_type = None  # type: str
        self.__file = None  # type: str
        self.__attachment_name = None  # type: str
        self.__file_key = None  # type: str
        

    @property
    def attachment_type(self):
        """
        The type of attachment. Valid values are:  SIGNATURE_AUTHORIZATION_LETTER: indicates a document that allows someone to sign on behalf of an individual or a company. ARTICLES_OF_ASSOCIATION: indicates the regulations and rules of a company.   LOGO: indicates the merchant&#39;s logo. Specify attachmentType as LOGO when the value of paymentMethodType is TRUEMONEY. More information:  Maximum length: 64 characters
        """
        return self.__attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self.__attachment_type = value
    @property
    def file(self):
        """Gets the file of this Attachment.
        
        """
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value
    @property
    def attachment_name(self):
        """
        The name of the attachment file, including the file extension, such as XXX.jpg or XXX.png.    More information:  Maximum length: 256 characters 
        """
        return self.__attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self.__attachment_name = value
    @property
    def file_key(self):
        """
        The unique key value of the attachment file. Maximum file size: 32MB.  The value of this parameter is obtained from the attachmentKey parameter in the submitAttachment API. Prior attachment submission using the submitAttachment API is required.    More information:  Maximum length: 256 characters 
        """
        return self.__file_key

    @file_key.setter
    def file_key(self, value):
        self.__file_key = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "attachment_type") and self.attachment_type is not None:
            params['attachmentType'] = self.attachment_type
        if hasattr(self, "file") and self.file is not None:
            params['file'] = self.file
        if hasattr(self, "attachment_name") and self.attachment_name is not None:
            params['attachmentName'] = self.attachment_name
        if hasattr(self, "file_key") and self.file_key is not None:
            params['fileKey'] = self.file_key
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'attachmentType' in response_body:
            self.__attachment_type = response_body['attachmentType']
        if 'file' in response_body:
            self.__file = response_body['file']
        if 'attachmentName' in response_body:
            self.__attachment_name = response_body['attachmentName']
        if 'fileKey' in response_body:
            self.__file_key = response_body['fileKey']
