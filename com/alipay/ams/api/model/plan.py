import json

from com.alipay.ams.api.model.amount import Amount


class Plan(object):
    def __init__(self):
        self.__interest_rate = None
        self.__min_installment_amount = None  # type: Amount
        self.__max_installment_amount = None  # type: Amount
        self.__installment_num = None
        self.__interval = None
        self.__enabled = None

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = value

    @property
    def min_installment_amount(self):
        return self.__min_installment_amount

    @min_installment_amount.setter
    def min_installment_amount(self, value):
        self.__min_installment_amount = value

    @property
    def max_installment_amount(self):
        return self.__max_installment_amount

    @max_installment_amount.setter
    def max_installment_amount(self, value):
        self.__max_installment_amount = value

    @property
    def installment_num(self):
        return self.__installment_num

    @installment_num.setter
    def installment_num(self, value):
        self.__installment_num = value

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, value):
        self.__interval = value

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "interest_rate") and self.interest_rate:
            params['interestRate'] = self.interest_rate

        if hasattr(self, "min_installment_amount") and self.min_installment_amount:
            params['minInstallmentAmount'] = self.min_installment_amount.to_ams_dict()

        if hasattr(self, "max_installment_amount") and self.max_installment_amount:
            params['maxInstallmentAmount'] = self.max_installment_amount.to_ams_dict()

        if hasattr(self, "installment_num") and self.installment_num:
            params['installmentNum'] = self.installment_num

        if hasattr(self, "interval") and self.interval:
            params['interval'] = self.interval

        if hasattr(self, "enabled") and self.enabled:
            params['enabled'] = self.enabled
        return params

    def parse_rsp_body(self, plan_body):
        if type(plan_body) == str:
            payment_option_body = json.loads(plan_body)

        if "interestRate" in plan_body:
            self.interest_rate = plan_body["interestRate"]

        if "minInstallmentAmount" in plan_body:
            self.min_installment_amount = Amount()
            self.min_installment_amount.parse_rsp_body(plan_body["minInstallmentAmount"])

        if "maxInstallmentAmount" in plan_body:
            self.max_installment_amount = Amount()
            self.max_installment_amount.parse_rsp_body(plan_body["maxInstallmentAmount"])

        if "installmentNum" in plan_body:
            self.installment_num = plan_body["installmentNum"]

        if "interval" in plan_body:
            self.interval = plan_body["interval"]

        if "enabled" in plan_body:
            self.enabled = plan_body["enabled"]
