from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_method import PaymentMethod


class PaymentDetail:
    def __init__(self):
        self.__amount = None #type: Amount
        self.__payment_method = None #type: PaymentMethod

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    def to_ams_dict(self):
        params = dict()
        if self.amount:
            params['amount'] = self.amount.to_ams_dict()
        if self.payment_method:
            params['paymentMethod'] = self.payment_method.to_ams_dict()
        return params