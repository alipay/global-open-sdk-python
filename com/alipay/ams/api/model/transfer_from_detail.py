from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_method import PaymentMethod


class TransferFromDetail:
    def __init__(self):
        self.__transfer_from_method = None #type: PaymentMethod
        self.__transfer_from_amount = None #type: Amount


    @property
    def transfer_from_method(self):
        return self.__transfer_from_method

    @property
    def transfer_from_amount(self):
        return self.__transfer_from_amount

    @transfer_from_method.setter
    def transfer_from_method(self, value):
        self.__transfer_from_method = value

    @transfer_from_amount.setter
    def transfer_from_amount(self, value):
        self.__transfer_from_amount = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_from_method") and self.transfer_from_method:
            params['transferFromMethod'] = self.transfer_from_method.to_ams_dict()
        if hasattr(self, "transfer_from_amount") and self.transfer_from_amount:
            params['transferFromAmount'] = self.transfer_from_amount.to_ams_dict()
        return params