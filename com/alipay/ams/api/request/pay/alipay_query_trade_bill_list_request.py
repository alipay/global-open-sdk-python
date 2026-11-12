import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayQueryTradeBillListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayQueryTradeBillListRequest, self).__init__("/ams/api/v1/adaptor/queryTradeBillList") 

        self.__merchant_id = None  # type: str
        self.__current_page = None  # type: int
        self.__page_size = None  # type: int
        self.__start_timestamp = None  # type: int
        self.__end_timestamp = None  # type: int
        self.__time_zone = None  # type: str
        

    @property
    def merchant_id(self):
        """
        The internal identifier of the sub-merchant whose trade bills are queried. Must not be empty.
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self.__merchant_id = value
    @property
    def current_page(self):
        """
        The page number to query, starting from 1. Provide this field to request a page other than the first page. If omitted, page 1 is queried.
        """
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        self.__current_page = value
    @property
    def page_size(self):
        """
        The number of records per page, from 1 to 200. Provide this field to change the page size. If omitted, 20 records are requested.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def start_timestamp(self):
        """
        The start of the transaction time range as a 13-digit timestamp in milliseconds. Must be earlier than endTimestamp.
        """
        return self.__start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, value):
        self.__start_timestamp = value
    @property
    def end_timestamp(self):
        """
        The end of the transaction time range as a 13-digit timestamp in milliseconds. Must be earlier than the current time minus 30 minutes.
        """
        return self.__end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, value):
        self.__end_timestamp = value
    @property
    def time_zone(self):
        """
        The merchant&#39;s local time zone used to display transaction times for reconciliation. Accepts time-zone identifiers such as UTC, GMT, Europe/London, and America/New_York. If omitted, all times are returned in UTC.
        """
        return self.__time_zone

    @time_zone.setter
    def time_zone(self, value):
        self.__time_zone = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_id") and self.merchant_id is not None:
            params['merchantId'] = self.merchant_id
        if hasattr(self, "current_page") and self.current_page is not None:
            params['currentPage'] = self.current_page
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "start_timestamp") and self.start_timestamp is not None:
            params['startTimestamp'] = self.start_timestamp
        if hasattr(self, "end_timestamp") and self.end_timestamp is not None:
            params['endTimestamp'] = self.end_timestamp
        if hasattr(self, "time_zone") and self.time_zone is not None:
            params['timeZone'] = self.time_zone
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantId' in response_body:
            self.__merchant_id = response_body['merchantId']
        if 'currentPage' in response_body:
            self.__current_page = response_body['currentPage']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'startTimestamp' in response_body:
            self.__start_timestamp = response_body['startTimestamp']
        if 'endTimestamp' in response_body:
            self.__end_timestamp = response_body['endTimestamp']
        if 'timeZone' in response_body:
            self.__time_zone = response_body['timeZone']
