import json

from com.alipay.ams.api.model.amount import Amount


class Discount(object):

    def __init__(self):
        self.discountTag = None
        self.discountName = None
        self.savingsAmount = None  # type: Amount
        self.estimateSavingsAmount = None  # type: Amount

    @property
    def discountTag(self):
        return self.__discountTag

    @discountTag.setter
    def discountTag(self, value):
        self.__discountTag = value

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

    @property
    def estimateSavingsAmount(self):
        return self.__estimateSavingsAmount

    @estimateSavingsAmount.setter
    def estimateSavingsAmount(self, value):
        self.__estimateSavingsAmount = value

    def to_ams_dict(self):
        params = dict()
        if self.discountTag is not None:
            params['discountTag'] = self.discountTag
        if self.discountName is not None:
            params['discountName'] = self.discountName
        if self.savingsAmount is not None:
            params['savingsAmount'] = self.savingsAmount.to_ams_dict()
        if self.estimateSavingsAmount is not None:
            params['estimateSavingsAmount'] = self.estimateSavingsAmount.to_ams_dict()
        return params

    def parse_rsp_body(self, discount_body):
        if type(discount_body) == str:
            discount_body = json.loads(discount_body)

        if 'discountTag' in discount_body:
            self.discountTag = discount_body['discountTag']

        if 'discountName' in discount_body:
            self.discountName = discount_body['discountName']

        if 'savingsAmount' in discount_body:
            payment_amount = Amount()
            payment_amount.parse_rsp_body(discount_body['savingsAmount'])
            self.__savingsAmount = payment_amount

        if 'estimateSavingsAmount' in discount_body:
            payment_amount = Amount()
            payment_amount.parse_rsp_body(discount_body['estimateSavingsAmount'])
            self.__estimateSavingsAmount = payment_amount