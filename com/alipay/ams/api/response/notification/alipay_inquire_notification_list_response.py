import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.notification_event import NotificationEvent



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireNotificationListResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__notifications = None  # type: [NotificationEvent]
        self.__has_more = None  # type: bool
        self.__next_starting_after = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireNotificationListResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def notifications(self):
        """
        Events in newest-first creation order, returned only when resultStatus is S. An empty array indicates no matching events.
        """
        return self.__notifications

    @notifications.setter
    def notifications(self, value):
        self.__notifications = value
    @property
    def has_more(self):
        """
        Whether another forward page exists. Returned only when resultStatus is S, including false for the last page.
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value):
        self.__has_more = value
    @property
    def next_starting_after(self):
        """
        The last returned event ID, used as startingAfter for the next page. Returned only when hasMore is true.
        """
        return self.__next_starting_after

    @next_starting_after.setter
    def next_starting_after(self, value):
        self.__next_starting_after = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "notifications") and self.notifications is not None:
            params['notifications'] = self.notifications
        if hasattr(self, "has_more") and self.has_more is not None:
            params['hasMore'] = self.has_more
        if hasattr(self, "next_starting_after") and self.next_starting_after is not None:
            params['nextStartingAfter'] = self.next_starting_after
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireNotificationListResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'notifications' in response_body:
            self.__notifications = []
            for item in response_body['notifications']:
                obj = NotificationEvent()
                obj.parse_rsp_body(item)
                self.__notifications.append(obj)
        if 'hasMore' in response_body:
            self.__has_more = response_body['hasMore']
        if 'nextStartingAfter' in response_body:
            self.__next_starting_after = response_body['nextStartingAfter']
