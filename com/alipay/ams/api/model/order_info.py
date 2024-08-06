import json


class OrderInfo(object):
    def __init__(self):
        self.__order_amount = None

    @property
    def order_amount(self):
        return self.__order_amount

    @order_amount.setter
    def order_amount(self, value):
        self.__order_amount = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.order_amount is not None:
            params['orderAmount'] = self.order_amount
