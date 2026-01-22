import json




class TotalCount:
    def __init__(self):
        
        self.__total_page_number = None  # type: str
        self.__current_page_number = None  # type: str
        

    @property
    def total_page_number(self):
        """Gets the total_page_number of this TotalCount.
        
        """
        return self.__total_page_number

    @total_page_number.setter
    def total_page_number(self, value):
        self.__total_page_number = value
    @property
    def current_page_number(self):
        """Gets the current_page_number of this TotalCount.
        
        """
        return self.__current_page_number

    @current_page_number.setter
    def current_page_number(self, value):
        self.__current_page_number = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "total_page_number") and self.total_page_number is not None:
            params['totalPageNumber'] = self.total_page_number
        if hasattr(self, "current_page_number") and self.current_page_number is not None:
            params['currentPageNumber'] = self.current_page_number
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'totalPageNumber' in response_body:
            self.__total_page_number = response_body['totalPageNumber']
        if 'currentPageNumber' in response_body:
            self.__current_page_number = response_body['currentPageNumber']
