import json
from com.alipay.ams.api.model.event import Event




class Meter:
    def __init__(self):
        
        self.__event_name = None  # type: str
        self.__events = None  # type: [Event]
        

    @property
    def event_name(self):
        """
        The event name. Maximum length: 128 characters.
        """
        return self.__event_name

    @event_name.setter
    def event_name(self, value):
        self.__event_name = value
    @property
    def events(self):
        """
        The events.
        """
        return self.__events

    @events.setter
    def events(self, value):
        self.__events = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "event_name") and self.event_name is not None:
            params['eventName'] = self.event_name
        if hasattr(self, "events") and self.events is not None:
            params['events'] = self.events
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'eventName' in response_body:
            self.__event_name = response_body['eventName']
        if 'events' in response_body:
            self.__events = []
            for item in response_body['events']:
                obj = Event()
                obj.parse_rsp_body(item)
                self.__events.append(obj)
