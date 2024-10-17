from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.settle_to_type import SettleToType


class SettlementDetail:
    def __init__(self):
        self.__settle_to = None #type: SettleToType
        self.__settlement_amount = None #type: Amount

    @property
    def settle_to(self):
        return self.__settle_to

    @settle_to.setter
    def settle_to(self, value):
        self.__settle_to = value

    @property
    def settlement_amount(self):
        return self.__settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self.__settlement_amount = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, 'settle_to') and self.settle_to:
            params['settleTo'] = self.settle_to.value
        if hasattr(self, 'settlement_amount') and self.settlement_amount:
            params['settlementAmount'] = self.settlement_amount.to_ams_dict()
        return params