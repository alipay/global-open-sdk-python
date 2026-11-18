import json




class ResultPropertiesResultCode:
    def __init__(self):
        
        self.__type = None  # type: str
        self.__description = None  # type: str
        

    @property
    def type(self):
        """Gets the type of this ResultPropertiesResultCode.
        
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def description(self):
        """Gets the description of this ResultPropertiesResultCode.
        
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'description' in response_body:
            self.__description = response_body['description']
