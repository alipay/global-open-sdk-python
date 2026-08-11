import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayMeterInquireListRequest(AlipayRequest):
    def __init__(self):
        super(AlipayMeterInquireListRequest, self).__init__("/ams/api/v1/meter/inquireList") 

        self.__page_num = None  # type: int
        self.__page_size = None  # type: int
        self.__meter_name = None  # type: str
        self.__event_name = None  # type: str
        self.__status = None  # type: str
        self.__start_date_time = None  # type: str
        self.__end_date_time = None  # type: str
        

    @property
    def page_num(self):
        """
        The page number. The value must be at least 1. The default value is 1. A page beyond the last page returns SUCCESS with an empty &#x60;meters&#x60; array.
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
    def meter_name(self):
        """
        The meter name. Maximum length: 255 characters.
        """
        return self.__meter_name

    @meter_name.setter
    def meter_name(self, value):
        self.__meter_name = value
    @property
    def event_name(self):
        """
        The event name. Maximum length: 100 characters.
        """
        return self.__event_name

    @event_name.setter
    def event_name(self, value):
        self.__event_name = value
    @property
    def status(self):
        """
        The current status. Maximum length: 8 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def start_date_time(self):
        """
        The start date time. Maximum length: 32 characters.
        """
        return self.__start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        self.__start_date_time = value
    @property
    def end_date_time(self):
        """
        The end date time. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        self.__end_date_time = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "page_num") and self.page_num is not None:
            params['pageNum'] = self.page_num
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "meter_name") and self.meter_name is not None:
            params['meterName'] = self.meter_name
        if hasattr(self, "event_name") and self.event_name is not None:
            params['eventName'] = self.event_name
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "start_date_time") and self.start_date_time is not None:
            params['startDateTime'] = self.start_date_time
        if hasattr(self, "end_date_time") and self.end_date_time is not None:
            params['endDateTime'] = self.end_date_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'pageNum' in response_body:
            self.__page_num = response_body['pageNum']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'meterName' in response_body:
            self.__meter_name = response_body['meterName']
        if 'eventName' in response_body:
            self.__event_name = response_body['eventName']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'startDateTime' in response_body:
            self.__start_date_time = response_body['startDateTime']
        if 'endDateTime' in response_body:
            self.__end_date_time = response_body['endDateTime']
