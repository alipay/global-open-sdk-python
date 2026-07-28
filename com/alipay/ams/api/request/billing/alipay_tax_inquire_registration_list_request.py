import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayTaxInquireRegistrationListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayTaxInquireRegistrationListRequest, self).__init__("/ams/api/v1/tax/inquireRegistrationList") 

        self.__status = None  # type: str
        self.__current_page = None  # type: int
        self.__page_size = None  # type: int
        

    @property
    def status(self):
        """
        The current status. Maximum length: 16 characters. Note: See documentation for details.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def current_page(self):
        """
        The current page number.
        """
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        self.__current_page = value
    @property
    def page_size(self):
        """
        The number of records per page.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "current_page") and self.current_page is not None:
            params['currentPage'] = self.current_page
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'currentPage' in response_body:
            self.__current_page = response_body['currentPage']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
