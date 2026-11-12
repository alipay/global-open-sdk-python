import json




class EvidenceFile:
    def __init__(self):
        
        self.__file_name = None  # type: str
        self.__file_format = None  # type: str
        self.__file_content = None  # type: str
        

    @property
    def file_name(self):
        """
        The file name including its extension. Cannot be empty.
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value
    @property
    def file_format(self):
        """
        The uppercase file format. Supported values: PDF, JPG, JPEG, PNG, WORD. JPG and JPEG are equivalent. Other values return FILE_FORMAT_NOT_SUPPORTED. Cannot be empty.
        """
        return self.__file_format

    @file_format.setter
    def file_format(self, value):
        self.__file_format = value
    @property
    def file_content(self):
        """
        The Base64-encoded content of one file, limited to 4,000,000 Base64 characters (up to 3 MB of raw material). Cannot be empty.
        """
        return self.__file_content

    @file_content.setter
    def file_content(self, value):
        self.__file_content = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "file_name") and self.file_name is not None:
            params['fileName'] = self.file_name
        if hasattr(self, "file_format") and self.file_format is not None:
            params['fileFormat'] = self.file_format
        if hasattr(self, "file_content") and self.file_content is not None:
            params['fileContent'] = self.file_content
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'fileName' in response_body:
            self.__file_name = response_body['fileName']
        if 'fileFormat' in response_body:
            self.__file_format = response_body['fileFormat']
        if 'fileContent' in response_body:
            self.__file_content = response_body['fileContent']
