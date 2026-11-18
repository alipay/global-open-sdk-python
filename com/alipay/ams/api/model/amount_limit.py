import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class AmountLimit:
    def __init__(self):
        
        self.__max_amount = None  # type: Amount
        self.__min_amount = None  # type: Amount
        self.__remain_amount = None  # type: Amount
        

    @property
    def max_amount(self):
        """Gets the max_amount of this AmountLimit.
        
        """
        return self.__max_amount

    @max_amount.setter
    def max_amount(self, value):
        self.__max_amount = value
    @property
    def min_amount(self):
        """Gets the min_amount of this AmountLimit.
        
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value):
        self.__min_amount = value
    @property
    def remain_amount(self):
        """Gets the remain_amount of this AmountLimit.
        
        """
        return self.__remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self.__remain_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "max_amount") and self.max_amount is not None:
            params['maxAmount'] = self.max_amount
        if hasattr(self, "min_amount") and self.min_amount is not None:
            params['minAmount'] = self.min_amount
        if hasattr(self, "remain_amount") and self.remain_amount is not None:
            params['remainAmount'] = self.remain_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'maxAmount' in response_body:
            self.__max_amount = Amount()
            self.__max_amount.parse_rsp_body(response_body['maxAmount'])
        if 'minAmount' in response_body:
            self.__min_amount = Amount()
            self.__min_amount.parse_rsp_body(response_body['minAmount'])
        if 'remainAmount' in response_body:
            self.__remain_amount = Amount()
            self.__remain_amount.parse_rsp_body(response_body['remainAmount'])
