import json
from com.alipay.ams.api.model.result import Result
from com.alipay.ams.api.model.notification_event import NotificationEvent



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayInquireNotificationResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: Result
        self.__notification = None  # type: NotificationEvent
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayInquireNotificationResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def notification(self):
        """Gets the notification of this AlipayInquireNotificationResponse.
        
        """
        return self.__notification

    @notification.setter
    def notification(self, value):
        self.__notification = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "notification") and self.notification is not None:
            params['notification'] = self.notification
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayInquireNotificationResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = Result()
            self.__result.parse_rsp_body(response_body['result'])
        if 'notification' in response_body:
            self.__notification = NotificationEvent()
            self.__notification.parse_rsp_body(response_body['notification'])
