import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.order_info import OrderInfo
from com.alipay.ams.api.model.period_rule import PeriodRule
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipaySubscriptionUpdateRequest(AlipayRequest):

    def __init__(self):
        super(AlipaySubscriptionUpdateRequest, self).__init__(AntomPathConstants.SUBSCRIPTION_UPDATE_PATH)
        self.__subscription_update_requestId = None
        self.__subscription_id = None
        self.__subscription_description = None
        self.__period_rule = None #type: PeriodRule
        self.__payment_amount = None #type: Amount
        self.__subscription_end_time = None
        self.__order_info = None #type: OrderInfo

    @property
    def subscription_update_requestId(self):
        return self.__subscription_update_requestId

    @subscription_update_requestId.setter
    def subscription_update_requestId(self, value):
        self.__subscription_update_requestId = value

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
    def period_rule(self):
        return self.__period_rule

    @period_rule.setter
    def period_rule(self, value):
        self.__period_rule = value

    @property
    def payment_amount(self):
        return self.__payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self.__payment_amount = value

    @property
    def subscription_end_time(self):
        return self.__subscription_end_time

    @subscription_end_time.setter
    def subscription_end_time(self, value):
        self.__subscription_end_time = value

    @property
    def order_info(self):
        return self.__order_info

    @order_info.setter
    def order_info(self, value):
        self.__order_info = value


    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()

        if self.__subscription_update_requestId is not None:
            params['subscriptionUpdateRequestId'] = self.__subscription_update_requestId
        if self.__subscription_id is not None:
            params['subscriptionId'] = self.__subscription_id
        if self.__subscription_description is not None:
            params['subscriptionDescription'] = self.__subscription_description
        if self.__period_rule is not None:
            params['periodRule'] = self.__period_rule.to_ams_dict()
        if self.__payment_amount is not None:
            params['paymentAmount'] = self.__payment_amount.to_ams_dict()
        if self.__subscription_end_time is not None:
            params['subscriptionEndTime'] = self.__subscription_end_time
        if self.__order_info is not None:
            params['orderInfo'] = self.__order_info.to_ams_dict()
        return params




