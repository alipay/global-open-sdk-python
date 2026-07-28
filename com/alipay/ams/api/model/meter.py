import json




class Meter:
    def __init__(self):
        
        self.__meter_id = None  # type: str
        self.__meter_name = None  # type: str
        self.__event_name = None  # type: str
        self.__status = None  # type: str
        self.__aggregation_method = None  # type: str
        self.__event_time_window = None  # type: str
        self.__value_key_override = None  # type: str
        self.__created_date_time = None  # type: str
        self.__updated_date_time = None  # type: str
        

    @property
    def meter_id(self):
        """
        The meter ID. Maximum length: 64 characters.
        """
        return self.__meter_id

    @meter_id.setter
    def meter_id(self, value):
        self.__meter_id = value
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
    def aggregation_method(self):
        """
        The aggregation method. Maximum length: 8 characters.
        """
        return self.__aggregation_method

    @aggregation_method.setter
    def aggregation_method(self, value):
        self.__aggregation_method = value
    @property
    def event_time_window(self):
        """
        The event time window. Maximum length: 4 characters.
        """
        return self.__event_time_window

    @event_time_window.setter
    def event_time_window(self, value):
        self.__event_time_window = value
    @property
    def value_key_override(self):
        """
        The value key override. Maximum length: 256 characters.
        """
        return self.__value_key_override

    @value_key_override.setter
    def value_key_override(self, value):
        self.__value_key_override = value
    @property
    def created_date_time(self):
        """
        The created date time. Maximum length: 32 characters.
        """
        return self.__created_date_time

    @created_date_time.setter
    def created_date_time(self, value):
        self.__created_date_time = value
    @property
    def updated_date_time(self):
        """
        The updated date time. Maximum length: 32 characters.
        """
        return self.__updated_date_time

    @updated_date_time.setter
    def updated_date_time(self, value):
        self.__updated_date_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "meter_id") and self.meter_id is not None:
            params['meterId'] = self.meter_id
        if hasattr(self, "meter_name") and self.meter_name is not None:
            params['meterName'] = self.meter_name
        if hasattr(self, "event_name") and self.event_name is not None:
            params['eventName'] = self.event_name
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "aggregation_method") and self.aggregation_method is not None:
            params['aggregationMethod'] = self.aggregation_method
        if hasattr(self, "event_time_window") and self.event_time_window is not None:
            params['eventTimeWindow'] = self.event_time_window
        if hasattr(self, "value_key_override") and self.value_key_override is not None:
            params['valueKeyOverride'] = self.value_key_override
        if hasattr(self, "created_date_time") and self.created_date_time is not None:
            params['createdDateTime'] = self.created_date_time
        if hasattr(self, "updated_date_time") and self.updated_date_time is not None:
            params['updatedDateTime'] = self.updated_date_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'meterId' in response_body:
            self.__meter_id = response_body['meterId']
        if 'meterName' in response_body:
            self.__meter_name = response_body['meterName']
        if 'eventName' in response_body:
            self.__event_name = response_body['eventName']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'aggregationMethod' in response_body:
            self.__aggregation_method = response_body['aggregationMethod']
        if 'eventTimeWindow' in response_body:
            self.__event_time_window = response_body['eventTimeWindow']
        if 'valueKeyOverride' in response_body:
            self.__value_key_override = response_body['valueKeyOverride']
        if 'createdDateTime' in response_body:
            self.__created_date_time = response_body['createdDateTime']
        if 'updatedDateTime' in response_body:
            self.__updated_date_time = response_body['updatedDateTime']
