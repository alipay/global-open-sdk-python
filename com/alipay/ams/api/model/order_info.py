import json
from com.alipay.ams.api.model.amount import Amount




class OrderInfo:
    def __init__(self):
        
        self.__order_amount = None  # type: Amount
        

    @property
    def order_amount(self):
        """Gets the order_amount of this OrderInfo.
        
        """
        return self.__order_amount

    @order_amount.setter
    def order_amount(self, value):
        self.__order_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "order_amount") and self.order_amount is not None:
            params['orderAmount'] = self.order_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'orderAmount' in response_body:
            self.__order_amount = Amount()
            self.__order_amount.parse_rsp_body(response_body['orderAmount'])
