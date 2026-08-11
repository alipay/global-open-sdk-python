import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayCreditGrantInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayCreditGrantInquireListRequest, self).__init__("/ams/api/v1/meter/creditGrant/inquireList") 

        self.__page_num = None  # type: int
        self.__page_size = None  # type: int
        self.__customer_id = None  # type: str
        self.__status = None  # type: str
        

    @property
    def page_num(self):
        """
        The page number. The value must be at least 1. The default value is 1. A page beyond the last page returns SUCCESS with an empty &#x60;creditGrants&#x60; array.
        """
        return self.__page_num

    @page_num.setter
    def page_num(self, value):
        self.__page_num = value
    @property
    def page_size(self):
        """
        The number of records per page. Value range: 1-100. The default value is 10.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def status(self):
        """
        The current status. Maximum length: 8 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "page_num") and self.page_num is not None:
            params['pageNum'] = self.page_num
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'pageNum' in response_body:
            self.__page_num = response_body['pageNum']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'status' in response_body:
            self.__status = response_body['status']
