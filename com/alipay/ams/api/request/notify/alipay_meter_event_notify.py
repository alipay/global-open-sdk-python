from com.alipay.ams.api.model.error_event import ErrorEvent
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayMeterEventNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayMeterEventNotify, self).__init__()
        self.__event_name = None  # type: str
        self.__error_events = None  # type: list[ErrorEvent]
        self.__parse_notify_body(notify_body)

    @property
    def event_name(self):
        return self.__event_name

    @event_name.setter
    def event_name(self, value):
        self.__event_name = value

    @property
    def error_events(self):
        return self.__error_events

    @error_events.setter
    def error_events(self, value):
        self.__error_events = value

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayMeterEventNotify, self).parse_notify_body(notify_body)
        if "eventName" in notify:
            self.__event_name = notify["eventName"]
        if "errorEvents" in notify:
            self.__error_events = []
            for item in notify["errorEvents"]:
                error_event = ErrorEvent()
                error_event.parse_rsp_body(item)
                self.__error_events.append(error_event)
