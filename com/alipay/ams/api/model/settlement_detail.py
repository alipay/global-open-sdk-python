import json
from com.alipay.ams.api.model.settle_to_type import SettleToType
from com.alipay.ams.api.model.amount import Amount




class SettlementDetail:
    def __init__(self):
        
        self.__settle_to = None  # type: SettleToType
        self.__settlement_amount = None  # type: Amount
        

    @property
    def settle_to(self):
        """Gets the settle_to of this SettlementDetail.
        
        """
        return self.__settle_to

    @settle_to.setter
    def settle_to(self, value):
        self.__settle_to = value
    @property
    def settlement_amount(self):
        """Gets the settlement_amount of this SettlementDetail.
        
        """
        return self.__settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self.__settlement_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "settle_to") and self.settle_to is not None:
            params['settleTo'] = self.settle_to
        if hasattr(self, "settlement_amount") and self.settlement_amount is not None:
            params['settlementAmount'] = self.settlement_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'settleTo' in response_body:
            settle_to_temp = SettleToType.value_of(response_body['settleTo'])
            self.__settle_to = settle_to_temp
        if 'settlementAmount' in response_body:
            self.__settlement_amount = Amount()
            self.__settlement_amount.parse_rsp_body(response_body['settlementAmount'])
