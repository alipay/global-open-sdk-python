import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquiryStatementListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquiryStatementListRequest, self).__init__("/ams/api/v1/aba/accounts/inquiryStatementList") 

        self.__customer_id = None  # type: str
        self.__access_token = None  # type: str
        self.__start_time = None  # type: str
        self.__end_time = None  # type: str
        self.__transaction_type_list = None  # type: [str]
        self.__currency_list = None  # type: [str]
        self.__page_size = None  # type: str
        self.__page_number = None  # type: str
        

    @property
    def customer_id(self):
        """Gets the customer_id of this AlipayInquiryStatementListRequest.
        
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def access_token(self):
        """Gets the access_token of this AlipayInquiryStatementListRequest.
        
        """
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value
    @property
    def start_time(self):
        """Gets the start_time of this AlipayInquiryStatementListRequest.
        
        """
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value
    @property
    def end_time(self):
        """Gets the end_time of this AlipayInquiryStatementListRequest.
        
        """
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value
    @property
    def transaction_type_list(self):
        """Gets the transaction_type_list of this AlipayInquiryStatementListRequest.
        
        """
        return self.__transaction_type_list

    @transaction_type_list.setter
    def transaction_type_list(self, value):
        self.__transaction_type_list = value
    @property
    def currency_list(self):
        """Gets the currency_list of this AlipayInquiryStatementListRequest.
        
        """
        return self.__currency_list

    @currency_list.setter
    def currency_list(self, value):
        self.__currency_list = value
    @property
    def page_size(self):
        """Gets the page_size of this AlipayInquiryStatementListRequest.
        
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def page_number(self):
        """Gets the page_number of this AlipayInquiryStatementListRequest.
        
        """
        return self.__page_number

    @page_number.setter
    def page_number(self, value):
        self.__page_number = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "access_token") and self.access_token is not None:
            params['accessToken'] = self.access_token
        if hasattr(self, "start_time") and self.start_time is not None:
            params['startTime'] = self.start_time
        if hasattr(self, "end_time") and self.end_time is not None:
            params['endTime'] = self.end_time
        if hasattr(self, "transaction_type_list") and self.transaction_type_list is not None:
            params['transactionTypeList'] = self.transaction_type_list
        if hasattr(self, "currency_list") and self.currency_list is not None:
            params['currencyList'] = self.currency_list
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "page_number") and self.page_number is not None:
            params['pageNumber'] = self.page_number
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'accessToken' in response_body:
            self.__access_token = response_body['accessToken']
        if 'startTime' in response_body:
            self.__start_time = response_body['startTime']
        if 'endTime' in response_body:
            self.__end_time = response_body['endTime']
        if 'transactionTypeList' in response_body:
            self.__transaction_type_list = response_body['transactionTypeList']
        if 'currencyList' in response_body:
            self.__currency_list = response_body['currencyList']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'pageNumber' in response_body:
            self.__page_number = response_body['pageNumber']
