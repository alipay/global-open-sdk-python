import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireNotificationRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireNotificationRequest, self).__init__("/ams/api/v1/notification/inquireNotification") 

        self.__event_id = None  # type: str
        

    @property
    def event_id(self):
        """
        The UUID v4 event ID from a webhook or notification list query.
        """
        return self.__event_id

    @event_id.setter
    def event_id(self, value):
        self.__event_id = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "event_id") and self.event_id is not None:
            params['eventId'] = self.event_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'eventId' in response_body:
            self.__event_id = response_body['eventId']
