import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class Limit:
    def __init__(self):
        
        self.__remaining_limit = None  # type: Amount
        self.__range_limit = None  # type: Amount
        self.__used_limit = None  # type: Amount
        

    @property
    def remaining_limit(self):
        """Gets the remaining_limit of this Limit.
        
        """
        return self.__remaining_limit

    @remaining_limit.setter
    def remaining_limit(self, value):
        self.__remaining_limit = value
    @property
    def range_limit(self):
        """Gets the range_limit of this Limit.
        
        """
        return self.__range_limit

    @range_limit.setter
    def range_limit(self, value):
        self.__range_limit = value
    @property
    def used_limit(self):
        """Gets the used_limit of this Limit.
        
        """
        return self.__used_limit

    @used_limit.setter
    def used_limit(self, value):
        self.__used_limit = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "remaining_limit") and self.remaining_limit is not None:
            params['remainingLimit'] = self.remaining_limit
        if hasattr(self, "range_limit") and self.range_limit is not None:
            params['rangeLimit'] = self.range_limit
        if hasattr(self, "used_limit") and self.used_limit is not None:
            params['usedLimit'] = self.used_limit
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'remainingLimit' in response_body:
            self.__remaining_limit = Amount()
            self.__remaining_limit.parse_rsp_body(response_body['remainingLimit'])
        if 'rangeLimit' in response_body:
            self.__range_limit = Amount()
            self.__range_limit.parse_rsp_body(response_body['rangeLimit'])
        if 'usedLimit' in response_body:
            self.__used_limit = Amount()
            self.__used_limit.parse_rsp_body(response_body['usedLimit'])
