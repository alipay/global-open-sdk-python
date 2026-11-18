import json




class InvoiceCustomField:
    def __init__(self):
        
        self.__label = None  # type: str
        self.__value = None  # type: str
        

    @property
    def label(self):
        """
        Custom field label. Maximum length: 256 characters.
        """
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value
    @property
    def value(self):
        """
        Custom field value. Maximum length: 512 characters.
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "label") and self.label is not None:
            params['label'] = self.label
        if hasattr(self, "value") and self.value is not None:
            params['value'] = self.value
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'label' in response_body:
            self.__label = response_body['label']
        if 'value' in response_body:
            self.__value = response_body['value']
