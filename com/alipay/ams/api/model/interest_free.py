import json

from com.alipay.ams.api.model.amount import Amount


class InterestFree(object):
    def __init__(self):
        self.__provider = None
        self.__expireTime = None
        self.__installment_free_nums = None  # type:list[str]
        self.__min_payment_amount = None  # type:Amount
        self.__max_payment_amount = None  # type:Amount
        self.__free_percentage = None

    @property
    def provider(self):
        return self.__provider

    @provider.setter
    def provider(self, value):
        self.__provider = value

    @property
    def expireTime(self):
        return self.__expireTime

    @expireTime.setter
    def expireTime(self, value):
        self.__expireTime = value

    @property
    def installment_free_nums(self):
        return self.__installment_free_nums

    @installment_free_nums.setter
    def installment_free_nums(self, value):
        self.__installment_free_nums = value

    @property
    def min_payment_amount(self):
        return self.__min_payment_amount

    @min_payment_amount.setter
    def min_payment_amount(self, value):
        self.__min_payment_amount = value

    @property
    def max_payment_amount(self):
        return self.__max_payment_amount

    @max_payment_amount.setter
    def max_payment_amount(self, value):
        self.__max_payment_amount = value

    @property
    def free_percentage(self):
        return self.__free_percentage

    @free_percentage.setter
    def free_percentage(self, value):
        self.__free_percentage = value

    def parse_rsp_body(self, interest_free_body):
        if type(interest_free_body) == str:
            interest_free_body = json.loads(interest_free_body)

        if 'provider' in interest_free_body:
            self.provider = interest_free_body['provider']

        if 'expireTime' in interest_free_body:
            self.expireTime = interest_free_body['expireTime']

        if 'installmentFreeNums' in interest_free_body:
            self.installment_free_nums = interest_free_body['installmentFreeNums']

        if 'minPaymentAmount' in interest_free_body:
            self.min_payment_amount = Amount()
            self.min_payment_amount.parse_rsp_body(interest_free_body['minPaymentAmount'])

        if 'maxPaymentAmount' in interest_free_body:
            self.max_payment_amount = Amount()
            self.max_payment_amount.parse_rsp_body(interest_free_body['maxPaymentAmount'])

        if 'freePercentage' in interest_free_body:
            self.free_percentage = interest_free_body['freePercentage']
