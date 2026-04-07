import json




class Paginator:
    def __init__(self):
        
        self.__current_page = None  # type: int
        self.__page_size = None  # type: int
        self.__total_page = None  # type: int
        self.__total_count = None  # type: int
        

    @property
    def current_page(self):
        """
        The current page number, start from 1.
        """
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        self.__current_page = value
    @property
    def page_size(self):
        """
        The maximum records returned per page.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def total_page(self):
        """
        Total number of pages.
        """
        return self.__total_page

    @total_page.setter
    def total_page(self, value):
        self.__total_page = value
    @property
    def total_count(self):
        """
        Total items that match the criteria.
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "current_page") and self.current_page is not None:
            params['currentPage'] = self.current_page
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "total_page") and self.total_page is not None:
            params['totalPage'] = self.total_page
        if hasattr(self, "total_count") and self.total_count is not None:
            params['totalCount'] = self.total_count
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'currentPage' in response_body:
            self.__current_page = response_body['currentPage']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'totalPage' in response_body:
            self.__total_page = response_body['totalPage']
        if 'totalCount' in response_body:
            self.__total_count = response_body['totalCount']
