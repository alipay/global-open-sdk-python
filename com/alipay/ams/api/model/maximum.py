import json




class Maximum:
    def __init__(self):
        
        self.__unit = None  # type: str
        self.__value = None  # type: int
        

    @property
    def unit(self):
        """
        The unit. Maximum length: 8 characters.
        """
        return self.__unit

    @unit.setter
    def unit(self, value):
        self.__unit = value
    @property
    def value(self):
        """
        The value of the amount as a positive integer in the smallest currency unit.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "unit") and self.unit is not None:
            params['unit'] = self.unit
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'unit' in response_body:
            self.__unit = response_body['unit']
        if 'value' in response_body:
            self.__value = response_body['value']
