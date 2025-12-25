import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquiryStatementRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquiryStatementRequest, self).__init__("/ams/api/v1/aba/accounts/inquiryStatement") 

        self.__customer_id = None  # type: str
        self.__access_token = None  # type: str
        self.__start_time = None  # type: bool, date, datetime, dict, float, int, list, str, none_type
        self.__end_time = None  # type: str
        self.__transaction_type_list = None  # type: [str]
        self.__currency_list = None  # type: [str]
        self.__page_size = None  # type: int
        self.__page_number = None  # type: int
        

    @property
    def customer_id(self):
        """
        antom ABA merchant id
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def access_token(self):
        """
        access token for the relevant antom ABA merchant
        """
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value
    @property
    def start_time(self):
        """
        start time of statement query. The value follows the ISO 8601 standard format. The time interval between startTime and endTime cannot be more than 3 months (equivalent to 100 days).
        """
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value
    @property
    def end_time(self):
        """
        end time of statement query. The value follows the ISO 8601 standard format. The time interval between startTime and endTime cannot be more than 3 months (equivalent to 100 days).
        """
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value
    @property
    def transaction_type_list(self):
        """
        If no value passed, the API shall return all transactions. Antom only supports [0-1] single type for the current time.
        """
        return self.__transaction_type_list

    @transaction_type_list.setter
    def transaction_type_list(self, value):
        self.__transaction_type_list = value
    @property
    def currency_list(self):
        """
        If no value passed, the API shall return the defined transaction type with all currencies. The value shall follow the ISO currency standard (e.g., USD, EUR).
        """
        return self.__currency_list

    @currency_list.setter
    def currency_list(self, value):
        self.__currency_list = value
    @property
    def page_size(self):
        """
        Indicates the number of items on each page.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def page_number(self):
        """
        Indicates the current page index that contains statement information.
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
