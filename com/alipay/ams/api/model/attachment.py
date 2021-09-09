class Attachment(object):
    def __init__(self):
        self.__attachment_type = None
        self.__file = None
        self.__attachment_name = None

    @property
    def attachment_type(self):
        return self.__attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self.__attachment_type = value

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value

    @property
    def attachment_name(self):
        return self.__attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self.__attachment_name = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "attachment_type") and self.attachment_type:
            params['attachmentType'] = self.attachment_type

        if hasattr(self, "file") and self.file:
            params['file'] = self.file

        if hasattr(self, "attachment_name") and self.attachment_name:
            params['attachmentName'] = self.attachment_name

        return params
