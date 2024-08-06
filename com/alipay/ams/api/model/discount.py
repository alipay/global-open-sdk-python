import json

from com.alipay.ams.api.model import amount
from com.alipay.ams.api.model.amount import Amount


class Discount(object):

    def __init__(self):
        self.discountName = None
        self.savingsAmount = None  # type: amount

    @property
    def discountName(self):
        return self.__discountName

    @discountName.setter
    def discountName(self, value):
        self.__discountName = value

    @property
    def savingsAmount(self):
        return self.__savingsAmount

    @savingsAmount.setter
    def savingsAmount(self, value):
        self.__savingsAmount = value

    def to_ams_dict(self):
        params = dict()
        if self.discountName is not None:
            params['discountName'] = self.discountName
        if self.savingsAmount is not None:
            params['savingsAmount'] = self.savingsAmount.to_ams_dict()
        return params

    def parse_rsp_body(self, amount_body):
        if type(amount_body) == str:
            amount_body = json.loads(amount_body)

        if 'discountName' in amount_body:
            self.discountName = amount_body['discountName']

        if 'savingsAmount' in amount_body:
            payment_amount = Amount()
            payment_amount.parse_rsp_body(amount_body['savingsAmount'])
            self.__savingsAmount = payment_amount
