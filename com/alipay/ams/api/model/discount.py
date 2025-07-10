import json

from com.alipay.ams.api.model.amount import Amount


class Discount(object):

    def __init__(self):
        self.__discount_tag = None
        self.__discount_name = None
        self.__savings_amount = None  # type: Amount
        self.__estimate_savings_amount = None  # type: Amount
        self.__promotion_code = None

    @property
    def discount_tag(self):
        return self.__discount_tag

    @discount_tag.setter
    def discount_tag(self, value):
        self.__discount_tag = value

    @property
    def discount_name(self):
        return self.__discount_name

    @discount_name.setter
    def discount_name(self, value):
        self.__discount_name = value

    @property
    def savings_amount(self):
        return self.__savings_amount

    @savings_amount.setter
    def savings_amount(self, value):
        self.__savings_amount = value

    @property
    def estimate_savings_amount(self):
        return self.__estimate_savings_amount

    @estimate_savings_amount.setter
    def estimate_savings_amount(self, value):
        self.__estimate_savings_amount = value

    @property
    def promotion_code(self):
        return self.__promotion_code

    @promotion_code.setter
    def promotion_code(self, value):
        self.__promotion_code = value

    @property
    def savingsAmount(self):
        return self.__savings_amount

    @savingsAmount.setter
    def savingsAmount(self, value):
        self.__savings_amount = value

    @property
    def estimateSavingsAmount(self):
        return self.__estimate_savings_amount

    @estimateSavingsAmount.setter
    def estimateSavingsAmount(self, value):
        self.__estimate_savings_amount = value

    @property
    def promotionCode(self):
        return self.__promotion_code

    @promotionCode.setter
    def promotionCode(self, value):
        self.__promotion_code = value

    def to_ams_dict(self):
        params = dict()
        if self.discountTag is not None:
            params['discountTag'] = self.discount_tag
        if self.discountName is not None:
            params['discountName'] = self.discount_name
        if self.savingsAmount is not None:
            params['savingsAmount'] = self.savings_amount.to_ams_dict()
        if self.estimateSavingsAmount is not None:
            params['estimateSavingsAmount'] = self.estimate_savings_amount.to_ams_dict()
        if self.promotionCode is not None:
            params['promotionCode'] = self.promotion_code
        return params

    def parse_rsp_body(self, discount_body):
        if type(discount_body) == str:
            discount_body = json.loads(discount_body)

        if 'discountTag' in discount_body:
            self.discount_tag = discount_body['discountTag']

        if 'discountName' in discount_body:
            self.discount_name = discount_body['discountName']

        if 'savingsAmount' in discount_body:
            payment_amount = Amount()
            payment_amount.parse_rsp_body(discount_body['savingsAmount'])
            self.savings_amount = payment_amount

        if 'estimateSavingsAmount' in discount_body:
            payment_amount = Amount()
            payment_amount.parse_rsp_body(discount_body['estimateSavingsAmount'])
            self.estimate_savings_amount = payment_amount
        if 'promotionCode' in discount_body:
            self.promotion_code = discount_body['promotionCode']
