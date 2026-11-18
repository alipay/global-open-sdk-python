import json




class ResultPropertiesResultStatus:
    def __init__(self):
        
        self.__description = None  # type: str
        self.__ref = None  # type: str
        

    @property
    def description(self):
        """Gets the description of this ResultPropertiesResultStatus.
        
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def ref(self):
        """Gets the ref of this ResultPropertiesResultStatus.
        
        """
        return self.__ref

    @ref.setter
    def ref(self, value):
        self.__ref = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "ref") and self.ref is not None:
            params['$ref'] = self.ref
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'description' in response_body:
            self.__description = response_body['description']
        if '$ref' in response_body:
            self.__ref = response_body['$ref']
