from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.subscription_notification_type import SubscriptionNotificationType
from com.alipay.ams.api.model.subscription_status import SubscriptionStatus
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipaySubscriptionNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipaySubscriptionNotify, self).__init__()
        self.__subscription_request_id = None
        self.__subscription_id = None
        self.__subscription_status = None # type: SubscriptionStatus
        self.__subscription_notification_type = None # type: SubscriptionNotificationType
        self.__subscription_start_time = None
        self.__subscription_end_time = None
        self.__period_rule = None # type: PeriodRule
        self.__parse_notify_body(notify_body)

    @property
    def subscription_request_id(self):
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value

    @property
    def subscription_id(self):
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value

    @property
    def subscription_status(self):
        return self.__subscription_status

    @subscription_status.setter
    def subscription_status(self, value):
        self.__subscription_status = value

    @property
    def subscription_notification_type(self):
        return self.__subscription_notification_type

    @subscription_notification_type.setter
    def subscription_notification_type(self, value):
        self.__subscription_notification_type = value

    @property
    def subscription_start_time(self):
        return self.__subscription_start_time

    @subscription_start_time.setter
    def subscription_start_time(self, value):
        self.__subscription_start_time = value

    @property
    def subscription_end_time(self):
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value

    @property
    def period_rule(self):
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value

    def __parse_notify_body(self, notify_body):
        notify = super(AlipaySubscriptionNotify, self).parse_notify_body(notify_body)
        if 'subscription_id' in notify:
            self.__subscription_id = notify['subscription_id']
        if 'subscription_status' in notify:
            self.__subscription_status = SubscriptionStatus.get_by_value(notify['subscription_status'])
        if 'subscription_notification_type' in notify:
            self.__subscription_notification_type = SubscriptionNotificationType.get_by_value(notify['subscription_notification_type'])
        if 'subscription_start_time' in notify:
            self.__subscription_start_time = notify['subscription_start_time']
        if 'subscription_end_time' in notify:
            self.__subscription_end_time = notify['subscription_end_time']
        if 'period_rule' in notify:
            periodRule = PeriodRule()
            periodRule.parse_rsp_body(notify['period_rule'])
            self.__period_rule = periodRule


