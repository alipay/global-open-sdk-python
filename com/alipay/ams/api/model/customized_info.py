import json




class CustomizedInfo:
    def __init__(self):
        
        self.__customized_field1 = None  # type: str
        self.__customized_field2 = None  # type: str
        self.__customized_field3 = None  # type: str
        self.__customized_field4 = None  # type: str
        self.__customized_field5 = None  # type: str
        

    @property
    def customized_field1(self):
        """
        Customized field 1
        """
        return self.__customized_field1

    @customized_field1.setter
    def customized_field1(self, value):
        self.__customized_field1 = value
    @property
    def customized_field2(self):
        """
        Customized field 2
        """
        return self.__customized_field2

    @customized_field2.setter
    def customized_field2(self, value):
        self.__customized_field2 = value
    @property
    def customized_field3(self):
        """
        Customized field 3
        """
        return self.__customized_field3

    @customized_field3.setter
    def customized_field3(self, value):
        self.__customized_field3 = value
    @property
    def customized_field4(self):
        """
        Customized field 4
        """
        return self.__customized_field4

    @customized_field4.setter
    def customized_field4(self, value):
        self.__customized_field4 = value
    @property
    def customized_field5(self):
        """
        Customized field 5
        """
        return self.__customized_field5

    @customized_field5.setter
    def customized_field5(self, value):
        self.__customized_field5 = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customized_field1") and self.customized_field1 is not None:
            params['customizedField1'] = self.customized_field1
        if hasattr(self, "customized_field2") and self.customized_field2 is not None:
            params['customizedField2'] = self.customized_field2
        if hasattr(self, "customized_field3") and self.customized_field3 is not None:
            params['customizedField3'] = self.customized_field3
        if hasattr(self, "customized_field4") and self.customized_field4 is not None:
            params['customizedField4'] = self.customized_field4
        if hasattr(self, "customized_field5") and self.customized_field5 is not None:
            params['customizedField5'] = self.customized_field5
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customizedField1' in response_body:
            self.__customized_field1 = response_body['customizedField1']
        if 'customizedField2' in response_body:
            self.__customized_field2 = response_body['customizedField2']
        if 'customizedField3' in response_body:
            self.__customized_field3 = response_body['customizedField3']
        if 'customizedField4' in response_body:
            self.__customized_field4 = response_body['customizedField4']
        if 'customizedField5' in response_body:
            self.__customized_field5 = response_body['customizedField5']
