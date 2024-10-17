import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.order_info import OrderInfo
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipaySubscriptionChangeRequest(AlipayRequest):
    def __init__(self):
        super(AlipaySubscriptionChangeRequest, self).__init__(AntomPathConstants.SUBSCRIPTION_CHANGE_PATH)
        self.__subscription_change_request_id = None
        self.__subscription_id = None
        self.__subscription_description = None
        self.__subscription_start_time = None
        self.__subscription_end_time = None
        self.__period_rule = None  # type: PeriodRule
        self.__subscription_expiry_time = None
        self.__order_info = None  # type: OrderInfo
        self.__payment_amount = None  # type: Amount
        self.__payment_amount_difference = None  # type: Amount

    @property
    def subscription_change_request_id(self):
        return self.__subscription_change_request_id

    @subscription_change_request_id.setter
    def subscription_change_request_id(self, value):
        self.__subscription_change_request_id = value

    @property
    def subscription_id(self):
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value

    @property
    def subscription_description(self):
        return self.__subscription_description

    @subscription_description.setter
    def subscription_description(self, value):
        self.__subscription_description = value

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

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscription_change_request_id") and self.subscription_change_request_id:
            params['subscriptionChangeRequestId'] = self.subscription_change_request_id

        if hasattr(self, "subscription_id") and self.subscription_id:
            params['subscriptionId'] = self.subscription_id

        if hasattr(self, "subscription_description") and self.subscription_description:
            params['subscriptionDescription'] = self.subscription_description

        if hasattr(self, "subscription_start_time") and self.subscription_start_time:
            params['subscriptionStartTime'] = self.subscription_start_time

        if hasattr(self, "subscription_end_time") and self.subscription_end_time:
            params['subscriptionEndTime'] = self.subscription_end_time

        if hasattr(self, "period_rule") and self.period_rule:
            params['periodRule'] = self.period_rule

        if hasattr(self, "subscription_expiry_time") and self.subscription_expiry_time:
            params['subscriptionExpiryTime'] = self.subscription_expiry_time

        if hasattr(self, "order_info") and self.order_info:
            params['orderInfo'] = self.order_info

        if hasattr(self, "payment_amount") and self.payment_amount:
            params['paymentAmount'] = self.payment_amount

        if hasattr(self, "payment_amount_difference") and self.payment_amount_difference:
            params['paymentAmountDifference'] = self.payment_amount_difference

        return params
