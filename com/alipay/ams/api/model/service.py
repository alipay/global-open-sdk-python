import json




class Service:
    def __init__(self):
        
        self.__category_code = None  # type: str
        self.__sub_category_code = None  # type: str
        

    @property
    def category_code(self):
        """
        Category code for the service
        """
        return self.__category_code

    @category_code.setter
    def category_code(self, value):
        self.__category_code = value
    @property
    def sub_category_code(self):
        """
        Sub-category code for the service
        """
        return self.__sub_category_code

    @sub_category_code.setter
    def sub_category_code(self, value):
        self.__sub_category_code = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "category_code") and self.category_code is not None:
            params['categoryCode'] = self.category_code
        if hasattr(self, "sub_category_code") and self.sub_category_code is not None:
            params['subCategoryCode'] = self.sub_category_code
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'categoryCode' in response_body:
            self.__category_code = response_body['categoryCode']
        if 'subCategoryCode' in response_body:
            self.__sub_category_code = response_body['subCategoryCode']
