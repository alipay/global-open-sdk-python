import json

from com.alipay.ams.api.model.amount import Amount


class OrderInfo(object):
    def __init__(self):
        self.__order_amount = None #type: Amount

    @property
    def order_amount(self):
        return self.__order_amount

    @order_amount.setter
    def order_amount(self, value):
        self.__order_amount = value

    def to_ams_dict(self):
        params = dict()
        if self.order_amount is not None:
            params['orderAmount'] = self.order_amount.to_ams_dict()
        return params
