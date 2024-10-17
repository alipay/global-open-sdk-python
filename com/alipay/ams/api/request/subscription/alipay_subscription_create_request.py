import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.order_info import OrderInfo
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.model.settlement_strategy import SettlementStrategy
from com.alipay.ams.api.model.trial import Trial
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipaySubscriptionCreateRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubscriptionCreateRequest, self).__init__(AntomPathConstants.SUBSCRIPTION_CREATE_PATH)
        self.__subscription_request_id = None
        self.__subscription_description = None
        self.__subscription_redirect_url = None
        self.__subscription_start_time = None
        self.__subscription_end_time = None
        self.__period_rule = None  # type: PeriodRule
        self.__subscription_expiry_time = None
        self.__payment_method = None  # type: PaymentMethod
        self.__subscription_notification_url = None
        self.__payment_notification_url = None
        self.__order_info = None  # type: OrderInfo
        self.__payment_amount = None  # type: Amount
        self.__payment_amount_difference = None  # type: Amount
        self.__settlement_strategy = None  # type: SettlementStrategy
        self.__env = None  # type: Env
        self.__trials = None  # type: list[Trial]

    @property
    def subscription_request_id(self):
        return self.__subscription_request_id

    @subscription_request_id.setter
    def subscription_request_id(self, value):
        self.__subscription_request_id = value

    @property
    def subscription_description(self):
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value

    @property
    def subscription_redirect_url(self):
        return self.__subscription_redirect_url

    @subscription_redirect_url.setter
    def subscription_redirect_url(self, value):
        self.__subscription_redirect_url = value

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

    @property
    def subscription_expiry_time(self):
        return self.__subscription_expiry_time

    @subscription_expiry_time.setter
    def subscription_expiry_time(self, value):
        self.__subscription_expiry_time = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    @property
    def subscription_notification_url(self):
        return self.__subscription_notification_url

    @subscription_notification_url.setter
    def subscription_notification_url(self, value):
        self.__subscription_notification_url = value

    @property
    def payment_notification_url(self):
        return self.__payment_notification_url

    @payment_notification_url.setter
    def payment_notification_url(self, value):
        self.__payment_notification_url = value

    @property
    def order_info(self):
        return self.__order_info

    @order_info.setter
    def order_info(self, value):
        self.__order_info = value

    @property
    def payment_amount(self):
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value

    @property
    def payment_amount_difference(self):
        return self.__payment_amount_difference

    @payment_amount_difference.setter
    def payment_amount_difference(self, value):
        self.__payment_amount_difference = value

    @property
    def settlement_strategy(self):
        return self.__settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        self.__settlement_strategy = value

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value

    @property
    def trials(self):
        return self.__trials

    @trials.setter
    def trials(self, value):
        self.__trials = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()

        if self.__subscription_request_id is not None:
            params['subscriptionRequestId'] = self.__subscription_request_id
        if self.__subscription_description is not None:
            params['subscriptionDescription'] = self.__subscription_description
        if self.__subscription_redirect_url is not None:
            params['subscriptionRedirectUrl'] = self.__subscription_redirect_url
        if self.__subscription_start_time is not None:
            params['subscriptionStartTime'] = self.__subscription_start_time
        if self.__subscription_end_time is not None:
            params['subscriptionEndTime'] = self.__subscription_end_time
        if self.__period_rule is not None:
            params['periodRule'] = self.__period_rule.to_ams_dict()
        if self.__subscription_expiry_time is not None:
            params['subscriptionExpiryTime'] = self.__subscription_expiry_time
        if self.__payment_method is not None:
            params['paymentMethod'] = self.__payment_method.to_ams_dict()
        if self.__subscription_notification_url is not None:
            params['subscriptionNotificationUrl'] = self.__subscription_notification_url
        if self.__payment_notification_url is not None:
            params['paymentNotificationUrl'] = self.__payment_notification_url
        if self.__order_info is not None:
            params['orderInfo'] = self.__order_info.to_ams_dict()
        if self.__payment_amount is not None:
            params['paymentAmount'] = self.__payment_amount.to_ams_dict()
        if self.__payment_amount_difference is not None:
            params['paymentAmountDifference'] = self.__payment_amount_difference.to_ams_dict()
        if self.__settlement_strategy is not None:
            params['settlementStrategy'] = self.__settlement_strategy.to_ams_dict()
        if self.__env is not None:
            params['env'] = self.__env.to_ams_dict()
        if self.__trials is not None:
            trials_list = []
            for trial in self.__trials:
                trials_list.append(trial.to_ams_json())
                params['trials'] = trials_list

        return params
