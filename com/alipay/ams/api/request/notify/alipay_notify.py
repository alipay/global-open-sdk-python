import json

from com.alipay.ams.api.model.result import Result


class AlipayNotify(object):

    def __init__(self):
        self.__notify_type = None
        self.__result = None  #type: Result

    @property
    def notify_type(self):
        return self.__notify_type

    @property
    def result(self):
        return self.__result

    def parse_notify_body(self, notify_body):
        notify = json.loads(notify_body)
        if 'notifyType' in notify:
            self.__notify_type = notify['notifyType']
        if 'result' in notify:
            result = Result()
            result.parse_rsp_body(notify['result'])
            self.__result = result
        return notify