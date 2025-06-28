import json
from com.alipay.ams.api.model.code_value_type import CodeValueType
from com.alipay.ams.api.model.display_type import DisplayType




class CodeDetail:
    def __init__(self):
        
        self.__code_value_type = None  # type: CodeValueType
        self.__code_value = None  # type: str
        self.__display_type = None  # type: DisplayType
        

    @property
    def code_value_type(self):
        """Gets the code_value_type of this CodeDetail.
        
        """
        return self.__code_value_type

    @code_value_type.setter
    def code_value_type(self, value):
        self.__code_value_type = value
    @property
    def code_value(self):
        """
        The value of the code.    If the value of displayType is set toSMALLIMAGE, MIDDLEIMAGE, or BIGIMAGE, this parameter indicates a plain or Base64-encoded image URL. If the value of displayType is set to TEXT, this parameter indicates a text string.   More information:  Maximum length: 2048 characters
        """
        return self.__code_value

    @code_value.setter
    def code_value(self, value):
        self.__code_value = value
    @property
    def display_type(self):
        """Gets the display_type of this CodeDetail.
        
        """
        return self.__display_type

    @display_type.setter
    def display_type(self, value):
        self.__display_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "code_value_type") and self.code_value_type is not None:
            params['codeValueType'] = self.code_value_type
        if hasattr(self, "code_value") and self.code_value is not None:
            params['codeValue'] = self.code_value
        if hasattr(self, "display_type") and self.display_type is not None:
            params['displayType'] = self.display_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'codeValueType' in response_body:
            code_value_type_temp = CodeValueType.value_of(response_body['codeValueType'])
            self.__code_value_type = code_value_type_temp
        if 'codeValue' in response_body:
            self.__code_value = response_body['codeValue']
        if 'displayType' in response_body:
            display_type_temp = DisplayType.value_of(response_body['displayType'])
            self.__display_type = display_type_temp
