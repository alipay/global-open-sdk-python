import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.refund_from_type import RefundFromType




class RefundDetail:
    def __init__(self):
        
        self.__refund_amount = None  # type: Amount
        self.__refund_from = None  # type: RefundFromType
        

    @property
    def refund_amount(self):
        """Gets the refund_amount of this RefundDetail.
        
        """
        return self.__refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self.__refund_amount = value
    @property
    def refund_from(self):
        """Gets the refund_from of this RefundDetail.
        
        """
        return self.__refund_from

    @refund_from.setter
    def refund_from(self, value):
        self.__refund_from = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "refund_amount") and self.refund_amount is not None:
            params['refundAmount'] = self.refund_amount
        if hasattr(self, "refund_from") and self.refund_from is not None:
            params['refundFrom'] = self.refund_from
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'refundAmount' in response_body:
            self.__refund_amount = Amount()
            self.__refund_amount.parse_rsp_body(response_body['refundAmount'])
        if 'refundFrom' in response_body:
            refund_from_temp = RefundFromType.value_of(response_body['refundFrom'])
            self.__refund_from = refund_from_temp
