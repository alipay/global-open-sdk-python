from com.alipay.ams.api.model.dispute_accept_reason_type import DisputeAcceptReasonType
from com.alipay.ams.api.model.dispute_notification_type import DisputeNotificationType
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify

class AlipayDisputeNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayDisputeNotify, self).__init__()
        self.__payment_request_id = None
        self.__dispute_id = None
        self.__payment_id = None
        self.__dispute_time = None
        self.__dispute_amount = None
        self.__dispute_notification_type = None #type: DisputeNotificationType
        self.__dispute_reason_msg = None
        self.__dispute_judged_time = None
        self.__dispute_judged_amount = None
        self.__dispute_judged_result = None #type: DisputeJudgedResult
        self.__defense_due_time = None
        self.__dispute_reason_code = None
        self.__dispute_source = None
        self.__arn = None
        self.__dispute_accept_reason = None #type: DisputeAcceptReasonType
        self.__dispute_accept_time = None
        self.__dispute_type = None
        self.__defendable = None
        self.__parse_notify_body(notify_body)

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @property
    def dispute_id(self):
        return self.__dispute_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def dispute_time(self):
        return self.__dispute_time

    @property
    def dispute_amount(self):
        return self.__dispute_amount

    @property
    def dispute_notification_type(self):
        return self.__dispute_notification_type

    @property
    def dispute_reason_msg(self):
        return self.__dispute_reason_msg

    @property
    def dispute_judged_time(self):
        return self.__dispute_judged_time

    @property
    def dispute_judged_amount(self):
        return self.__dispute_judged_amount

    @property
    def dispute_judged_result(self):
        return self.__dispute_judged_result

    @property
    def defense_due_time (self):
        return self.__defense_due_time

    @property
    def dispute_reason_code(self):
        return self.__dispute_reason_code

    @property
    def dispute_source(self):
        return self.__dispute_source

    @property
    def arn(self):
        return self.__arn

    @property
    def dispute_accept_reason(self):
        return self.__dispute_accept_reason

    @property
    def dispute_accept_time(self):
        return self.__dispute_accept_time

    @property
    def dispute_type(self):
        return self.__dispute_type

    @property
    def defendable(self):
        return self.__defendable

    def __parse_notify_body(self, notify_body):
        notify =  super(AlipayDisputeNotify, self).parse_notify_body(notify_body)

        if 'payment_request_id' in notify:
            self.__payment_request_id = notify['payment_request_id']
        if 'dispute_id' in notify:
            self.__dispute_id = notify['dispute_id']
        if 'payment_id' in notify:
            self.__payment_id = notify['payment_id']
        if 'dispute_time' in notify:
            self.__dispute_time = notify['dispute_time']
        if 'dispute_amount' in notify:
            self.__dispute_amount = notify['dispute_amount']
        if 'dispute_notification_type' in notify:
            self.__dispute_notification_type = notify['dispute_notification_type']
        if 'dispute_reason_msg' in notify:
            self.__dispute_reason_msg = notify['dispute_reason_msg']
        if 'dispute_judged_time' in notify:
            self.__dispute_judged_time = notify['dispute_judged_time']
        if 'dispute_judged_amount' in notify:
            self.__dispute_judged_amount = notify['dispute_judged_amount']
        if 'dispute_judged_result' in notify:
            self.__dispute_judged_result = notify['dispute_judged_result']
        if 'defense_due_time' in notify:
            self.__defense_due_time = notify['defense_due_time']
        if 'dispute_reason_code' in notify:
            self.__dispute_reason_code = notify['dispute_reason_code']
        if 'dispute_source' in notify:
            self.__dispute_source = notify['dispute_source']
        if 'arn' in notify:
            self.__arn = notify['arn']
        if 'dispute_accept_reason' in notify:
            self.__dispute_accept_reason = notify['dispute_accept_reason']
        if 'dispute_accept_time' in notify:
            self.__dispute_accept_time = notify['dispute_accept_time']
        if 'dispute_type' in notify:
            self.__dispute_type = notify['dispute_type']
        if 'defendable' in notify:
            self.__defendable = notify['defendable']
